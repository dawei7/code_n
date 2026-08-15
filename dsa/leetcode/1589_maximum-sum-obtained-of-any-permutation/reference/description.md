### 1. Description

We have an array of integers, `nums`, and an array of `requests` where $\text{requests}[i] = [\text{start}_{i}, \text{end}_{i}]$. The $$i^{\text{th}}$$ request asks for the sum of $nums[\text{start}_{i}] + nums[\text{start}_{i} + 1] + ... + nums[\text{end}_{i} - 1] + nums[\text{end}_{i}]$. Both $\text{start}_{i}$ and $\text{end}_{i}$ are *0-indexed*.

Return *the maximum total sum of all requests **among all permutations** of* `nums`.

Since the answer may be too large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `requests`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,3,4,5], requests = [[1,3],[0,1]]`
- **Output:** `19`
- **Explanation:** One permutation of nums is [2,1,3,4,5] with the following result:
requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
Total sum: 8 + 3 = 11.
A permutation with a higher total sum is [3,5,4,2,1] with the following result:
requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
requests[1] -> nums[0] + nums[1] = 3 + 5  = 8
Total sum: 11 + 8 = 19, which is the best that you can do.

#### Example 2

- **Input:** `nums = [1,2,3,4,5,6], requests = [[0,1]]`
- **Output:** `11`
- **Explanation:** A permutation with the max total sum is [6,5,4,3,2,1] with request sums [11].

#### Example 3

- **Input:** `nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]`
- **Output:** `47`
- **Explanation:** A permutation with the max total sum is [4,10,5,3,2,1] with request sums [19,18,10].

### 4. Constraints

- $n = \text{nums.length}$

- $1 \le n \le 10^{5}$

- $0 \le \text{nums}[i] \le 10^{5}$

- $1 \le \text{requests.length} \le 10^{5}$

- $\text{requests}[i].length = 2$

- $0 \le \text{start}_{i} \le \text{end}_{i} < n$
