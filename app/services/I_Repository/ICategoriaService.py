from abc import ABC, abstractmethod


class ICategoriaService(ABC):

    @abstractmethod
    def validar(self, categoria):
        pass

    @abstractmethod
    def incluir(self, categoria) -> object:
        pass

    @abstractmethod
    def alterar(self, categoria) -> object:
        pass

    @abstractmethod
    def excluir(self, categoria):
        pass

    @abstractmethod
    def obter_por_id(self, id: int) -> object:
        pass

    @abstractmethod
    def listar(self) -> list:
        pass