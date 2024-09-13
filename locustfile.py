from locust import HttpUser, TaskSet, task, between

class PetStoreTasks(TaskSet):

    @task
    def add_pet(self):
        url = '/v2/pet'
        body = {
            "id": 103,
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

        self.client.post(url, json=body, headers=headers)

    @task
    def upload_image_pet(self):
        petID = 103
        url = f'/v2/pet/{petID}/uploadImage'

        headers = {
            'accept': 'application/json',
        }

        files = {
            'file': ('PetDogs.jpg', open('Document/UploadFile/PetDogs.jpg', 'rb'), 'image/jpeg')
        }

        self.client.post(url, headers=headers, files=files)

class WebsiteUser(HttpUser):
    tasks = [PetStoreTasks]
    wait_time = between(1, 5)
