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


from linebot.models import LocationSendMessage

from skills import add_skill


@add_skill(r'장소', help_text='파이콘 2019 행사가 열리는 장소를 알려드릴게요.')
def get_location(message):
    return LocationSendMessage(
        title='장소',
        address='서울 강남구 영동대로 513 (삼성동) 코엑스 그랜드볼룸',
        latitude=37.5130556,
        longitude=127.0586111
    )
