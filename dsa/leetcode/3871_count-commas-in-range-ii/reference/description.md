### 1. Description

You are given an integer `n`.

Return the **total** number of commas used when writing all integers from `[1, n]` (inclusive) in **standard** number formatting.

In **standard** formatting:

- A comma is inserted after **every three** digits from the right.

- Numbers with **fewer** than 4 digits contain no commas.

### 2. Function Contract

**Inputs**

- `n`: The inclusive upper endpoint of the positive integer range.

Format each integer in ordinary decimal notation without leading zeros. Insert a comma between each adjacent pair of three-digit groups counted from the right. Let $K$ be the number of powers $1000^k$ with $k\ge 1$ that do not exceed `n`; these are exactly the comma thresholds reached by the range.

**Return value**

Return the total number of commas in the formatted representations of all integers $x$ for which $1\le x\le n$.

### 3. Examples

#### Example 1

- **Input:** n = 1002

- **Output:** 3

- **Explanation:** The numbers `"1,000"`, `"1,001"`, and `"1,002"` each contain one comma, giving a total of 3.

#### Example 2

- **Input:** n = 998

- **Output:** 0

- **Explanation:** 

****All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

### 4. Constraints

- $1 \le n \le 10^{15}$
