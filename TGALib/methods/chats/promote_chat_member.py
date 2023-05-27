
from ..advanced.bot import send


class promoteChatMember:

    """
   Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user. Returns True on success.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            user_id (int) : Unique identifier of the target user.

        Optional :

            is_anonymous (bool) : ass True if the administrator's presence in the chat is hidden.

            can_manage_chat (bool) : Pass True if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege.

            can_post_messages (bool) : Pass True if the administrator can create channel posts, channels only.

            can_edit_messages (bool) : Pass True if the administrator can edit messages of other users and can pin messages, channels only.

            can_delete_messages (bool) : Pass True if the administrator can delete messages of other users.

            can_manage_video_chats (bool) : Pass True if the administrator can manage video chats.

            can_restrict_members (bool) : Pass True if the administrator can restrict, ban or unban chat members.

            can_promote_members (bool) : Pass True if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by him).

            can_change_info (bool) : Pass True if the administrator can change chat title, photo and other settings.

            can_invite_users (bool) : Pass True if the administrator can invite new users to the chat.

            can_pin_messages (bool) : Pass True if the administrator can pin messages, supergroups only.

            can_manage_topics (bool) : Pass True if the user is allowed to create, rename, close, and reopen forum topics, supergroups only.
        
    """

    async def promote_chat_member(self,
        token : str,
        chat_id : [str | int],
        user_id : int,
        is_anonymous : bool = None,
        can_manage_chat : bool = None,
        can_post_messages : bool = None,
        can_edit_messages : bool = None,
        can_delete_messages : bool = None,
        can_manage_video_chats : bool = None,
        can_restrict_members : bool = None,
        can_promote_members : bool = None,
        can_change_info : bool = None,
        can_invite_users : bool = None,
        can_pin_messages : bool = None,
        can_manage_topics : bool = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('promoteChatMember', {

            "chat_id" : chat_id,
            "user_id" : user_id,
            "is_anonymous" : is_anonymous,
            "can_manage_chat" : can_manage_chat,
            "can_post_messages" : can_post_messages,
            "can_edit_messages" : can_edit_messages,
            "can_delete_messages" : can_delete_messages,
            "can_manage_video_chats" : can_manage_video_chats,
            "can_restrict_members" : can_restrict_members,
            "can_promote_members" : can_promote_members,
            "can_change_info" : can_change_info,
            "can_invite_users" : can_invite_users,
            "can_pin_messages" : can_pin_messages,
            "can_manage_topics" : can_manage_topics,

        }, token, bot_api_server, response)