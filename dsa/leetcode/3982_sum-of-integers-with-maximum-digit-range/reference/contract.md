## Function Contract

`solve(nums) -> int`

Let $S$ be the total number of decimal digits across the input values:

$$
S = \sum_{x \in \texttt{nums}} \operatorname{digits}(x).
$$

**Inputs**

- `nums`: A nonempty list of positive integers.

Each array position is a separate contribution candidate. The digit range of a value is its maximum decimal digit minus its minimum decimal digit.

**Output**

Return the sum of all values whose digit range equals the largest digit range present anywhere in `nums`.
