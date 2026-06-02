from app.services.I_DAO.IConexaoBD import IConexaoBD
from app.services.I_DAO.ICategoriaDAO import ICategoriaDAO
from app.entities.Categoria import Categoria


class CategoriaDAO(ICategoriaDAO):

    def __init__(self, conexao: IConexaoBD):
        self.conexao = conexao

    def incluir(self, categoria: Categoria) -> Categoria:
        sql = f"""
            INSERT INTO Categoria (descricao)
            VALUES ('{categoria.descricao}')
        """
        self.conexao.executar_comando(sql, commit=True)
        return categoria

    def alterar(self, categoria: Categoria) -> Categoria:
        sql = f"""
            UPDATE Categoria
            SET descricao = '{categoria.descricao}'
            WHERE id = {categoria.id}
        """
        self.conexao.executar_comando(sql, commit=True)
        return categoria

    def excluir(self, categoria: Categoria):
        sql = f"""
            DELETE FROM Categoria WHERE id = {categoria.id}
        """
        self.conexao.executar_comando(sql, commit=True)

    def obter_por_id(self, id: int) -> Categoria:
        sql = f"""
            SELECT id, descricao
            FROM Categoria
            WHERE id = {id}
        """
        registros = self.conexao.executar_select(sql)
        if registros:
            reg = registros[0]
            return Categoria(id=reg[0], descricao=reg[1])
        return None

    def listar(self) -> list:
        sql = """
            SELECT id, descricao
            FROM Categoria
            ORDER BY descricao
        """
        registros = self.conexao.executar_select(sql)
        return [Categoria(id=reg[0], descricao=reg[1]) for reg in registros]