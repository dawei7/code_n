## Function Contract

**Input**

`Numbers(num, frequency)` stores one distinct number per row together with its occurrence count. Let $R$ be the number of rows in `Numbers`, and let $T$ be the sum of all `frequency` values.

**Return value**

Return a one-row table with a `median` column. Its value is the middle decompressed value when $T$ is odd or the average of the two middle values when $T$ is even, rounded to one decimal place.
