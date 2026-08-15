### 1. Description

Given a **0-indexed** integer array `nums` of size `n`, find the **maximum difference** between $\text{nums}[i]$ and $\text{nums}[j]$ (i.e., $\text{nums}[j] - \text{nums}[i]$), such that $0 \le i < j < n$ and $\text{nums}[i] < \text{nums}[j]$.

Return *the **maximum difference**. *If no such `i` and `j` exists, return `-1`.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [7,**<u>1</u>**,**<u>5</u>**,4]`
- **Output:** `4`
- **Explanation:** The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

#### Example 2

- **Input:** `nums = [9,4,3,2]`
- **Output:** `-1`
- **Explanation:** There is no i and j such that i < j and nums[i] < nums[j].

#### Example 3

- **Input:** `nums = [**<u>1</u>**,5,2,**<u>10</u>**]`
- **Output:** `9`
- **Explanation:** The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.

### 4. Constraints

- $n = \text{nums.length}$

- $2 \le n \le 1000$

- $1 \le \text{nums}[i] \le 10^{9}$
