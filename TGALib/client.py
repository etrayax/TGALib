
def Update(update_id : int, message : "Message", edited_message : "Message", channel_post : "Message", edited_channel_post : "Message", inline_query : "InlineQuery", chosen_inline_result : "ChosenInlineResult", callback_query : "CallbackQuery", shipping_query : "ShippingQuery", pre_checkout_query : "PreCheckoutQuery", poll : "Poll", poll_answer : "PollAnswer", my_chat_member : "ChatMemberUpdated", chat_member : "ChatMemberUpdated", chat_join_request : "ChatJoinRequest"):
    
    return {
        "update_id" : update_id, "message" : message, "edited_message" : edited_message, "channel_post" : channel_post, "edited_channel_post" : edited_channel_post, "inline_query" : inline_query, "chosen_inline_result" : chosen_inline_result, "callback_query" : callback_query, "shipping_query" : shipping_query, "pre_checkout_query" : pre_checkout_query, "poll" : poll, "poll_answer" : poll_answer, "my_chat_member" : my_chat_member, "chat_member" : chat_member, "chat_join_request" : chat_join_request
    }

def getUpdates(offset : int = None, limit : int = None, timeout : int = None, allowed_updates : "Array of String" = None):
    
    return {
        "offset" : offset, "limit" : limit, "timeout" : timeout, "allowed_updates" : allowed_updates
    }

def setWebhook(url : str, certificate : "InputFile" = None, ip_address : str = None, max_connections : int = None, allowed_updates : "Array of String" = None, drop_pending_updates : "Boolean" = None, secret_token : str = None):
    
    return {
        "url" : url, "certificate" : certificate, "ip_address" : ip_address, "max_connections" : max_connections, "allowed_updates" : allowed_updates, "drop_pending_updates" : drop_pending_updates, "secret_token" : secret_token
    }

def deleteWebhook(drop_pending_updates : "Boolean" = None):
    
    return {
        "drop_pending_updates" : drop_pending_updates
    }

def getWebhookInfo():
    
    return {
        
    }

def WebhookInfo(url : str, has_custom_certificate : "Boolean", pending_update_count : int, ip_address : str, last_error_date : int, last_error_message : str, last_synchronization_error_date : int, max_connections : int, allowed_updates : "Array of String"):
    
    return {
        "url" : url, "has_custom_certificate" : has_custom_certificate, "pending_update_count" : pending_update_count, "ip_address" : ip_address, "last_error_date" : last_error_date, "last_error_message" : last_error_message, "last_synchronization_error_date" : last_synchronization_error_date, "max_connections" : max_connections, "allowed_updates" : allowed_updates
    }

def User(id : int, is_bot : "Boolean", first_name : str, last_name : str, username : str, language_code : str, is_premium : "True", added_to_attachment_menu : "True", can_join_groups : "Boolean", can_read_all_group_messages : "Boolean", supports_inline_queries : "Boolean"):
    
    return {
        "id" : id, "is_bot" : is_bot, "first_name" : first_name, "last_name" : last_name, "username" : username, "language_code" : language_code, "is_premium" : is_premium, "added_to_attachment_menu" : added_to_attachment_menu, "can_join_groups" : can_join_groups, "can_read_all_group_messages" : can_read_all_group_messages, "supports_inline_queries" : supports_inline_queries
    }

def Chat(id : int, type : str, title : str, username : str, first_name : str, last_name : str, is_forum : "True", photo : "ChatPhoto", active_usernames : "Array of String", emoji_status_custom_emoji_id : str, bio : str, has_private_forwards : "True", has_restricted_voice_and_video_messages : "True", join_to_send_messages : "True", join_by_request : "True", description : str, invite_link : str, pinned_message : "Message", permissions : "ChatPermissions", slow_mode_delay : int, message_auto_delete_time : int, has_aggressive_anti_spam_enabled : "True", has_hidden_members : "True", has_protected_content : "True", sticker_set_name : str, can_set_sticker_set : "True", linked_chat_id : int, location : "ChatLocation"):
    
    return {
        "id" : id, "type" : type, "title" : title, "username" : username, "first_name" : first_name, "last_name" : last_name, "is_forum" : is_forum, "photo" : photo, "active_usernames" : active_usernames, "emoji_status_custom_emoji_id" : emoji_status_custom_emoji_id, "bio" : bio, "has_private_forwards" : has_private_forwards, "has_restricted_voice_and_video_messages" : has_restricted_voice_and_video_messages, "join_to_send_messages" : join_to_send_messages, "join_by_request" : join_by_request, "description" : description, "invite_link" : invite_link, "pinned_message" : pinned_message, "permissions" : permissions, "slow_mode_delay" : slow_mode_delay, "message_auto_delete_time" : message_auto_delete_time, "has_aggressive_anti_spam_enabled" : has_aggressive_anti_spam_enabled, "has_hidden_members" : has_hidden_members, "has_protected_content" : has_protected_content, "sticker_set_name" : sticker_set_name, "can_set_sticker_set" : can_set_sticker_set, "linked_chat_id" : linked_chat_id, "location" : location
    }

def Message(message_id : int, message_thread_id : int, _from, sender_chat : "Chat", date : int, chat : "Chat", forward_from : "User", forward_from_chat : "Chat", forward_from_message_id : int, forward_signature : str, forward_sender_name : str, forward_date : int, is_topic_message : "True", is_automatic_forward : "True", reply_to_message : "Message", via_bot : "User", edit_date : int, has_protected_content : "True", media_group_id : str, author_signature : str, text : str, entities : "Array of MessageEntity", animation : "Animation", audio : "Audio", document : "Document", photo : "Array of PhotoSize", sticker : "Sticker", video : "Video", video_note : "VideoNote", voice : "Voice", caption : str, caption_entities : "Array of MessageEntity", has_media_spoiler : "True", contact : "Contact", dice : "Dice", game : "Game", poll : "Poll", venue : "Venue", location : "Location", new_chat_members : "Array of User", left_chat_member : "User", new_chat_title : str, new_chat_photo : "Array of PhotoSize", delete_chat_photo : "True", group_chat_created : "True", supergroup_chat_created : "True", channel_chat_created : "True", message_auto_delete_timer_changed : "MessageAutoDeleteTimerChanged", migrate_to_chat_id : int, migrate_from_chat_id : int, pinned_message : "Message", invoice : "Invoice", successful_payment : "SuccessfulPayment", user_shared : "UserShared", chat_shared : "ChatShared", connected_website : str, write_access_allowed : "WriteAccessAllowed", passport_data : "PassportData", proximity_alert_triggered : "ProximityAlertTriggered", forum_topic_created : "ForumTopicCreated", forum_topic_edited : "ForumTopicEdited", forum_topic_closed : "ForumTopicClosed", forum_topic_reopened : "ForumTopicReopened", general_forum_topic_hidden : "GeneralForumTopicHidden", general_forum_topic_unhidden : "GeneralForumTopicUnhidden", video_chat_scheduled : "VideoChatScheduled", video_chat_started : "VideoChatStarted", video_chat_ended : "VideoChatEnded", video_chat_participants_invited : "VideoChatParticipantsInvited", web_app_data : "WebAppData", reply_markup : "InlineKeyboardMarkup"):
    
    return {
        "message_id" : message_id, "message_thread_id" : message_thread_id, "_from" : "_from", "sender_chat" : sender_chat, "date" : date, "chat" : chat, "forward_from" : forward_from, "forward_from_chat" : forward_from_chat, "forward_from_message_id" : forward_from_message_id, "forward_signature" : forward_signature, "forward_sender_name" : forward_sender_name, "forward_date" : forward_date, "is_topic_message" : is_topic_message, "is_automatic_forward" : is_automatic_forward, "reply_to_message" : reply_to_message, "via_bot" : via_bot, "edit_date" : edit_date, "has_protected_content" : has_protected_content, "media_group_id" : media_group_id, "author_signature" : author_signature, "text" : text, "entities" : entities, "animation" : animation, "audio" : audio, "document" : document, "photo" : photo, "sticker" : sticker, "video" : video, "video_note" : video_note, "voice" : voice, "caption" : caption, "caption_entities" : caption_entities, "has_media_spoiler" : has_media_spoiler, "contact" : contact, "dice" : dice, "game" : game, "poll" : poll, "venue" : venue, "location" : location, "new_chat_members" : new_chat_members, "left_chat_member" : left_chat_member, "new_chat_title" : new_chat_title, "new_chat_photo" : new_chat_photo, "delete_chat_photo" : delete_chat_photo, "group_chat_created" : group_chat_created, "supergroup_chat_created" : supergroup_chat_created, "channel_chat_created" : channel_chat_created, "message_auto_delete_timer_changed" : message_auto_delete_timer_changed, "migrate_to_chat_id" : migrate_to_chat_id, "migrate_from_chat_id" : migrate_from_chat_id, "pinned_message" : pinned_message, "invoice" : invoice, "successful_payment" : successful_payment, "user_shared" : user_shared, "chat_shared" : chat_shared, "connected_website" : connected_website, "write_access_allowed" : write_access_allowed, "passport_data" : passport_data, "proximity_alert_triggered" : proximity_alert_triggered, "forum_topic_created" : forum_topic_created, "forum_topic_edited" : forum_topic_edited, "forum_topic_closed" : forum_topic_closed, "forum_topic_reopened" : forum_topic_reopened, "general_forum_topic_hidden" : general_forum_topic_hidden, "general_forum_topic_unhidden" : general_forum_topic_unhidden, "video_chat_scheduled" : video_chat_scheduled, "video_chat_started" : video_chat_started, "video_chat_ended" : video_chat_ended, "video_chat_participants_invited" : video_chat_participants_invited, "web_app_data" : web_app_data, "reply_markup" : reply_markup
    }

