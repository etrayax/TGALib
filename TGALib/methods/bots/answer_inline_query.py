
from ..advanced.bot import send


class answerInlineQuery:

    """
   Use this method to send answers to an inline query. On success, True is returned.
   No more than 50 results per query are allowed.

    Parameters

        Required :

            inline_query_id (str) : Unique identifier for the answered query.

            results : A JSON-serialized array of results for the inline query.

        Optional :

            cache_time (int) : The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.

            is_personal (bool) : Pass True if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query.

            next_offset (str) : Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes.

            button : A JSON-serialized object describing a button to be shown above inline query results.

    """

    async def answer_inline_query(self,
        token : str,
        callback_query_id : str,
        text : str = None,
        show_alert : bool = None,
        url : str = None,
        cache_time : int = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('answerInlineQuery', {
            
            "callback_query_id" : callback_query_id,
            "text" : text,
            "show_alert" : show_alert,
            "url" : url,
            "cache_time" : cache_time,

        }, token, bot_api_server, response)