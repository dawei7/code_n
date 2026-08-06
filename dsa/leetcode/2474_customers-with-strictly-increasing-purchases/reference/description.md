## Description

The `Orders` table records individual purchases. Each row has a unique order identifier, the customer who placed it, its date, and its price. A customer's total purchases for a calendar year are the sum of all their order prices during that year.

Report every customer whose yearly totals are strictly increasing from the year of their first order through the year of their last order. Every intervening calendar year participates in the comparison; if a customer placed no order in such a year, that year's total is zero. The output order is unrestricted.