def MessageId(message_id : int):
    
    return {
        "message_id" : message_id
    }

def MessageEntity(type : str, offset : int, length : int, url : str, user : "User", language : str, custom_emoji_id : str):
    
    return {
        "type" : type, "offset" : offset, "length" : length, "url" : url, "user" : user, "language" : language, "custom_emoji_id" : custom_emoji_id
    }

def PhotoSize(file_id : str, file_unique_id : str, width : int, height : int, file_size : int):
    
    return {
        "file_id" : file_id, "file_unique_id" : file_unique_id, "width" : width, "height" : height, "file_size" : file_size
    }

def Animation(file_id : str, file_unique_id : str, width : int, height : int, duration : int, thumbnail : "PhotoSize", file_name : str, mime_type : str, file_size : int):
    
    return {
        "file_id" : file_id, "file_unique_id" : file_unique_id, "width" : width, "height" : height, "duration" : duration, "thumbnail" : thumbnail, "file_name" : file_name, "mime_type" : mime_type, "file_size" : file_size
    }

def Audio(file_id : str, file_unique_id : str, duration : int, performer : str, title : str, file_name : str, mime_type : str, file_size : int, thumbnail : "PhotoSize"):
    
    return {
        "file_id" : file_id, "file_unique_id" : file_unique_id, "duration" : duration, "performer" : performer, "title" : title, "file_name" : file_name, "mime_type" : mime_type, "file_size" : file_size, "thumbnail" : thumbnail
    }

def Document(file_id : str, file_unique_id : str, thumbnail : "PhotoSize", file_name : str, mime_type : str, file_size : int):
    
    return {
        "file_id" : file_id, "file_unique_id" : file_unique_id, "thumbnail" : thumbnail, "file_name" : file_name, "mime_type" : mime_type, "file_size" : file_size
    }

def Video(file_id : str, file_unique_id : str, width : int, height : int, duration : int, thumbnail : "PhotoSize", file_name : str, mime_type : str, file_size : int):
    
    return {
        "file_id" : file_id, "file_unique_id" : file_unique_id, "width" : width, "height" : height, "duration" : duration, "thumbnail" : thumbnail, "file_name" : file_name, "mime_type" : mime_type, "file_size" : file_size
    }

def VideoNote(file_id : str, file_unique_id : str, length : int, duration : int, thumbnail : "PhotoSize", file_size : int):
    
    return {
        "file_id" : file_id, "file_unique_id" : file_unique_id, "length" : length, "duration" : duration, "thumbnail" : thumbnail, "file_size" : file_size
    }

def Voice(file_id : str, file_unique_id : str, duration : int, mime_type : str, file_size : int):
    
    return {
        "file_id" : file_id, "file_unique_id" : file_unique_id, "duration" : duration, "mime_type" : mime_type, "file_size" : file_size
    }

def Contact(phone_number : str, first_name : str, last_name : str, user_id : int, vcard : str):
    
    return {
        "phone_number" : phone_number, "first_name" : first_name, "last_name" : last_name, "user_id" : user_id, "vcard" : vcard
    }

def Dice(emoji : str, value : int):
    
    return {
        "emoji" : emoji, "value" : value
    }

def PollOption(text : str, voter_count : int):
    
    return {
        "text" : text, "voter_count" : voter_count
    }

def PollAnswer(poll_id : str, user : "User", option_ids : "Array of Integer"):
    
    return {
        "poll_id" : poll_id, "user" : user, "option_ids" : option_ids
    }

def Poll(id : str, question : str, options : "Array of PollOption", total_voter_count : int, is_closed : "Boolean", is_anonymous : "Boolean", type : str, allows_multiple_answers : "Boolean", correct_option_id : int, explanation : str, explanation_entities : "Array of MessageEntity", open_period : int, close_date : int):
    
    return {
        "id" : id, "question" : question, "options" : options, "total_voter_count" : total_voter_count, "is_closed" : is_closed, "is_anonymous" : is_anonymous, "type" : type, "allows_multiple_answers" : allows_multiple_answers, "correct_option_id" : correct_option_id, "explanation" : explanation, "explanation_entities" : explanation_entities, "open_period" : open_period, "close_date" : close_date
    }

def Location(longitude : "Float", latitude : "Float", horizontal_accuracy : "Float number", live_period : int, heading : int, proximity_alert_radius : int):
    
    return {
        "longitude" : longitude, "latitude" : latitude, "horizontal_accuracy" : horizontal_accuracy, "live_period" : live_period, "heading" : heading, "proximity_alert_radius" : proximity_alert_radius
    }

def Venue(location : "Location", title : str, address : str, foursquare_id : str, foursquare_type : str, google_place_id : str, google_place_type : str):
    
    return {
        "location" : location, "title" : title, "address" : address, "foursquare_id" : foursquare_id, "foursquare_type" : foursquare_type, "google_place_id" : google_place_id, "google_place_type" : google_place_type
    }

def WebAppData(data : str, button_text : str):
    
    return {
        "data" : data, "button_text" : button_text
    }

def ProximityAlertTriggered(traveler : "User", watcher : "User", distance : int):
    
    return {
        "traveler" : traveler, "watcher" : watcher, "distance" : distance
    }

def MessageAutoDeleteTimerChanged(message_auto_delete_time : int):
    
    return {
        "message_auto_delete_time" : message_auto_delete_time
    }

def ForumTopicCreated(name : str, icon_color : int, icon_custom_emoji_id : str):
    
    return {
        "name" : name, "icon_color" : icon_color, "icon_custom_emoji_id" : icon_custom_emoji_id
    }

def ForumTopicClosed():
    
    return {
        
    }

def ForumTopicEdited(name : str, icon_custom_emoji_id : str):
    
    return {
        "name" : name, "icon_custom_emoji_id" : icon_custom_emoji_id
    }

def ForumTopicReopened():
    
    return {
        
    }

def GeneralForumTopicHidden():
    
    return {
        
    }

def GeneralForumTopicUnhidden():
    
    return {
        
    }

def UserShared(request_id : int, user_id : int):
    
    return {
        "request_id" : request_id, "user_id" : user_id
    }

def ChatShared(request_id : int, chat_id : int):
    
    return {
        "request_id" : request_id, "chat_id" : chat_id
    }

def WriteAccessAllowed(web_app_name : str):
    
    return {
        "web_app_name" : web_app_name
    }

def VideoChatScheduled(start_date : int):
    
    return {
        "start_date" : start_date
    }

def VideoChatStarted():
    
    return {
        
    }

def VideoChatEnded(duration : int):
    
    return {
        "duration" : duration
    }

def VideoChatParticipantsInvited(users : "Array of User"):
    
    return {
        "users" : users
    }

def UserProfilePhotos(total_count : int, photos : "Array of Array of PhotoSize"):
    
    return {
        "total_count" : total_count, "photos" : photos
    }

def File(file_id : str, file_unique_id : str, file_size : int, file_path : str):
    
    return {
        "file_id" : file_id, "file_unique_id" : file_unique_id, "file_size" : file_size, "file_path" : file_path
    }

def WebAppInfo(url : str):
    
    return {
        "url" : url
    }

def ReplyKeyboardMarkup(keyboard : "Array of Array of KeyboardButton", is_persistent : "Boolean", resize_keyboard : "Boolean", one_time_keyboard : "Boolean", input_field_placeholder : str, selective : "Boolean"):
    
    return {
        "keyboard" : keyboard, "is_persistent" : is_persistent, "resize_keyboard" : resize_keyboard, "one_time_keyboard" : one_time_keyboard, "input_field_placeholder" : input_field_placeholder, "selective" : selective
    }

def KeyboardButton(text : str, request_user : "KeyboardButtonRequestUser", request_chat : "KeyboardButtonRequestChat", request_contact : "Boolean", request_location : "Boolean", request_poll : "KeyboardButtonPollType", web_app : "WebAppInfo"):
    
    return {
        "text" : text, "request_user" : request_user, "request_chat" : request_chat, "request_contact" : request_contact, "request_location" : request_location, "request_poll" : request_poll, "web_app" : web_app
    }

def KeyboardButtonRequestUser(request_id : int, user_is_bot : "Boolean", user_is_premium : "Boolean"):
    
    return {
        "request_id" : request_id, "user_is_bot" : user_is_bot, "user_is_premium" : user_is_premium
    }

def KeyboardButtonRequestChat(request_id : int, chat_is_channel : "Boolean", chat_is_forum : "Boolean", chat_has_username : "Boolean", chat_is_created : "Boolean", user_administrator_rights : "ChatAdministratorRights", bot_administrator_rights : "ChatAdministratorRights", bot_is_member : "Boolean"):
    
    return {
        "request_id" : request_id, "chat_is_channel" : chat_is_channel, "chat_is_forum" : chat_is_forum, "chat_has_username" : chat_has_username, "chat_is_created" : chat_is_created, "user_administrator_rights" : user_administrator_rights, "bot_administrator_rights" : bot_administrator_rights, "bot_is_member" : bot_is_member
    }

def KeyboardButtonPollType(type : str):
    
    return {
        "type" : type
    }

def ReplyKeyboardRemove(remove_keyboard : "True", selective : "Boolean"):
    
    return {
        "remove_keyboard" : remove_keyboard, "selective" : selective
    }

def InlineKeyboardMarkup(inline_keyboard : "Array of Array of InlineKeyboardButton"):
    
    return {
        "inline_keyboard" : inline_keyboard
    }

