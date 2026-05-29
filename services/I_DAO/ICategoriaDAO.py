from abc import ABC, abstractmethod

class ICategoriaDAO(ABC):

    @abstractmethod
    def incluir(self, categoria)