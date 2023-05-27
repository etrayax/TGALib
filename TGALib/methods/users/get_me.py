
from ..advanced.bot import send


class getMe:

    """
   A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object.

    """

    async def get_me(self,
        token : str,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('getMe', {}, token, bot_api_server, response)