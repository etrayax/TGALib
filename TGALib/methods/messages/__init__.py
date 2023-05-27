from .edit_message_caption import editMessageCaption
from .send_animation import sendAnimation
from .send_video_note import sendVideoNote
from .send_photo import sendPhoto
from .send_media_group import sendMediaGroup
from .send_dice import sendDice
from .edit_message_reply_markup import editMessageReplyMarkup
from .delete_messages import deleteMessage
from .stop_poll import stopPoll
from .edit_message_media import editMessageMedia
from .send_document import sendDocument
from .edit_message_text import editMessageText
from .send_video import sendVideo
from .send_chat_action import sendChatAction
from .copy_message import copyMessage
from .send_audio import sendAudio
from .send_message import sendMessage
from .get_custom_emoji_stickers import getCustomEmojiStickers
from .send_location import sendLocation
from .send_venue import sendVenue
from .send_poll import sendPoll
from .forward_messages import forwardMessage
from .send_contact import sendContact
from .send_sticker import sendSticker
from .send_voice import sendVoice

class Messages(
    editMessageCaption,
    sendAnimation,
    sendVideoNote,
    sendPhoto,
    sendMediaGroup,
    sendDice,
    editMessageReplyMarkup,
    deleteMessage,
    stopPoll,
    editMessageMedia,
    sendDocument,
    editMessageText,
    sendVideo,
    sendChatAction,
    copyMessage,
    sendAudio,
    sendMessage,
    getCustomEmojiStickers,
    sendLocation,
    sendVenue,
    sendPoll,
    forwardMessage,
    sendContact,
    sendSticker,
    sendVoice,
):...