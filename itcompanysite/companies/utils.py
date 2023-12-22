import re


def has_russian_letters(input_string):
    russian_letters_pattern = re.compile('[а-яА-Я]')
    return bool(russian_letters_pattern.search(input_string))
