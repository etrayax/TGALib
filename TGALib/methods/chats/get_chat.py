
from ..advanced.bot import send


class getChat:

    """
   Use this method to get the number of members in a chat. Returns Int on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

    """

    async def get_chat(self,
        token : str,
        chat_id : [str, int],
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('getChat', {

            "chat_id" : chat_id,

        }, token, bot_api_server, response)