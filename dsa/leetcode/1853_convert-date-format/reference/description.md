## Description

The `Days` table stores unique calendar dates in a single `DATE` column named `day`. Produce one result row for every input row, converting the stored date into a human-readable English string while preserving the date itself rather than filtering, grouping, or reordering it.

The required text has the form `"day_name, month_name day, year"`. Spell out the weekday and month with their usual capitalization, place a comma after the weekday and before the year, and write the numeric day of the month without a leading zero. The returned column must also be named `day`; row order is unrestricted.
