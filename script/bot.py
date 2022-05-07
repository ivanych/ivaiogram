import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

BOT_TOKEN = os.environ.get("BOT_TOKEN")

dp = Dispatcher()


@dp.message(commands=["help"])
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    # Most of event objects has an aliases for API methods to be called in event context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage` method automatically
    # or call API method directly via Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(
        f"Бот отвечает на сообщения, содержащие некоторые слова (регистр не учитывается).\nВсего есть 20 вариантов, дальше мне было лень сочинять.")


@dp.message()
async def reply_spec_handler(message: types.Message) -> None:
    """
    Message reply.
    """
    fruits = {
        "300": "Отсоси у тракториста!",
        "триста": "Отсоси у тракториста!",
        "превед": f"Превед, {message.from_user.full_name}!",
        "хуй": "Последний хуй без соли доедаем.",
        "пизда": "...рулю",
        "блядь": "Не те бляди,\nчто хлеба ради\nспереди и сзади\nдают нам ебти,\nБог их прости!\nА те бляди - лгущие,\nденьги сосущие,\nеть не дающие -\nвот бляди сущие,\nмать их ети!\n\n В.В. Маяковский.",
        "ебать": "В русском языке всего четыре матерных корня.",
        "жопа": "Разверзлись бездны...",
        "много": "Стопицот!",
        "салат": "Салат рекурсивный: огурцы, помидоры, салат.)",
        "иванов": "Иванов утром ходит без штанов:)",
        "дибров": "Сатурну больше не наливать!",
        "созиев": "Созие мое...",
        "созие": "Какое «созие-мое», пёс смердячий?!",
        "рамазова": ".NET не самый хороший язык для ботов 😡",
        "виноградова": "https://www.youtube.com/watch?v=NMjzUHIwjfA",
        "звонарёв": "Губит людей не пиво, губит людей вода!",
        "сорокоумов": "Уважали дядю Степу\nЗа такую высоту.\nШел с работы дядя Степа —\nВидно было за версту.",
        "ого": "О-го-го!!!",
        "тест": "У вас две полоски.",
        "амбидекстер": "— Коля у нас амбидекстер.\n— Кто?\n— Коля!",
        "бот": "Чо?",
        "не знаю": "Ну шо ты сразу сдаёшься-то?!",
        "макось": "Хуякось! При Джобсе такого не было!",
        "вокабуляр": "Лови филолога!",
        "впн": "Правильный VPN — https://hi-l.eu/",
        "vpn": "Правильный VPN — https://hi-l.eu/",
    }

    keys = fruits.keys()

    text = message.text.lower()

    matches = [key for key in keys if (key in text)]

    if matches:
        result = fruits.get(matches[0])

        await message.reply(result)


def main() -> None:
    # Initialize Bot instance with an default parse mode which will be passed to all API calls
    bot = Bot(BOT_TOKEN, parse_mode="HTML")
    # And the run events dispatching
    dp.run_polling(bot)


if __name__ == "__main__":
    main()
