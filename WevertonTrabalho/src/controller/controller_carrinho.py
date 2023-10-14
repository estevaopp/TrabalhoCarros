from model.carrinho import Carrinho
from conexion.oracle_queries import OracleQueries
from datetime import datetime

class Controller_Carrinho:
    def __init__(self):
        pass
        
    def inserir_carrinho(self) -> Carrinho:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuario o novo id_carrinho
        id_carrinho = input("id_carrinho (Novo): ")

        if self.verifica_existencia_carrinho(oracle, id_carrinho):
            # Solicita ao usuario o novo data_criacao
            data_criacao = datetime.now()
            # Insere e persiste o novo carrinho
            oracle.write(f"insert into carrinhos values ('{id_carrinho}', '{data_criacao}')")
            # Recupera os dados do novo carrinho criado transformando em um DataFrame
            df_carrinho = oracle.sqlToDataFrame(f"select id_carrinho, data_criacao from carrinhos where id_carrinho = '{id_carrinho}'")
            # Cria um novo objeto Carrinho
            novo_carrinho = Carrinho(df_carrinho.id_carrinho.values[0], df_carrinho.data_criacao.values[0])
            # Exibe os atributos do novo carrinho
            print(novo_carrinho.to_string())
            # Retorna o objeto novo_carrinho para utilização posterior, caso necessário
            return novo_carrinho
        else:
            print(f"O id_carrinho {id_carrinho} já está cadastrado.")
            return None

    def excluir_carrinho(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o id_carrinho do Carrinho a ser alterado
        id_carrinho = int(input("id_carrinho do Carrinho que irá excluir: "))        

        # Verifica se o carrinho existe na base de dados
        if not self.verifica_existencia_carrinho(oracle, id_carrinho):            
            # Recupera os dados do novo carrinho criado transformando em um DataFrame
            df_carrinho = oracle.sqlToDataFrame(f"select id_carrinho, data_criacao from carrinhos where id_carrinho = {id_carrinho}")
            # Revome o carrinho da tabela
            oracle.write(f"delete from itensCarrinhos where id_carrinho = {id_carrinho}")
            oracle.write(f"delete from carrinhos where id_carrinho = {id_carrinho}")
            # Cria um novo objeto Carrinho para informar que foi removido
            carrinho_excluido = Carrinho(df_carrinho.id_carrinho.values[0], df_carrinho.data_criacao.values[0])
            # Exibe os atributos do carrinho excluído
            print("Carrinho Removido com Sucesso!")
            print(carrinho_excluido.to_string())
        else:
            print(f"O id_carrinho {id_carrinho} não existe.")

    def verifica_existencia_carrinho(self, oracle:OracleQueries, id_carrinho:str=None) -> bool:
        # Recupera os dados do novo carrinho criado transformando em um DataFrame
        df_carrinho = oracle.sqlToDataFrame(f"select id_carrinho, data_criacao from carrinhos where id_carrinho = {id_carrinho}")
        return df_carrinho.empty