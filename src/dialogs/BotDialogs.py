from src.dialogs.DialogGenerator import DialogGenerator

from src.dialogs.AdminDialogs import AdminDialogs
from src.dialogs.UserDialogs import UserDialogs

#! Аналогичный файл создаётся ручками
class BotDialogs:
    def __init__(self):
        self.dialog_generator = DialogGenerator()
   
        
    def enable_dialogs(self):
        #? Включаем команды и диалоги админа и пользователей 
        UserDialogs().set_user_dialogs()
        AdminDialogs().set_admin_dialogs()
    
        print('Все команды и диалоги подключены ✅')