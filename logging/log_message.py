from datetime import datetime


# LogMessage Class
class LogMessage:
    def __init__(self, timestamp: datetime, log_level, content: str):
        self.timestamp = timestamp
        self.log_level = log_level
        self.content = content