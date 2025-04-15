from os import getenv
from dataclasses import dataclass, field
from typing import Callable, List, Optional

#? engine
from libs.bot_engine.languages.Locale import Locale
from libs.bot_engine.dialogs.BotDialogs import BotDialogs
from libs.bot_engine.languages.Languages import Languages
from libs.bot_engine.dialogs.DialogGenerator import DialogGenerator
from libs.bot_engine.bot.Bot import Bot
from libs.bot_engine.database.Database import Database



@dataclass
class BotConfigs:
    """ 
        Bot dependencies manager. 
        You can customize this class by extending its methods 

        set_database()
        set_languages()
        set_menu_commands()
        set_dialog_generator()
        set_bot_dialogs()
        set_extra_settings()

        or you can use set_all and pass all data there (*future)

    """
    bot: Bot
    languages: Languages
    db: Database
    dialogGenerator: Optional[DialogGenerator] = None
    botDialogs: Optional[BotDialogs] = None

    
    def set_database(self):
        """ Connects MongoDB, prepares cache """
        # DB = Database()
        pass


    def set_languages(self, locales: list[Locale], bot_language = "ru"):
        """ sets locales and active language """
        for locale in locales:
            self.languages.add_locale(locale)

        self.languages.active_lang = bot_language


    def set_menu_commands(self):
        """ Sets bot menu commands """
        menu_commands = self.languages.get_menu_commands()
        
        self.bot._bot.set_my_commands([])
        self.bot._bot.set_my_commands(menu_commands)
        print("🔉 Slash commands set!")



    def set_dialog_generator(self):
        """ Prepares DialogGenerator for work """
        pass


    def set_bot_dialogs(self):
        """ Prepares all bot dialogs """
        pass

    def set_extra_settings(self):
        """ You can define your extra setup settings here """
        pass


    # def set_all_components(self):
    #     """ all bot plugin functions """
    #     self.set_database()
    #     self.set_languages()
    #     self.set_menu_commands()
    #     self.set_dialog_generator()
    #     self.set_bot_dialogs()
    #     self.set_extra_settings()

