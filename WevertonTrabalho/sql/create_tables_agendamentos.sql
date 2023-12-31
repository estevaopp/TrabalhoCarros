/*Apaga os relacionamentos*/
ALTER TABLE LABDATABASE.ITENSCARRINHOS DROP CONSTRAINT PRODUTOS_ITENSCARRINHOS_FK;
ALTER TABLE LABDATABASE.ITENSCARRINHOS DROP CONSTRAINT CARRINHOS_ITENSCARRINHOS_FK;

/*Apaga as tabelas*/
DROP TABLE LABDATABASE.PRODUTOS;
DROP TABLE LABDATABASE.CARRINHOS;
DROP TABLE LABDATABASE.ITENSCARRINHOS;

/*Apaga as sequences*/
DROP SEQUENCE LABDATABASE.ITENSCARRINHOS_CODIGO_ITENSCARRINHO_SEQ;

/*Cria as tabelas*/
CREATE TABLE LABDATABASE.PRODUTOS (
                CODIGO_PRODUTO VARCHAR2(11) NOT NULL,
                NOME VARCHAR2(255) NOT NULL,
                VALOR NUMBER(9,2) not null,
                CONSTRAINT PRODUTOS_PK PRIMARY KEY (CODIGO_PRODUTO)
);

CREATE TABLE LABDATABASE.CARRINHOS (
                ID_CARRINHO VARCHAR2(11) NOT NULL,
                DATA_CRIACAO DATETIME NOT NULL,
                CONSTRAINT CARRINHOS_PK PRIMARY KEY (ID_CARRINHO)
);

CREATE TABLE LABDATABASE.ITENSCARRINHOS (
                CODIGO_ITENSCARRINHO NUMBER NOT NULL,
                DATA_ITENSCARRINHO DATETIME NOT NULL,
                ID_CARRINHO VARCHAR2(11) NOT NULL,
                CODIGO_PRODUTO VARCHAR2(11) NOT NULL,
                CONSTRAINT ITENSCARRINHOS_PK PRIMARY KEY (CODIGO_ITENSCARRINHO)
);

/*Cria as sequences*/
CREATE SEQUENCE LABDATABASE.ITENSCARRINHOS_CODIGO_ITENSCARRINHO_SEQ;

/*Cria os relacionamentos*/
ALTER TABLE LABDATABASE.ITENSCARRINHOS ADD CONSTRAINT PRODUTOS_ITENSCARRINHOS_FK
FOREIGN KEY (CODIGO_PRODUTO)
REFERENCES LABDATABASE.PRODUTOS (CODIGO_PRODUTO)
NOT DEFERRABLE;

ALTER TABLE LABDATABASE.ITENSCARRINHOS ADD CONSTRAINT CARRINHOS_ITENSCARRINHOS_FK
FOREIGN KEY (ID_CARRINHO)
REFERENCES LABDATABASE.CARRINHOS (ID_CARRINHO)
NOT DEFERRABLE;

/*Garante acesso total as tabelas*/
GRANT ALL ON LABDATABASE.PRODUTOS TO LABDATABASE;
GRANT ALL ON LABDATABASE.CARRINHOS TO LABDATABASE;
GRANT ALL ON LABDATABASE.ITENSCARRINHOS TO LABDATABASE;

ALTER USER LABDATABASE quota unlimited on USERS;

commit;