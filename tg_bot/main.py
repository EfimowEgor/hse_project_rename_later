import asyncio
from config import bot_token
from bot_infrastructure.commands import command_menu
from bot_infrastructure.dispatcher import dp
from aiogram import Bot

    
async def create_bot() -> Bot:
    bot = Bot(bot_token)
    await bot.set_my_commands(command_menu)
    return bot


async def main() -> None:
    bot = await create_bot()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
