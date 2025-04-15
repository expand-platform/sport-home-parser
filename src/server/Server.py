from dataclasses import dataclass

#? bot engine
from src.libs.bot_engine.server.FastAPIServer import FastAPIServer

@dataclass
class BotServer(FastAPIServer):
    pass
