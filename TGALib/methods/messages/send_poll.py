
from ..advanced.bot import send


class sendPoll:

    """
    Use this method to send a native poll. On success, the sent Message is returned.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            question (str) : Poll question, 1-300 characters.

            options : A JSON-serialized list of answer options, 2-10 strings 1-100 characters each.
        
        Optional :

            message_thread_id (int) : Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            is_anonymous (bool) : True, if the poll needs to be anonymous, defaults to True.

            type (str) : Poll type, “quiz” or “regular”, defaults to “regular".

            allows_multiple_answers (bool) : True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False.

            correct_option_id (int) : 0-based identifier of the correct answer option, required for polls in quiz mode.

            explanation (str) : Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing.

            explanation_parse_mode (str) : Mode for parsing entities in the explanation. See formatting options for more details.

            explanation_entities :  JSON-serialized list of special entities that appear in the poll explanation, which can be specified instead of parse_mode.

            open_period (int) : Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date.

            lose_date (int) : Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with open_period.

            is_closed (bool) : Pass True if the poll needs to be immediately closed. This can be useful for poll preview.

            disable_notification (bool) : Sends the message silently. Users will receive a notification with no sound.

            protect_content (bool) : Protects the contents of the sent message from forwarding and saving.

            reply_to_message_id (int) : If the message is a reply, ID of the original message.

            allow_sending_without_reply (bool) : Pass True if the message should be sent even if the specified replied-to message is not found.

            reply_markup : Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """

    async def send_poll(self,
        token : str,
        chat_id : [str, int],
        question : str,
        options,
        message_thread_id : int = None,
        is_anonymous : bool = None,
        _type : str = None,
        allows_multiple_answers : bool = None,
        correct_option_id : int = None,
        explanation : str = None,
        explanation_parse_mode : str = None,
        explanation_entities = None,
        open_period : int = None,
        close_date : int = None,
        is_closed : bool = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
        reply_markup = None,
        response : bool = True,
        bot_api_server : str = "https://api.telegram.org"
    ):

        return await send("sendPoll", {

            "chat_id" : chat_id,
            "question" : question,
            "options" : options,
            "message_thread_id" : message_thread_id,
            "is_anonymous" : is_anonymous,
            "type" : _type,
            "allows_multiple_answers" : allows_multiple_answers,
            "correct_option_id" : correct_option_id,
            "explanation" : explanation,
            "explanation_parse_mode" : explanation_parse_mode,
            "explanation_entities" : explanation_entities,
            "open_period" : open_period,
            "close_date" : close_date,
            "is_closed" : is_closed,
            "disable_notification" : disable_notification,
            "protect_content" : protect_content,
            "reply_to_message_id" : reply_to_message_id,
            "allow_sending_without_reply" : allow_sending_without_reply,
            "reply_markup" : reply_markup,

        }, token, bot_api_server, response)