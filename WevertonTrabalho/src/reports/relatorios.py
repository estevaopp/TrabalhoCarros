from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("/home/labdatabase/GitHub/TrabalhoCarros/WevertonTrabalho/src/sql/relatorio_itensCarrinhos.sql") as f:
            self.query_relatorio_itensCarrinhos = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("/home/labdatabase/GitHub/TrabalhoCarros/WevertonTrabalho/src/sql/relatorio_itensCarrinhos_por_carrinho.sql") as f:
            self.query_relatorio_itensCarrinhos_por_carrinho = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("/home/labdatabase/GitHub/TrabalhoCarros/WevertonTrabalho/src/sql/relatorio_carrinhos.sql") as f:
            self.query_relatorio_carrinhos = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("/home/labdatabase/GitHub/TrabalhoCarros/WevertonTrabalho/src/sql/relatorio_produtos.sql") as f:
            self.query_relatorio_produtos = f.read()

    def get_relatorio_itensCarrinhos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_itensCarrinhos))
        input("Pressione Enter para Sair do Relatório de ItensCarrinhos")

    def get_relatorio_itensCarrinhos_por_carrinho(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_itensCarrinhos_por_carrinho))
        input("Pressione Enter para Sair do Relatório de Produtos")

    def get_relatorio_carrinhos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_carrinhos))
        input("Pressione Enter para Sair do Relatório de Carrinhos")

    def get_relatorio_produtos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_produtos))
        input("Pressione Enter para Sair do Relatório de Produtos")