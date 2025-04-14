from dataclasses import dataclass, field

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
        Database()


    def setup_languages(self):
        Languages(active_lang="uk")


    def setup_dialog_generator(self):
        pass


    def setup_dialogs(self):
        pass


    def setup_plugins(self):
        return [
            self.setup_database,
            self.setup_languages,
            self.setup_dialog_generator,
            self.setup_dialogs,
        ]

