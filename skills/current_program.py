"""현재 진행중인 세션을 표시하는 기능"""
import datetime

from linebot.models import (
    CarouselTemplate, CarouselColumn,
    TemplateSendMessage, TextSendMessage, URIAction,
)

from skills import add_skill
from skills.programs import get_programs


def utcnow():
    """Actual UTC datetime with UTC timezone attached"""
    return datetime.datetime.now(datetime.timezone.utc)


@add_skill(r'[현재세션|현재프로그램]')
def get_current_program(message) -> TemplateSendMessage:
    """현재 진행중인 프로그램을 소개합니다."""
    def limit_len(text, limit):
        return text if len(text) < limit else text[:limit-1] + '…'

    current_programs = [
        p for p in get_programs()
        if p.startedAt < utcnow() < p.finishedAt
    ]

    columns = [
        CarouselColumn(
            thumbnail_image_url=program.owner.profile.image,
            title=limit_len(program.name, 40),
            text=limit_len(program.desc, 60),
            actions=[
                URIAction(
                    label='자세히 보기',
                    uri=(f"https://www.pycon.kr/program/talk-detail"
                         f"?id={program.id}")
                )
            ]
        )
        for program in current_programs
    ][:10]

    if not columns:
        return TextSendMessage(
            '현재 진행중인 프로그램이 없네요! 부스를 둘러보시는 것은 어떨까요?'
        )

    return TemplateSendMessage(
        alt_text='https://www.pycon.kr/program/talks',
        template=CarouselTemplate(columns=columns)
    )
