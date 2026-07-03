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


def kz_female_surname(surname: str) -> str:
    if surname.endswith(("ов", "ев", "ёв", "ин", "ын")):
        return surname + "а"

    if surname.endswith("ский"):
        return surname[:-4] + "ская"

    if surname.endswith("цкий"):
        return surname[:-4] + "цкая"

    return surname


_RU_TRANSLIT_MAP = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d",
    "е": "e", "ё": "e", "ж": "zh", "з": "z", "и": "i",
    "й": "i", "к": "k", "л": "l", "м": "m", "н": "n",
    "о": "o", "п": "p", "р": "r", "с": "s", "т": "t",
    "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch",
    "ш": "sh", "щ": "shch", "ъ": "ie", "ы": "y", "ь": "",
    "э": "e", "ю": "yu", "я": "ya",
}

_UA_TRANSLIT_MAP = {
    "а": "a", "б": "b", "в": "v", "г": "h", "ґ": "g",
    "д": "d", "е": "e", "є": "ie", "ж": "zh", "з": "z",
    "и": "y", "і": "i", "ї": "i", "й": "i", "к": "k",
    "л": "l", "м": "m", "н": "n", "о": "o", "п": "p",
    "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f",
    "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch",
    "ь": "", "ю": "yu", "я": "ya",
}

_UA_TRANSLIT_INITIAL_MAP = {
    "є": "ye", "ї": "yi", "й": "y", "ю": "yu", "я": "ya",
}

_UA_APOSTROPHES = "'’ʼ"


def translit_ru(text: str) -> str:
    result = []
    for ch in text:
        mapped = _RU_TRANSLIT_MAP.get(ch.lower(), ch.lower())
        if ch.isupper() and mapped:
            mapped = mapped[0].upper() + mapped[1:]
        result.append(mapped)
    return "".join(result)


def translit_ua(text: str) -> str:
    result = []
    at_word_start = True
    for ch in text:
        if ch in _UA_APOSTROPHES:
            continue

        lower = ch.lower()
        if lower in (" ", "-"):
            result.append(ch)
            at_word_start = True
            continue

        mapped = None
        if at_word_start:
            mapped = _UA_TRANSLIT_INITIAL_MAP.get(lower)
        if mapped is None:
            mapped = _UA_TRANSLIT_MAP.get(lower, lower)

        if ch.isupper() and mapped:
            mapped = mapped[0].upper() + mapped[1:]

        result.append(mapped)
        at_word_start = False
    return "".join(result)