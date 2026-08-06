WITH years(report_year, year_start, year_end) AS (
    VALUES
        ('2018', '2018-01-01', '2018-12-31'),
        ('2019', '2019-01-01', '2019-12-31'),
        ('2020', '2020-01-01', '2020-12-31')
)
SELECT p.product_id,
       p.product_name,
       y.report_year,
       s.average_daily_sales * CAST(
           julianday(MIN(s.period_end, y.year_end))
           - julianday(MAX(s.period_start, y.year_start))
           + 1 AS INTEGER
       ) AS total_amount
FROM Sales AS s
JOIN Product AS p
  ON p.product_id = s.product_id
JOIN years AS y
  ON s.period_start <= y.year_end
 AND s.period_end >= y.year_start
ORDER BY p.product_id, y.report_year;
