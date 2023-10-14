with sumariza_itensCarrinhos as (
    select ID_CARRINHO
         , count(1) as qtd_itensCarrinhos
      from itensCarrinhos
      group by ID_CARRINHO
)

select e.ID_CARRINHO as carrinho
     , sp.qtd_itensCarrinhos
     , sum(f.valor) as TotalCarrinho
  from itensCarrinhos p
  inner join sumariza_itensCarrinhos sp
  on p.ID_CARRINHO = sp.ID_CARRINHO
  inner join produtos f
  on p.codigo_produto = f.codigo_produto
  inner join carrinhos e
  on p.ID_CARRINHO = e.ID_CARRINHO
  group by sp.qtd_itensCarrinhos, e.ID_CARRINHO
  order by e.nome