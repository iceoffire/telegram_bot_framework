import random

def roll_dice(context):
    args = __getArgs(context)
    faces = 6
    if (len(args) == 1 and __intTryParse(args[0])[1]):
        faces = __intTryParse(args[0])[0]
    return random.randint(1, faces)

def random_pick(context):
    args = __getArgs(context)
    if (len(args) == 0):
        return 'Expected: /random_pick <choice 1>, <choice 2>, <choice 3>...'
    opcoes = ' '.join(args).split(', ')
    return 'Hmm, I choose: ' + opcoes[random.randint(0, len(opcoes)-1)] + '.'

def should_I(context):
    args = __getArgs(context)
    if (len(args) == 0):
        return 'Expected: /should_i <question?>'
    return 'Yes.' if random.randint(0,1) == 1 else 'No.'

def russian_roulette():
    number = random.randint(1, 6)
    if (number == 3):
        return 'You died. RIP'
    return 'Smoke comes out of the gun, nothing happens.'

def __intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False

def __getArgs(context):
    return context.args