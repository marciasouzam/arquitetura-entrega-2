from app.implementation.ConexaoBD import ConexaoBD
from app.implementation.CategoriaDAO import CategoriaDAO
from app.implementation.ProdutoDAO import ProdutoDAO
from app.implementation.repository.CategoriaService import CategoriaService
from app.implementation.repository.ProdutoService import ProdutoService


def criar_categoria_service() -> CategoriaService:
    conexao = ConexaoBD()
    dao = CategoriaDAO(conexao)
    return CategoriaService(dao)


def criar_produto_service() -> ProdutoService:
    conexao = ConexaoBD()
    dao = ProdutoDAO(conexao)
    return ProdutoService(dao)