from app.services.I_DAO.IProdutoDAO import IProdutoDAO
from app.entities.Produto import Produto


class ProdutoService:

    def __init__(self, dao: IProdutoDAO):
        self.dao = dao

    def validar(self, produto: Produto):
        """Valida os dados de um produto antes de persistir."""
        if not produto.descricao or produto.descricao.strip() == "":
            raise ValueError("A descrição do produto não pode ser vazia.")
        if len(produto.descricao.strip()) < 2:
            raise ValueError("A descrição do produto deve ter ao menos 2 caracteres.")
        if produto.preco_unitario is None or produto.preco_unitario < 0:
            raise ValueError("O preço unitário deve ser maior ou igual a zero.")
        if produto.quantidade_estoque is None or produto.quantidade_estoque < 0:
            raise ValueError("A quantidade em estoque deve ser maior ou igual a zero.")
        if produto.categoria_id is None:
            raise ValueError("O produto deve estar vinculado a uma categoria.")
        produto.descricao = produto.descricao.strip()

    def incluir(self, produto: Produto) -> Produto:
        """Valida e inclui um novo produto."""
        self.validar(produto)
        return self.dao.incluir(produto)

    def alterar(self, produto: Produto) -> Produto:
        """Valida e altera um produto existente."""
        if produto.id is None:
            raise ValueError("ID do produto não informado para alteração.")
        self.validar(produto)
        return self.dao.alterar(produto)

    def excluir(self, produto: Produto):
        """Exclui um produto pelo objeto."""
        if produto.id is None:
            raise ValueError("ID do produto não informado para exclusão.")
        self.dao.excluir(produto)

    def obter_por_id(self, id: int) -> Produto:
        """Retorna um produto pelo ID."""
        if id is None or id <= 0:
            raise ValueError("ID inválido.")
        return self.dao.obter_por_id(id)

    def listar(self) -> list:
        """Retorna a lista de todos os produtos."""
        return self.dao.listar()