from linebot.models import TextSendMessage

from skills import add_skill


@add_skill(r'안녕')
def get_location(message):
    return TextSendMessage(text='안녕하세요')
