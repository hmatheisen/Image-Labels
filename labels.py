import requests
import os
import json
from requests.auth import HTTPBasicAuth


class ImageLabels:

    def __init__(self):
        self.uri = "https://gateway.watsonplatform.net"
        self.collection_id = os.getenv("COLLECTION_ID")
        self.username = os.getenv("VISUAL_USERNAME")
        self.password = os.getenv("VISUAL_PASSWORD")

    def fetch_images(self):
        url = self.uri + "/visual-recognition/api/v4/collections/" + self.collection_id + "/images"
        querystring = {"version": "2019-02-11"}
        headers = {
            'X-Watson-Technology-Preview': "2018-10-15",
        }
        auth = HTTPBasicAuth(self.username, self.password)

        return requests.request("GET", url, params=querystring, headers=headers, auth=auth)

    def fetch_image_details(self, image_id):
        url = self.uri + "/visual-recognition/api/v4/collections/" + self.collection_id + "/images/" + image_id
        querystring = {"version": "2019-02-11"}
        headers = {
            'X-Watson-Technology-Preview': "2018-10-15",
        }
        auth = HTTPBasicAuth(self.username, self.password)

        return requests.request("GET", url, params=querystring, headers=headers, auth=auth)

    def update_training_data(self, image):
        url = self.uri + "/visual-recognition/api/v4/collections/" + self.collection_id + "/images/" + image["image_id"] + "/training_data"
        querystring = {"version": "2019-02-11"}
        headers = {
            "Content-Type": "application/json",
            "X-Watson-Technology-Preview": "2018-10-15",
        }
        auth = HTTPBasicAuth(self.username, self.password)

        for obj in image["training_data"]["objects"]:
            obj["object"] = "MM"
        body = json.dumps({
            "objects": image["training_data"]["objects"]
        })

        return requests.request("POST", url, params=querystring, headers=headers, auth=auth, data=body)

    @staticmethod
    def create_file(folder, file):
        f = open(folder + file["source"]["filename"] + ".json", "+w")
        f.write(json.dumps(file))
        f.close()
