from abc import ABC, abstractmethod

class IConexaoDAO(ABC):

    @abstractmethod
    def obter_conexao(self)
        pass

    @abstractmethod
    def executar_comando(self, sql_comando: str, commit: boolean) -> Any
        pass

    @abstractmethod 
    def executar_select (self, sql_select) -> list[Any]:
        pass





