from bot_engine.bot.Bot import Bot
# from bot_engine.database.Database import Database

from src.server.server import Server

bot = Bot()

#? Сервер FastAPI работает, под его капотом работает бот.
#? Следующая задача - начать делать юзерские / админские диалоги и внедрить их в сервер (по факту просто передать их как параметр или переопределить метод класса FastAPIServer)
server = Server(bot)
app = server.app
