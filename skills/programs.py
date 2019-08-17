"""Define dataclass models for pyconkr 2019 objects"""

import datetime
from functools import lru_cache

from marshmallow_dataclass import dataclass
from marshmallow import Schema as MarshmallowSchema
import requests
from typing import ClassVar, Dict, List, Optional, Type


@dataclass
class User:
    """PyconKR 2019 User"""
    name: str
    image: str
    avatarUrl: str
    bio: str
    blogUrl: str


@dataclass
class Profile:
    """User Profile"""
    profile: User


@dataclass
class Place:
    """Room number for coex. ex) 103호"""
    name: str


@dataclass
class Category:
    """Category of the talk"""
    name: str


@dataclass
class Difficulty:
    """Difficulty of the talk. ex) 초급, 중급, 고급"""
    name: str


@dataclass
class Program:
    """Programs for pycon. Includes break time and lightning talk"""
    id: int
    owner: Optional[Profile]
    name: str
    place: Optional[Place]
    duration: str
    startedAt: datetime.datetime
    finishedAt: datetime.datetime
    desc: str
    language: str
    backgroundDesc: str
    category: Optional[Category]
    difficulty: Optional[Difficulty]

    Schema: ClassVar[Type[Schema]] = MarshmallowSchema

    @classmethod
    def deserialize(cls, data: Dict):
        result = cls.Schema().load(data)
        if result.errors:
            raise ValueError(
                'Deserialization failed for following object.',
                result,
            )
        # These shouldn't be necessary but this breaks somehow...
        result.data.startedAt = result.data.startedAt.replace(
            tzinfo=datetime.timezone.utc,
        )
        result.data.finishedAt = result.data.finishedAt.replace(
            tzinfo=datetime.timezone.utc,
        )
        return result.data


@lru_cache()
def get_programs() -> List[Program]:
    """Download all program list and deserialize"""
    response = requests.post(
        'https://www.pycon.kr/api/graphql',
        json={
            "query":
                """query getPresentations  {
                    presentations  {
                        id
                        owner {
                            profile {
                                name
                                image
                                avatarUrl
                                bio
                                blogUrl
                            }
                        }
                        name
                        place {
                            name
                        }
                        duration
                        startedAt
                        finishedAt
                        desc
                        language
                        backgroundDesc
                        category {
                            name
                        }
                        difficulty {
                            name
                        }
                        startedAt
                        finishedAt
                        }
                    }"""
        }
    )
    response.raise_for_status()

    program_data = response.json()['data']['presentations']
    return [Program.deserialize(data) for data in program_data]
