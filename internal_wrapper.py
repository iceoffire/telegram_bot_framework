import logging
from custom_exceptions import BotNotAllowed
from telegram.ext import CommandHandler

# formating the log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def internal_command_handler(command_name, func):
    return CommandHandler(command_name, lambda update, context: wrap(func, update, context))
    
# every REGISTERED action pass through this wrap, that way we can filter and log actions.
def wrap(action, update=None, context=None):
    if (update == None or context == None):
        return

    # log action and filter
    log(action, update, context)
    filter(update)

    # invoke action
    action(update, context)

# put filters here.
def filter(update):
    user_filter(update.message.from_user)

def user_filter(user):
    if (user.is_bot):
        raise BotNotAllowed("Bot are not allowed to send messages.")

def log(action, update, context):
    logger.info({
        'full_name': update.message.from_user,
        'action': action.__name__,
        'args': context.args
    })
