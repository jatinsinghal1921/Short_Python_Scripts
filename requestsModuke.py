import json
import requests
from requests.auth import HTTPBasicAuth,HTTPDigestAuth


cred_obj = open("cred.json","r")
cred_dict = json.load(cred_obj)

# username = cred_dict["user"]
# password = cred_dict["password"]

username = "jatin.singhal@wdc.com"
password = "SansjAlmmn@1913"
session_id = "pc4eq4lwgymfkfi5eputnabm"
url = "http://10.66.5.18/Home.aspx"

payload = {
	'Authorization' : session_id
}

def using_session_id():
	ses = requests.session()
	res = ses.post(url, data=payload)
	print("Response is : ", res)
	res = ses.get(url)
	print(res)


def main():
	using_session_id()


main()