import requests


def get_response_divar():
    url = "https://api.divar.ir/v8/postlist/w/search"

    json = {
        "city_ids": ["1"],
        "pagination_data": {
            "@type": "type.googleapis.com/post_list.PaginationData",
            "last_post_date": "2024-08-21T21:23:11.461693Z",
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


res = get_response_divar()
data = res.json()
last_post_date = data["pagination"]["data"]["last_post_date"]

list_of_tokens = []

count = 0
while True:

    json = {
        "city_ids": ["1"],
        "pagination_data": {
            "@type": "type.googleapis.com/post_list.PaginationData",
            "last_post_date": last_post_date,
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


    res = get_response_divar()
    data = res.json()
    last_post_date = data["pagination"]["data"]["last_post_date"]

    for widget in data['list_widgets']:
        token = widget["data"]["action"]["payload"]["token"]
        list_of_tokens.append(token)
        count += 1
        print(token)

    if count >= 100:
        break
print(list_of_tokens)
txt_file = open('tokens.txt', 'w', encoding='utf8')
txt_file.write(','.join(list_of_tokens))
txt_file.close()
