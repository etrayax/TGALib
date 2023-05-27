
# from ..advanced.bot import send


class editMessageMedia:

    """
    Use this method to edit animation, audio, document, photo, or video messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

    Parameters

        Required :

            media : A JSON-serialized object for a new media content of the message.

        Optional :

            chat_id (str | int) : Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int) : Required if inline_message_id is not specified. Identifier of the message to edit.

            inline_message_id (str) : Required if chat_id and message_id are not specified. Identifier of the inline message.

            reply_markup : A JSON-serialized object for an inline keyboard.
            
    """

    async def edit_message_media(self,
        token : str,
        medai,
        chat_id : [str, int] = None,
        message_id : int = None,
        inline_message_id : str = None,
        reply_markup = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('editMessageMedia', {

            "media" : media,
            "chat_id" : chat_id,
            "message_id" : message_id,
            "inline_message_id" : inline_message_id,
            "reply_markup" : reply_markup,

        }, token, bot_api_server, response)

