
from ..advanced.bot import send


class unbanChatMember:

    """
   Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            user_id (int) : Unique identifier of the target user.

        Optional :

            only_if_banned (bool) : Do nothing if the user is not banned.

    """

    async def unban_chat_member(self,
        token : str,
        chat_id : [str, int],
        user_id : int,
        only_if_banned : bool = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('unbanChatMember', {

            "chat_id" : chat_id,
            "user_id" : user_id,
            "only_if_banned" : only_if_banned,

        }, token, bot_api_server, response)