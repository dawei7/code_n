### 1. Description

A **peak** in an array `arr` is an element that is **greater** than its previous and next element in `arr`.

You are given an integer array `nums` and a 2D integer array `queries`.

You have to process queries of two types:

- $\text{queries}[i] = [1, l_{i}, r_{i}]$, determine the count of **peak** elements in the subarray $nums[l_{i}..r_{i}]$.<!-- notionvc: 73b20b7c-e1ab-4dac-86d0-13761094a9ae -->

- $\text{queries}[i] = [2, \text{index}_{i}, \text{val}_{i}]$, change $nums[\text{index}_{i}]$ to $\text{val}_{i}$.

Return an array `answer` containing the results of the queries of the first type in order.<!-- notionvc: a9ccef22-4061-4b5a-b4cc-a2b2a0e12f30 -->

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `queries`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `List[int]`.

### 3. Note

- The **first** and the **last** element of an array or a subarray<!-- notionvc: fcffef72-deb5-47cb-8719-3a3790102f73 --> **cannot** be a peak.

### 4. Examples

#### Example 1

- **Input:** nums = [3,1,4,2,5], queries = [[2,3,4],[1,0,4]]

- **Output:** [0]

- **Explanation:** First query: We change $\text{nums}[3]$ to 4 and `nums` becomes `[3,1,4,4,5]`.

Second query: The number of peaks in the `[3,1,4,4,5]` is 0.

#### Example 2

- **Input:** nums = [4,1,4,2,1,5], queries = [[2,2,4],[1,0,2],[1,0,4]]

- **Output:** [0,1]

- **Explanation:** First query: $\text{nums}[2]$ should become 4, but it is already set to 4.

Second query: The number of peaks in the `[4,1,4]` is 0.

Third query: The second 4 is a peak in the `[4,1,4,2,1]`.

### 5. Constraints

- $3 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i][0] = 1$ or $\text{queries}[i][0] = 2$

- For all `i` that:

		- $\text{queries}[i][0] = 1$: $0 \le \text{queries}[i][1] \le \text{queries}[i][2] \le \text{nums.length} - 1$

- $\text{queries}[i][0] = 2$: $0 \le \text{queries}[i][1] \le \text{nums.length} - 1$, $1 \le \text{queries}[i][2] \le 10^{5}$
