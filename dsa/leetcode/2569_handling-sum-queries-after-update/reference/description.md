### 1. Description

You are given two **0-indexed** arrays `nums1` and `nums2` and a 2D array `queries` of queries. There are three types of queries:

- For a query of type 1, $\text{queries}[i] = [1, l, r]$. Flip the values from `0` to `1` and from `1` to `0` in `nums1` from index `l` to index `r`. Both `l` and `r` are **0-indexed**.

- For a query of type 2, $\text{queries}[i] = [2, p, 0]$. For every index $0 \le i < n$, set $\text{nums2}[i] = \text{nums2}[i] + \text{nums1}[i] * p$.

- For a query of type 3, $\text{queries}[i] = [3, 0, 0]$. Find the sum of the elements in `nums2`.

Return *an array containing all the answers to the third type queries.*

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]$
- **Output:** `[3]`
- **Explanation:** After the first query nums1 becomes [1,1,1]. After the second query, nums2 becomes [1,1,1], so the answer to the third query is 3. Thus, [3] is returned.
#### Example 2

- **Input:** $nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]$
- **Output:** `[5]`
- **Explanation:** After the first query, nums2 remains [5], so the answer to the second query is 5. Thus, [5] is returned.

### 4. Constraints

- $1 \le \text{nums1.length},\text{nums2.length} \le 10^{5}$

- $\text{nums1.length} = \text{nums2.length}$

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i].length = 3$

- $0 \le l \le r \le \text{nums1.length} - 1$

- $0 \le p \le 10^{6}$

- $0 \le \text{nums1}[i] \le 1$

- $0 \le \text{nums2}[i] \le 10^{9}$