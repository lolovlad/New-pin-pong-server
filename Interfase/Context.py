from abc import ABC, abstractmethod


class Context(ABC):
    @abstractmethod
    def create_context(self):
        pass