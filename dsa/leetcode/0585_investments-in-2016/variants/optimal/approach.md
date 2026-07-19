## General
**Classify both kinds of duplicate independently**

Use one partition count grouped by `tiv_2015` and another grouped by the coordinate pair `(lat, lon)`. Every policy row then carries the size of its value group and its location group.

**Apply the two conditions together**

A row qualifies only when the 2015-value count is greater than one and the location count equals one. The first condition requires at least one other policy with the same value; the second rejects every member of a duplicated coordinate pair.

**Sum only after row classification**

Filter the classified rows, sum their `tiv_2016` values, and round the aggregate to two decimal places. Counting with windows preserves individual policy rows, so each qualifying investment contributes exactly once.

**Why the aggregate is exact**

Partition counts equal the total occurrences of each relevant key over the full table. The filter therefore accepts exactly the intersection of the shared-value set and unique-location set. Summing the 2016 values of those retained rows is precisely the requested total; no grouping collapses distinct qualifying policies before the sum.

## Complexity detail
For `n` policies, database window partitions generally require sorting or indexed grouping in $O(n \log n)$ time and $O(n)$ working space. The final filter and sum are linear.

## Alternatives and edge cases
- **Grouped key tables and joins:** compute duplicated 2015 values and unique coordinate pairs in separate grouped relations, then join them to `Insurance`; it has the same asymptotic bound.
- **Correlated counts per policy:** directly tests both conditions but may scan all policies twice per row and take $O(n^2)$ time.
- **Group only by latitude or longitude:** is incorrect because location uniqueness applies to the coordinate pair.
- **Unique 2015 value:** fails even when the location is unique.
- **Duplicated location:** every policy at that coordinate fails, regardless of its 2015 value.
- **Several policies sharing a 2015 value:** all may qualify when their locations are individually unique.
- **Decimal sum:** round the final aggregate, not each input value separately.
- **Output alias:** preserve the required `tiv_2016` column name.
