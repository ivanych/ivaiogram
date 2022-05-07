import re

from aiogram import Dispatcher, Bot, types
from aiogram.types import Message

from ivaiogram.vocabulary import vocabulary

dp = Dispatcher()


def start(bot_token: str) -> None:
    # Initialize Bot instance with an default parse mode which will be passed to all API calls
    bot = Bot(bot_token, parse_mode="HTML")

    # And the run events dispatching
    dp.run_polling(bot)

@dp.message(commands=["help"])
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    len_vcb = len(vocabulary)

    await message.answer(
        f"Бот отвечает на сообщения, содержащие некоторые слова или словосочетания (регистр не учитывается).\n"
        f"Есть {len_vcb} вариантов, дальше мне было лень сочинять.")


@dp.message()
async def reply_spec_handler(message: types.Message) -> None:
    """
    Message reply.
    """
    text = message.text.lower()
    keys = vocabulary.keys()

    matches = [key for key in keys if (re.search(rf'\b{key}\b', text))]

    if matches:
        result = vocabulary.get(matches[0])

        await message.reply(result)