def InlineKeyboardButton(text : str, url : str, callback_data : str, web_app : "WebAppInfo", login_url : "LoginUrl", switch_inline_query : str, switch_inline_query_current_chat : str, switch_inline_query_chosen_chat : "SwitchInlineQueryChosenChat", callback_game : "CallbackGame", pay : "Boolean"):
    
    return {
        "text" : text, "url" : url, "callback_data" : callback_data, "web_app" : web_app, "login_url" : login_url, "switch_inline_query" : switch_inline_query, "switch_inline_query_current_chat" : switch_inline_query_current_chat, "switch_inline_query_chosen_chat" : switch_inline_query_chosen_chat, "callback_game" : callback_game, "pay" : pay
    }

def LoginUrl(url : str, forward_text : str, bot_username : str, request_write_access : "Boolean"):
    
    return {
        "url" : url, "forward_text" : forward_text, "bot_username" : bot_username, "request_write_access" : request_write_access
    }

def SwitchInlineQueryChosenChat(query : str, allow_user_chats : "Boolean", allow_bot_chats : "Boolean", allow_group_chats : "Boolean", allow_channel_chats : "Boolean"):
    
    return {
        "query" : query, "allow_user_chats" : allow_user_chats, "allow_bot_chats" : allow_bot_chats, "allow_group_chats" : allow_group_chats, "allow_channel_chats" : allow_channel_chats
    }

def CallbackQuery(id : str, _from, message : "Message", inline_message_id : str, chat_instance : str, data : str, game_short_name : str):
    
    return {
        "id" : id, "_from" : "_from", "message" : message, "inline_message_id" : inline_message_id, "chat_instance" : chat_instance, "data" : data, "game_short_name" : game_short_name
    }

def ForceReply(force_reply : "True", input_field_placeholder : str, selective : "Boolean"):
    
    return {
        "force_reply" : force_reply, "input_field_placeholder" : input_field_placeholder, "selective" : selective
    }

def ChatPhoto(small_file_id : str, small_file_unique_id : str, big_file_id : str, big_file_unique_id : str):
    
    return {
        "small_file_id" : small_file_id, "small_file_unique_id" : small_file_unique_id, "big_file_id" : big_file_id, "big_file_unique_id" : big_file_unique_id
    }

def ChatInviteLink(invite_link : str, creator : "User", creates_join_request : "Boolean", is_primary : "Boolean", is_revoked : "Boolean", name : str, expire_date : int, member_limit : int, pending_join_request_count : int):
    
    return {
        "invite_link" : invite_link, "creator" : creator, "creates_join_request" : creates_join_request, "is_primary" : is_primary, "is_revoked" : is_revoked, "name" : name, "expire_date" : expire_date, "member_limit" : member_limit, "pending_join_request_count" : pending_join_request_count
    }

def ChatAdministratorRights(is_anonymous : "Boolean", can_manage_chat : "Boolean", can_delete_messages : "Boolean", can_manage_video_chats : "Boolean", can_restrict_members : "Boolean", can_promote_members : "Boolean", can_change_info : "Boolean", can_invite_users : "Boolean", can_post_messages : "Boolean", can_edit_messages : "Boolean", can_pin_messages : "Boolean", can_manage_topics : "Boolean"):
    
    return {
        "is_anonymous" : is_anonymous, "can_manage_chat" : can_manage_chat, "can_delete_messages" : can_delete_messages, "can_manage_video_chats" : can_manage_video_chats, "can_restrict_members" : can_restrict_members, "can_promote_members" : can_promote_members, "can_change_info" : can_change_info, "can_invite_users" : can_invite_users, "can_post_messages" : can_post_messages, "can_edit_messages" : can_edit_messages, "can_pin_messages" : can_pin_messages, "can_manage_topics" : can_manage_topics
    }

def ChatMember():
    
    return {
        
    }

def ChatMemberOwner(status : str, user : "User", is_anonymous : "Boolean", custom_title : str):
    
    return {
        "status" : status, "user" : user, "is_anonymous" : is_anonymous, "custom_title" : custom_title
    }

def ChatMemberAdministrator(status : str, user : "User", can_be_edited : "Boolean", is_anonymous : "Boolean", can_manage_chat : "Boolean", can_delete_messages : "Boolean", can_manage_video_chats : "Boolean", can_restrict_members : "Boolean", can_promote_members : "Boolean", can_change_info : "Boolean", can_invite_users : "Boolean", can_post_messages : "Boolean", can_edit_messages : "Boolean", can_pin_messages : "Boolean", can_manage_topics : "Boolean", custom_title : str):
    
    return {
        "status" : status, "user" : user, "can_be_edited" : can_be_edited, "is_anonymous" : is_anonymous, "can_manage_chat" : can_manage_chat, "can_delete_messages" : can_delete_messages, "can_manage_video_chats" : can_manage_video_chats, "can_restrict_members" : can_restrict_members, "can_promote_members" : can_promote_members, "can_change_info" : can_change_info, "can_invite_users" : can_invite_users, "can_post_messages" : can_post_messages, "can_edit_messages" : can_edit_messages, "can_pin_messages" : can_pin_messages, "can_manage_topics" : can_manage_topics, "custom_title" : custom_title
    }

def ChatMemberMember(status : str, user : "User"):
    
    return {
        "status" : status, "user" : user
    }

def ChatMemberRestricted(status : str, user : "User", is_member : "Boolean", can_send_messages : "Boolean", can_send_audios : "Boolean", can_send_documents : "Boolean", can_send_photos : "Boolean", can_send_videos : "Boolean", can_send_video_notes : "Boolean", can_send_voice_notes : "Boolean", can_send_polls : "Boolean", can_send_other_messages : "Boolean", can_add_web_page_previews : "Boolean", can_change_info : "Boolean", can_invite_users : "Boolean", can_pin_messages : "Boolean", can_manage_topics : "Boolean", until_date : int):
    
    return {
        "status" : status, "user" : user, "is_member" : is_member, "can_send_messages" : can_send_messages, "can_send_audios" : can_send_audios, "can_send_documents" : can_send_documents, "can_send_photos" : can_send_photos, "can_send_videos" : can_send_videos, "can_send_video_notes" : can_send_video_notes, "can_send_voice_notes" : can_send_voice_notes, "can_send_polls" : can_send_polls, "can_send_other_messages" : can_send_other_messages, "can_add_web_page_previews" : can_add_web_page_previews, "can_change_info" : can_change_info, "can_invite_users" : can_invite_users, "can_pin_messages" : can_pin_messages, "can_manage_topics" : can_manage_topics, "until_date" : until_date
    }

def ChatMemberLeft(status : str, user : "User"):
    
    return {
        "status" : status, "user" : user
    }

def ChatMemberBanned(status : str, user : "User", until_date : int):
    
    return {
        "status" : status, "user" : user, "until_date" : until_date
    }

def ChatMemberUpdated(chat : "Chat", _from, date : int, old_chat_member : "ChatMember", new_chat_member : "ChatMember", invite_link : "ChatInviteLink", via_chat_folder_invite_link : "Boolean"):
    
    return {
        "chat" : chat, "_from" : "_from", "date" : date, "old_chat_member" : old_chat_member, "new_chat_member" : new_chat_member, "invite_link" : invite_link, "via_chat_folder_invite_link" : via_chat_folder_invite_link
    }

def ChatJoinRequest(chat : "Chat", _from, user_chat_id : int, date : int, bio : str, invite_link : "ChatInviteLink"):
    
    return {
        "chat" : chat, "_from" : "_from", "user_chat_id" : user_chat_id, "date" : date, "bio" : bio, "invite_link" : invite_link
    }

def ChatPermissions(can_send_messages : "Boolean", can_send_audios : "Boolean", can_send_documents : "Boolean", can_send_photos : "Boolean", can_send_videos : "Boolean", can_send_video_notes : "Boolean", can_send_voice_notes : "Boolean", can_send_polls : "Boolean", can_send_other_messages : "Boolean", can_add_web_page_previews : "Boolean", can_change_info : "Boolean", can_invite_users : "Boolean", can_pin_messages : "Boolean", can_manage_topics : "Boolean"):
    
    return {
        "can_send_messages" : can_send_messages, "can_send_audios" : can_send_audios, "can_send_documents" : can_send_documents, "can_send_photos" : can_send_photos, "can_send_videos" : can_send_videos, "can_send_video_notes" : can_send_video_notes, "can_send_voice_notes" : can_send_voice_notes, "can_send_polls" : can_send_polls, "can_send_other_messages" : can_send_other_messages, "can_add_web_page_previews" : can_add_web_page_previews, "can_change_info" : can_change_info, "can_invite_users" : can_invite_users, "can_pin_messages" : can_pin_messages, "can_manage_topics" : can_manage_topics
    }

def ChatLocation(location : "Location", address : str):
    
    return {
        "location" : location, "address" : address
    }

def ForumTopic(message_thread_id : int, name : str, icon_color : int, icon_custom_emoji_id : str):
    
    return {
        "message_thread_id" : message_thread_id, "name" : name, "icon_color" : icon_color, "icon_custom_emoji_id" : icon_custom_emoji_id
    }

def BotCommand(command : str, description : str):
    
    return {
        "command" : command, "description" : description
    }

def BotCommandScope():
    
    return {
        
    }

def BotCommandScopeDefault(type : str):
    
    return {
        "type" : type
    }

def BotCommandScopeAllPrivateChats(type : str):
    
    return {
        "type" : type
    }

def BotCommandScopeAllGroupChats(type : str):
    
    return {
        "type" : type
    }

def BotCommandScopeAllChatAdministrators(type : str):
    
    return {
        "type" : type
    }

def BotCommandScopeChat(type : str, chat_id : [int, str]):
    
    return {
        "type" : type, "chat_id" : chat_id
    }

