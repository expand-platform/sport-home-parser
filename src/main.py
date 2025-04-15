#? bot engine
from libs.bot_engine.bot.Bot import Bot
from libs.bot_engine.languages.Languages import Languages
from libs.bot_engine.database.Database import Database
from libs.bot_engine.data.env import DEFAULT_LANGUAGE

#? engine customization
from bot.BotConfigs import MyBotConfigs
from server.Server import BotServer

#? languages
from data.locales.uk import UK_LOCALE
from data.locales.ru import RU_LOCALE

#? dialogs
from dialogs.AdminDialogs import AdminDialogs


# Bot components
db = Database()
languages = Languages()
bot = Bot(db)

# Bot plugins and settings are created here
bot_configs = MyBotConfigs(bot=bot, languages=languages, db=db)
bot_configs.set_languages(locales=[UK_LOCALE, RU_LOCALE], bot_language=DEFAULT_LANGUAGE)
bot_configs.set_menu_commands()


if __name__ == "__main__":
    server = BotServer(bot=bot)
    server.run()



