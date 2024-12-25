import asyncio
from config import BOT_TOKEN
from commands import command_menu
from dispatcher import dp
from aiogram import Bot

    
async def create_bot() -> Bot:
    bot = Bot(BOT_TOKEN)
    await bot.set_my_commands(command_menu)
    return bot


async def main() -> None:
    bot = await create_bot()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
