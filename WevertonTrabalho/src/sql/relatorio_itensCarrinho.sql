select p.codigo_itensCarrinho
     , p.data_itensCarrinho
     , c.ID_CARRINHO as carrinho
     , f.nome as produto
  from itensCarrinhos p
  inner join carrinhos c
  on p.ID_CARRINHO = c.ID_CARRINHO
  inner join produtos f
  on p.codigo_produto = f.codigo_produto
  order by c.ID_CARRINHO