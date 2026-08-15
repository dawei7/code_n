### 1. Description

You are given two **0-indexed** integer arrays `nums1` and `nums2`, each of length `n`, and a **1-indexed 2D array** `queries` where $\text{queries}[i] = [x_{i}, y_{i}]$.

For the $$i^{\text{th}}$$ query, find the **maximum value** of $\text{nums1}[j] + \text{nums2}[j]$ among all indices `j` $(0 \le j < n)$, where $\text{nums1}[j] \ge x_{i}$ and $\text{nums2}[j] \ge y_{i}$, or **-1** if there is no `j` satisfying the constraints.

Return *an array *`answer`* where *$\text{answer}[i]$* is the answer to the *$$i^{\text{th}}$$* query.*

### 2. Function Contract

**Inputs**

- `nums1`: Input parameter (`List[int]`).
- `nums2`: Input parameter (`List[int]`).
- `queries`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** $nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]]$
- **Output:** `[6,10,7]`
- **Explanation:** For the 1st query x_i = 4 and y_i = 1, we can select index j = 0 since nums1[j] >= 4 and nums2[j] >= 1. The sum nums1[j] + nums2[j] is 6, and we can show that 6 is the maximum we can obtain.
For the 2nd query x_i = 1 and y_i = 3, we can select index j = 2 since nums1[j] >= 1 and nums2[j] >= 3. The sum nums1[j] + nums2[j] is 10, and we can show that 10 is the maximum we can obtain.
For the 3rd query x_i = 2 and y_i = 5, we can select index j = 3 since nums1[j] >= 2 and nums2[j] >= 5. The sum nums1[j] + nums2[j] is 7, and we can show that 7 is the maximum we can obtain.
Therefore, we return [6,10,7].

#### Example 2

- **Input:** $nums1 = [3,2,5], nums2 = [2,3,4], queries = [[4,4],[3,2],[1,1]]$
- **Output:** `[9,9,9]`
- **Explanation:** For this example, we can use index j = 2 for all the queries since it satisfies the constraints for each query.

#### Example 3

- **Input:** $nums1 = [2,1], nums2 = [2,3], queries = [[3,3]]$
- **Output:** `[-1]`
- **Explanation:** There is one query in this example with x_i = 3 and y_i = 3. For every index, j, either nums1[j] < x_i or nums2[j] < y_i. Hence, there is no solution.

### 4. Constraints

- $\text{nums1.length} = \text{nums2.length}$

- $n = \text{nums1.length}$

- $1 \le n \le 10^{5}$

- $1 \le \text{nums1}[i], \text{nums2}[i] \le 10^{9}$

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i].length = 2$

- $x_{i} = \text{queries}[i][1]$

- $y_{i} = \text{queries}[i][2]$

- $1 \le x_{i}, y_{i} \le 10^{9}$
