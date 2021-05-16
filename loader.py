import logging
from os.path import dirname, basename, isfile, join
from internal_wrapper import internal_command_handler
from telegram.ext import Updater, MessageHandler, Filters
from inspect import getmembers, isfunction
import glob
import importlib
import os

all_options = []

# formating the log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def load_bot():
    return Updater(os.environ['TELEGRAM_BOT_KEY'], use_context=True)


def load_controllers(dispatcher):
    # loading all modules from folder /Controllers
    modules = glob.glob(join(dirname(__file__) + '/Controllers', "*.py"))

    # getting all files that contains _controller
    __all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py') and '_controller' in f]

    # iterate loading all endpoints (methods inside Controllers)
    for x in range(len(__all__)):
        file_path = modules[x]
        spec = importlib.util.spec_from_file_location("*", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        functions = [func for func in getmembers(module) if isfunction(func[1])]
        for func in functions:
            all_options.append(func[0])
            dispatcher.add_handler(internal_command_handler(func[0], func[1]))


def load_404_handler(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.text, __echo))


def load_error_handler(dispatcher):
    dispatcher.add_error_handler(__error)


def __error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def __echo(update, context):
    update.message.reply_text("You send something that it's not recognized as a command.")
