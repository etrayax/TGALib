
from ..advanced.bot import send


class setChatMenuButton:

    """
   Use this method to change the bot's menu button in a private chat, or the default menu button. Returns True on success.

    Parameters

        Optional :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            menu_button : A JSON-serialized object for the bot's new menu button. Defaults to MenuButtonDefault

    """

    async def set_chat_menu_button(self,
        token : str,
        chat_id : [str, int] = None,
        menu_button : str = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('setChatMenuButton', {

            "chat_id" : chat_id,
            "sticker_set_name" : sticker_set_name,

        }, token, bot_api_server, response)