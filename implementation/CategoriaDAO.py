from IConexaoBD import IConexaoDAO
from ICategoriaDAO import ICategoriaDAO
from models import Categoria
from typing import Any

class CategoriaDAO(ICategoriaDAO):

    def __init__(self, conexao: IConexaoDAO):
        self.conexao = conexao

    def incluir(self, categoria: Categoria) -> Categoria:
        sql = f'''
            INSERT INTO Categoria (descricao)
            VALUES ('{categoria.descricao}')
        '''
        self.conexao.executar_comando(sql, commit=True)
        return categoria

    def alterar(self, categoria: Categoria) -> Categoria:
        sql = f'''
            UPDATE Categoria
            SET descricao = '{categoria.descricao}'
            WHERE id = {categoria.id}
        '''
        self.conexao.executar_comando(sql, commit=True)
        return categoria

    def excluir(self, categoria: Categoria):
        sql = f'''
            DELETE FROM Categoria WHERE id = {categoria.id}
        '''
        self.conexao.executar_comando(sql, commit=True)

    def obtener_por_id(self, id: int) -> Categoria:
        sql = f'''
            SELECT id, descricao
            FROM Categoria
            WHERE id = {id}
        '''
        registros = self.conexao.executar_select(sql)
        
        if registros:
            reg = registros[0]
            return Categoria(id=reg[0], descricao=reg[1])
        return None

    def listar(self) -> list[Categoria]:
        sql = '''
            SELECT id, descricao
            FROM Categoria
            ORDER BY descricao
        '''
        registros = self.conexao.executar_select(sql)
        
        lista_categorias = []
        for reg in registros:
            lista_categorias.append(
                Categoria(id=reg[0], descricao=reg[1])
            )
        return lista_categorias