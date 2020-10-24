import json
import requests
import urllib.request


url = "http://10.65.8.38/Home.aspx"

cred_obj = open("cred.json","r")
cred_dict = json.load(cred_obj)

username = cred_dict["user"]
password = cred_dict["password"]

response = requests.get(url, auth=(username,password))
# response = urllib.request.urlopen(url)

print(response)

