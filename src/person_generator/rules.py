def ru_female_surname(surname: str) -> str:
    if surname.endswith(("ов", "ев", "ёв", "ин", "ын")):
        return surname + "а"

    if surname.endswith("ский"):
        return surname[:-4] + "ская"

    if surname.endswith("цкий"):
        return surname[:-4] + "цкая"

    if surname.endswith("ой"):
        return surname[:-2] + "ая"

    return surname


def ua_female_surname(surname: str) -> str:
    if surname.endswith("ський"):
        return surname[:-5] + "ська"

    if surname.endswith("цький"):
        return surname[:-5] + "цька"

    if surname.endswith("ий"):
        return surname[:-2] + "а"

    if surname.endswith("ій"):
        return surname[:-2] + "я"

    if surname.endswith("ов"):
        return surname + "а"

    return surname