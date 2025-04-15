from threading import Thread
from dataclasses import dataclass, field

#? engine
from bot_engine.server.FastAPIServer import FastAPIServer
from bot_engine.bot.Bot import Bot
from bot_engine.languages.Languages import Languages
from bot_engine.database.Database import Database

#? modules
from src.bot.BotPlugins import BotPlugins



#! 1) Следующий шаг: задать команду /start боту в левом меню (languages + DialogGenerator or a new class MenuCommands.set_menu_commands) 
#! 2) И, конечно же, задать команду /start боту, использую генератор диалогов DialogGenerator

#? initial setup
bot = Bot()
languages = Languages(active_lang="uk")
DB = Database()

#! Дописать BotPlugins таким образом, чтобы его легко можно было 
#! кастомизировать и наледоваться от него (предусмотреть extra_actions)

botPlugins = BotPlugins(bot, languages, DB)

#! В сервере со временем отвязать бота, сделать его тоже как батарейку
#! Сделать так, чтобы сервер работал с классом плагинов, которые просто будут запускаться
#! А BotPlugins перейдёт в BotConfig или что-то в этом духе 
server = FastAPIServer(bot, botPlugins)
app = server._app
