from app.services.I_DAO.ICategoriaDAO import ICategoriaDAO
from app.entities.Categoria import Categoria


class CategoriaService:

    def __init__(self, dao: ICategoriaDAO):
        self.dao = dao

    def validar(self, categoria: Categoria):
        if not categoria.descricao or categoria.descricao.strip() == "":
            raise ValueError("A descrição da categoria não pode ser vazia.")
        if len(categoria.descricao.strip()) < 2:
            raise ValueError("A descrição da categoria deve ter ao menos 2 caracteres.")
        categoria.descricao = categoria.descricao.strip()

    def incluir(self, categoria: Categoria) -> Categoria:
        self.validar(categoria)
        return self.dao.incluir(categoria)

    def alterar(self, categoria: Categoria) -> Categoria:
        """Valida e altera uma categoria existente."""
        if categoria.id is None:
            raise ValueError("ID da categoria não informado para alteração.")
        self.validar(categoria)
        return self.dao.alterar(categoria)

    def excluir(self, categoria: Categoria):
        """Exclui uma categoria pelo objeto."""
        if categoria.id is None:
            raise ValueError("ID da categoria não informado para exclusão.")
        self.dao.excluir(categoria)

    def obter_por_id(self, id: int) -> Categoria:
        """Retorna uma categoria pelo ID."""
        if id is None or id <= 0:
            raise ValueError("ID inválido.")
        return self.dao.obter_por_id(id)

    def listar(self) -> list:
        """Retorna a lista de todas as categorias."""
        return self.dao.listar()