WITH years(report_year, year_start, year_end) AS (
    VALUES
        ('2018', '2018-01-01', '2018-12-31'),
        ('2019', '2019-01-01', '2019-12-31'),
        ('2020', '2020-01-01', '2020-12-31')
)
SELECT p.product_id,
       p.product_name,
       y.report_year,
       CAST(
           SUM(
               (
                   julianday(MIN(s.period_end, y.year_end))
                   - julianday(MAX(s.period_start, y.year_start))
                   + 1
               ) * s.average_daily_sales
           ) AS INTEGER
       ) AS total_amount
FROM Product AS p
JOIN Sales AS s
  ON s.product_id = p.product_id
JOIN years AS y
  ON s.period_start <= y.year_end
 AND s.period_end >= y.year_start
GROUP BY p.product_id, p.product_name, y.report_year
ORDER BY p.product_id, y.report_year;
