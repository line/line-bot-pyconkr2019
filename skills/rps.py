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
                            TextSendMessage,
                            TemplateSendMessage,
                            )
from skills import add_skill

import random
rps = ["가위", "바위", "보"]
WIN_MESSAGE = "축하합니다, 이겼습니다!"
LOSE_MESSAGE = "아쉽네요, 졌습니다."
DRAW_MESSAGE = "비겼습니다."


def get_result_message(bot, result):
    return f"봇이 {bot}를 냈습니다. \n {result}"


def get_rps_result(bot, player):
    if player == bot:
        return get_result_message(bot, DRAW_MESSAGE)
    elif player == "바위":
        if bot == "보":
            return get_result_message(bot, LOSE_MESSAGE)
        else:
            return get_result_message(bot, WIN_MESSAGE)
    elif player == "보":
        if bot == "가위":
            return get_result_message(bot, LOSE_MESSAGE)
        else:
            return get_result_message(bot, WIN_MESSAGE)
    elif player == "가위":
        if bot == "보":
            return get_result_message(bot, LOSE_MESSAGE)
        else:
            return get_result_message(bot, WIN_MESSAGE)


@add_skill(r'가위바위보')
def get_menu(message):
    return TemplateSendMessage(
        alt_text='가위바위보게임',
        template=ButtonsTemplate(
            thumbnail_image_url='https://images.pexels.com/photos/1249214/pexels-photo-1249214.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940', # noqa
            title='가위바위보 게임입니다!!',
            text='봇과 가위바위보 게임을 해보세요! 아래 가위바위보 중에 하나를 골라주세요', # noqa
            actions=sorted([
                MessageAction(label='가위', text='가위'),
                MessageAction(label='바위', text='바위'),
                MessageAction(label='보', text='보')
            ], key=lambda x: x.label, reverse=False)
        )
    )


@add_skill(r'[가위|바위|보]')
def get_lunch(message):
    result = get_rps_result(random.choice(rps), message)
    return TextSendMessage(
        text=result
    )
