from telebot.types import BotCommand
from src.libs.bot_engine.languages.Locale import Locale

RU_LOCALE = Locale(
    lang="ru",
    
    menu_commands=[
        BotCommand(command="start", description="Старт")
    ],

    messages=[
        { "start": "Привет, {}! Чудный день, не так ли?" }
    ]
)
