from bot_engine.bot.Bot import Bot
# from bot_engine.database.Database import Database

from src.server.server import Server

bot = Bot()

server = Server(bot)
app = server.app
