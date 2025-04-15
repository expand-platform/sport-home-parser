import signal
from threading import Thread
from dataclasses import dataclass, field

from typing import Callable

import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from keyboard import add_hotkey

#? bot engine
from src.libs.bot_engine.data.env import ENVIRONMENT
from src.libs.bot_engine.bot.Bot import Bot


@dataclass
class FastAPIServer:
    """FastAPI server with thread & signal handling."""

    Bot: Bot 

    #? neccessary customizable bot dependencies
    components: list[Callable] = field(default_factory=list)
    
    #? private data
    _app: FastAPI = field(init=False)
    _bot_thread: Thread = field(init=False)
    _hotkey_listener_thread: Thread = field(init=False)


    def __post_init__(self):
        self._app = FastAPI(lifespan=self._lifespan)
        self._setup_signal_handlers()


    @asynccontextmanager
    async def _lifespan(self, app: FastAPI):
        print("⚡ FastAPI server started.")
        self.start_threads()
        try:
            yield
        finally:
            self.shutdown()

    def start_threads(self):
        if ENVIRONMENT in {"development", "testing"}:
            self._start_ctrl_c_listener()
        
        self._run_bot_components()


    def _run_bot_components(self):

        self._bot_thread = Thread(target=self.Bot.start, name="BotThread")
        self._bot_thread.start()


    def _start_ctrl_c_listener(self):
        self._hotkey_listener_thread = Thread(target=self._handle_ctrl_c, name="HotkeyListener")
        self._hotkey_listener_thread.start()


    def _handle_ctrl_c(self):
        add_hotkey("ctrl+c", self.shutdown)


    def _setup_signal_handlers(self):
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)


    def _signal_handler(self, signum, frame):
        print(f"⚠️ Signal received: {signal.Signals(signum).name}")
        self.shutdown()


    def shutdown(self):
        print("🛑 Shutting down...")

        self.Bot.disconnect()
        # uvicorn.server.Server.should_exit = True

        if self._hotkey_listener_thread and self._hotkey_listener_thread.is_alive():
            self._hotkey_listener_thread.join()

        if self._bot_thread and self._bot_thread.is_alive():
            self._bot_thread.join()

        print("❌ FastAPI server stopped.")
