# person-generator

Generator of realistic RU/UA names and surnames.

## Install

```bash
pip install person-generator
```

## Usage

```python
from person_generator import PersonGenerator

generator = PersonGenerator()

print(generator.generate_ua_male().full_name)
```