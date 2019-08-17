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


from os.path import dirname, basename, isfile, join
import glob


modules = glob.glob(join(dirname(__file__), "*.py"))
skills = dict()
skills_help_text = dict()


def add_skill(pattern, help_text=None):
    """
    라인 봇 기능 등록

    :param pattern: 기능 선택 문자열 정규식 패턴
    :param help_text: 기능 도움말
    :return wrapper: 선택된 기능(함수)를 반환하는 함수
    """
    def wrapper(func):
        skills[pattern] = func
        if help_text is not None:
            skills_help_text[pattern] = help_text
        return func
    return wrapper


__all__ = [
    basename(f)[:-3]
    for f in modules
    if isfile(f) and not f.endswith('__init__.py')
]
