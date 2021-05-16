import loader


def main():
    # bot load
    updater = loader.load_bot()

    dispatcher = updater.dispatcher

    # loading controllers
    loader.load_controllers(dispatcher)
    loader.load_404_handler(dispatcher)
    loader.load_error_handler(dispatcher)
    
    # start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
