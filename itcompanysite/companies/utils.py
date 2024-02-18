import re


def has_russian_letters(input_string):
    if input_string is None:
        return False

    russian_letters_pattern = re.compile('[а-яА-Я]')
    return bool(russian_letters_pattern.search(input_string))
