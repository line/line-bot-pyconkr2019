from linebot.models import TextSendMessage
from skills import add_skill
import random


@add_skill(r'주사위')
def get_dice(message):
    return TextSendMessage(
        text=str(random.randint(1, 6))
    )
