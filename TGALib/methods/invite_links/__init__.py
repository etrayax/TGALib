from .edit_chat_invite_link import editChatInviteLink
from .export_chat_invite_link import exportChatInviteLink
from .decline_chat_join_request import declineChatJoinRequest
from .create_chat_invite_link import createChatInviteLink
from .revoke_chat_invite_link import revokeChatInviteLink
from .approve_chat_join_request import approveChatJoinRequest

class InviteLinks(
    editChatInviteLink,
    exportChatInviteLink,
    declineChatJoinRequest,
    createChatInviteLink,
    revokeChatInviteLink,
    approveChatJoinRequest,
):...