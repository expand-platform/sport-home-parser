from dataclasses import dataclass, field
from typing import Callable, List

#? engine
from bot_engine.languages.Languages import Languages
from bot_engine.dialogs.DialogGenerator import DialogGenerator
from bot_engine.bot.Bot import Bot
from bot_engine.database.Database import Database

#? languages
from src.data.locales.uk import UK_LOCALE
from src.data.locales.ru import RU_LOCALE

#? modules
from src.dialogs.AdminDialogs import AdminDialogs


@dataclass
class BotPlugins:
    """ Bot dependencies manager """
    Bot: Bot
    Languages: Languages
    DB: Database

    
    def setup_database(self):
        """ Connects MongoDB, prepares cache """
        # DB = Database()
        pass


    def setup_languages(self):
        """ setup locales and active language """
        self.Languages.add_locale(UK_LOCALE)
        self.Languages.add_locale(RU_LOCALE)

        self.Languages.active_lang = "uk"

    def set_menu_commands(self):
        """ Sets bot menu commands """
        menu_commands = self.Languages.get_menu_commands()
        
        self.Bot._bot.set_my_commands([])
        self.Bot._bot.set_my_commands(menu_commands)
        print("🔉 Slash commands set!")



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
            self.set_menu_commands,
            self.setup_dialog_generator,
            self.setup_dialogs,
        ]

