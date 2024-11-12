import pytest
import json
import requests
from utils.config import BASE_URL
from pages.main_page import MainPage

with open('../data/addressId.json', 'r') as file:
    address = json.load(file)

with open('../data/unicornId.json', 'r') as file:
    unicorn = json.load(file)

def test_00_get_address_value(driver):
    main_page = MainPage(driver)
    endpoint = main_page.get_endpoint_value()
    new_address = endpoint.replace(f'{BASE_URL}/api/', "")

    address['addressId'] = new_address.strip()
    with open('../data/addressId.json', 'w') as address_file:
        json.dump(address, address_file, indent=4)

def test_01_get_address():
    # Arrange
    address_id = address.get('addressId')

    # Act
    response = requests.get(f'{BASE_URL}/api/{address_id}', verify=False)

    # Assertions
    assert response.status_code == 200
    assert response.json() == []

def test_02_create_new_unicorn():
    # Arrange
    address_id = address.get('addressId')
    body = {
        "name": "Sparkle Angel",
        "age": 2,
        "colour": "blue"
    }

    # Act
    response = requests.post(f'{BASE_URL}/api/{address_id}/unicorns', json=body, verify=False)

    # Assertions
    json_response = json.loads(response.content)
    assert response.status_code == 201
    assert json_response['name'] == "Sparkle Angel"
    assert json_response['age'] == 2
    assert json_response['colour'] == "blue"
    assert json_response['_id'] != ""

    unicorn['unicornId'] = json_response['_id']
    with open("../data/unicornId.json", 'w') as unicorn_file:
        json.dump(unicorn, unicorn_file, indent=4)

def test_03_get_unicorn():
    # Arrange
    unicorn_id = unicorn.get('unicornId')
    address_id = address.get('addressId')
    expected_unicorn = {
        "_id": unicorn_id,
        "name": "Sparkle Angel",
        "age": 2,
        "colour": "blue"
    }

    # Act
    response = requests.get(f'{BASE_URL}/api/{address_id}/unicorns/{unicorn_id}', verify=False)

    # Assertions
    assert response.status_code == 200
    assert response.json() == expected_unicorn

def test_04_update_unicorn_info():
    # Arrange
    unicorn_id = unicorn.get('unicornId')
    address_id = address.get('addressId')
    body = {
        "name": "Sparkle Angel",
        "age": 10,
        "colour": "red"
    }
    # Act
    response = requests.put(f'{BASE_URL}/api/{address_id}/unicorns/{unicorn_id}', json=body, verify=False)

    # Assertions
    assert response.status_code == 200

def test_05_get_updated_unicorn():
    # Arrange
    unicorn_id = unicorn.get('unicornId')
    address_id = address.get('addressId')
    expected_unicorn = {
        "_id": unicorn_id,
        "name": "Sparkle Angel",
        "age": 10,
        "colour": "red"
    }

    # Act
    response = requests.get(f'{BASE_URL}/api/{address_id}/unicorns/{unicorn_id}', verify=False)

    # Assertions
    assert response.status_code == 200
    assert response.json() == expected_unicorn

def test_06_delete_unicorn():
    # Arrange
    unicorn_id = unicorn.get('unicornId')
    address_id = address.get('addressId')

    # Act
    response = requests.delete(f'{BASE_URL}/api/{address_id}/unicorns/{unicorn_id}', verify=False)

    # Assertions
    assert response.status_code == 200

def test_07_validate_deleted_unicorn(teardown):
    # Arrange
    unicorn_id = unicorn.get('unicornId')
    address_id = address.get('addressId')

    # Act
    response = requests.get(f'{BASE_URL}/api/{address_id}/unicorns/{unicorn_id}', verify=False)

    assert response.status_code == 404
    json_response = json.loads(response.content)
    assert json_response['title'] == "Not Found"