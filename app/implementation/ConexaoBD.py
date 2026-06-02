import sqlite3
from typing import Any
from app.services.I_DAO.IConexaoBD import IConexaoBD


class ConexaoBD(IConexaoBD):

    def __init__(self, nome_banco: str = "db_solid.sqlite3"):
        self.nome_banco = nome_banco
        self._conexao_ativa = None

    def obter_conexao(self):
        if self._conexao_ativa is None:
            self._conexao_ativa = sqlite3.connect(self.nome_banco)
            self._conexao_ativa.execute("PRAGMA foreign_keys = ON;")
        return self._conexao_ativa

    def executar_comando(self, sql_comando: str, commit: bool = True):
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(sql_comando)
        if commit:
            conexao.commit()

    def executar_select(self, sql_select) -> list:
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(sql_select)
        return cursor.fetchall()