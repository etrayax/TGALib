
# from ..advanced.bot import send


class deleteMessage:

    """
    Use this method to delete a message, including service messages, with the following limitations:

    - A message can only be deleted if it was sent less than 48 hours ago.
    - Service messages about a supergroup, channel, or forum topic creation can't be deleted.
    - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
    - Bots can delete outgoing messages in private chats, groups, and supergroups.
    - Bots can delete incoming messages in private chats.
    - Bots granted can_post_messages permissions can delete outgoing messages in channels.
    - If the bot is an administrator of a group, it can delete any message there.
    - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.
    Returns True on success.

    The following methods and objects allow your bot to handle stickers and sticker sets.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int) : Identifier of the message to delete.
    """

    async def delete_message(self,
        token : str,
        chat_id : [str, int],
        message_id : int,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('deleteMessage', {

            "chat_id" : chat_id,
            "message_id" : message_id,

        }, token, bot_api_server, response)

