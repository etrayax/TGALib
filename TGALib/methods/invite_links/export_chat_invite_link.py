
from ..advanced.bot import send


class exportChatInviteLink:

    """
   Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as String on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

    """

    async def export_chat_invite_link(self,
        token : str,
        chat_id : [str, int],
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('exportChatInviteLink', {

            "chat_id" : chat_id,

        }, token, bot_api_server, response)