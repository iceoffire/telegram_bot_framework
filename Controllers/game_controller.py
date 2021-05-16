from Services import GameService


def roll_dice(update, context):
    update.message.reply_text(GameService.roll_dice(context))


def random_pick(update, context):
    update.message.reply_text(GameService.random_pick(context))


def should_i(update, context):
    update.message.reply_text(GameService.should_I(context))


def russian_roulette(update, context):
    update.message.reply_text(GameService.russian_roulette())
