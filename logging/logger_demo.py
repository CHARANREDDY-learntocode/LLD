from log_config import LogConfig
from logging import Logger
from log_level import LogLevel
from channel import ConsoleChannel, FileChannel


# DemoLoggerApp Class (demonstrating the logger in action)
class DemoLoggerApp:
    def __init__(self):
        # Setup the log configuration with level INFO and using the demo console channel
        self.config = LogConfig(level=LogLevel.DEBUG, channel=ConsoleChannel())
        self.logger = Logger(self.config)

    def run(self):
        # Log messages of various levels
        self.logger.debug("This is a debug message")  # Will not be logged (level < INFO)
        self.logger.info("This is an info message")   # Will be logged
        self.logger.warning("This is a warning message")  # Will be logged
        self.logger.critical("This is a critical message")  # Will be logged

        self.config.set_channel(FileChannel("Output.txt"))
        self.logger.debug("This is a debug message")  # Will not be logged (level < INFO)
        self.logger.info("This is an info message")  # Will be logged
        self.logger.warning("This is a warning message")  # Will be logged
        self.logger.critical("This is a critical message")

        self.config.set_channel(ConsoleChannel())
        self.config.set_level(LogLevel.WARNING)
        self.logger.debug("This is a debug message")  # Will not be logged (level < INFO)
        self.logger.info("This is an info message")  # Will be logged
        self.logger.warning("This is a warning message")  # Will be logged
        self.logger.critical("This is a critical message")


# Running the demo
demo_app = DemoLoggerApp()
demo_app.run()
