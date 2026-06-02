from abc import ABC, abstractmethod


class IProdutoService(ABC):

    @abstractmethod
    def validar(self, produto):
        pass

    @abstractmethod
    def incluir(self, produto) -> object:
        pass

    @abstractmethod
    def alterar(self, produto) -> object:
        pass

    @abstractmethod
    def excluir(self, produto):
        pass

    @abstractmethod
    def obter_por_id(self, id: int) -> object:
        pass

    @abstractmethod
    def listar(self) -> list:
        pass