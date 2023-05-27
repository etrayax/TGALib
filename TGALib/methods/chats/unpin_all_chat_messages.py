
from ..advanced.bot import send


class unpinAllChatMessages:

    """
   Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

    """

    async def unpin_all_chat_messages(self,
        token : str,
        chat_id : [str, int],
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('unpinAllChatMessages', {

            "chat_id" : chat_id,

        }, token, bot_api_server, response)