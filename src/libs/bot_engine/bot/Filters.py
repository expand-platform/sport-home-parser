from typing import Union, TYPE_CHECKING
from telebot.custom_filters import AdvancedCustomFilter
from telebot.types import Message, CallbackQuery

#? engine types
if TYPE_CHECKING:
    from libs.bot_engine.database.Database import Database


class AccessLevelFilter(AdvancedCustomFilter):
    key = 'access_level'

    def __init__(self, db: "Database"):
        # self.bot = bot
        self.db = db
        

    def check(self, message: Union[Message, CallbackQuery], access_level: str):
        print(f"Filters (check)")
        
        #? if user replies with a keyboard
        if not hasattr(message, 'chat'):
            print(f"no message.chat found: { message.message.chat.id }")
            message = message.message
            
        
        active_user = self.db.get_active_user(message)

        # if a list...
        if isinstance(access_level, list):
            return active_user["access_level"] in access_level
       

