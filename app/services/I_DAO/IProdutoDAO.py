from abc import ABC, abstractmethod
from app.entities.Produto import Produto
class IProdutoDAO(ABC):
    
    @abstractmethod
    def incluir (self, produto: Produto) -> Produto:
        pass

    @abstractmethod
    def alterar(self, produto: Produto) -> Produto:
        pass

    @abstractmethod
    def excluir(self, produto: Produto):
        pass
     
    @abstractmethod
    def obter_por_id(self, id) -> Produto:
        pass

    @abstractmethod
    def listar(self) -> list:
        pass