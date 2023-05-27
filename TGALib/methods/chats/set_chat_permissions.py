
from ..advanced.bot import send


class setChatPermissions:

    """
   Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members administrator rights. Returns True on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            permissions : A JSON-serialized object for new default chat permissions.

            use_independent_chat_permissions (bool) : Pass True if chat permissions are set independently. Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages, can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission.

    """

    async def set_chat_permissions(self,
        token : str,
        chat_id : [str, int],
        permissions,
        use_independent_chat_permissions : bool,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('setChatPermissions', {

            "chat_id" : chat_id,
            "permissions" : permissions,
            "use_independent_chat_permissions" : use_independent_chat_permissions,

        }, token, bot_api_server, response)