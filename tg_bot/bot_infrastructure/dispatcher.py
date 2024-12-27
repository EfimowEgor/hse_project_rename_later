from bot_infrastructure import commands, handler, messages
from aiogram import Dispatcher, types

dp = Dispatcher()
accepted_command = ''

handle_command_functions = {
    commands.start: handler.handle_start_command,
    commands.find_students_by_incomplete_name: handler.handle_find_student_by_incomplete_name_command,
    commands.get_rating_student_by_name: handler.handle_get_rating_student_by_name_command,
    '': handler.handle_unknow_command
}


@dp.message(commands.start)
async def accepted_start_command(message: types.Message) -> None:
    accepted_command = commands.start
    handle_command_function = handle_command_functions[accepted_command]
    _, answer = await handle_command_function(message.text)
    accepted_command = ''
    await message.answer(answer)


@dp.message(commands.find_students_by_incomplete_name)
async def accepted_find_student_by_incomplete_name_command(message: types.Message) -> None:
    global accepted_command
    accepted_command = commands.find_students_by_incomplete_name
    await message.answer(messages.find_students_by_incomplete_name_message)


@dp.message(commands.get_rating_student_by_name)
async def accepted_get_rating_student_by_name_command(message: types.Message) -> None:
    global accepted_command
    accepted_command = commands.get_rating_student_by_name
    await message.answer(messages.get_rating_student_by_name_message)
    

@dp.message()
async def accepted_message(message: types.Message) -> None:
    global accepted_command
    handle_command_function = handle_command_functions[accepted_command]
    is_handled_command, answer = await handle_command_function(message.text)
    
    if is_handled_command:
        accepted_command = ''
        
    if type(answer) == str:
        await message.answer(answer)
        return
    
    for item in answer:
        await message.answer(item)
