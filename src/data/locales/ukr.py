from telebot.types import BotCommand
from bot_engine.languages.Locale import Locale

UK_LOCALE = Locale(
    lang="ukr",
    
    menu_commands=[
        BotCommand(command="start", description="Старт")
    ],

    messages=[
        {"start": "Привiт, {}! Чудовий день, чи не так?"}
    ]
)
