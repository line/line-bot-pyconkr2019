from linebot.models import LocationSendMessage

from skills import add_skill


@add_skill(r'장소')
def get_location(message):
    return LocationSendMessage(
        title='장소',
        address='서울 강남구 영동대로 513 (삼성동) 코엑스 그랜드볼룸',
        latitude=37.5130556,
        longitude=127.0586111
    )
