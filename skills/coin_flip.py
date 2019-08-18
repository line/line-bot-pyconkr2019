from linebot.models import TextSendMessage
from skills import add_skill
import random


@add_skill(r'동전던지기')
def get_coin(message):
    if random.randint(0, 1) == 0:
        return TextSendMessage(
            text='앞면'
            )
    else:
        return TextSendMessage(
            text='뒷면'
            )
