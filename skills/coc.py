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


@add_skill(r'행동강령')
def get_coc(message):
    return TextSendMessage(
        text='파이콘 한국은 모든 참가자를 포용합니다.'
        ' 파이콘 한국 행동강령(이하 행동강령)은'
        ' 누구도 배제되지 않는 파이썬 커뮤니티를 위해 구성원들이 지켜야 하는 최소한의 약속입니다.'
        ' 자세한 내용은 홈페이지 https://www.pycon.kr/coc 에서 보실 수 있습니다.'
    )
