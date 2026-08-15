### 1. Description

An array is **squareful** if the sum of every pair of adjacent elements is a **perfect square**.

Given an integer array nums, return *the number of permutations of *`nums`* that are **squareful***.

Two permutations `perm1` and `perm2` are different if there is some index `i` such that $\text{perm1}[i] \neq \text{perm2}[i]$.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,17,8]`
- **Output:** `2`
- **Explanation:** [1,8,17] and [17,8,1] are the valid permutations.

#### Example 2

- **Input:** `nums = [2,2,2]`
- **Output:** `1`

### 4. Constraints

- $1 \le \text{nums.length} \le 12$

- $0 \le \text{nums}[i] \le 10^{9}$
