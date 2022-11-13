import requests
import json
import datetime

GET_TOKEN_URL = "https://api.iq.inrix.com/auth/v1/appToken"


class InrixAPI:
    def __init__(self):
        self.app_token = None
        self.expire_date=""
        self.c=0
    def get(self, url, params):
        #if not self.expire_date or datetime.datetime.strptime(self.expire_date,'%Y-%m-%dT%H:%M:%S.%fZ') < datetime.datetime.now():
        self.app_token = self.get_auth_token()
        self.c+=1
        #print(self.c)
        header = {"Authorization": f"Bearer {self.app_token}"}
        result = requests.get(url, headers=header, params=params)
        return result.json()

    def get_auth_token(self, settings_path="./ConfigFiles/inrix_app.json"):
        app_request_header = {"Accept": "application/json"}

        with open(settings_path, "r") as fp:
            # Not going to reveal my app token
            app_data = json.loads(fp.read())

        # Make the GET request for app token
        # Note: Needs to be stored until expiry date where we'd need to re-call the API to get new token
        params = {"appId": app_data["app_id"], "hashToken": app_data["hash_token"]}
        app_token_request = requests.get(GET_TOKEN_URL, headers=app_request_header, params=params)

        # Note: May need some error handling
        if app_token_request.status_code == 200:
            res = app_token_request.json()
            self.app_token = res["result"]["token"]
            self.expire_date=res["result"]["expiry"]
            return self.app_token
        return None