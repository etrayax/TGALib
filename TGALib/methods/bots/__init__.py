
from .answer_callback_query import answerCallbackQuery
from .answer_inline_query import answerInlineQuery
from .answer_web_app_query import answerWebAppQuery

class Bots(
    answerCallbackQuery,
    answerInlineQuery,
    answerWebAppQuery
):...