
from ..advanced.bot import send


class getChatAdministrators:

    """
   Use this method to get the number of members in a chat. Returns Int on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

    """

    async def get_chat_administrators(self,
        token : str,
        chat_id : [str, int],
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('getChatAdministrators', {

            "chat_id" : chat_id,

        }, token, bot_api_server, response)