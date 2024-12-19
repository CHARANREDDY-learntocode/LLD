# LogConfig Class
class LogConfig:
    def __init__(self, level, channel):
        self.level = level
        self.channel = channel

    def set_level(self, level):
        self.level = level

    def set_channel(self, channel):
        self.channel = channel