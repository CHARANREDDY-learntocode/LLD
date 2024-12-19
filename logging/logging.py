import threading
from datetime import datetime
from log_level import LogLevel
from log_message import LogMessage

# Logger Class (Singleton)
class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self, config):
        with self._lock:
            if not hasattr(self, "initialized"):
                self.config = config
                self.initialized = True

    def _log(self, log_level, message):
        if log_level.value >= self.config.level.value:
            log_message = LogMessage(datetime.now(), log_level, message)
            with self._lock:
                self.config.channel.write(log_message)

    def info(self, message):
        self._log(LogLevel.INFO, message)

    def debug(self, message):
        self._log(LogLevel.DEBUG, message)

    def warning(self, message):
        self._log(LogLevel.WARNING, message)

    def critical(self, message):
        self._log(LogLevel.CRITICAL, message)
