from loader import all_options


def help(update, context):
    update.message.reply_text('available commands: ' + ', '.join(all_options))
