import api, commands, messages
from aiogram import Dispatcher, types

dp = Dispatcher()


@dp.message(commands.start)
async def handle_start(msg: types.Message) -> None:
    await msg.answer(messages.welcome_message)


@dp.message(commands.find_students_by_incomplete_name)
async def handle_find_student_by_name(msg: types.Message) -> None:
    await msg.answer(messages.unrealized_command_message)


@dp.message(commands.get_student_info_by_name)
async def handle_get_student_info_by_name(msg: types.Message) -> None:
    await msg.answer(messages.unrealized_command_message)
