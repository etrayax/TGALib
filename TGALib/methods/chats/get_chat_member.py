
from ..advanced.bot import send


class getChatMember:

    """
   Use this method to get information about a member of a chat. The method is only guaranteed to work for other users if the bot is an administrator in the chat. Returns a ChatMember object on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).
        
            user_id (int) : Unique identifier of the target user.
        
    """

    async def get_chat_member(self,
        token : str,
        chat_id : [str | int],
        user_id : int,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('getChatMember', {

            "chat_id" : chat_id,
            "user_id" : user_id,

        }, token, bot_api_server, response)