### 1. Description

Given an integer array `nums` that may contain duplicates, return *all possible* *subsets** (the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

### 2. Function Contract

**Inputs**

- `nums`: An integer array that may contain duplicates.

**Return value**

Return every distinct subset of the input multiset, including the empty subset.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,2]`
- **Output:** `[[],[1],[1,2],[1,2,2],[2],[2,2]]`
#### Example 2

- **Input:** `nums = [0]`
- **Output:** `[[],[0]]`

### 4. Constraints

- $1 \le \text{nums.length} \le 10$

- $-10 \le \text{nums}[i] \le 10$