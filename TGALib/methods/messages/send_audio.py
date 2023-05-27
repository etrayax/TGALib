
from ..advanced.bot import send


class sendAudio:

    """
    Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
    
    For sending voice messages, use the sendVoice method instead.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            audio : Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files.

        Optional :

            message_thread_id (int) : Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            caption (str) : Animation caption (may also be used when resending animation by file_id), 0-1024 characters after entities parsing.

            parse_mode (str) : Mode for parsing entities in the animation caption. See formatting options for more details.

            caption_entities : A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode.

            duration (int) : Duration of the audio in seconds.

            performer (str) : Performer.

            title (str) : Track name.

            thumbnail : Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files.

            disable_notification (bool) : Sends the message silently. Users will receive a notification with no sound.

            protect_content (bool) : Protects the contents of the sent message from forwarding and saving.

            reply_to_message_id (int) : If the message is a reply, ID of the original message.

            allow_sending_without_reply (bool) : Pass True if the message should be sent even if the specified replied-to message is not found.

            reply_markup : Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

    """

    async def send_audio(self,
        token : str,
        chat_id : (str, int) = None,
        audio = None,
        message_thread_id : intstr = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities = None,
        duration : int = None,
        performer : str = None,
        title : str = None,
        thumbnail = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
        reply_markup = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('sendAudio', {
            "chat_id" : chat_id,
            "audio" : audio,
            "message_thread_id" : message_thread_id,
            "caption" : caption,
            "parse_mode" : parse_mode,
            "caption_entities" : caption_entities,
            "duration" : duration,
            "performer" : performer,
            "title" : title,
            "thumbnail" : thumbnail,
            "disable_notification" : disable_notification,
            "protect_content" : protect_content,
            "reply_to_message_id" : reply_to_message_id,
            "allow_sending_without_reply" : allow_sending_without_reply,
            "reply_markup" : reply_markup,

        }, token, bot_api_server, response)