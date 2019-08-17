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


from linebot.models import (
    LocationSendMessage,
    TextSendMessage,
)

from skills import add_skill


@add_skill(r'장소')
def get_location(message):
    return LocationSendMessage(
        title='장소',
        address='서울 강남구 영동대로 513 (삼성동) 코엑스 그랜드볼룸',
        latitude=37.5130556,
        longitude=127.0586111
    )

@add_skill(r'지도')
def get_coex_map(message):
    return TextSendMessage(
        text='지도는 http://www.coex.co.kr/blog/coex-reference/23249 에서 확인해주세요'
    )
