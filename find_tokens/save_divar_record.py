from get_data_by_count_down_date import get_data
from mongo_util import save_collection_mongo, clean_mongo


def save_divar_record():


    clean_mongo()
    data_array = get_data()
    items = []
    for data in data_array:
      for widget in data['list_widgets']:
        token = widget["data"]["action"]["payload"]["token"]
        title = widget["data"]["title"]
        try:
            # some time appartement has no price then has no middle_description_text field
            price = widget["data"]["middle_description_text"]
            price_without_unit = price.replace('تومان', '').strip()
            token = widget["data"]["action"]["payload"]["token"]
            # neighborhood_name = find_neighborhood_by_soup(token)
            item = {"title": title, "price": price_without_unit, "token": token}

            items.append(item)

        except Exception as e:
              continue
    save_collection_mongo(items)
