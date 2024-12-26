from aiogram.filters import CommandStart, Command
from aiogram.types import BotCommand


def _create_command(name: str) -> Command:
    return Command(commands=[name])


def _get_command_name(command: Command) -> str:
    return command.commands[0]


start = CommandStart()
find_students_by_incomplete_name = _create_command('find_students_by_incomplete_name')
get_rating_student_by_name = _create_command('get_rating_student_by_name')


command_descriptions = {
    _get_command_name(find_students_by_incomplete_name): 'поиск студентов по неполному ФИО',
    _get_command_name(get_rating_student_by_name): 'получить информацию о студенте по ФИО',
}

command_menu = [BotCommand(command=key, description=value) for key, value in command_descriptions.items()]
