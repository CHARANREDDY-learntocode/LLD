from abc import ABC, abstractmethod


# BaseChannel Interface Class
class BaseChannel(ABC):
    @abstractmethod
    def write(self, log_message):
        pass

# ConsoleChannel Class
class ConsoleChannel(BaseChannel):
    def write(self, log_message):
        print(f"[{log_message.timestamp}] {log_message.log_level.name}: {log_message.content}")

# FileChannel Class
class FileChannel(BaseChannel):
    def __init__(self, filename):
        self.filename = filename

    def write(self, log_message):
        with open(self.filename, 'a') as file:
            file.write(f"{log_message.timestamp} - {log_message.log_level.name}: {log_message.content}\n")