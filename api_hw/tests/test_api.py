import requests
from requests import Response
from pytest_voluptuous import S
from api_hw.schemas.reqresin import list_user_schema, list_unknown_schema


def test_count_users():
    url = 'https://reqres.in/api/users'
    response: Response = requests.get(url, params={"page": 2})
    total = response.json()["total"]
    assert total == 12


def test_single_user_name():
    url = 'https://reqres.in/api/users/2'
    response: Response = requests.get(url)
    assert response.json()["data"]["first_name"] == "Janet"


def test_user_not_found():
    url = 'https://reqres.in/api/users/23'
    response: Response = requests.get(url)
    assert response.status_code == 404


def test_unknown_validate_schema():
    url = 'https://reqres.in/api/unknown'
    response: Response = requests.get(url)
    assert S(list_unknown_schema) == response.json()


def test_single_resourse_status():
    url = 'https://reqres.in/api/unknown/2'
    response: Response = requests.get(url)
    assert response.status_code != 500


def test_single_resourse_support_url():
    url = 'https://reqres.in/api/unknown/2'
    response: Response = requests.get(url)
    assert response.json()["support"]["url"] == "https://reqres.in/#support-heading"


def test_resourse_response_empty():
    url = 'https://reqres.in/api/unknown/23'
    response: Response = requests.get(url)
    assert response.json() == {}


def test_delay_page_number():
    url = 'https://reqres.in/api/users'
    response: Response = requests.get(url, params={'delay': 3})
    assert response.json()['page'] == 1


def test_email_for_id1():
    url = 'https://reqres.in/api/users'
    response: Response = requests.get(url, params={'delay': 3})
    per_page = response.json()['per_page']
    assert per_page <= 6


def test_delay_response_schema():
    url = 'https://reqres.in/api/users'
    response: Response = requests.get(url, params={'delay': 3})
    assert S(list_user_schema) == response.json()