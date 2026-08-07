### 1. Description

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

### 2. Function Contract

**Inputs**

- `nums`: An array of distinct integers to arrange.

Let $n = \lvert\texttt{nums}\rvert$.

**Return value**

Return all complete orderings of `nums`, in any order.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,3]`
- **Output:** `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`
#### Example 2

- **Input:** `nums = [0,1]`
- **Output:** `[[0,1],[1,0]]`
#### Example 3

- **Input:** `nums = [1]`
- **Output:** `[[1]]`

### 4. Constraints

- $1 \le \text{nums.length} \le 6$

- $-10 \le \text{nums}[i] \le 10$

- All the integers of `nums` are **unique**.