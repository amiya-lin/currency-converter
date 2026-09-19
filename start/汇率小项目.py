import requests
import json

def get_rates():
    url = "https://open.er-api.com/v6/latest/usd"

    response = requests.get(url)
    date = response.json()
    return date["rates"]


def get_amount():
    while True:
        try :
            a = float(input("please input the amountUS"))

            if a<= 0:
                print("it must bigger than 0")
                continue

            return a

        except ValueError:
            print("please write the correct number")

rates = get_rates()
usd = get_amount()

CNY = usd * rates["CNY"]
JPY = usd * rates["JPY"]

print(f"RMB:{CNY}")
print(f"JPY:{JPY}")
