
from ..advanced.bot import send


class pinChatMessage:

    """
   Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int) : Identifier of a message to pin.

        Optional :

            disable_notification (bool) : Pass True if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats.
    """

    async def pin_chat_message(self,
        token : str,
        chat_id : [str, int],
        message_id : int,
        disable_notification : bool = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('pinChatMessage', {

            "chat_id" : chat_id,
            "message_id" : message_id,
            "disable_notification" : disable_notification,

        }, token, bot_api_server, response)