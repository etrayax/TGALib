
from ..advanced.bot import send


class answerCallbackQuery:

    """
   Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned.

    Parameters

        Required :

            callback_query_id (str) : Unique identifier for the query to be answered.

        Optional :

            text (str) : Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters.

            show_alert (bool) : If True, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false.

            url (str) : URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @BotFather, specify the URL that opens your game - note that this will only work if the query comes from a callback_game button.
            
            Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.

            cache_time (int) : The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0.

    """

    async def answer_callback_query(self,
        token : str,
        callback_query_id : str,
        text : str = None,
        show_alert : bool = None,
        url : str = None,
        cache_time : int = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('answerCallbackQuery', {
            
            "callback_query_id" : callback_query_id,
            "text" : text,
            "show_alert" : show_alert,
            "url" : url,
            "cache_time" : cache_time,

        }, token, bot_api_server, response)