import requests
import json

from Demos.getfilever import n

BASE_URL = 'https://petstore.swagger.io/v2'


def test_sql_injection():
    url = f'{BASE_URL}/pet'
    body = {
        "id": 103,
        "category": {
            "id": 1,
            "name": "dogs"
        },
        "name": "jimmyPet'; DROP TABLE pets; --",
        "photoUrls": [
            "./PetDogs.jpg"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    response = requests.post(url, headers=headers, data=json.dumps(body))
    print("\n====================Start JSON File====================")
    print(json.dumps(response.json(), indent=4))
    print("=====================End JSON File=====================")

    # بررسی دقیق‌تر محتوای پاسخ سرور
    assert response.status_code == 200, f"Request failed with status code {response.status_code}"
    response_text = response.text.lower()
    sql_errors = ["syntax error", "unrecognized token", "near", "unterminated", "error in your sql syntax"]
    assert not any(error in response_text for error in sql_errors), "Possible SQL Injection vulnerability detected"


def test_xss():
    url = f'{BASE_URL}/pet'
    body = {
        "id": 103,
        "category": {
            "id": 1,
            "name": "dogs"
        },
        "name": "<script>alert('XSS');</script>",
        "photoUrls": [
            "./PetDogs.jpg"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    response = requests.post(url, headers=headers, data=json.dumps(body))
    print("\n====================Start JSON File====================")
    print(json.dumps(response.json(), indent=4))
    print("=====================End JSON File=====================")

    assert response.status_code == 200, f"Request failed with status code {response.status_code}"
    response_text = response.text.lower()  # تبدیل پاسخ به حروف کوچک برای مقایسه آسان‌تر

    # بررسی وجود اسکریپت در پاسخ سرور
    assert 'alert(' in response_text, "Possible XSS vulnerability detected"


if __name__ == "__main__":
    test_sql_injection()
    test_xss()
