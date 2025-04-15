from telebot.types import BotCommand
from src.libs.bot_engine.languages.Locale import Locale

UK_LOCALE = Locale(
    lang="uk",
    
    menu_commands=[
        BotCommand(command="start", description="Старт")
    ],

    messages=[
        {"start": "Привiт, {}! Чудовий день, чи не так?"}
    ]
)
