import requests

resp = requests.get("http://localhost:9999/echo/aaa")
if resp.status_code == 200 and \
resp.text == "Say hello to my little friend: aaa!":
    print("OK")