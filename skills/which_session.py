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


from linebot.models import TextSendMessage

from skills import add_skill

from random import randint


@add_skill(r'뭐듣지?')
@add_skill(r'랜덤세션')
def get_location(message):
    location_list = [
        "101호", "102호", "103호",
        "104호", "105호", "2층 열린공간", "느긋하게 스폰서 부스",
        ]

    switch = randint(0, len(location_list) - 1)

    text = "{}에 가보시는 건 어떠신가요?".format(location_list[switch])

    return TextSendMessage(text=text)
