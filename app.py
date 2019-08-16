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
import re

import requests
from flask import Flask, request, abort, jsonify, render_template
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            TemplateSendMessage,
                            URIAction,
                            CarouselTemplate,
                            CarouselColumn,)

from skills import * # noqa
from skills import skills


app = Flask(__name__)


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


def get_message(from_message):
    for pattern, skill in skills.items():
        if re.match(pattern, from_message):
            return skill(from_message)

    if '프로그램' in from_message:
        return get_programs()
    else:
        return get_programs(from_message)


@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route('/answer')
def get_answer():
    return jsonify(get_message(request.values['message']).as_json_dict())


@app.route("/callback", methods=['POST'])
def callback():
    channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
    channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
    if not channel_secret:
        print('Specify LINE_CHANNEL_SECRET as environment variable.')
        abort(500)
    if not channel_access_token:
        print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
        abort(500)

    line_bot_api = LineBotApi(channel_access_token)
    parser = WebhookParser(channel_secret)
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
        # if event is MessageEvent and message is TextMessage, then echo text
        for event in events:
            if not isinstance(event, MessageEvent):
                continue
            if not isinstance(event.message, TextMessage):
                continue

            line_bot_api.reply_message(event.reply_token,
                                       get_message(event.message.text))

    except InvalidSignatureError:
        abort(400)

    return 'OK'
