## Function Contract

**Inputs**

- `n`: The inclusive upper endpoint of the positive integer range.

Format each integer in ordinary decimal notation without leading zeros. Insert a comma between each adjacent pair of three-digit groups counted from the right. Let $K$ be the number of powers $1000^k$ with $k\ge 1$ that do not exceed `n`; these are exactly the comma thresholds reached by the range.

**Return value**

Return the total number of commas in the formatted representations of all integers $x$ for which $1\le x\le n$.
