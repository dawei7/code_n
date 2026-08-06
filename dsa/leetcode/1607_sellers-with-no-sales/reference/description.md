## Description

The database records customers, sellers, and orders. Each order identifies its customer and seller, its cost, and the date on which the sale occurred.

Find every seller who made no sale from January 1, 2020 through December 31, 2020, including both boundary dates. A seller still qualifies when they have orders outside 2020 or have never appeared in `Orders` at all. Return the qualifying seller names in ascending lexicographic order.
