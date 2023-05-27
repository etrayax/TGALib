
from ..advanced.bot import send


class restrictChatMember:

    """
   Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user. Returns True on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            user_id (int) : Unique identifier of the target user.

            permissions : A JSON-serialized object for new user permissions.

        Optional :

            use_independent_chat_permissions (bool) : Pass True if chat permissions are set independently. Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages, can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission.

            until_date (int) : Date when restrictions will be lifted for the user, unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever.
        
    """

    async def restrict_chat_member(self,
        token : str,
        chat_id : [str | int],
        user_id : int,
        permissions,
        use_independent_chat_permissions : bool = None,
        until_date : int = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('restrictChatMember', {

            "chat_id" : chat_id,
            "user_id" : user_id,
            "permissions" : permissions,
            "use_independent_chat_permissions" : use_independent_chat_permissions,
            "until_date" : until_date,

        }, token, bot_api_server, response)