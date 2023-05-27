
from ..advanced.bot import send


class sendChatAction:

    """
    Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success.
    
    We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            action (str) : Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_voice or upload_voice for voice notes, upload_document for general files, choose_sticker for stickers, find_location for location data, record_video_note or upload_video_note for video notes.

        Optional :

            message_thread_id (int) : Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

    """

    async def send_chat_action(self,
        token : str,
        chat_id : [str, int],
        action : str,
        message_thread_id : int = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('sendChatAction', {

            "chat_id" : chat_id,
            "action" : action,
            "message_thread_id" : message_thread_id,

        }, token, bot_api_server, response)