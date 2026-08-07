### 1. Description

You are given two **0-indexed** integer arrays `nums1` and `nums2`, each of size `n`, and an integer `diff`. Find the number of **pairs** `(i, j)` such that:

- $0 \le i < j \le n - 1$ **and**

- $\text{nums1}[i] - \text{nums1}[j] \le \text{nums2}[i] - \text{nums2}[j] + diff$.

Return* the **number of pairs** that satisfy the conditions.*

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $nums1 = [3,2,5], nums2 = [2,2,1], diff = 1$
- **Output:** `3`
- **Explanation:**
There are 3 pairs that satisfy the conditions:
1. i = 0, j = 1: 3 - 2 <= 2 - 2 + 1. Since i < j and 1 <= 1, this pair satisfies the conditions.
2. i = 0, j = 2: 3 - 5 <= 2 - 1 + 1. Since i < j and -2 <= 2, this pair satisfies the conditions.
3. i = 1, j = 2: 2 - 5 <= 2 - 1 + 1. Since i < j and -3 <= 2, this pair satisfies the conditions.
Therefore, we return 3.
#### Example 2

- **Input:** $nums1 = [3,-1], nums2 = [-2,2], diff = -1$
- **Output:** `0`
- **Explanation:**
Since there does not exist any pair that satisfies the conditions, we return 0.

### 4. Constraints

- $n = \text{nums1.length} = \text{nums2.length}$

- $2 \le n \le 10^{5}$

- $-10^{4} \le \text{nums1}[i], \text{nums2}[i] \le 10^{4}$

- $-10^{4} \le diff \le 10^{4}$