
from ..advanced.bot import send


class forwardMessage:

    """
   Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent Message is returned.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).
        
            message_id (int) : Message identifier in the chat specified in from_chat_id.
        
            from_chat_id (int) : Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername).

        Optional :

            message_thread_id (int) : Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            disable_notification (bool) : Sends the message silently. Users will receive a notification with no sound.

            protect_content (bool) : Protects the contents of the forwarded message from forwarding and saving.
    """

    async def forward_message(self,
        token : str,
        chat_id : [str | int],
        from_chat_id : [str | int],
        message_id : int,
        message_thread_id : int = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('forwardMessage', {

            "chat_id" : chat_id,
            "message_id" : message_id,
            "from_chat_id" : from_chat_id,
            "message_thread_id" : message_thread_id,
            "disable_notification" : disable_notification,
            "protect_content" : protect_content,

        }, token, bot_api_server, response)