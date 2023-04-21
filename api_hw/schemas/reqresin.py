from voluptuous import Schema

user_schema = Schema({
    "id": int,
    "email": str,
    "first_name": str,
    "last_name": str,
    "avatar": str
})

list_user_schema = Schema({
    "page": int,
    "per_page": int,
    "total": int,
    "total_pages": int,
    "data": [user_schema],
    "support": {
        "url": str,
        "text": str}
})

list_unknown_data_schema = Schema({
    "id": int,
    "name": str,
    "year": int,
    "color": str,
    "pantone_value": str
})

list_unknown_schema = Schema({
    "page": int,
    "per_page": int,
    "total": int,
    "total_pages": int,
    "data": [list_unknown_data_schema],
    "support": {
        "url": str,
        "text": str}
})

