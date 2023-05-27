
from ..advanced.bot import send


class setChatStickerSet:

    """
   Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            sticker_set_name (str) : Name of the sticker set to be set as the group sticker set.

    """

    async def set_chat_sticker_set(self,
        token : str,
        chat_id : [str, int],
        sticker_set_name : str,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('setChatStickerSet', {

            "chat_id" : chat_id,
            "sticker_set_name" : sticker_set_name,

        }, token, bot_api_server, response)