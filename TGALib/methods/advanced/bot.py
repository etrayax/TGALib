import requests
from threading import Thread

async def send(method : str, params : dict, token : str, bot_api_server : str, response : bool):

    if not token:

        return {"ok": 'false', 'resaul': "Token van not be empty."}
    
    if not method:

        return {"ok": 'false', 'resaul': "Methods van not be empty."}

    if response:

        try:

            return requests.post(f"{bot_api_server}/bot{token}/{method}", data=params).json()['result']

        except Exception as error:

            return {"ok": 'false', 'resaul': error}
    
    else:

        try:
            Thread(target=requests.post, kwargs={"url" : f"{bot_api_server}/bot{token}/{method}", "data" : params}).start()

        except:

            ...

    return {"ok": 'True'}