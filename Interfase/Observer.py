from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self, struct):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass
