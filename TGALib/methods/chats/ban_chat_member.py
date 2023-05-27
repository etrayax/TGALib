
from ..advanced.bot import send


class banChatMember:

    """
   Use this method to get the number of members in a chat. Returns Int on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            user_id (int) : Unique identifier of the target user.

        Optional:

            until_date (int) : Date when the user will be unbanned, unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only.

            revoke_messages (bool) : Pass True to delete all messages from the chat for the user that is being removed. If False, the user will be able to see messages in the group that were sent before the user was removed. Always True for supergroups and channels.
    """

    async def ban_chat_member(self,
        token : str,
        chat_id : [str, int],
        user_id : int,
        until_date : int = None,
        revoke_messages : bool = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('banChatMember', {

            "chat_id" : chat_id,
            "user_id" : user_id,
            "until_date" : until_date,
            "revoke_messages" : revoke_messages,

        }, token, bot_api_server, response)