from threading import Thread
from dataclasses import dataclass, field

#? engine
from bot_engine.server.FastAPIServer import FastAPIServer
from bot_engine.bot.Bot import Bot

#? modules
from src.bot.BotPlugins import BotPlugins


#! 1) Следующий шаг: задать команду /start боту в левом меню (languages + DialogGenerator or a new class MenuCommands.set_menu_commands) 
#! 2) И, конечно же, задать команду /start боту, использую генератор диалогов DialogGenerator

bot = Bot()
plugins = BotPlugins().setup_plugins()

server = FastAPIServer(bot, plugins)
app = server._app
