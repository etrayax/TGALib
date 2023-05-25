from threading import Thread
from requests import post
import sys

def Bot(method : str, params : dict ,token : str, response : bool = True, bot_api_server : str = "https://api.telegram.org") -> dict:
    
    if not token:

        print("Token can not empty.")
        sys.exit()
    
    if not method:

        print("Method can not empty.")
        sys.exit()

    if response:

        try:

            return post(f"{bot_api_server}/bot{token}/{method}", data=params).json()

        except Exception as error:

            return {"ok": 'false', 'resaul': error}
    
    else:

        Thread(target=post, kwargs={"url" : f"{bot_api_server}/bot{token}/{method}", "data" : params}).start()

