from IConexaoBD import IConexaoDAO
from IProdutoDAO import IProdutoDAO 
from models import Produto, Categoria  # os dois modelos são necessários
from typing import Any

class ProdutoDAO(IProdutoDAO): #herdando a interface

    # o construtor do DAO sempre pede a CONEXÃO
    def __init__(self, conexao: IConexaoBD):
        self.conexao = conexao

    def incluir (self, produto: Produto) -> Produto:
        sql = f''' INSERT INTO Produto (descricao, preco_unitario, quantidade_estoque, categoria_id)
        VALUES ('{produto.descricao}', {produto.preco_unitario}, {produto.quantidade_estoque}, {produto.categoria_id})
        ''' 

        parametros = ( #não está sendo utilizada
            produto.descricao,
            produto.preco_unitario,
            produto.quantidade_estoque,
            produto.categoria_id
        )

        self.conexao.executar_comando(sql, commit=True) # enviando exatamente 2 argumentos (sql, commit) para respeitar as exigências da interface
        return produto

    
    def alterar(self, produto: Produto) - > Produto:
        sql = f'''
            UPDATE Produto
            SET descricao = '{produto.descricao}',
                preco_unitario = {produto.preco_unitario},
                quantidade_estoque = {produto.quantidade_estoque},
                categoria_id = {produto.categoria_id}
            WHERE id = {produto.id}
        '''
 
        self.conexao.executar_comando(sql, commit=True)
        return produto
        

   
    def excluir(self, produto: Produto):
       
        sql = f'''
            DELETE FROM Produto WHERE id = {produto.id}
        '''
        self.conexao.executar_comando(sql, commit=True)
        
   
    def obter_por_id(self, id) -> Produto:

        sql = f'''
            SELECT  pro.id,
                    pro.descricao,
                    pro.preco_unitario,
                    pro.quantidade_estoque,
                    pro.categoria_id
            FROM Produto pro
            WHERE pro.id = {id}
        '''
        
        registros = self.conexao.executar_select(sql)
        
        if registros:
            reg = registros[0] 
            return Produto(
                id=reg[0], 
                descricao=reg[1], 
                preco_unitario=reg[2], 
                quantidade_estoque=reg[3], 
                categoria_id=reg[4]
            )
        return None
        

    def listar(self) -> list[Categoria]:

        sql = '''
            SELECT  pro.id,
                    pro.descricao,
                    pro.preco_unitario,
                    pro.quantidade_estoque,
                    pro.categoria_id,
                    cat.descricao as categoria

            FROM Produto pro

            INNER JOIN Categoria cat
                ON cat.id = pro.categoria_id

            ORDER BY pro.descricao
        '''

        registros = self.conexao.executar_select(sql)
        
        lista_produtos = []
        for reg in registros:
            lista_produtos.append(
                Produto(
                    id=reg[0], 
                    descricao=reg[1], 
                    preco_unitario=reg[2], 
                    quantidade_estoque=reg[3], 
                    categoria_id=reg[4]
                )
            )
        return lista_produtos
        



 
