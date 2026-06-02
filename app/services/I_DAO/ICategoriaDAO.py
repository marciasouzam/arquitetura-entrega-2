from abc import ABC, abstractmethod
from app.entities.Categoria import Categoria

class ICategoriaDAO(ABC):

    @abstractmethod
    def incluir(self, categoria: Categoria) -> Categoria:
        pass

    @abstractmethod
    def alterar(self, categoria: Categoria) -> Categoria:
        pass

    @abstractmethod
    def excluir(self, categoria: Categoria):
        pass

    @abstractmethod
    def obter_por_id(self, id: int) -> Categoria:
        pass

    @abstractmethod
    def listar(self) -> list:
        pass
