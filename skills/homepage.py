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


@add_skill(r'홈페이지')
def get_location(message):
    return TextSendMessage(text='안녕하세요. 파이콘 한국 2019의 행사 홈페이지 URL은 '
                                'https://www.pycon.kr/ 입니다.')
