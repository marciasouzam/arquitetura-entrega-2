from ICategoriaDAO import ICategoriaDAO
from IConexaoBD import IConexaoBD
from models import Categoria
from typing import Any

class CategoriaDAO(ICategoriaDAO): #herdando a interface

    def __init__(self, conexao: IConexaoBD):


    def incluir(self, categoria: Categoria):
  

    def alterar(self, categoria: Categoria):
 
    
    def excluir(self, categoria: Categoria):


    def obter_por_id(self, id: int) -> Categoria:

    
    def listar(self) -> list[Categoria]:
      
