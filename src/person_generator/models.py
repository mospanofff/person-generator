from dataclasses import dataclass
from .enums import Gender, Locale


@dataclass(frozen=True)
class Person:
    first_name: str
    last_name: str
    first_name_en: str
    last_name_en: str
    gender: Gender
    locale: Locale

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name_en(self) -> str:
        return f"{self.first_name_en} {self.last_name_en}"