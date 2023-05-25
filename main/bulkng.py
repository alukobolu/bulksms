from django.conf import settings
import requests
import json
class Bulkng:
    BULKNG_SECRET_KEY = "XKfaxg0swE55wDH8KxG7xCFvQNwi9xKLEcT8UlBFVa1yZpT84XUXk16ewmax"#settings.BULKNG_SECRET_KEY
    base_url = "https://www.bulksmsnigeria.com/api/v2/sms"


    headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
    def send(self,send_from,to,body):
        path = ""
        url = self.base_url + path
        data1={
            "api_token": self.BULKNG_SECRET_KEY,
            "from": send_from,
            "to": to,
            "body": body,
        }
        data2 = json.dumps(data1 , indent=4)
        response = requests.post(url=url , headers=self.headers ,  data=data2)
        print(response.text)
        if response.status_code == 200:
            # response_data = response.json()
            # print(response_data)
            # data =response_data['data']
            # status = response_data['status']
            # return status,data
            return
        else:
            print("wrong")
            return False,"failed"