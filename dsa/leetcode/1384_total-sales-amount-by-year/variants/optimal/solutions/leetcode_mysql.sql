SELECT p.product_id,
       p.product_name,
       annual.report_year,
       SUM(annual.total_amount) AS total_amount
FROM Product AS p
JOIN (
    SELECT product_id,
           '2018' AS report_year,
           average_daily_sales * (
               DATEDIFF(
                   LEAST(period_end, '2018-12-31'),
                   GREATEST(period_start, '2018-01-01')
               ) + 1
           ) AS total_amount
    FROM Sales
    WHERE period_start <= '2018-12-31'
      AND period_end >= '2018-01-01'

    UNION ALL

    SELECT product_id,
           '2019' AS report_year,
           average_daily_sales * (
               DATEDIFF(
                   LEAST(period_end, '2019-12-31'),
                   GREATEST(period_start, '2019-01-01')
               ) + 1
           ) AS total_amount
    FROM Sales
    WHERE period_start <= '2019-12-31'
      AND period_end >= '2019-01-01'

    UNION ALL

    SELECT product_id,
           '2020' AS report_year,
           average_daily_sales * (
               DATEDIFF(
                   LEAST(period_end, '2020-12-31'),
                   GREATEST(period_start, '2020-01-01')
               ) + 1
           ) AS total_amount
    FROM Sales
    WHERE period_start <= '2020-12-31'
      AND period_end >= '2020-01-01'
) AS annual
  ON annual.product_id = p.product_id
GROUP BY p.product_id, p.product_name, annual.report_year
ORDER BY p.product_id, annual.report_year;