def BotCommandScopeChatAdministrators(type : str, chat_id : [int, str]):
    
    return {
        "type" : type, "chat_id" : chat_id
    }

def BotCommandScopeChatMember(type : str, chat_id : [int, str], user_id : int):
    
    return {
        "type" : type, "chat_id" : chat_id, "user_id" : user_id
    }

def BotName(name : str):
    
    return {
        "name" : name
    }

def BotDescription(description : str):
    
    return {
        "description" : description
    }

def BotShortDescription(short_description : str):
    
    return {
        "short_description" : short_description
    }

def MenuButton():
    
    return {
        
    }

def MenuButtonCommands(type : str):
    
    return {
        "type" : type
    }

def MenuButtonWebApp(type : str, text : str, web_app : "WebAppInfo"):
    
    return {
        "type" : type, "text" : text, "web_app" : web_app
    }

def MenuButtonDefault(type : str):
    
    return {
        "type" : type
    }

def ResponseParameters(migrate_to_chat_id : int, retry_after : int):
    
    return {
        "migrate_to_chat_id" : migrate_to_chat_id, "retry_after" : retry_after
    }

def InputMedia():
    
    return {
        
    }

def InputMediaPhoto(type : str, media : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", has_spoiler : "Boolean"):
    
    return {
        "type" : type, "media" : media, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "has_spoiler" : has_spoiler
    }

def InputMediaVideo(type : str, media : str, thumbnail : "InputFile or String", caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", width : int, height : int, duration : int, supports_streaming : "Boolean", has_spoiler : "Boolean"):
    
    return {
        "type" : type, "media" : media, "thumbnail" : thumbnail, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "width" : width, "height" : height, "duration" : duration, "supports_streaming" : supports_streaming, "has_spoiler" : has_spoiler
    }

def InputMediaAnimation(type : str, media : str, thumbnail : "InputFile or String", caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", width : int, height : int, duration : int, has_spoiler : "Boolean"):
    
    return {
        "type" : type, "media" : media, "thumbnail" : thumbnail, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "width" : width, "height" : height, "duration" : duration, "has_spoiler" : has_spoiler
    }

def InputMediaAudio(type : str, media : str, thumbnail : "InputFile or String", caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", duration : int, performer : str, title : str):
    
    return {
        "type" : type, "media" : media, "thumbnail" : thumbnail, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "duration" : duration, "performer" : performer, "title" : title
    }

def InputMediaDocument(type : str, media : str, thumbnail : "InputFile or String", caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", disable_content_type_detection : "Boolean"):
    
    return {
        "type" : type, "media" : media, "thumbnail" : thumbnail, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "disable_content_type_detection" : disable_content_type_detection
    }

def InputFile():
    
    return {
        
    }

def getMe():
    
    return {
        
    }

def logOut():
    
    return {
        
    }

def close():
    
    return {
        
    }

def sendMessage(chat_id : [int, str], text : str, message_thread_id : int = None, parse_mode : str = None, entities : "Array of MessageEntity" = None, disable_web_page_preview : "Boolean" = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "text" : text, "parse_mode" : parse_mode, "entities" : entities, "disable_web_page_preview" : disable_web_page_preview, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def forwardMessage(chat_id : [int, str], from_chat_id : [int, str], message_id : int, message_thread_id : int = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "from_chat_id" : from_chat_id, "disable_notification" : disable_notification, "protect_content" : protect_content, "message_id" : message_id
    }

def copyMessage(chat_id : [int, str], from_chat_id : [int, str], message_id : int, message_thread_id : int = None, caption : str = None, parse_mode : str = None, caption_entities : "Array of MessageEntity" = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "from_chat_id" : from_chat_id, "message_id" : message_id, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def sendPhoto(chat_id : [int, str], photo : "InputFile or String", message_thread_id : int = None, caption : str = None, parse_mode : str = None, caption_entities : "Array of MessageEntity" = None, has_spoiler : "Boolean" = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "photo" : photo, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "has_spoiler" : has_spoiler, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def sendAudio(chat_id : [int, str], audio : "InputFile or String", message_thread_id : int = None, caption : str = None, parse_mode : str = None, caption_entities : "Array of MessageEntity" = None, duration : int = None, performer : str = None, title : str = None, thumbnail : "InputFile or String" = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "audio" : audio, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "duration" : duration, "performer" : performer, "title" : title, "thumbnail" : thumbnail, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def sendDocument(chat_id : [int, str], document : "InputFile or String", message_thread_id : int = None, thumbnail : "InputFile or String" = None, caption : str = None, parse_mode : str = None, caption_entities : "Array of MessageEntity" = None, disable_content_type_detection : "Boolean" = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "document" : document, "thumbnail" : thumbnail, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "disable_content_type_detection" : disable_content_type_detection, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def sendVideo(chat_id : [int, str], video : "InputFile or String", message_thread_id : int = None, duration : int = None, width : int = None, height : int = None, thumbnail : "InputFile or String" = None, caption : str = None, parse_mode : str = None, caption_entities : "Array of MessageEntity" = None, has_spoiler : "Boolean" = None, supports_streaming : "Boolean" = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "video" : video, "duration" : duration, "width" : width, "height" : height, "thumbnail" : thumbnail, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "has_spoiler" : has_spoiler, "supports_streaming" : supports_streaming, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def sendAnimation(chat_id : [int, str], animation : "InputFile or String", message_thread_id : int = None, duration : int = None, width : int = None, height : int = None, thumbnail : "InputFile or String" = None, caption : str = None, parse_mode : str = None, caption_entities : "Array of MessageEntity" = None, has_spoiler : "Boolean" = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "animation" : animation, "duration" : duration, "width" : width, "height" : height, "thumbnail" : thumbnail, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "has_spoiler" : has_spoiler, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def sendVoice(chat_id : [int, str], voice : "InputFile or String", message_thread_id : int = None, caption : str = None, parse_mode : str = None, caption_entities : "Array of MessageEntity" = None, duration : int = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "voice" : voice, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "duration" : duration, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def sendVideoNote(chat_id : [int, str], video_note : "InputFile or String", message_thread_id : int = None, duration : int = None, length : int = None, thumbnail : "InputFile or String" = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "video_note" : video_note, "duration" : duration, "length" : length, "thumbnail" : thumbnail, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def sendMediaGroup(chat_id : [int, str], media : "Array of InputMediaAudio, InputMediaDocument, InputMediaPhoto and InputMediaVideo", message_thread_id : int = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "media" : media, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply
    }

def sendLocation(chat_id : [int, str], latitude : "Float number", longitude : "Float number", message_thread_id : int = None, horizontal_accuracy : "Float number" = None, live_period : int = None, heading : int = None, proximity_alert_radius : int = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "latitude" : latitude, "longitude" : longitude, "horizontal_accuracy" : horizontal_accuracy, "live_period" : live_period, "heading" : heading, "proximity_alert_radius" : proximity_alert_radius, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def sendVenue(chat_id : [int, str], latitude : "Float number", longitude : "Float number", title : str, address : str, message_thread_id : int = None, foursquare_id : str = None, foursquare_type : str = None, google_place_id : str = None, google_place_type : str = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "latitude" : latitude, "longitude" : longitude, "title" : title, "address" : address, "foursquare_id" : foursquare_id, "foursquare_type" : foursquare_type, "google_place_id" : google_place_id, "google_place_type" : google_place_type, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def sendContact(chat_id : [int, str], phone_number : str, first_name : str, message_thread_id : int = None, last_name : str = None, vcard : str = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "phone_number" : phone_number, "first_name" : first_name, "last_name" : last_name, "vcard" : vcard, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def sendPoll(chat_id : [int, str], question : str, options : "Array of String", message_thread_id : int = None, is_anonymous : "Boolean" = None, type : str = None, allows_multiple_answers : "Boolean" = None, correct_option_id : int = None, explanation : str = None, explanation_parse_mode : str = None, explanation_entities : "Array of MessageEntity" = None, open_period : int = None, close_date : int = None, is_closed : "Boolean" = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "question" : question, "options" : options, "is_anonymous" : is_anonymous, "type" : type, "allows_multiple_answers" : allows_multiple_answers, "correct_option_id" : correct_option_id, "explanation" : explanation, "explanation_parse_mode" : explanation_parse_mode, "explanation_entities" : explanation_entities, "open_period" : open_period, "close_date" : close_date, "is_closed" : is_closed, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def sendDice(chat_id : [int, str], message_thread_id : int = None, emoji : str = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "emoji" : emoji, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def sendChatAction(chat_id : [int, str], action : str, message_thread_id : int = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "action" : action
    }

def getUserProfilePhotos(user_id : int, offset : int = None, limit : int = None):
    
    return {
        "user_id" : user_id, "offset" : offset, "limit" : limit
    }

def getFile(file_id : str):
    
    return {
        "file_id" : file_id
    }

def banChatMember(chat_id : [int, str], user_id : int, until_date : int = None, revoke_messages : "Boolean" = None):
    
    return {
        "chat_id" : chat_id, "user_id" : user_id, "until_date" : until_date, "revoke_messages" : revoke_messages
    }

def unbanChatMember(chat_id : [int, str], user_id : int, only_if_banned : "Boolean" = None):
    
    return {
        "chat_id" : chat_id, "user_id" : user_id, "only_if_banned" : only_if_banned
    }

def restrictChatMember(chat_id : [int, str], user_id : int, permissions : "ChatPermissions", use_independent_chat_permissions : "Boolean" = None, until_date : int = None):
    
    return {
        "chat_id" : chat_id, "user_id" : user_id, "permissions" : permissions, "use_independent_chat_permissions" : use_independent_chat_permissions, "until_date" : until_date
    }

def promoteChatMember(chat_id : [int, str], user_id : int, is_anonymous : "Boolean" = None, can_manage_chat : "Boolean" = None, can_post_messages : "Boolean" = None, can_edit_messages : "Boolean" = None, can_delete_messages : "Boolean" = None, can_manage_video_chats : "Boolean" = None, can_restrict_members : "Boolean" = None, can_promote_members : "Boolean" = None, can_change_info : "Boolean" = None, can_invite_users : "Boolean" = None, can_pin_messages : "Boolean" = None, can_manage_topics : "Boolean" = None):
    
    return {
        "chat_id" : chat_id, "user_id" : user_id, "is_anonymous" : is_anonymous, "can_manage_chat" : can_manage_chat, "can_post_messages" : can_post_messages, "can_edit_messages" : can_edit_messages, "can_delete_messages" : can_delete_messages, "can_manage_video_chats" : can_manage_video_chats, "can_restrict_members" : can_restrict_members, "can_promote_members" : can_promote_members, "can_change_info" : can_change_info, "can_invite_users" : can_invite_users, "can_pin_messages" : can_pin_messages, "can_manage_topics" : can_manage_topics
    }

def setChatAdministratorCustomTitle(chat_id : [int, str], user_id : int, custom_title : str):
    
    return {
        "chat_id" : chat_id, "user_id" : user_id, "custom_title" : custom_title
    }

def banChatSenderChat(chat_id : [int, str], sender_chat_id : int):
    
    return {
        "chat_id" : chat_id, "sender_chat_id" : sender_chat_id
    }

def unbanChatSenderChat(chat_id : [int, str], sender_chat_id : int):
    
    return {
        "chat_id" : chat_id, "sender_chat_id" : sender_chat_id
    }

def setChatPermissions(chat_id : [int, str], permissions : "ChatPermissions", use_independent_chat_permissions : "Boolean" = None):
    
    return {
        "chat_id" : chat_id, "permissions" : permissions, "use_independent_chat_permissions" : use_independent_chat_permissions
    }

def exportChatInviteLink(chat_id : [int, str]):
    
    return {
        "chat_id" : chat_id
    }

def createChatInviteLink(chat_id : [int, str], name : str = None, expire_date : int = None, member_limit : int = None, creates_join_request : "Boolean" = None):
    
    return {
        "chat_id" : chat_id, "name" : name, "expire_date" : expire_date, "member_limit" : member_limit, "creates_join_request" : creates_join_request
    }

def editChatInviteLink(chat_id : [int, str], invite_link : str, name : str = None, expire_date : int = None, member_limit : int = None, creates_join_request : "Boolean" = None):
    
    return {
        "chat_id" : chat_id, "invite_link" : invite_link, "name" : name, "expire_date" : expire_date, "member_limit" : member_limit, "creates_join_request" : creates_join_request
    }

def revokeChatInviteLink(chat_id : [int, str], invite_link : str):
    
    return {
        "chat_id" : chat_id, "invite_link" : invite_link
    }

def approveChatJoinRequest(chat_id : [int, str], user_id : int):
    
    return {
        "chat_id" : chat_id, "user_id" : user_id
    }

def declineChatJoinRequest(chat_id : [int, str], user_id : int):
    
    return {
        "chat_id" : chat_id, "user_id" : user_id
    }

def setChatPhoto(chat_id : [int, str], photo : "InputFile"):
    
    return {
        "chat_id" : chat_id, "photo" : photo
    }

def deleteChatPhoto(chat_id : [int, str]):
    
    return {
        "chat_id" : chat_id
    }

def setChatTitle(chat_id : [int, str], title : str):
    
    return {
        "chat_id" : chat_id, "title" : title
    }

def setChatDescription(chat_id : [int, str], description : str = None):
    
    return {
        "chat_id" : chat_id, "description" : description
    }

def pinChatMessage(chat_id : [int, str], message_id : int, disable_notification : "Boolean" = None):
    
    return {
        "chat_id" : chat_id, "message_id" : message_id, "disable_notification" : disable_notification
    }

def unpinChatMessage(chat_id : [int, str], message_id : int = None):
    
    return {
        "chat_id" : chat_id, "message_id" : message_id
    }

def unpinAllChatMessages(chat_id : [int, str]):
    
    return {
        "chat_id" : chat_id
    }

def leaveChat(chat_id : [int, str]):
    
    return {
        "chat_id" : chat_id
    }

def getChat(chat_id : [int, str]):
    
    return {
        "chat_id" : chat_id
    }

def getChatAdministrators(chat_id : [int, str]):
    
    return {
        "chat_id" : chat_id
    }

def getChatMemberCount(chat_id : [int, str]):
    
    return {
        "chat_id" : chat_id
    }

def getChatMember(chat_id : [int, str], user_id : int):
    
    return {
        "chat_id" : chat_id, "user_id" : user_id
    }

def setChatStickerSet(chat_id : [int, str], sticker_set_name : str):
    
    return {
        "chat_id" : chat_id, "sticker_set_name" : sticker_set_name
    }

def deleteChatStickerSet(chat_id : [int, str]):
    
    return {
        "chat_id" : chat_id
    }

def getForumTopicIconStickers():
    
    return {
        
    }

def createForumTopic(chat_id : [int, str], name : str, icon_color : int = None, icon_custom_emoji_id : str = None):
    
    return {
        "chat_id" : chat_id, "name" : name, "icon_color" : icon_color, "icon_custom_emoji_id" : icon_custom_emoji_id
    }

def editForumTopic(chat_id : [int, str], message_thread_id : int, name : str = None, icon_custom_emoji_id : str = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "name" : name, "icon_custom_emoji_id" : icon_custom_emoji_id
    }

def closeForumTopic(chat_id : [int, str], message_thread_id : int):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id
    }

def reopenForumTopic(chat_id : [int, str], message_thread_id : int):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id
    }

def deleteForumTopic(chat_id : [int, str], message_thread_id : int):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id
    }

def unpinAllForumTopicMessages(chat_id : [int, str], message_thread_id : int):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id
    }

def editGeneralForumTopic(chat_id : [int, str], name : str):
    
    return {
        "chat_id" : chat_id, "name" : name
    }

def closeGeneralForumTopic(chat_id : [int, str]):
    
    return {
        "chat_id" : chat_id
    }

def reopenGeneralForumTopic(chat_id : [int, str]):
    
    return {
        "chat_id" : chat_id
    }

def hideGeneralForumTopic(chat_id : [int, str]):
    
    return {
        "chat_id" : chat_id
    }

def unhideGeneralForumTopic(chat_id : [int, str]):
    
    return {
        "chat_id" : chat_id
    }

def answerCallbackQuery(callback_query_id : str, text : str = None, show_alert : "Boolean" = None, url : str = None, cache_time : int = None):
    
    return {
        "callback_query_id" : callback_query_id, "text" : text, "show_alert" : show_alert, "url" : url, "cache_time" : cache_time
    }

def setMyCommands(commands : "Array of BotCommand", scope : "BotCommandScope" = None, language_code : str = None):
    
    return {
        "commands" : commands, "scope" : scope, "language_code" : language_code
    }

def deleteMyCommands(scope : "BotCommandScope" = None, language_code : str = None):
    
    return {
        "scope" : scope, "language_code" : language_code
    }

def getMyCommands(scope : "BotCommandScope" = None, language_code : str = None):
    
    return {
        "scope" : scope, "language_code" : language_code
    }

def setMyName(name : str = None, language_code : str = None):
    
    return {
        "name" : name, "language_code" : language_code
    }

def getMyName(language_code : str = None):
    
    return {
        "language_code" : language_code
    }

def setMyDescription(description : str = None, language_code : str = None):
    
    return {
        "description" : description, "language_code" : language_code
    }

def getMyDescription(language_code : str = None):
    
    return {
        "language_code" : language_code
    }

def setMyShortDescription(short_description : str = None, language_code : str = None):
    
    return {
        "short_description" : short_description, "language_code" : language_code
    }

def getMyShortDescription(language_code : str = None):
    
    return {
        "language_code" : language_code
    }

def setChatMenuButton(chat_id : int = None, menu_button : "MenuButton" = None):
    
    return {
        "chat_id" : chat_id, "menu_button" : menu_button
    }

def getChatMenuButton(chat_id : int = None):
    
    return {
        "chat_id" : chat_id
    }

def setMyDefaultAdministratorRights(rights : "ChatAdministratorRights" = None, for_channels : "Boolean" = None):
    
    return {
        "rights" : rights, "for_channels" : for_channels
    }

def getMyDefaultAdministratorRights(for_channels : "Boolean" = None):
    
    return {
        "for_channels" : for_channels
    }

def editMessageText(text : str, chat_id : [int, str] = None, message_id : int = None, inline_message_id : str = None, parse_mode : str = None, entities : "Array of MessageEntity" = None, disable_web_page_preview : "Boolean" = None, reply_markup : "InlineKeyboardMarkup" = None):
    
    return {
        "chat_id" : chat_id, "message_id" : message_id, "inline_message_id" : inline_message_id, "text" : text, "parse_mode" : parse_mode, "entities" : entities, "disable_web_page_preview" : disable_web_page_preview, "reply_markup" : reply_markup
    }

def editMessageCaption(chat_id : [int, str] = None, message_id : int = None, inline_message_id : str = None, caption : str = None, parse_mode : str = None, caption_entities : "Array of MessageEntity" = None, reply_markup : "InlineKeyboardMarkup" = None):
    
    return {
        "chat_id" : chat_id, "message_id" : message_id, "inline_message_id" : inline_message_id, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "reply_markup" : reply_markup
    }

def editMessageMedia(media : "InputMedia", chat_id : [int, str] = None, message_id : int = None, inline_message_id : str = None, reply_markup : "InlineKeyboardMarkup" = None):
    
    return {
        "chat_id" : chat_id, "message_id" : message_id, "inline_message_id" : inline_message_id, "media" : media, "reply_markup" : reply_markup
    }

def editMessageLiveLocation(latitude : "Float number", longitude : "Float number", chat_id : [int, str] = None, message_id : int = None, inline_message_id : str = None, horizontal_accuracy : "Float number" = None, heading : int = None, proximity_alert_radius : int = None, reply_markup : "InlineKeyboardMarkup" = None):
    
    return {
        "chat_id" : chat_id, "message_id" : message_id, "inline_message_id" : inline_message_id, "latitude" : latitude, "longitude" : longitude, "horizontal_accuracy" : horizontal_accuracy, "heading" : heading, "proximity_alert_radius" : proximity_alert_radius, "reply_markup" : reply_markup
    }

def stopMessageLiveLocation(chat_id : [int, str] = None, message_id : int = None, inline_message_id : str = None, reply_markup : "InlineKeyboardMarkup" = None):
    
    return {
        "chat_id" : chat_id, "message_id" : message_id, "inline_message_id" : inline_message_id, "reply_markup" : reply_markup
    }

def editMessageReplyMarkup(chat_id : [int, str] = None, message_id : int = None, inline_message_id : str = None, reply_markup : "InlineKeyboardMarkup" = None):
    
    return {
        "chat_id" : chat_id, "message_id" : message_id, "inline_message_id" : inline_message_id, "reply_markup" : reply_markup
    }

def stopPoll(chat_id : [int, str], message_id : int, reply_markup : "InlineKeyboardMarkup" = None):
    
    return {
        "chat_id" : chat_id, "message_id" : message_id, "reply_markup" : reply_markup
    }

def deleteMessage(chat_id : [int, str], message_id : int):
    
    return {
        "chat_id" : chat_id, "message_id" : message_id
    }

def Sticker(file_id : str, file_unique_id : str, type : str, width : int, height : int, is_animated : "Boolean", is_video : "Boolean", thumbnail : "PhotoSize", emoji : str, set_name : str, premium_animation : "File", mask_position : "MaskPosition", custom_emoji_id : str, needs_repainting : "True", file_size : int):
    
    return {
        "file_id" : file_id, "file_unique_id" : file_unique_id, "type" : type, "width" : width, "height" : height, "is_animated" : is_animated, "is_video" : is_video, "thumbnail" : thumbnail, "emoji" : emoji, "set_name" : set_name, "premium_animation" : premium_animation, "mask_position" : mask_position, "custom_emoji_id" : custom_emoji_id, "needs_repainting" : needs_repainting, "file_size" : file_size
    }

def StickerSet(name : str, title : str, sticker_type : str, is_animated : "Boolean", is_video : "Boolean", stickers : "Array of Sticker", thumbnail : "PhotoSize"):
    
    return {
        "name" : name, "title" : title, "sticker_type" : sticker_type, "is_animated" : is_animated, "is_video" : is_video, "stickers" : stickers, "thumbnail" : thumbnail
    }

def MaskPosition(point : str, x_shift : "Float number", y_shift : "Float number", scale : "Float number"):
    
    return {
        "point" : point, "x_shift" : x_shift, "y_shift" : y_shift, "scale" : scale
    }

def InputSticker(sticker : "InputFile or String", emoji_list : "Array of String", mask_position : "MaskPosition", keywords : "Array of String"):
    
    return {
        "sticker" : sticker, "emoji_list" : emoji_list, "mask_position" : mask_position, "keywords" : keywords
    }

def sendSticker(chat_id : [int, str], sticker : "InputFile or String", message_thread_id : int = None, emoji : str = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "sticker" : sticker, "emoji" : emoji, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def getStickerSet(name : str):
    
    return {
        "name" : name
    }

def getCustomEmojiStickers(custom_emoji_ids : "Array of String"):
    
    return {
        "custom_emoji_ids" : custom_emoji_ids
    }

def uploadStickerFile(user_id : int, sticker : "InputFile", sticker_format : str):
    
    return {
        "user_id" : user_id, "sticker" : sticker, "sticker_format" : sticker_format
    }

def createNewStickerSet(user_id : int, name : str, title : str, stickers : "Array of InputSticker", sticker_format : str, sticker_type : str = None, needs_repainting : "Boolean" = None):
    
    return {
        "user_id" : user_id, "name" : name, "title" : title, "stickers" : stickers, "sticker_format" : sticker_format, "sticker_type" : sticker_type, "needs_repainting" : needs_repainting
    }

def addStickerToSet(user_id : int, name : str, sticker : "InputSticker"):
    
    return {
        "user_id" : user_id, "name" : name, "sticker" : sticker
    }

def setStickerPositionInSet(sticker : str, position : int):
    
    return {
        "sticker" : sticker, "position" : position
    }

def deleteStickerFromSet(sticker : str):
    
    return {
        "sticker" : sticker
    }

def setStickerEmojiList(sticker : str, emoji_list : "Array of String"):
    
    return {
        "sticker" : sticker, "emoji_list" : emoji_list
    }

def setStickerKeywords(sticker : str, keywords : "Array of String" = None):
    
    return {
        "sticker" : sticker, "keywords" : keywords
    }

def setStickerMaskPosition(sticker : str, mask_position : "MaskPosition" = None):
    
    return {
        "sticker" : sticker, "mask_position" : mask_position
    }

def setStickerSetTitle(name : str, title : str):
    
    return {
        "name" : name, "title" : title
    }

def setStickerSetThumbnail(name : str, user_id : int, thumbnail : "InputFile or String" = None):
    
    return {
        "name" : name, "user_id" : user_id, "thumbnail" : thumbnail
    }

def setCustomEmojiStickerSetThumbnail(name : str, custom_emoji_id : str = None):
    
    return {
        "name" : name, "custom_emoji_id" : custom_emoji_id
    }

def deleteStickerSet(name : str):
    
    return {
        "name" : name
    }

def InlineQuery(id : str, _from, query : str, offset : str, chat_type : str, location : "Location"):
    
    return {
        "id" : id, "_from" : "_from", "query" : query, "offset" : offset, "chat_type" : chat_type, "location" : location
    }

def answerInlineQuery(inline_query_id : str, results : "Array of InlineQueryResult", cache_time : int = None, is_personal : "Boolean" = None, next_offset : str = None, button : "InlineQueryResultsButton" = None):
    
    return {
        "inline_query_id" : inline_query_id, "results" : results, "cache_time" : cache_time, "is_personal" : is_personal, "next_offset" : next_offset, "button" : button
    }

def InlineQueryResultsButton(text : str, web_app : "WebAppInfo", start_parameter : str):
    
    return {
        "text" : text, "web_app" : web_app, "start_parameter" : start_parameter
    }

def InlineQueryResult():
    
    return {
        
    }

def InlineQueryResultArticle(type : str, id : str, title : str, input_message_content : "InputMessageContent", reply_markup : "InlineKeyboardMarkup", url : str, hide_url : "Boolean", description : str, thumbnail_url : str, thumbnail_width : int, thumbnail_height : int):
    
    return {
        "type" : type, "id" : id, "title" : title, "input_message_content" : input_message_content, "reply_markup" : reply_markup, "url" : url, "hide_url" : hide_url, "description" : description, "thumbnail_url" : thumbnail_url, "thumbnail_width" : thumbnail_width, "thumbnail_height" : thumbnail_height
    }

def InlineQueryResultPhoto(type : str, id : str, photo_url : str, thumbnail_url : str, photo_width : int, photo_height : int, title : str, description : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent"):
    
    return {
        "type" : type, "id" : id, "photo_url" : photo_url, "thumbnail_url" : thumbnail_url, "photo_width" : photo_width, "photo_height" : photo_height, "title" : title, "description" : description, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "reply_markup" : reply_markup, "input_message_content" : input_message_content
    }

def InlineQueryResultGif(type : str, id : str, gif_url : str, gif_width : int, gif_height : int, gif_duration : int, thumbnail_url : str, thumbnail_mime_type : str, title : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent"):
    
    return {
        "type" : type, "id" : id, "gif_url" : gif_url, "gif_width" : gif_width, "gif_height" : gif_height, "gif_duration" : gif_duration, "thumbnail_url" : thumbnail_url, "thumbnail_mime_type" : thumbnail_mime_type, "title" : title, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "reply_markup" : reply_markup, "input_message_content" : input_message_content
    }

def InlineQueryResultMpeg4Gif(type : str, id : str, mpeg4_url : str, mpeg4_width : int, mpeg4_height : int, mpeg4_duration : int, thumbnail_url : str, thumbnail_mime_type : str, title : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent"):
    
    return {
        "type" : type, "id" : id, "mpeg4_url" : mpeg4_url, "mpeg4_width" : mpeg4_width, "mpeg4_height" : mpeg4_height, "mpeg4_duration" : mpeg4_duration, "thumbnail_url" : thumbnail_url, "thumbnail_mime_type" : thumbnail_mime_type, "title" : title, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "reply_markup" : reply_markup, "input_message_content" : input_message_content
    }

def InlineQueryResultVideo(type : str, id : str, video_url : str, mime_type : str, thumbnail_url : str, title : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", video_width : int, video_height : int, video_duration : int, description : str, reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent"):
    
    return {
        "type" : type, "id" : id, "video_url" : video_url, "mime_type" : mime_type, "thumbnail_url" : thumbnail_url, "title" : title, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "video_width" : video_width, "video_height" : video_height, "video_duration" : video_duration, "description" : description, "reply_markup" : reply_markup, "input_message_content" : input_message_content
    }

def InlineQueryResultAudio(type : str, id : str, audio_url : str, title : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", performer : str, audio_duration : int, reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent"):
    
    return {
        "type" : type, "id" : id, "audio_url" : audio_url, "title" : title, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "performer" : performer, "audio_duration" : audio_duration, "reply_markup" : reply_markup, "input_message_content" : input_message_content
    }

def InlineQueryResultVoice(type : str, id : str, voice_url : str, title : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", voice_duration : int, reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent"):
    
    return {
        "type" : type, "id" : id, "voice_url" : voice_url, "title" : title, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "voice_duration" : voice_duration, "reply_markup" : reply_markup, "input_message_content" : input_message_content
    }

def InlineQueryResultDocument(type : str, id : str, title : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", document_url : str, mime_type : str, description : str, reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent", thumbnail_url : str, thumbnail_width : int, thumbnail_height : int):
    
    return {
        "type" : type, "id" : id, "title" : title, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "document_url" : document_url, "mime_type" : mime_type, "description" : description, "reply_markup" : reply_markup, "input_message_content" : input_message_content, "thumbnail_url" : thumbnail_url, "thumbnail_width" : thumbnail_width, "thumbnail_height" : thumbnail_height
    }

def InlineQueryResultLocation(type : str, id : str, latitude : "Float number", longitude : "Float number", title : str, horizontal_accuracy : "Float number", live_period : int, heading : int, proximity_alert_radius : int, reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent", thumbnail_url : str, thumbnail_width : int, thumbnail_height : int):
    
    return {
        "type" : type, "id" : id, "latitude" : latitude, "longitude" : longitude, "title" : title, "horizontal_accuracy" : horizontal_accuracy, "live_period" : live_period, "heading" : heading, "proximity_alert_radius" : proximity_alert_radius, "reply_markup" : reply_markup, "input_message_content" : input_message_content, "thumbnail_url" : thumbnail_url, "thumbnail_width" : thumbnail_width, "thumbnail_height" : thumbnail_height
    }

def InlineQueryResultVenue(type : str, id : str, latitude : "Float", longitude : "Float", title : str, address : str, foursquare_id : str, foursquare_type : str, google_place_id : str, google_place_type : str, reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent", thumbnail_url : str, thumbnail_width : int, thumbnail_height : int):
    
    return {
        "type" : type, "id" : id, "latitude" : latitude, "longitude" : longitude, "title" : title, "address" : address, "foursquare_id" : foursquare_id, "foursquare_type" : foursquare_type, "google_place_id" : google_place_id, "google_place_type" : google_place_type, "reply_markup" : reply_markup, "input_message_content" : input_message_content, "thumbnail_url" : thumbnail_url, "thumbnail_width" : thumbnail_width, "thumbnail_height" : thumbnail_height
    }

def InlineQueryResultContact(type : str, id : str, phone_number : str, first_name : str, last_name : str, vcard : str, reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent", thumbnail_url : str, thumbnail_width : int, thumbnail_height : int):
    
    return {
        "type" : type, "id" : id, "phone_number" : phone_number, "first_name" : first_name, "last_name" : last_name, "vcard" : vcard, "reply_markup" : reply_markup, "input_message_content" : input_message_content, "thumbnail_url" : thumbnail_url, "thumbnail_width" : thumbnail_width, "thumbnail_height" : thumbnail_height
    }

def InlineQueryResultGame(type : str, id : str, game_short_name : str, reply_markup : "InlineKeyboardMarkup"):
    
    return {
        "type" : type, "id" : id, "game_short_name" : game_short_name, "reply_markup" : reply_markup
    }

def InlineQueryResultCachedPhoto(type : str, id : str, photo_file_id : str, title : str, description : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent"):
    
    return {
        "type" : type, "id" : id, "photo_file_id" : photo_file_id, "title" : title, "description" : description, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "reply_markup" : reply_markup, "input_message_content" : input_message_content
    }

def InlineQueryResultCachedGif(type : str, id : str, gif_file_id : str, title : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent"):
    
    return {
        "type" : type, "id" : id, "gif_file_id" : gif_file_id, "title" : title, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "reply_markup" : reply_markup, "input_message_content" : input_message_content
    }

def InlineQueryResultCachedMpeg4Gif(type : str, id : str, mpeg4_file_id : str, title : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent"):
    
    return {
        "type" : type, "id" : id, "mpeg4_file_id" : mpeg4_file_id, "title" : title, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "reply_markup" : reply_markup, "input_message_content" : input_message_content
    }

def InlineQueryResultCachedSticker(type : str, id : str, sticker_file_id : str, reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent"):
    
    return {
        "type" : type, "id" : id, "sticker_file_id" : sticker_file_id, "reply_markup" : reply_markup, "input_message_content" : input_message_content
    }

def InlineQueryResultCachedDocument(type : str, id : str, title : str, document_file_id : str, description : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent"):
    
    return {
        "type" : type, "id" : id, "title" : title, "document_file_id" : document_file_id, "description" : description, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "reply_markup" : reply_markup, "input_message_content" : input_message_content
    }

def InlineQueryResultCachedVideo(type : str, id : str, video_file_id : str, title : str, description : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent"):
    
    return {
        "type" : type, "id" : id, "video_file_id" : video_file_id, "title" : title, "description" : description, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "reply_markup" : reply_markup, "input_message_content" : input_message_content
    }

def InlineQueryResultCachedVoice(type : str, id : str, voice_file_id : str, title : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent"):
    
    return {
        "type" : type, "id" : id, "voice_file_id" : voice_file_id, "title" : title, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "reply_markup" : reply_markup, "input_message_content" : input_message_content
    }

def InlineQueryResultCachedAudio(type : str, id : str, audio_file_id : str, caption : str, parse_mode : str, caption_entities : "Array of MessageEntity", reply_markup : "InlineKeyboardMarkup", input_message_content : "InputMessageContent"):
    
    return {
        "type" : type, "id" : id, "audio_file_id" : audio_file_id, "caption" : caption, "parse_mode" : parse_mode, "caption_entities" : caption_entities, "reply_markup" : reply_markup, "input_message_content" : input_message_content
    }

def InputMessageContent():
    
    return {
        
    }

def InputTextMessageContent(message_text : str, parse_mode : str, entities : "Array of MessageEntity", disable_web_page_preview : "Boolean"):
    
    return {
        "message_text" : message_text, "parse_mode" : parse_mode, "entities" : entities, "disable_web_page_preview" : disable_web_page_preview
    }

def InputLocationMessageContent(latitude : "Float", longitude : "Float", horizontal_accuracy : "Float number", live_period : int, heading : int, proximity_alert_radius : int):
    
    return {
        "latitude" : latitude, "longitude" : longitude, "horizontal_accuracy" : horizontal_accuracy, "live_period" : live_period, "heading" : heading, "proximity_alert_radius" : proximity_alert_radius
    }

def InputVenueMessageContent(latitude : "Float", longitude : "Float", title : str, address : str, foursquare_id : str, foursquare_type : str, google_place_id : str, google_place_type : str):
    
    return {
        "latitude" : latitude, "longitude" : longitude, "title" : title, "address" : address, "foursquare_id" : foursquare_id, "foursquare_type" : foursquare_type, "google_place_id" : google_place_id, "google_place_type" : google_place_type
    }

def InputContactMessageContent(phone_number : str, first_name : str, last_name : str, vcard : str):
    
    return {
        "phone_number" : phone_number, "first_name" : first_name, "last_name" : last_name, "vcard" : vcard
    }

def InputInvoiceMessageContent(title : str, description : str, payload : str, provider_token : str, currency : str, prices : "Array of LabeledPrice", max_tip_amount : int, suggested_tip_amounts : "Array of Integer", provider_data : str, photo_url : str, photo_size : int, photo_width : int, photo_height : int, need_name : "Boolean", need_phone_number : "Boolean", need_email : "Boolean", need_shipping_address : "Boolean", send_phone_number_to_provider : "Boolean", send_email_to_provider : "Boolean", is_flexible : "Boolean"):
    
    return {
        "title" : title, "description" : description, "payload" : payload, "provider_token" : provider_token, "currency" : currency, "prices" : prices, "max_tip_amount" : max_tip_amount, "suggested_tip_amounts" : suggested_tip_amounts, "provider_data" : provider_data, "photo_url" : photo_url, "photo_size" : photo_size, "photo_width" : photo_width, "photo_height" : photo_height, "need_name" : need_name, "need_phone_number" : need_phone_number, "need_email" : need_email, "need_shipping_address" : need_shipping_address, "send_phone_number_to_provider" : send_phone_number_to_provider, "send_email_to_provider" : send_email_to_provider, "is_flexible" : is_flexible
    }

def ChosenInlineResult(result_id : str, _from, location : "Location", inline_message_id : str, query : str):
    
    return {
        "result_id" : result_id, "_from" : "_from", "location" : location, "inline_message_id" : inline_message_id, "query" : query
    }

def answerWebAppQuery(web_app_query_id : str, result : "InlineQueryResult"):
    
    return {
        "web_app_query_id" : web_app_query_id, "result" : result
    }

def SentWebAppMessage(inline_message_id : str):
    
    return {
        "inline_message_id" : inline_message_id
    }

def sendInvoice(chat_id : [int, str], title : str, description : str, payload : str, provider_token : str, currency : str, prices : "Array of LabeledPrice", message_thread_id : int = None, max_tip_amount : int = None, suggested_tip_amounts : "Array of Integer" = None, start_parameter : str = None, provider_data : str = None, photo_url : str = None, photo_size : int = None, photo_width : int = None, photo_height : int = None, need_name : "Boolean" = None, need_phone_number : "Boolean" = None, need_email : "Boolean" = None, need_shipping_address : "Boolean" = None, send_phone_number_to_provider : "Boolean" = None, send_email_to_provider : "Boolean" = None, is_flexible : "Boolean" = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "title" : title, "description" : description, "payload" : payload, "provider_token" : provider_token, "currency" : currency, "prices" : prices, "max_tip_amount" : max_tip_amount, "suggested_tip_amounts" : suggested_tip_amounts, "start_parameter" : start_parameter, "provider_data" : provider_data, "photo_url" : photo_url, "photo_size" : photo_size, "photo_width" : photo_width, "photo_height" : photo_height, "need_name" : need_name, "need_phone_number" : need_phone_number, "need_email" : need_email, "need_shipping_address" : need_shipping_address, "send_phone_number_to_provider" : send_phone_number_to_provider, "send_email_to_provider" : send_email_to_provider, "is_flexible" : is_flexible, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def createInvoiceLink(title : str, description : str, payload : str, provider_token : str, currency : str, prices : "Array of LabeledPrice", max_tip_amount : int = None, suggested_tip_amounts : "Array of Integer" = None, provider_data : str = None, photo_url : str = None, photo_size : int = None, photo_width : int = None, photo_height : int = None, need_name : "Boolean" = None, need_phone_number : "Boolean" = None, need_email : "Boolean" = None, need_shipping_address : "Boolean" = None, send_phone_number_to_provider : "Boolean" = None, send_email_to_provider : "Boolean" = None, is_flexible : "Boolean" = None):
    
    return {
        "title" : title, "description" : description, "payload" : payload, "provider_token" : provider_token, "currency" : currency, "prices" : prices, "max_tip_amount" : max_tip_amount, "suggested_tip_amounts" : suggested_tip_amounts, "provider_data" : provider_data, "photo_url" : photo_url, "photo_size" : photo_size, "photo_width" : photo_width, "photo_height" : photo_height, "need_name" : need_name, "need_phone_number" : need_phone_number, "need_email" : need_email, "need_shipping_address" : need_shipping_address, "send_phone_number_to_provider" : send_phone_number_to_provider, "send_email_to_provider" : send_email_to_provider, "is_flexible" : is_flexible
    }

def answerShippingQuery(shipping_query_id : str, ok : "Boolean", shipping_options : "Array of ShippingOption" = None, error_message : str = None):
    
    return {
        "shipping_query_id" : shipping_query_id, "ok" : ok, "shipping_options" : shipping_options, "error_message" : error_message
    }

def answerPreCheckoutQuery(pre_checkout_query_id : str, ok : "Boolean", error_message : str = None):
    
    return {
        "pre_checkout_query_id" : pre_checkout_query_id, "ok" : ok, "error_message" : error_message
    }

def LabeledPrice(label : str, amount : int):
    
    return {
        "label" : label, "amount" : amount
    }

def Invoice(title : str, description : str, start_parameter : str, currency : str, total_amount : int):
    
    return {
        "title" : title, "description" : description, "start_parameter" : start_parameter, "currency" : currency, "total_amount" : total_amount
    }

def ShippingAddress(country_code : str, state : str, city : str, street_line1 : str, street_line2 : str, post_code : str):
    
    return {
        "country_code" : country_code, "state" : state, "city" : city, "street_line1" : street_line1, "street_line2" : street_line2, "post_code" : post_code
    }

def OrderInfo(name : str, phone_number : str, email : str, shipping_address : "ShippingAddress"):
    
    return {
        "name" : name, "phone_number" : phone_number, "email" : email, "shipping_address" : shipping_address
    }

def ShippingOption(id : str, title : str, prices : "Array of LabeledPrice"):
    
    return {
        "id" : id, "title" : title, "prices" : prices
    }

def SuccessfulPayment(currency : str, total_amount : int, invoice_payload : str, shipping_option_id : str, order_info : "OrderInfo", telegram_payment_charge_id : str, provider_payment_charge_id : str):
    
    return {
        "currency" : currency, "total_amount" : total_amount, "invoice_payload" : invoice_payload, "shipping_option_id" : shipping_option_id, "order_info" : order_info, "telegram_payment_charge_id" : telegram_payment_charge_id, "provider_payment_charge_id" : provider_payment_charge_id
    }

def ShippingQuery(id : str, _from, invoice_payload : str, shipping_address : "ShippingAddress"):
    
    return {
        "id" : id, "_from" : "_from", "invoice_payload" : invoice_payload, "shipping_address" : shipping_address
    }

def PreCheckoutQuery(id : str, _from, currency : str, total_amount : int, invoice_payload : str, shipping_option_id : str, order_info : "OrderInfo"):
    
    return {
        "id" : id, "_from" : "_from", "currency" : currency, "total_amount" : total_amount, "invoice_payload" : invoice_payload, "shipping_option_id" : shipping_option_id, "order_info" : order_info
    }

def PassportData(data : "Array of EncryptedPassportElement", credentials : "EncryptedCredentials"):
    
    return {
        "data" : data, "credentials" : credentials
    }

def PassportFile(file_id : str, file_unique_id : str, file_size : int, file_date : int):
    
    return {
        "file_id" : file_id, "file_unique_id" : file_unique_id, "file_size" : file_size, "file_date" : file_date
    }

def EncryptedPassportElement(type : str, data : str, phone_number : str, email : str, files : "Array of PassportFile", front_side : "PassportFile", reverse_side : "PassportFile", selfie : "PassportFile", translation : "Array of PassportFile", hash : str):
    
    return {
        "type" : type, "data" : data, "phone_number" : phone_number, "email" : email, "files" : files, "front_side" : front_side, "reverse_side" : reverse_side, "selfie" : selfie, "translation" : translation, "hash" : hash
    }

def EncryptedCredentials(data : str, hash : str, secret : str):
    
    return {
        "data" : data, "hash" : hash, "secret" : secret
    }

def setPassportDataErrors(user_id : int, errors : "Array of PassportElementError"):
    
    return {
        "user_id" : user_id, "errors" : errors
    }

def PassportElementError():
    
    return {
        
    }

def PassportElementErrorDataField(source : str, type : str, field_name : str, data_hash : str, message : str):
    
    return {
        "source" : source, "type" : type, "field_name" : field_name, "data_hash" : data_hash, "message" : message
    }

def PassportElementErrorFrontSide(source : str, type : str, file_hash : str, message : str):
    
    return {
        "source" : source, "type" : type, "file_hash" : file_hash, "message" : message
    }

def PassportElementErrorReverseSide(source : str, type : str, file_hash : str, message : str):
    
    return {
        "source" : source, "type" : type, "file_hash" : file_hash, "message" : message
    }

def PassportElementErrorSelfie(source : str, type : str, file_hash : str, message : str):
    
    return {
        "source" : source, "type" : type, "file_hash" : file_hash, "message" : message
    }

def PassportElementErrorFile(source : str, type : str, file_hash : str, message : str):
    
    return {
        "source" : source, "type" : type, "file_hash" : file_hash, "message" : message
    }

def PassportElementErrorFiles(source : str, type : str, file_hashes : "Array of String", message : str):
    
    return {
        "source" : source, "type" : type, "file_hashes" : file_hashes, "message" : message
    }

def PassportElementErrorTranslationFile(source : str, type : str, file_hash : str, message : str):
    
    return {
        "source" : source, "type" : type, "file_hash" : file_hash, "message" : message
    }

def PassportElementErrorTranslationFiles(source : str, type : str, file_hashes : "Array of String", message : str):
    
    return {
        "source" : source, "type" : type, "file_hashes" : file_hashes, "message" : message
    }

def PassportElementErrorUnspecified(source : str, type : str, element_hash : str, message : str):
    
    return {
        "source" : source, "type" : type, "element_hash" : element_hash, "message" : message
    }

def sendGame(chat_id : int, game_short_name : str, message_thread_id : int = None, disable_notification : "Boolean" = None, protect_content : "Boolean" = None, reply_to_message_id : int = None, allow_sending_without_reply : "Boolean" = None, reply_markup : "InlineKeyboardMarkup" = None):
    
    return {
        "chat_id" : chat_id, "message_thread_id" : message_thread_id, "game_short_name" : game_short_name, "disable_notification" : disable_notification, "protect_content" : protect_content, "reply_to_message_id" : reply_to_message_id, "allow_sending_without_reply" : allow_sending_without_reply, "reply_markup" : reply_markup
    }

def Game(title : str, description : str, photo : "Array of PhotoSize", text : str, text_entities : "Array of MessageEntity", animation : "Animation"):
    
    return {
        "title" : title, "description" : description, "photo" : photo, "text" : text, "text_entities" : text_entities, "animation" : animation
    }

def CallbackGame():
    
    return {
        
    }

def setGameScore(user_id : int, score : int, force : "Boolean" = None, disable_edit_message : "Boolean" = None, chat_id : int = None, message_id : int = None, inline_message_id : str = None):
    
    return {
        "user_id" : user_id, "score" : score, "force" : force, "disable_edit_message" : disable_edit_message, "chat_id" : chat_id, "message_id" : message_id, "inline_message_id" : inline_message_id
    }

def getGameHighScores(user_id : int, chat_id : int = None, message_id : int = None, inline_message_id : str = None):
    
    return {
        "user_id" : user_id, "chat_id" : chat_id, "message_id" : message_id, "inline_message_id" : inline_message_id
    }
