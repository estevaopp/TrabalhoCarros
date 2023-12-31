/*INSERE DADOS NA TABELA DE ITENSCARRINHOS E ITENS*/
DECLARE
  VCOD_ITENSCARRINHO NUMBER;
BEGIN
  VCOD_ITENSCARRINHO := LABDATABASE.ITENSCARRINHOS_CODIGO_ITENSCARRINHO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.ITENSCARRINHOS VALUES(VCOD_ITENSCARRINHO,    /*CODIGO_ITENSCARRINHO*/
                             SYSDATE,        /*DATA_ITENSCARRINHO*/
                             '43201234567',  /*CPF*/
                             '12855579797'/*CNPJ*/
                             );

END;
--
DECLARE
  VCOD_ITENSCARRINHO NUMBER;
BEGIN
  VCOD_ITENSCARRINHO := LABDATABASE.ITENSCARRINHOS_CODIGO_ITENSCARRINHO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.ITENSCARRINHOS VALUES(VCOD_ITENSCARRINHO,    /*CODIGO_ITENSCARRINHO*/
                             SYSDATE,        /*DATA_ITENSCARRINHO*/
                             '01234567891',  /*CPF*/
                             '012345678912'/*CNPJ*/
                             );
END;
--
DECLARE
  VCOD_ITENSCARRINHO NUMBER;
  VCOD_ITEM_ITENSCARRINHO NUMBER;
  VCOD_PRODUTO NUMBER;
BEGIN
  VCOD_ITENSCARRINHO := LABDATABASE.ITENSCARRINHOS_CODIGO_ITENSCARRINHO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.ITENSCARRINHOS VALUES(VCOD_ITENSCARRINHO,    /*CODIGO_ITENSCARRINHO*/
                             SYSDATE,        /*DATA_ITENSCARRINHO*/
                             '87654320123',  /*CPF*/
                             '12855579796'/*CNPJ*/
                             );
  
END;
--
DECLARE
  VCOD_ITENSCARRINHO NUMBER;
  VCOD_ITEM_ITENSCARRINHO NUMBER;
  VCOD_PRODUTO NUMBER;
BEGIN
  VCOD_ITENSCARRINHO := LABDATABASE.ITENSCARRINHOS_CODIGO_ITENSCARRINHO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.ITENSCARRINHOS VALUES(VCOD_ITENSCARRINHO,    /*CODIGO_ITENSCARRINHO*/
                             SYSDATE,        /*DATA_ITENSCARRINHO*/
                             '32012345678',  /*CPF*/
                             '12855579795'/*CNPJ*/
                             );
                                  
END;
--
DECLARE
  VCOD_ITENSCARRINHO NUMBER;
  VCOD_ITEM_ITENSCARRINHO NUMBER;
  VCOD_PRODUTO NUMBER;
BEGIN
  VCOD_ITENSCARRINHO := LABDATABASE.ITENSCARRINHOS_CODIGO_ITENSCARRINHO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.ITENSCARRINHOS VALUES(VCOD_ITENSCARRINHO,    /*CODIGO_ITENSCARRINHO*/
                             SYSDATE,        /*DATA_ITENSCARRINHO*/
                             '76543201234',  /*CPF*/
                             '12855579794'/*CNPJ*/
                             );
                                  
END;