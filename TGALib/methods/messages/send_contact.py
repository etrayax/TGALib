
from ..advanced.bot import send


class sendContact:

    """
    Use this method to send phone contacts. On success, the sent Message is returned.

    Parameters

        Required :

            chat_id (str | int) : Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            phone_number (str) : Contact's phone number.

            first_name (str) : Contact's first name.

        Optional :

            message_thread_id (int) : Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            last_name (str) : Contact's last name.

            vcard (str) : Additional data about the contact in the form of a vCard, 0-2048 bytes.

            disable_notification (bool) : Sends the message silently. Users will receive a notification with no sound.

            protect_content (bool) : Protects the contents of the sent message from forwarding and saving.

            reply_to_message_id (int) : If the message is a reply, ID of the original message.

            allow_sending_without_reply (bool) : Pass True if the message should be sent even if the specified replied-to message is not found.

            reply_markup : Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.


    """

    async def send_contact(self,
        token : str,
        chat_id : [str, int],
        phone_number : str,
        first_name : str,
        message_thread_id : int = None,
        last_name : str = None,
        vcard : str = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
        reply_markup = None,
        response : bool = True,
        bot_api_server : str = 'https://api.telegram.org'
    ):

        return await send('sendContact', {

            "chat_id" : chat_id,
            "phone_number" : phone_number,
            "first_name" : first_name,
            "message_thread_id" : message_thread_id,
            "last_name" : last_name,
            "vcard" : vcard,
            "disable_notification" : disable_notification,
            "protect_content" : protect_content,
            "reply_to_message_id" : reply_to_message_id,
            "allow_sending_without_reply" : allow_sending_without_reply,
            "reply_markup" : reply_markup,

        }, token, bot_api_server, response)