import requests
import json


def uploadImagePet(petID):
    # URL API
    url = f'https://petstore.swagger.io/v2/pet/{petID}/uploadImage'

    # پارامترهای درخواست
    headers = {
        'accept': 'application/json',
    }

    # فایل برای آپلود
    files = {
        'file': ('PetDogs.jpg', open('Document/UploadFile/PetDogs.jpg', 'rb'), 'image/jpeg')
    }

    print("=============Start Test 1=================")
    # ارسال درخواست POST
    response = requests.post(url, headers=headers, files=files)
    print(f'Status Code: {response.status_code}')

    printResponse1 = input("Do you want the response to be printed? (Y/N): ")
    if printResponse1 == 'Y':
        # نمایش وضعیت و پاسخ سرور
        print(f'Status Code: {response.status_code}')
        try:
            print(f'Response JSON: {response.json()}')
        except json.JSONDecodeError:
            print("Response content is not in JSON format")
        print(f'Response Headers: {response.headers}')

    if response.status_code == 200:
        print('Test "Add Image To Pet" : PASS')
    else:
        print(f'Status Code: {response.status_code}')
        print('Add Image to pet Fail : X')

    print("==============End Test 1===================")

def addPet():
    urlAddPet = 'https://petstore.swagger.io/v2/pet'
    body = {
        "id": f'{petID}',
        "category": {
            "id": 1,
            "name": "dogs"
        },
        "name": "jimmyPet",
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

    print("=============Start Test 2==================")

    response = requests.post(urlAddPet, headers=headers, data=json.dumps(body))
    print(f'Status Code: {response.status_code}')

    printResponse = input("Do you want the response to be printed? (Y/N): ")
    if printResponse == "Y":
        try:
            assert response.status_code == 200
            print(f"Status Code : {response.status_code}")
            print(f"Response JSON : {response.json()}")
            print(f"Response Headers : {response.headers}")
        except AssertionError:
            print(f"Status Code : {response.status_code}")
            print("Test Fail : X")
        except json.JSONDecodeError:
            print("Response content is not in JSON format")
            print(f"Response Text : {response.text}")
            print(f"Response Headers : {response.headers}")

    if response.status_code == 200:
        print('Test "Add Pet" : PASS')
    else:
        print('Test "Add Pet" : FAIL')

    print("==============End Test 2===================")

# فراخوانی توابع برای تست
if __name__ == "__main__":
    petID = int(input("Enter your pet ID: "))
    uploadImagePet(petID)
    addPet()
