import random
from enum import Enum


class Locale(str, Enum):
    RU = "RU"
    UA = "UA"

    @classmethod
    def random(cls) -> "Locale":
        values = list(cls)
        return random.choice(values)


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"

    @classmethod
    def random(cls) -> "Gender":
        values = list(cls)
        return random.choice(values)