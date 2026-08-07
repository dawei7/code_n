## Description

You are given an integer `n` representing the number of sheets.

You are also given an integer array `limit` of size `m`, where $\text{limit}[i]$ is the **maximum** number of sheets that can be painted using color `i`.

You must paint **all** `n` sheets under the following conditions:

- **Exactly two distinct** colors are used.

- Each color must cover a **single contiguous** segment of sheets.

- The number of sheets painted with color `i` cannot exceed $\text{limit}[i]$.

Return an integer denoting the number of **distinct** ways to paint all sheets. Since the answer may be large, return it **modulo** $10^{9} + 7$.

**Note:** Two ways differ if **at least** one sheet is painted with a different color.
### Function Contract

**Inputs**

- `n`: The number of sheets in the ordered row.
- `limit`: An array where `limit[i]` is the maximum segment length allowed for color `i`.

Both color segments must be nonempty. Their lengths sum to $n$, and their order matters because one color covers the first segment and the other covers the second.

**Return value**

Return the number of distinct valid full-row paintings, reduced modulo $1{,}000{,}000{,}007$.

### Examples
#### Example 1

<div class="example-block">
**Input:** n = 4, limit = [3,1,2]

**Output:** 6

**Explanation:**​​​​​​​

For each ordered pair `(i, j)`, where color `i` is used for the first segment and color `j` for the second segment ($i \neq j$), a split of `x` and $4 - x$ is valid if $1 \le x \le \text{limit}[i]$ and $1 \le 4 - x \le \text{limit}[j]$.

Valid pairs and counts are:

- $(0, 1): x = 3$

- $(0, 2): x = 2, 3$

- $(1, 0): x = 1$

- $(2, 0): x = 1, 2$

Therefore, there are 6 valid ways in total.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 3, limit = [1,2]

**Output:** 2

**Explanation:**

For each ordered pair `(i, j)`, where color `i` is used for the first segment and color `j` for the second segment ($i \neq j$), a split of `x` and $3 - x$ is valid if $1 \le x \le \text{limit}[i]$ and $1 \le 3 - x \le \text{limit}[j]$.

Valid pairs and counts are:

- $(0, 1): x = 1$

- $(1, 0): x = 2$

Hence, there are 2 valid ways in total.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 3, limit = [2,2]

**Output:** 4

**Explanation:**

For each ordered pair `(i, j)`, where color `i` is used for the first segment and color `j` for the second segment ($i \neq j$), a split of `x` and $3 - x$ is valid if $1 \le x \le \text{limit}[i]$ and $1 \le 3 - x \le \text{limit}[j]$.

Valid pairs and counts are:

- $(0, 1): x = 1, 2$

- $(1, 0): x = 1, 2$

Therefore, there are 4 valid ways in total.

</div>
### Constraints

- $2 \le n \le 10^{9}$

- $2 \le m = \text{limit.length} \le 10^{5}$

- $1 \le \text{limit}[i] \le 10^{9}$