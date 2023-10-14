from pydoc import cli
from model.itensCarrinho import ItensCarrinho
from model.carrinho import Carrinho
from controller.controller_carrinho import Controller_Carrinho
from model.produto import Produto
from controller.controller_produto import Controller_Produto
from conexion.oracle_queries import OracleQueries
from datetime import datetime

class Controller_ItensCarrinho:
    def __init__(self):
        self.ctrl_carrinho = Controller_Carrinho()
        self.ctrl_produto = Controller_Produto()
        
    def inserir_itensCarrinho(self) -> ItensCarrinho:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        
        # Lista os carrinhos existentes para inserir no itensCarrinho
        self.listar_carrinhos(oracle, need_connect=True)
        id_carrinho = str(input("Digite o número do id_carrinho do Carrinho: "))
        carrinho = self.valida_carrinho(oracle, id_carrinho)
        if carrinho == None:
            return None

        # Lista os produtos existentes para inserir no itensCarrinho
        self.listar_produtos(oracle, need_connect=True)
        codigo_produto = str(input("Digite o número do codigo_produto do Produto: "))
        produto = self.valida_produto(oracle, codigo_produto)
        if produto == None:
            return None

        data_hoje = datetime.now()

        # Recupera o cursos para executar um bloco PL/SQL anônimo
        cursor = oracle.connect()
        # Cria a variável de saída com o tipo especificado
        output_value = cursor.var(int)

        # Cria um dicionário para mapear as variáveis de entrada e saída
        data = dict(codigo=output_value, data_itensCarrinho=data_hoje, id_carrinho=carrinho.get_id_carrinho(), codigo_produto=produto.get_codigo_produto())
        # Executa o bloco PL/SQL anônimo para inserção do novo produto e recuperação da chave primária criada pela sequence
        cursor.execute("""
        begin
            :codigo := ITENSCARRINHOS_CODIGO_ITENSCARRINHO_SEQ.NEXTVAL;
            insert into itensCarrinhos values(:codigo, :data_itensCarrinho, :id_carrinho, :codigo_produto);
        end;
        """, data)
        # Recupera o código do novo produto
        codigo_itensCarrinho = output_value.getvalue()
        # Persiste (confirma) as alterações
        oracle.conn.commit()
        # Recupera os dados do novo produto criado transformando em um DataFrame
        df_itensCarrinho = oracle.sqlToDataFrame(f"select codigo_itensCarrinho, data_itensCarrinho from itensCarrinhos where codigo_itensCarrinho = {codigo_itensCarrinho}")
        # Cria um novo objeto Produto
        novo_itensCarrinho = ItensCarrinho(df_itensCarrinho.codigo_itensCarrinho.values[0], df_itensCarrinho.data_itensCarrinho.values[0], carrinho, produto)
        # Exibe os atributos do novo produto
        print(novo_itensCarrinho.to_string())
        # Retorna o objeto novo_itensCarrinho para utilização posterior, caso necessário
        return novo_itensCarrinho

    def atualizar_itensCarrinho(self) -> ItensCarrinho:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        codigo_itensCarrinho = int(input("Código do ItensCarrinho que irá alterar: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_itensCarrinho(oracle, codigo_itensCarrinho):

            # Lista os carrinhos existentes para inserir no itensCarrinho
            self.listar_carrinhos(oracle)
            id_carrinho = str(input("Digite o número do id_carrinho do Carrinho: "))
            carrinho = self.valida_carrinho(oracle, id_carrinho)
            if carrinho == None:
                return None

            # Lista os produtos existentes para inserir no itensCarrinho
            self.listar_produtos(oracle)
            codigo_produto = str(input("Digite o número do codigo_produto do Produto: "))
            produto = self.valida_produto(oracle, codigo_produto)
            if produto == None:
                return None
            
            data_hoje = datetime.now()

            # Atualiza a descrição do produto existente
            oracle.write(f"update itensCarrinhos set id_carrinho = '{carrinho.get_id_carrinho()}', codigo_produto = '{produto.get_codigo_produto()}', data_itensCarrinho = to_date('{data_hoje}','yyyy-mm-dd') where codigo_itensCarrinho = {codigo_itensCarrinho}")
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_itensCarrinho = oracle.sqlToDataFrame(f"select codigo_itensCarrinho, data_itensCarrinho from itensCarrinhos where codigo_itensCarrinho = {codigo_itensCarrinho}")
            # Cria um novo objeto Produto
            itensCarrinho_atualizado = ItensCarrinho(df_itensCarrinho.codigo_itensCarrinho.values[0], df_itensCarrinho.data_itensCarrinho.values[0], carrinho, produto)
            # Exibe os atributos do novo produto
            print(itensCarrinho_atualizado.to_string())
            # Retorna o objeto itensCarrinho_atualizado para utilização posterior, caso necessário
            return itensCarrinho_atualizado
        else:
            print(f"O código {codigo_itensCarrinho} não existe.")
            return None

    def excluir_itensCarrinho(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        codigo_itensCarrinho = int(input("Código do ItensCarrinho que irá excluir: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_itensCarrinho(oracle, codigo_itensCarrinho):            
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_itensCarrinho = oracle.sqlToDataFrame(f"select codigo_itensCarrinho, data_itensCarrinho, id_carrinho, codigo_produto from itensCarrinhos where codigo_itensCarrinho = {codigo_itensCarrinho}")
            carrinho = self.valida_carrinho(oracle, df_itensCarrinho.id_carrinho.values[0])
            produto = self.valida_produto(oracle, df_itensCarrinho.codigo_produto.values[0])
            
            opcao_excluir = input(f"Tem certeza que deseja excluir o itensCarrinho {codigo_itensCarrinho} [S ou N]: ")
            if opcao_excluir.lower() == "s":
                print("Atenção, caso o itensCarrinho possua itens, também serão excluídos!")
                    # Revome o produto da tabela
                oracle.write(f"delete from itensCarrinhos where codigo_itensCarrinho = {codigo_itensCarrinho}")
                # Cria um novo objeto Produto para informar que foi removido
                itensCarrinho_excluido = ItensCarrinho(df_itensCarrinho.codigo_itensCarrinho.values[0], df_itensCarrinho.data_itensCarrinho.values[0], carrinho, produto)
                # Exibe os atributos do produto excluído
                print("ItensCarrinho Removido com Sucesso!")
                print(itensCarrinho_excluido.to_string())
        else:
            print(f"O código {codigo_itensCarrinho} não existe.")

    def verifica_existencia_itensCarrinho(self, oracle:OracleQueries, codigo:int=None) -> bool:
        # Recupera os dados do novo itensCarrinho criado transformando em um DataFrame
        df_itensCarrinho = oracle.sqlToDataFrame(f"select codigo_itensCarrinho, data_itensCarrinho from itensCarrinhos where codigo_itensCarrinho = {codigo}")
        return df_itensCarrinho.empty

    def listar_carrinhos(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select c.id_carrinho
                    , c.data_criacao 
                from carrinhos c
                order by c.data_criacao
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def listar_produtos(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select f.codigo_produto
                    , f.nome
                    , f.valor
                from produtos f
                order by f.nome
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def valida_carrinho(self, oracle:OracleQueries, id_carrinho:str=None) -> Carrinho:
        if self.ctrl_carrinho.verifica_existencia_carrinho(oracle, id_carrinho):
            print(f"O id_carrinho {id_carrinho} informado não existe na base.")
            return None
        else:
            oracle.connect()
            # Recupera os dados do novo carrinho criado transformando em um DataFrame
            df_carrinho = oracle.sqlToDataFrame(f"select id_carrinho, data_criacao from carrinhos where id_carrinho = {id_carrinho}")
            # Cria um novo objeto carrinho
            carrinho = Carrinho(df_carrinho.id_carrinho.values[0], df_carrinho.data_criacao.values[0])
            return carrinho

    def valida_produto(self, oracle:OracleQueries, codigo_produto:str=None) -> Produto:
        if self.ctrl_produto.verifica_existencia_produto(oracle, codigo_produto):
            print(f"O codigo_produto {codigo_produto} informado não existe na base.")
            return None
        else:
            oracle.connect()
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_produto = oracle.sqlToDataFrame(f"select codigo_produto, nome, valor from produtos where codigo_produto = {codigo_produto}")
            # Cria um novo objeto produto
            produto = Produto(df_produto.codigo_produto.values[0], df_produto.nome.values[0], df_produto.valor.values[0])
            return produto