
from ..advanced.bot import send


class unpinChatMessage:

    """
   Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

        Optional :

            message_id (int) : Identifier of a message to unpin. If not specified, the most recent pinned message (by sending date) will be unpinned.
    """

    async def unpin_chat_message(self,
        token : str,
        chat_id : [str, int],
        message_id : int = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('unpinChatMessage', {

            "chat_id" : chat_id,
            "message_id" : message_id,

        }, token, bot_api_server, response)