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
                            )
from linebot.models import TextSendMessage
from skills import add_skill


@add_skill(r'열린점심')
def get_lunch_sunday(message):
    return TemplateSendMessage(
        alt_text='열린 점심 위치 안내',
        template=ButtonsTemplate(
            title='열린 점심',
            text='열린 점심 목록입니다',
            actions=sorted([
                MessageAction(label='피알앤디컴퍼니', text='피알앤디컴퍼니'),
                MessageAction(label='ML2', text='ML2'),
                MessageAction(label='미래에셋대우', text='미래에셋대우'),
                MessageAction(label='SW마이스터고등학교', text='SW마이스터고등학교')
            ], key=lambda x: x.label, reverse=False)
        )
    )


@add_skill(r'피알앤디컴퍼니')
def get_lunch_pr(message):
    return TextSendMessage(
        text='일요일 오후 1시 ~ 2시 코엑스 그랜드볼룸 2층 209호B 피알앤디컴퍼니',
    )


@add_skill(r'ML2')
def get_lunch_ML2(message):
    return TextSendMessage(
        text='일요일 오후 1시 ~ 2시 코엑스 그랜드볼룸 2층 201호 (G,10)',
    )


@add_skill(r'미래에셋대우')
def get_lunch_MIRAE(message):
    return TextSendMessage(
        text='일요일 오후 1시 ~ 2시 코엑스 그랜드볼룸 2층 201호 미래에셋대우',
    )


@add_skill(r'SW마이스터고등학교')
def get_lunch_SW(message):
    return TextSendMessage(
        text='일요일 오후 12시 ~ 1시 30분 코엑스 그랜드볼룸 2층 209A호',
    )
