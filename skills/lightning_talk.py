from linebot.models import TextSendMessage
import requests

from skills import add_skill


def request_lightning_talk_info() -> requests.Response:
    return requests.post(
        url='https://www.pycon.kr/api/graphql',
        json={
            "operationName": "LightningTalks",
            "variables": {},
            "query": """query LightningTalks {
                        schedule {
                            id
                            lightningTalkProposalStartAt
                            lightningTalkProposalFinishAt
                            __typename
                        }
                        lightningTalks {
                            id
                            name
                            day
                            owner {
                                profile {
                                id
                                name
                                __typename
                                }
                            __typename
                            }
                        __typename
                        }
                    }""",
        },
    )


def extract_data(lightning_talk: dict) -> dict:
    return {
        'name': lightning_talk['name'],
        'speaker': lightning_talk['owner']['profile']['name'],
    }


def parse_lightning_talk_json(response: requests.Response) -> dict:
    lightning_talk_data = {'day1': [], 'day2': []}
    for lightning_talk in response.json()['data']['lightningTalks']:
        if lightning_talk['day'] == 1:
            lightning_talk_data['day1'] += [extract_data(lightning_talk)]
        else:
            lightning_talk_data['day2'] += [extract_data(lightning_talk)]

    return lightning_talk_data


def format_lightning_talk_info(i: int, lightning_talk: dict) -> str:
    return f'{i+1}.{lightning_talk["name"]} - {lightning_talk["speaker"]}님\n'


def create_message(lightning_talk_data: dict):
    message = '라이트닝 토크 안내입니다.\n\n'

    message += '[토요일]\n'
    for i, lightning_talk in enumerate(lightning_talk_data['day1']):
        message += format_lightning_talk_info(i, lightning_talk)

    message += '\n[일요일]\n'
    for i, lightning_talk in enumerate(lightning_talk_data['day2']):
        message += format_lightning_talk_info(i, lightning_talk)

    lightning_talk_count = len(lightning_talk_data['day2'])
    if lightning_talk_count <= 10:
        message += f'\n아직 {10-lightning_talk_count}개의 라이트닝토크 신청이 남았습니다.\n'
        message += f'신청은 https://www.pycon.kr/program/lightning-talk 에서 가능합니다.'

    return message


@add_skill(
    pattern=r'(라이트닝토크|lightningtalk)',
    help_text='현재 신청된 라이트닝 토크 리스트를 제공합니다.'
)
def get_lightning_talk_info(message):
    response = request_lightning_talk_info()
    lightning_talk_data = parse_lightning_talk_json(response)
    message = create_message(lightning_talk_data)
    return TextSendMessage(message)
