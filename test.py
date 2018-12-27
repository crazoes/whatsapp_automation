import requests

headers = {'content-type' : 'application/json'}
data={"mobile_number":"+91 82916 13939","emulator_name":"Pixel_2_XL_API_28"}
url = "http://localhost:5000/api/v0.1/add_new_contact"
response=requests.post(url,json=data,headers=headers)

