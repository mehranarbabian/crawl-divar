from find_divar_tokens import get_response_divar

res=get_response_divar()

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

        count += 1
        print(token)
