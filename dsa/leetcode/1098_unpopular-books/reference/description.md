## Description

Assume the current date is `2019-06-23`. Report the books that sold fewer than 10 copies during the last year, after excluding books that have been available for less than one month.

The age rule excludes only releases later than `2019-05-23`; a book available on that date has reached one full month and remains eligible. For each eligible book, add the `quantity` values of orders dispatched from `2018-06-23` through `2019-06-23`, including both endpoints. A book with no orders in that period has sold zero copies. Return qualifying books in any order.
