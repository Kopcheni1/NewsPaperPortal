from django import template


register = template.Library()


@register.filter()
def censor(value):
    bad_words = ('редиска', 'дурак', 'придурок')

    if not isinstance(value, str):
        raise ValueError('Невозможно применить цензор не к строке')

    for word in value.split():
        if word.lower() in bad_words:
            value = value.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
    return value