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


import os
import sys

import requests
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    TemplateSendMessage, MessageAction, ButtonsTemplate,
    LocationSendMessage, URIAction,
    CarouselTemplate, CarouselColumn,
)


app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


def get_programs(topic: str = None) -> TemplateSendMessage:
    def limit_len(text, limit):
        return text if len(text) < limit else text[:limit-1] + '…'

    columns = [
        CarouselColumn(
            thumbnail_image_url=program['owner']['profile']['image'],
            title=limit_len(program['name'], 40),
            text=limit_len(program['desc'], 60),
            actions=[
                URIAction(
                    label='자세히 보기',
                    uri=(f"https://www.pycon.kr/program/talk-detail"
                         f"?id={program['id']}")
                )
            ]
        )
        for program
        in requests.post(
            'https://www.pycon.kr/api/graphql',
            headers={
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            data='{"query":"query getPresentations {\\n  presentations {\\n    id\\n    owner {\\n      profile {\\n        name\\n        image\\n        avatarUrl\\n        bio\\n        blogUrl\\n      }\\n    }\\n    name\\n    place {\\n      name\\n    }\\n    duration\\n    startedAt\\n    finishedAt\\n    desc\\n    language\\n    backgroundDesc\\n    category {\\n      name\\n    }\\n    difficulty {\\n      name\\n    }\\n    startedAt\\n    finishedAt\\n  }\\n}","variables":{}}' # noqa
        ).json()['data']['presentations']
        if not topic or topic in program['name']
    ][:10]
    return TemplateSendMessage(
        alt_text='https://www.pycon.kr/program/talks',
        template=CarouselTemplate(columns=columns)
    ) if len(columns) > 0 else TextSendMessage(
        '말씀하신 주제에 관련된 발표나 정보를 찾지 못했어요. 😢'
    )


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        if '장소' in event.message.text:
            message = LocationSendMessage(
                title='장소',
                address='서울 강남구 영동대로 513 (삼성동) 코엑스 그랜드볼룸',
                latitude=37.5130556,
                longitude=127.0586111
            )
        elif '메뉴' in event.message.text:
            message = TemplateSendMessage(
                alt_text='Welcome!',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://www.pycon.kr/static/images/og-pyconkr-image.png', # noqa
                    title='환영합니다!',
                    text='안녕하세요. 파이콘 한국 2019의 행사 참여를 돕는 LINE 챗봇입니다. 궁금하신 것을 말씀해주세요!', # noqa
                    actions=[
                        MessageAction(label='장소', text='장소'),
                        MessageAction(label='프로그램', text='프로그램'),
                        URIAction(label='홈페이지', uri='https://www.pycon.kr/')
                    ]
                )
            )
        elif '프로그램' in event.message.text:
            message = get_programs()
        else:
            message = get_programs(event.message.text)
        line_bot_api.reply_message(event.reply_token, message)

    return 'OK'
