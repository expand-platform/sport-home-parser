#? bot engine
from src.libs.bot_engine.bot.Bot import Bot
from src.libs.bot_engine.languages.Languages import Languages
from src.libs.bot_engine.database.Database import Database

#? engine customization
from src.bot.BotConfigs import MyBotConfigs
from src.server.Server import BotServer

#? languages
from src.data.locales.uk import UK_LOCALE
from src.data.locales.ru import RU_LOCALE

#? dialogs
from src.dialogs.AdminDialogs import AdminDialogs


# Bot components
db = Database()
languages = Languages()
bot = Bot(db)

# Bot plugins and settings are created here
bot_configs = MyBotConfigs(bot=bot, languages=languages, db=db)
bot_configs.set_languages(locales=[UK_LOCALE, RU_LOCALE], bot_language="uk")
bot_configs.set_menu_commands()

server = BotServer(bot)
app = server._app
