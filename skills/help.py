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

import re

from linebot.models import TextSendMessage

from skills import add_skill
from skills import skills as skill_list
from skills import skills_help_text


@add_skill(r'(헬프)|(help)|(도움)|(도와줘)', help_text='파이콘 한국 2019 도우미 LINE BOT이 제공하는 기능을 알려드립니다.')
def get_timetable(message):
    global skill_list

    special_char = re.compile(r'[^a-zA-Z가-힣0-9\|]')
    sperated_skill_list = []

    for skill_name in skill_list:
        help_text = skills_help_text.get(skill_name, '이 기능은 도움말을 제공하지 않습니다.')
        pure_skill_names = special_char.sub('', skill_name)

        if re.search(r'\|', pure_skill_names):
            pure_skill_names = pure_skill_names.split('|')

        sperated_skill_list.append((pure_skill_names, help_text,))

    return TextSendMessage(
        text=make_guide(sperated_skill_list)
    )


def make_guide(skills):
    guide = ''
    for skill, help_text in skills:
        if isinstance(skill, list):
            skill = ', '.join(skill)
        guide += f'• 🗣 "{skill}" 라고 물어봐주세요. <br/> ({help_text})<br/><br/>'

    return guide

