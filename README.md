# Telegram bot framework
> Telegram bot framework is a tool to facilitate the creation of new bots using python. The creation of new controllers is very similar to creating new controllers using ASP.NET.

#

- [Creating New Commands](#Creating-new-commands)
- [Usage Examples](#usage-examples)
- [Current Development State](#current-development-state)
- [Author](#author)

### Install
In order to use it, clone the repo
```
git clone https://github.com/iceoffire/telegram_bot_framework.git
```

To be able to use it, you need a telegram bot key, if you don't have one already, I suggest that you read [this doc](https://core.telegram.org/api/obtaining_api_id).

With your telegram key, add it to the Environment Variable as ```TELEGRAM_BOT_KEY``` and you are good to go.

### Creating New commands
In order to create a new command, you just need to add a new method inside any file with **_controller** in the path:

```
telegram_bot_framework/
    Controllers
```

You just need to add a new function, like this:

```python
def new_command(context):
    # do something
    pass
```


### Usage Examples
In this repository, we already have an [example file](https://github.com/iceoffire/telegram_bot_framework/blob/master/Controllers/game_controller.py), in the path:

```
telegram_bot_framework/
    Controllers/
        game_controller.py
```

In [game_controller.py](https://github.com/iceoffire/telegram_bot_framework/blob/master/Controllers/game_controller.py), we have 4 commands, we have:
* roll_dice
    * Return a six-side dice, or N sides if user send it in the context as a argument.
* random_pick
    * Return a random option in the list of objects that user send through arguments (e.g. /random_pick option 1, option 2, option 3)
* should_i
    * Return Yes/No to you question.
* russian_roulette
    * Return the result of a match of russian roulette.


### Current Development State

| Tool             | Status |
| ---------        | ------ |
| Controller       | `Ok`   |
| Filter           | `Ok`   |
| Logging          | `Ok`   |
| Error handling   | `Ok`   |
| Database         | Wip    |
| Domain           | Wip    |
| Repository       | Wip    |
| Better examples  | Wip    |
| requirements.txt | Wip    |


### Author

**Ulisses Gandini**

* [github/iceoffire](https://github.com/iceoffire)
* [twitter/gandhi_iceoffire](https://twitter.com/gandhi_sandman)

