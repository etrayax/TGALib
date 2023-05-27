
from ..advanced.bot import send


class setChatTitle:

    """
   Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            title (str) : New chat title, 1-128 characters.

    """

    async def set_chat_title(self,
        token : str,
        chat_id : [str, int],
        title : str,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('setChatTitle', {

            "chat_id" : chat_id,
            "title" : title,

        }, token, bot_api_server, response)