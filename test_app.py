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


from app import get_message


def test_message():
    response = get_message('장소')
    assert response.type == 'location'

    response = get_message('모든프로그램')
    assert response.type == 'template'

    response = get_message('홈페이지')
    assert response.type == 'text'

    response = get_message('절대 안 나올 것 같은 질의')
    assert response.type == 'text'

    response = get_message('헬프')
    assert response.type == 'text'
