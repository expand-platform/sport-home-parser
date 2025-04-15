#? bot engine
from src.libs.bot_engine.dialogs.BotDialogs import BotDialogs


class AdminDialogs(BotDialogs):

    def set_dialogs(self):
        self.DialogGenerator.make_dialog(
            access_level=["user", "admin"],
            handler_type="command",
            command_name="start",
            
            #! Разделить на userMessages и adminMessages
            bot_before_message=self.messages["start"],
        )
