
from ..advanced.bot import send


class getCustomEmojiStickers:

    """
    Use this method to get information about custom emoji stickers by their identifiers. Returns an Array of Sticker objects.

    Parameters

        Required :

            custom_emoji_ids : List of custom emoji identifiers. At most 200 custom emoji identifiers can be specified.

    """

    async def get_custom_emoji_stickers(self,
        token : str,
        custom_emoji_ids = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('getCustomEmojiStickers', {

            "custom_emoji_ids" : custom_emoji_ids,

        }, token, bot_api_server, response)