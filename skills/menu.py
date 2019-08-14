from linebot.models import (ButtonsTemplate,
                            MessageAction,
                            TemplateSendMessage,
                            URIAction,)

from skills import add_skill


@add_skill(r'메뉴')
def get_menu(message):
    return TemplateSendMessage(
        alt_text='Welcome!',
        template=ButtonsTemplate(
            thumbnail_image_url='https://www.pycon.kr/static/images/og-pyconkr-image.png', # noqa
            title='환영합니다!',
            text='안녕하세요. 파이콘 한국 2019의 행사 참여를 돕는 LINE 챗봇입니다. 궁금하신 것을 말씀해주세요!', # noqa
            actions=[
                MessageAction(label='장소', text='장소'),
                MessageAction(label='프로그램', text='프로그램'),
                URIAction(label='홈페이지', uri='https://www.pycon.kr/')
            ]
        )
    )
