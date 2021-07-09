import requests

#url = "https://api.opensea.io/api/v1/asset_contract/0xedb61f74b0d09b2558f1eeb79b247c1f363ae452"


#response = requests.request("GET", url)


url = "https://api.opensea.io/api/v1/assets"


for i in range(1,10):

    querystring = {"token_ids":i,"collection":"guttercatgang"}
    response = requests.request("GET", url, params=querystring)
    json_response = response.json()

    if json_response["assets"][0]["sell_orders"] is not None:        
        print(json_response["assets"][0]["sell_orders"][0]["current_price"])
    else:
        print(i)
