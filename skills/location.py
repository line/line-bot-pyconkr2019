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


@add_skill(r'장소')
def get_location(message):
    return LocationSendMessage(
        title='장소',
        address='서울 강남구 영동대로 513 (삼성동) 코엑스 그랜드볼룸',
        latitude=37.5130556,
        longitude=127.0586111
    )


@add_skill(r'피알앤디컴퍼니')
def get_lunch_pr(message):
    return LocationSendMessage(
        title='장고 서버개발 이야기',
        address='코엑스 그랜드볼룸 2층 209호B 피알앤디컴퍼니',
        date='2019년 8월 18일 일요일 오후 1시 ~ 2시',
    )

@add_skill(r'ML2')
def get_lunch_ML2(message):
    return LocationSendMessage(
        title='최근 머신러닝 트렌드 소개',
        address='코엑스 그랜드볼룸 2층 201호 (G,10)',
        date='2019.08.18. 일요일. 오후1시~2시',
    )


@add_skill(r'미래에셋대우')
def get_lunch_MIRAE(message):
    return LocationSendMessage(
        title=' 증권사에서 빅데이터의 활용',
        address='코엑스 그랜드볼룸 2층 201호 미래에셋대우 테이블',
        date='2019년 8월 18일 일요일 오호 1시 ~ 2시',
    )


@add_skill(r'소프트웨어마이스터고등학교')
def get_lunch_SW(message):
    return LocationSendMessage(
        title='SW마이스터고등학교 선생님께 듣는 마이스터고 이야기',
        address='코엑스 그랜드볼룸 2층 209A호',
        date='2019.08.18.(일) 12:00~13:30',
    )
