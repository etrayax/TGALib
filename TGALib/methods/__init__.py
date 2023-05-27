from .messages import Messages
from .chats import Chats
from .invite_links import InviteLinks
from .users import Users
from .bots import Bots

class Methods(
    Messages,
    Chats,
    InviteLinks,
    Users,
    Bots
):...