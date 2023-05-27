
from ..advanced.bot import send


class editMessageText:

    """
    Use this method to edit text and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

    Parameters

        Required :

            text (str) : Text of the message to be sent, 1-4096 characters after entities parsing.
        
        Optional :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int) : Required if inline_message_id is not specified. Identifier of the message to edit.

            inline_message_id (str) : Required if chat_id and message_id are not specified. Identifier of the inline message.

            parse_mode (str) : Mode for parsing entities in the message text. See formatting options for more details.

            entities : A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode.

            disable_web_page_preview (bool) : Disables link previews for links in this message.

            reply_markup : A JSON-serialized object for an inline keyboard.
    """

    async def edit_message_text(self,
        token : str,
        text : str,
        chat_id : [str | int] = None,
        message_id : int = None,
        inline_message_id : str = None,
        parse_mode : str = None,
        entities = None,
        disable_web_page_preview : bool = None,
        reply_markup = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('editMessageText', {

            "text" : text,
            "chat_id" : chat_id,
            "message_id" : message_id,
            "inline_message_id" : inline_message_id,
            "parse_mode" : parse_mode,
            "entities" : entities,
            "disable_web_page_preview" : disable_web_page_preview,
            "reply_markup" : reply_markup,

        }, token, bot_api_server, response)