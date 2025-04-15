from dataclasses import dataclass

#? bot engine
from libs.bot_engine.server.FastAPIServer import FastAPIServer


@dataclass
class BotServer(FastAPIServer):
    pass
