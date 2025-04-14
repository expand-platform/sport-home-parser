from dataclasses import dataclass, field
from typing import Callable, List

#? engine
from bot_engine.languages.Languages import Languages
from bot_engine.dialogs.DialogGenerator import DialogGenerator
from bot_engine.bot.Bot import Bot
from bot_engine.database.Database import Database

#? languages
from src.data.locales.ukr import UK_LOCALE
from src.data.locales.ru import RU_LOCALE

#? modules
from src.dialogs.AdminDialogs import AdminDialogs


@dataclass
class BotPlugins:

    #? bot dependencies
    def setup_database(self):
        """ Connects MongoDB, prepares cache """
        Database()


    def setup_languages(self):
        """ setup locales and active language """
        languages = Languages()

        languages.add_locale(UK_LOCALE)
        languages.add_locale(RU_LOCALE)

        languages.active_lang = "uk"


    def setup_dialog_generator(self):
        """ Prepares DialogGenerator for work """
        pass


    def setup_dialogs(self):
        """ Prepares all bot dialogs """
        pass


    def setup_plugins(self) -> List[Callable]:
        """ returns a list of all bot plugin functions """
        return [
            self.setup_database,
            self.setup_languages,
            self.setup_dialog_generator,
            self.setup_dialogs,
        ]

