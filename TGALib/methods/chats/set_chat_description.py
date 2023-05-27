
from ..advanced.bot import send


class setChatDescription:

    """
   Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            description (str) : New chat description, 0-255 characters.

    """

    async def set_chat_description(self,
        token : str,
        chat_id : [str, int],
        description : str,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('setChatDescription', {

            "chat_id" : chat_id,
            "description" : description,

        }, token, bot_api_server, response)