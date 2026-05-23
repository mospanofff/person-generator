from src.person_generator import Locale, PersonGenerator

generator = PersonGenerator()
person = generator.generate(Locale.RU)
print(person)