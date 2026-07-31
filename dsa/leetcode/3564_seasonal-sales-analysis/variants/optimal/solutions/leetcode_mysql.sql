WITH x AS (
 SELECT ELT(MOD(MONTH(sale_date),12) DIV 3+1,'Winter','Spring','Summer','Fall') season,
        category,SUM(quantity) total_quantity,SUM(quantity*price) total_revenue
 FROM sales JOIN products USING(product_id)
 GROUP BY season,category
), y AS (
 SELECT x.*,ROW_NUMBER() OVER(
  PARTITION BY season
  ORDER BY total_quantity DESC,total_revenue DESC,category
 ) r
 FROM x
)
SELECT season,category,total_quantity,total_revenue
FROM y
WHERE r=1
ORDER BY season
