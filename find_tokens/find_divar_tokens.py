from Utils import get_data_array_by_count_down,save_collection_mongo


data_array = get_data_array_by_count_down()
items = []
for data in data_array:
    for widget in data['list_widgets']:
        token = widget["data"]["action"]["payload"]["token"]
        title = widget["data"]["title"]
        try:
            # some time appartement has no price then has no middle_description_text field
            price = widget["data"]["middle_description_text"]
            price_without_unit = price.replace('تومان', '').strip()
            item = {"title": title, "price": price_without_unit}
            items.append(item)

        except Exception as e:
            continue
save_collection_mongo(items)