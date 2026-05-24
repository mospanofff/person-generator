import random
from datetime import datetime

from .data.ru import RU_FEMALE_NAMES, RU_MALE_NAMES, RU_SURNAMES
from .data.ua import UA_FEMALE_NAMES, UA_MALE_NAMES, UA_SURNAMES
from .enums import Gender, Locale
from .models import Person
from .rules import ru_female_surname, ua_female_surname


class PersonGenerator:
    def __init__(self, seed: int | None = None):
        self.random = random.Random(
            seed if seed is not None else datetime.now().timestamp()
        )

    def generate(
        self,
        locale: Locale = Locale.UA,
        gender: Gender | None = None,
    ) -> Person:
        gender = gender or Gender.random()

        if locale == Locale.RU:
            return self._generate_ru(gender)

        if locale == Locale.UA:
            return self._generate_ua(gender)

        raise ValueError(f"Unsupported locale: {locale}")

    def generate_random(self) -> Person:
        locale = Locale.random()
        gender = Gender.random()
        return self.generate(locale=locale, gender=gender)

    def generate_ru_male(self) -> Person:
        return self.generate(Locale.RU, Gender.MALE)

    def generate_ru_female(self) -> Person:
        return self.generate(Locale.RU, Gender.FEMALE)

    def generate_ua_male(self) -> Person:
        return self.generate(Locale.UA, Gender.MALE)

    def generate_ua_female(self) -> Person:
        return self.generate(Locale.UA, Gender.FEMALE)

    def _generate_ru(self, gender: Gender) -> Person:
        first_name = self.random.choice(
            RU_MALE_NAMES if gender == Gender.MALE else RU_FEMALE_NAMES
        )

        surname = self.random.choice(RU_SURNAMES)

        last_name = (
            surname
            if gender == Gender.MALE
            else ru_female_surname(surname)
        )

        return Person(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            locale=Locale.RU,
        )

    def _generate_ua(self, gender: Gender) -> Person:
        first_name = self.random.choice(
            UA_MALE_NAMES if gender == Gender.MALE else UA_FEMALE_NAMES
        )

        surname = self.random.choice(UA_SURNAMES)

        last_name = (
            surname
            if gender == Gender.MALE
            else ua_female_surname(surname)
        )

        return Person(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            locale=Locale.UA,
        )