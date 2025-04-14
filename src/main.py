from threading import Thread
from dataclasses import dataclass, field

#? engine
from bot_engine.server.FastAPIServer import FastAPIServer
from bot_engine.bot.Bot import Bot

#? modules
from src.bot.BotPlugins import BotPlugins


bot = Bot()
plugins = BotPlugins().setup_plugins()

server = FastAPIServer(bot, plugins)
app = server._app
