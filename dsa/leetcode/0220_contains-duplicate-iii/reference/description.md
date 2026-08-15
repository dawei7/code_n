### 1. Description

You are given an integer array `nums` and two integers `indexDiff` and `valueDiff`.

Find a pair of indices `(i, j)` such that:

- $i \neq j$,

- $abs(i - j) \le indexDiff$.

- $abs(\text{nums}[i] - \text{nums}[j]) \le valueDiff$, and

Return `true`* if such pair exists or *`false`* otherwise*.

### 2. Function Contract

**Inputs**

- `nums`: The integer array whose index-value pairs are compared.
- `indexDiff`: The maximum permitted absolute index difference.
- `valueDiff`: The maximum permitted absolute value difference.

**Return value**

Return `true` when a distinct pair satisfies both distance bounds; otherwise return `false`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,3,1], indexDiff = 3, valueDiff = 0`
- **Output:** `true`
- **Explanation:** We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

#### Example 2

- **Input:** `nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3`
- **Output:** `false`
- **Explanation:** After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.

### 4. Constraints

- $2 \le \text{nums.length} \le 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$

- $1 \le indexDiff \le \text{nums.length}$

- $0 \le valueDiff \le 10^{9}$
