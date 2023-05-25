# TGALib (Telegram Api Library)

# Usage

```python
from TGALib import Bot, client, method

Bot(
    method="",
      # To set method, example sendMessage, editMessageText and etc.
      # Use module method to see all Telegram methods
    
    params="",
      # To set data, example chat_id, text, message_id and etc.
      # Use the client module to build the data.
      
    token="",
      # To set bot token.
    
    response="",
      # If it is true, it will not wait for a response,
      # if it is false, it will wait for a response
    
    bot_api_server="",
)

