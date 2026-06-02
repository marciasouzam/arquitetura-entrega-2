from app.entities.Categoria import Categoria


class Produto:

    def __init__(
        self,
        id: int = None,
        descricao: str = "",
        preco_unitario: float = 0.0,
        quantidade_estoque: int = 0,
        categoria_id: int = None,
        categoria: Categoria = None,
    ):
        self.id = id
        self.descricao = descricao
        self.preco_unitario = preco_unitario
        self.quantidade_estoque = quantidade_estoque
        self.categoria_id = categoria_id
        self.categoria = categoria

    def __str__(self):
        return (
            f"Produto(id={self.id}, descricao={self.descricao}, "
            f"preco_unitario={self.preco_unitario}, "
            f"quantidade_estoque={self.quantidade_estoque}, "
            f"categoria_id={self.categoria_id})"
        )

    def __repr__(self):
        return self.__str__()