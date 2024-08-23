from datetime import datetime, timedelta
import requests
from pymongo import MongoClient


def __count_down():
    init_date= "2024-08-21T21:23:11.461693Z"
    count_down_date_array = []
    # Convert the string to a datetime object
    start_date = datetime.strptime(init_date, '%Y-%m-%dT%H:%M:%S.%fZ')

    # Ending date string
    end_date_str = '2024-08-20T21:06:03.618904Z'  # You can set this to whatever end date you like
    end_date = datetime.strptime(end_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')

    # Loop to count down one day at a time
    current_date = start_date
    while current_date >= end_date:
        # Convert the current datetime object back to a string
        date_str = current_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        count_down_date_array.append(date_str)
        print(date_str)

        # Subtract one day
        current_date -= timedelta(days=1)
    return count_down_date_array





def __change_response_by_last_modified_date(last_modified_date):
    url = "https://api.divar.ir/v8/postlist/w/search"
    json = {
        "city_ids": ["1"],
        "pagination_data": {
            "@type": "type.googleapis.com/post_list.PaginationData",
            "last_post_date": last_modified_date,
            "page": 1,
            "layer_page": 1

        },
        "search_data": {
            "form_data": {
                "data": {
                    "category": {"str": {"value": "real-estate"}},
                    "sort": {"str": {"value": "sort_date"}}
                }
            }
        }
    }
    headers = {
        "Content-Type": "application/json"
    }
    return requests.post(url, json=json, headers=headers)


def get_data_array_by_count_down():
    last_modified_date_array = __count_down()
    data_array = []
    for date in last_modified_date_array:
        response = __change_response_by_last_modified_date(date)
        data = response.json()
        data_array.append(data)
    return data_array

def save_collection_mongo(items):
    from pymongo import MongoClient

    # Create a connection to MongoDB
    client = MongoClient('mongodb://localhost:27017/')  # Adjust the URI if needed

    # Select the database
    db = client['Divar']

    # Select the collection
    collection = db['appartement']
    result = collection.insert_many(items)

    # Print the inserted IDs
    print(f"Documents inserted with IDs: {result.inserted_ids}")