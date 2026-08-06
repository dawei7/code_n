## Description

Each `Sales` row assigns one constant daily sales amount to an inclusive date interval for a product. Because an interval may cross a calendar-year boundary, its contribution must be divided among the years that it overlaps rather than assigned wholly to its starting or ending year.

For every product and calendar year containing at least one day of that product's sales period, report the product ID, product name, year, and total sales amount contributed by the days in that year. Order the result first by `product_id` and then by `report_year`.
