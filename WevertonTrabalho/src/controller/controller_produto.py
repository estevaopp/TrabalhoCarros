from model.produto import Produto
from conexion.oracle_queries import OracleQueries

class Controller_Produto:
    def __init__(self):
        pass
        
    def inserir_produto(self) -> Produto:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuario o novo codigo_produto
        codigo_produto = input("codigo_produto (Novo): ")

        if self.verifica_existencia_produto(oracle, codigo_produto):
            # Solicita ao usuario o novo nome
            nome = input("Nome (Novo): ")
            # Solicita ao usuario o novo valor conusulta
            valor = input("Valor (Novo): ") 
            # Insere e persiste o novo produto
            oracle.write(f"insert into produtos values ('{codigo_produto}', '{nome}', '{valor}')")
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_produto = oracle.sqlToDataFrame(f"select codigo_produto, nome, valor from produtos where codigo_produto = '{codigo_produto}'")
            # Cria um novo objeto produto
            novo_produto = Produto(df_produto.codigo_produto.values[0], df_produto.nome.values[0], df_produto.valor.values[0])
            # Exibe os atributos do novo produto
            print(novo_produto.to_string())
            # Retorna o objeto novo_produto para utilização posterior, caso necessário
            return novo_produto
        else:
            print(f"O codigo_produto {codigo_produto} já está cadastrado.")
            return None

    def atualizar_produto(self) -> Produto:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        codigo_produto = int(input("codigo_produto do produto que deseja atualizar: "))

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_produto(oracle, codigo_produto):
            # Solicita ao usuario o novo nome
            nome = input("Nome (Novo): ")  
            # Solicita ao usuario o novo valor conusulta
            valor = input("Valor (Novo): ")            
            # Atualiza o nome do produto existente
            oracle.write(f"update produtos set nome = '{nome}', valor = '{valor}'  where codigo_produto = {codigo_produto}")
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_produto = oracle.sqlToDataFrame(f"select codigo_produto, nome, valor from produtos where codigo_produto = {codigo_produto}")
            # Cria um novo objeto produto
            produto_atualizado = Produto(df_produto.codigo_produto.values[0], df_produto.nome.values[0], df_produto.valor.values[0])
            # Exibe os atributos do novo produto
            print(produto_atualizado.to_string())
            # Retorna o objeto produto_atualizado para utilização posterior, caso necessário
            return produto_atualizado
        else:
            print(f"O codigo_produto {codigo_produto} não existe.")
            return None

    def excluir_produto(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o id_carrinho do produto a ser alterado
        codigo_produto = int(input("codigo_produto do produto que irá excluir: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_produto(oracle, codigo_produto):            
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_produto = oracle.sqlToDataFrame(f"select codigo_produto, nome, valor from produtos where codigo_produto = {codigo_produto}")
            # Revome o produto da tabela
            oracle.write(f"delete from itensCarrinhos where codigo_produto = {codigo_produto}")    
            oracle.write(f"delete from produtos where codigo_produto = {codigo_produto}")            
            # Cria um novo objeto produto para informar que foi removido
            produto_excluido = Produto(df_produto.codigo_produto.values[0], df_produto.nome.values[0], df_produto.valor.values[0])
            # Exibe os atributos do produto excluído
            print("produto Removido com Sucesso!")
            print(produto_excluido.to_string())
        else:
            print(f"O codigo_produto {codigo_produto} não existe.")

    def verifica_existencia_produto(self, oracle:OracleQueries, codigo_produto:str=None) -> bool:
        # Recupera os dados do novo produto criado transformando em um DataFrame
        df_produto = oracle.sqlToDataFrame(f"select codigo_produto, nome, valor from produtos where codigo_produto = {codigo_produto}")
        return df_produto.empty