
from ..advanced.bot import send


class stopPoll:

    """
    Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int) : Identifier of the original message with the poll.

        Optional :

            reply_markup : A JSON-serialized object for a new message inline keyboard.
    """

    async def stop_poll(self,
        token : str,
        chat_id : [str, int],
        message_id : int,
        reply_markup = None,
        response : bool = True,
        bot_api_server : str = "https://api.telegram.org"
    ):

        return await send("stopPoll", {

            "chat_id" : chat_id,
            "message_id" : message_id,
            "reply_markup" : reply_markup,

        }, token, bot_api_server, response)