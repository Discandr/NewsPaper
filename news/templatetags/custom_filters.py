from django import template

register = template.Library()

BAD = [
    'еба',
    'пизд',
    'хуй',
    'хуе',
    'хуё',
    'мраз',
    'пидар',
    'педар',
    'бля',
    ]




@register.filter(name='stop_word')
def stop_word(value: str):
    text = value.split()

    for i in range(len(text)):
        for stop in BAD:
            if text[i].lower().find(stop) >= 0:
                text[i] = '*!!!*'

    return ' '.join(text)

