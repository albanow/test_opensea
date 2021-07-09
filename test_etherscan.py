import requests

url = "https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress=0xedb61f74b0d09b2558f1eeb79b247c1f363ae452&apikey=P5GXE22Y4R69W5ECI3V4H2XDTF1H93YZC9"


response = requests.request("GET", url)




json_response = response.json()

print(json_response)