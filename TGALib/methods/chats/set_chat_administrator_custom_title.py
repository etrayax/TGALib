
from ..advanced.bot import send


class setChatAdministratorCustomTitle:

    """
   Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            user_id (int) : Unique identifier of the target user.

            custom_title (str) : New custom title for the administrator; 0-16 characters, emoji are not allowed.

    """

    async def set_chat_administrator_custom_title(self,
        token : str,
        chat_id : [str, int],
        user_id : int,
        custom_title : str,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('setChatAdministratorCustomTitle', {

            "chat_id" : chat_id,
            "user_id" : user_id,
            "custom_title" : custom_title,

        }, token, bot_api_server, response)