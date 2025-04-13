from threading import Thread

# ? data
from src.languages.UKR import USER_MENU_COMMANDS_UKR
from src.data.commands_list import ADMIN_SLASH_COMMANDS

from bot_engine.languages.Language import Language
from bot_engine.dialogs.DialogGenerator import DialogGenerator
from bot_engine.server.FastAPIServer import FastAPIServer

from src.dialogs.AdminDialogs import AdminDialogs

class Server(FastAPIServer):

    def start_bot_thread(self):
        #! Было бы хорошо, чтобы Languages также создавались тут
        
        DialogGenerator(
            guest_slash_commands=[],
            user_slash_commands=USER_MENU_COMMANDS_UKR,
            admin_slash_commands=USER_MENU_COMMANDS_UKR,
        )

        AdminDialogs().set_dialogs()

        self.bot_thread = Thread(target=self.bot.start)
        self.bot_thread.start()

    # ? redeclare, if needed
    # def shut_server_down(self):
    #     pass
