
from ..advanced.bot import send


class approveChatJoinRequest:

    """
   Use this method to approve a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            user_id (int) : Unique identifier of the target user.

    """

    async def approve_chat_join_request(self,
        token : str,
        chat_id : [str, int],
        user_id : int,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('approveChatJoinRequest', {
            
            "chat_id" : chat_id,
            "user_id" : user_id,

        }, token, bot_api_server, response)