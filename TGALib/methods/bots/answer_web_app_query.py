
from ..advanced.bot import send


class answerWebAppQuery:

    """
   Use this method to send answers to an inline query. On success, True is returned.
   No more than 50 results per query are allowed.

    Parameters

        Required :

            web_app_query_id (str) : Unique identifier for the query to be answered.

            result : A JSON-serialized object describing the message to be sent.

    """

    async def answer_web_app_query(self,
        token : str,
        web_app_query_id : str,
        result,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('answerWebAppQuery', {
            
            "web_app_query_id" : web_app_query_id,
"            result" : result,

        }, token, bot_api_server, response)