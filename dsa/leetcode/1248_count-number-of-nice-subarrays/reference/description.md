### 1. Description

Given an array of integers `nums` and an integer `k`. A continuous subarray is called **nice** if there are `k` odd numbers on it.

Return *the number of **nice** sub-arrays*.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,1,2,1,1], k = 3`
- **Output:** `2`
- **Explanation:** The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

#### Example 2

- **Input:** `nums = [2,4,6], k = 1`
- **Output:** `0`
- **Explanation:** There are no odd numbers in the array.

#### Example 3

- **Input:** `nums = [2,2,2,1,2,2,1,2,2,2], k = 2`
- **Output:** `16`

### 4. Constraints

- $1 \le \text{nums.length} \le 50000$

- $1 \le \text{nums}[i] \le 10^{5}$

- $1 \le k \le \text{nums.length}$
