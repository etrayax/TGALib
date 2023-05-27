
from ..advanced.bot import send


class editChatInviteLink:

    """
   Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a ChatInviteLink object.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            invite_link (str) : The invite link to edit.
        
        Optional :

            name (str) : Invite link name; 0-32 characters.

            expire_date (int) : Point in time (Unix timestamp) when the link will expire.

            member_limit (int) : The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999.

            creates_join_request (bool) : True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified.

    """

    async def edit_chat_invite_link(self,
        token : str,
        chat_id : [str, int],
        invite_link : str = None,
        name : str = None,
        expire_date : int = None,
        member_limit : int = None,
        creates_join_request : bool = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('editChatInviteLink', {
            
            "chat_id" : chat_id,
            "invite_link" : invite_link,
            "name" : name,
            "expire_date" : expire_date,
            "member_limit" : member_limit,
            "creates_join_request" : creates_join_request,

        }, token, bot_api_server, response)