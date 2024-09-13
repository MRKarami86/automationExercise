import requests
import json
from jinja2 import Template

def uploadImagePet(petID):
    # URL API
    url = f'https://petstore.swagger.io/v2/pet/{petID}/uploadImage'

    # پارامترهای درخواست
    headers = {
        'accept': 'application/json',
    }

    # فایل برای آپلود فایل
    files = {
        'file': ('PetDogs.jpg', open('Document/UploadFile/PetDogs.jpg', 'rb'), 'image/jpeg')
    }

    # ارسال درخواست POST
    response = requests.post(url, headers=headers, files=files)
    result = {
        'test_name': 'Add Image To Pet',
        'status_code': response.status_code,
        'status': 'PASS' if response.status_code == 200 else 'FAIL',
        'response': response.json() if response.status_code == 200 else response.text
    }
    return result

def addPet():
    urlAddPet = 'https://petstore.swagger.io/v2/pet'
    body = {
        "id": f"{petID}",
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

    response = requests.post(urlAddPet, headers=headers, data=json.dumps(body))
    result = {
        'test_name': 'Add Pet',
        'status_code': response.status_code,
        'status': 'PASS' if response.status_code == 200 else 'FAIL',
        'response': response.json() if response.status_code == 200 else response.text
    }
    return result

def generate_html_report(results):
    template = Template("""
    <html>
    <head>
        <title>Test Report</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            table, th, td {
                border: 1px solid black;
            }
            th, td {
                padding: 10px;
                text-align: left;
            }
            .pass {
                background-color: #c8e6c9;
            }
            .fail {
                background-color: #ffcdd2;
            }
        </style>
    </head>
    <body>
        <h1>Test Report</h1>
        <table>
            <tr>
                <th>Test Name</th>
                <th>Status Code</th>
                <th>Status</th>
                <th>Response</th>
            </tr>
            {% for result in results %}
            <tr class="{{ 'pass' if result.status == 'PASS' else 'fail' }}">
                <td>{{ result.test_name }}</td>
                <td>{{ result.status_code }}</td>
                <td>{{ result.status }}</td>
                <td>{{ result.response }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """)
    html_content = template.render(results=results)
    with open('test_report.html', 'w') as f:
        f.write(html_content)


if __name__ == "__main__":
    petID = int(input("Enter your pet ID: "))
    results = []
    results.append(uploadImagePet(petID))
    results.append(addPet())
    generate_html_report(results)
