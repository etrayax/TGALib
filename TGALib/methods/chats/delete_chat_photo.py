
from ..advanced.bot import send


class deleteChatPhoto:

    """
   Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

    """

    async def delete_chat_photo(self,
        token : str,
        chat_id : [str, int],
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('deleteChatPhoto', {

            "chat_id" : chat_id,

        }, token, bot_api_server, response)