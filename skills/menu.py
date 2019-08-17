#  Copyright 2019 LINE Corporation
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.


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
            actions=sorted([
                MessageAction(label='장소', text='장소'),
                MessageAction(label='프로그램', text='프로그램'),
                MessageAction(label='가위바위보', text='가위바위보'),
                MessageAction(label='열린 점심', text='열린 점심'),
                URIAction(label='홈페이지', uri='https://www.pycon.kr/'),
                URIAction(
                    label='시간표',
                    uri='https://www.pycon.kr/timetable/talks'
                )
            ], key=lambda x: x.label, reverse=False)
        )
    )
