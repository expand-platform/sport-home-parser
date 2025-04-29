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
class BotPlugins:
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
    languages: Languages
    db: Database
    bot: Bot
    dialogGenerator: DialogGenerator
    # BotDialogs: BotDialogs

    
    def set_database(self):
        """ Connects MongoDB, prepares cache for users """
        #? Prepare users in cache for further interactions  
        self.db.cache_users()
        pass


    def set_languages(self, locales: list[Locale], bot_language = "ru"):
        """ sets locales and active language """
        for locale in locales:
            self.languages.add_locale(locale)

        self.languages.active_lang = bot_language
        self.languages.set_messages(bot_language)
        print(f"🌐 {bot_language } language set!")


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
        """ Prepares user and admin dialogs """
        pass

    def set_extra_settings(self):
        """ You can define your extra setup settings here """
        pass

