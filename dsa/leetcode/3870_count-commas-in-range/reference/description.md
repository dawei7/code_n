### 1. Description

You are given an integer `n`.

Return the **total** number of commas used when writing all integers from `[1, n]` (inclusive) in **standard** number formatting.

In **standard** formatting:

- A comma is inserted after **every three** digits from the right.

- Numbers with **fewer** than 4 digits contain no commas.

### 2. Function Contract

**Inputs**

- `n`: The inclusive upper endpoint of the range of positive integers to format.

Write each value in its ordinary decimal representation without leading zeros. Starting from the right, separate consecutive groups of three digits with commas. Because the largest permitted value is `100000`, every number that uses a comma contains exactly one.

**Return value**

Return an integer equal to the total number of commas appearing in the standard representations of all integers $x$ satisfying $1\le x\le n$.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 1002

**Output:** 3

**Explanation:**

The numbers `"1,000"`, `"1,001"`, and `"1,002"` each contain one comma, giving a total of 3.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 998

**Output:** 0

**Explanation:**

All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

</div>

### 4. Constraints

- $1 \le n \le 10^{5}$