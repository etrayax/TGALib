
from ..advanced.bot import send


class revokeChatInviteLink:

    """
   Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            invite_link (str) : The invite link to edit.

    """

    async def revoke_chat_invite_link(self,
        token : str,
        chat_id : [str, int],
        invite_link : str = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('revokeChatInviteLink', {
            
            "chat_id" : chat_id,
            "invite_link" : invite_link,

        }, token, bot_api_server, response)