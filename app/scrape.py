from threading import Timer
from pygame import mixer

import requests
import json

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


def check_availablity(skus, developer_key):
    print("running")

    for sku in skus:
        url = "https://api.bestbuy.com/v1/products/%s.json?apiKey=%s" %(sku, developer_key)

        res = requests.get(url)

        if (res.ok):
            jData = json.loads(res.content)

            if(jData["orderable"] != "SoldOut"):
                mixer.init()
                mixer.music.load('/1-creator-bawa-sushil-16348.mp3')
                mixer.music.play()

                print("==============================")
                print(json.dumps({
                    "name": jData["name"],
                    "orderable": jData["orderable"],
                    "addToCartUrl": jData["addToCartUrl"],
                    "mobileUrl": jData["mobileUrl"],
                    "inStoreAvailability": jData["inStoreAvailability"],
                    "inStoreAvailabilityUpdateDate": jData["inStoreAvailabilityUpdateDate"],
                    "itemUpdateDate": jData["itemUpdateDate"],
                    "onlineAvailability": jData["onlineAvailability"],
                    "onlineAvailabilityUpdateDate": jData["onlineAvailabilityUpdateDate"],
                }, indent=4))
            else:
                print("SKU: %s, Availablity: %s" %(sku, jData["orderable"]))
        else:
            print("API call failed")

def run():
    RTX_3060TI_SKU = "6439402"
    RTX_3070_SKU = "6429442"

    DEVELOPER_KEY = "SAMPLE_KEY_REPLACE_WITHACTUAL_KEY"
    TIMER = 15

    rt = RepeatedTimer(TIMER, check_availablity, [RTX_3060TI_SKU, RTX_3070_SKU], DEVELOPER_KEY)

if __name__ == "__main__":
    run()
