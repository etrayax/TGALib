
from ..advanced.bot import send


class setChatPhoto:

    """
   Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members administrator rights. Returns True on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            photo : New chat photo, uploaded using multipart/form-data.

    """

    async def set_chat_photo(self,
        token : str,
        chat_id : [str, int],
        photo,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('setChatPhoto', {

            "chat_id" : chat_id,
            "photo" : photo,

        }, token, bot_api_server, response)