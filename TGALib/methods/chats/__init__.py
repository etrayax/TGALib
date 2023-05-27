from .restrict_chat_member import restrictChatMember
from .delete_chat_photo import deleteChatPhoto
from .get_chat import getChat
from .get_chat_administrators import getChatAdministrators
from .unpin_chat_message import unpinChatMessage
from .set_chat_menu_button import setChatMenuButton
from .set_chat_administrator_custom_title import setChatAdministratorCustomTitle
from .pin_chat_message import pinChatMessage
from .set_chat_sticker_set import setChatStickerSet
from .set_chat_photo import setChatPhoto
from .delete_chat_sticker_set import deleteChatStickerSet
from .get_chat_member_count import getChatMemberCount
from .set_chat_title import setChatTitle
from .ban_chat_member import banChatMember
from .set_chat_permissions import setChatPermissions
from .promote_chat_member import promoteChatMember
from .get_chat_member import getChatMember
from .set_chat_description import setChatDescription
from .unban_chat_member import unbanChatMember
from .unpin_all_chat_messages import unpinAllChatMessages


class Chats(
    restrictChatMember,
    deleteChatPhoto,
    getChat,
    getChatAdministrators,
    unpinChatMessage,
    setChatMenuButton,
    setChatAdministratorCustomTitle,
    pinChatMessage,
    setChatStickerSet,
    setChatPhoto,
    deleteChatStickerSet,
    getChatMemberCount,
    setChatTitle,
    banChatMember,
    setChatPermissions,
    promoteChatMember,
    getChatMember,
    setChatDescription,
    unbanChatMember,
    unpinAllChatMessages,
):...