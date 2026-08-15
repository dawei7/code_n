### 1. Description

You are given an integer array `nums` (**0-indexed**). In one operation, you can choose an element of the array and increment it by `1`.

- For example, if `nums = [1,2,3]`, you can choose to increment $\text{nums}[1]$ to make `nums = [1,<u>**3**</u>,3]`.

Return *the **minimum** number of operations needed to make* `nums` ***strictly** **increasing**.*

An array `nums` is **strictly increasing** if $\text{nums}[i] < nums[i+1]$ for all $0 \le i < \text{nums.length} - 1$. An array of length `1` is trivially strictly increasing.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,1,1]`
- **Output:** `3`
- **Explanation:** You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,<u>**2**</u>].
2) Increment nums[1], so nums becomes [1,<u>**2**</u>,2].
3) Increment nums[2], so nums becomes [1,2,<u>**3**</u>].

#### Example 2

- **Input:** `nums = [1,5,2,4,1]`
- **Output:** `14`

#### Example 3

- **Input:** `nums = [8]`
- **Output:** `0`

### 4. Constraints

- $1 \le \text{nums.length} \le 5000$

- $1 \le \text{nums}[i] \le 10^{4}$
