
# from ..advanced.bot import send


class editMessageCaption:

    """
    Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

    Parameters

        Optional :

            chat_id (str | int) : Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int) : Required if inline_message_id is not specified. Identifier of the message to edit.

            inline_message_id (str) : Required if chat_id and message_id are not specified. Identifier of the inline message.

            caption (str) : New caption of the message, 0-1024 characters after entities parsing.

            parse_mode (str) : Mode for parsing entities in the message caption. See formatting options for more details.

            caption_entities : A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode.

            reply_markup : A JSON-serialized object for an inline keyboard.
            
    """

    async def edit_message_caption(self,
        token : str,
        chat_id : [str, int] = None,
        message_id : int = None,
        inline_message_id : str = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities = None,
        reply_markup = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('editMessageCaption', {

            "chat_id" : chat_id,
            "message_id" : message_id,
            "inline_message_id" : inline_message_id,
            "caption" : caption,
            "parse_mode" : parse_mode,
            "caption_entities" : caption_entities,
            "reply_markup" : reply_markup,

        }, token, bot_api_server, response)

