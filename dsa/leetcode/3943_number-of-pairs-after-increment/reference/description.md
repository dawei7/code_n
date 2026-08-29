### 1. Description

You are given two integer arrays `nums1` and `nums2`, and a 2D integer array `queries`.

Each $\text{queries}[i]$ is one of the following types:

- `[1, x, y, val]` – **Add** `val` to every element in `nums2[x..y]`.

- `[2, tot]` – **Compute** the number of pairs `(j, k)` such that $\text{nums1}[j] + \text{nums2}[k] = tot$.

Return an integer array `answer`, where $\text{answer}[j]$ is the number of pairs for the $j^{\text{th}}$ query of type 2.

### 2. Function Contract

**Inputs**

- `nums1`: A nonempty fixed array of positive integers.
- `nums2`: A nonempty array of positive integers whose current values are changed by type-1 queries.
- `queries`: A nonempty sequence containing inclusive range additions `[1, x, y, val]` and pair-count requests `[2, tot]`.

Queries are processed from left to right. A type-2 query observes every type-1 update that precedes it and none that follows it. Pair counts use indices, not merely distinct values.

**Return value**

Return one integer for every type-2 query, in query order. Each integer is the number of index pairs `(j, k)` for which the current sum $\text{nums1}[j] + \text{nums2}[k]$ equals that query's target.

### 3. Examples

#### Example 1

- **Input:** nums1 = [1,2], nums2 = [3,4], queries = [[2,5],[1,0,0,2],[2,5]]

- **Output:** [2,1]

- **Explanation:** 

- $\text{queries}[0] = [2, 5]$: Valid pairs are $\text{nums1}[0] + \text{nums2}[1] = 1 + 4 = 5$ and $\text{nums1}[1] + \text{nums2}[0] = 2 + 3 = 5$.

- $\text{queries}[1] = [1, 0, 0, 2]$: Add 2 to $\text{nums2}[0]$, resulting in $nums2 = [5, 4]$.

- $\text{queries}[2] = [2, 5]$: Valid pair is $\text{nums1}[0] + \text{nums2}[1] = 1 + 4 = 5$.

- Thus, the $answer = [2, 1]$.

#### Example 2

- **Input:** nums1 = [1,1], nums2 = [2,2,3], queries = [[2,4],[1,0,1,1],[2,4]]

- **Output:** [2,6]

- **Explanation:** 

- $\text{queries}[0] = [2, 4]$: Valid pairs are $\text{nums1}[0] + \text{nums2}[2] = 1 + 3$ and $\text{nums1}[1] + \text{nums2}[2] = 1 + 3$.

- $\text{queries}[1] = [1, 0, 1, 1]$: Add 1 to $\text{nums2}[0]$ and $\text{nums2}[1]$, resulting in $nums2 = [3, 3, 3]$.

- $\text{queries}[2] = [2, 4]$: Every element of $nums1 = [1, 1]$ pairs with every element of $nums2 = [3, 3, 3]$ as $1 + 3 = 4$. That gives $2 × 3 = 6$ pairs in total.

- Thus, the $answer = [2, 6]$.

#### Example 3

- **Input:** nums1 = [2,5,8,4], nums2 = [1,3,8], queries = [[2,9],[1,1,2,1],[2,10]]

- **Output:** [1,0]

- **Explanation:** 

- $\text{queries}[0] = [2, 9]$: Only valid pair is $\text{nums1}[2] + \text{nums2}[0] = 8 + 1 = 9$.

- $\text{queries}[1] = [1, 1, 2, 1]$: Add 1 to $\text{nums2}[1]$ and $\text{nums2}[2]$, resulting in $nums2 = [1, 4, 9]$.

- $\text{queries}[2] = [2, 10]$: No pair sums to `10`.

- Thus, the $answer = [1, 0]$.

### 4. Constraints

- $1 \le \text{nums1.length} \le 5$

- $1 \le \text{nums2.length} \le 5 * 10^{4}$

- $1 \le \text{nums1}[i], \text{nums2}[i] \le 10^{5}$

- $1 \le \text{queries.length} \le 5 * 10^{4}$

- $\text{queries}[i].length = 2 or 4$

		- $\text{queries}[i] = [1, x, y, val], or$

- $\text{queries}[i] = [2, tot]$

- $0 \le x \le y < \text{nums2.length}$

- $1 \le val \le 10^{5}$

- $1 \le tot \le 10^{9}$
