from typing import List
from IProdutoDAO import IProdutoDAO
from models import Categoria

class IProdutoService:

    def __init__(self, produto_dao: IProdutoDAO):
        self.produto_dao = produto_dao

    def validar(self, produto):

    def incluir (self, produto) - > Produto:

    def alterar (self, produto) - > Produto:
    
    def excluir(self, produto):

    def obter_por_id(self, id):
    
    def listar(self) -> list[Produto]:
