# person-generator

Generator of realistic RU/UA names and surnames.

## Install

```bash
pip install -U git+https://github.com/mospanofff/person-generator.git@v0.1.1
```

## Usage

```python
from person_generator import PersonGenerator, Locale

generator = PersonGenerator()

person = generator.generate(locale=Locale.UA)
```