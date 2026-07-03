import random
from datetime import datetime

from .data.ca import CA_FEMALE_NAMES, CA_MALE_NAMES, CA_SURNAMES
from .data.gb import GB_FEMALE_NAMES, GB_MALE_NAMES, GB_SURNAMES
from .data.kz import KZ_FEMALE_NAMES, KZ_MALE_NAMES, KZ_SURNAMES
from .data.ru import RU_FEMALE_NAMES, RU_MALE_NAMES, RU_SURNAMES
from .data.ua import UA_FEMALE_NAMES, UA_MALE_NAMES, UA_SURNAMES
from .data.us import US_FEMALE_NAMES, US_MALE_NAMES, US_SURNAMES
from .enums import Gender, Locale
from .models import Person
from .rules import (
    kz_female_surname,
    ru_female_surname,
    translit_ru,
    translit_ua,
    ua_female_surname,
)


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

        if locale == Locale.KZ:
            return self._generate_kz(gender)

        if locale == Locale.US:
            return self._generate_en(gender, Locale.US, US_MALE_NAMES, US_FEMALE_NAMES, US_SURNAMES)

        if locale == Locale.GB:
            return self._generate_en(gender, Locale.GB, GB_MALE_NAMES, GB_FEMALE_NAMES, GB_SURNAMES)

        if locale == Locale.CA:
            return self._generate_en(gender, Locale.CA, CA_MALE_NAMES, CA_FEMALE_NAMES, CA_SURNAMES)

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

    def generate_kz_male(self) -> Person:
        return self.generate(Locale.KZ, Gender.MALE)

    def generate_kz_female(self) -> Person:
        return self.generate(Locale.KZ, Gender.FEMALE)

    def generate_us_male(self) -> Person:
        return self.generate(Locale.US, Gender.MALE)

    def generate_us_female(self) -> Person:
        return self.generate(Locale.US, Gender.FEMALE)

    def generate_gb_male(self) -> Person:
        return self.generate(Locale.GB, Gender.MALE)

    def generate_gb_female(self) -> Person:
        return self.generate(Locale.GB, Gender.FEMALE)

    def generate_ca_male(self) -> Person:
        return self.generate(Locale.CA, Gender.MALE)

    def generate_ca_female(self) -> Person:
        return self.generate(Locale.CA, Gender.FEMALE)

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
            first_name_en=translit_ru(first_name),
            last_name_en=translit_ru(last_name),
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
            first_name_en=translit_ua(first_name),
            last_name_en=translit_ua(last_name),
            gender=gender,
            locale=Locale.UA,
        )

    def _generate_kz(self, gender: Gender) -> Person:
        first_name = self.random.choice(
            KZ_MALE_NAMES if gender == Gender.MALE else KZ_FEMALE_NAMES
        )

        surname = self.random.choice(KZ_SURNAMES)

        last_name = (
            surname
            if gender == Gender.MALE
            else kz_female_surname(surname)
        )

        return Person(
            first_name=first_name,
            last_name=last_name,
            first_name_en=translit_ru(first_name),
            last_name_en=translit_ru(last_name),
            gender=gender,
            locale=Locale.KZ,
        )

    def _generate_en(
        self,
        gender: Gender,
        locale: Locale,
        male_names: list,
        female_names: list,
        surnames: list,
    ) -> Person:
        first_name = self.random.choice(
            male_names if gender == Gender.MALE else female_names
        )
        last_name = self.random.choice(surnames)
        return Person(
            first_name=first_name,
            last_name=last_name,
            first_name_en=first_name,
            last_name_en=last_name,
            gender=gender,
            locale=locale,
        )