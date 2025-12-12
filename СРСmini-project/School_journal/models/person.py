from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, id, name, age):
        self._id = id
        self._name = name
        self._age = age

    @abstractmethod
    def get_info(self):
        pass

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age