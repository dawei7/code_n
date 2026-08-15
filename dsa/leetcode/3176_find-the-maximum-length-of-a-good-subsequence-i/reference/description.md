### 1. Description

You are given an integer array `nums` and a **non-negative** integer `k`. A sequence of integers `seq` is called **good** if there are **at most** `k` indices `i` in the range `[0, seq.length - 2]` such that $\text{seq}[i] \neq seq[i + 1]$.

Return the **maximum** possible length of a **good** subsequence of `nums`.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [1,2,1,1,3], k = 2

- **Output:** 4

- **Explanation:** The maximum length subsequence is `[<u>1</u>,<u>2</u>,<u>1</u>,<u>1</u>,3]`.

#### Example 2

- **Input:** nums = [1,2,3,4,5,1], k = 0

- **Output:** 2

- **Explanation:** The maximum length subsequence is `[<u>1</u>,2,3,4,5,<u>1</u>]`.

### 4. Constraints

- $1 \le \text{nums.length} \le 500$

- $1 \le \text{nums}[i] \le 10^{9}$

- $0 \le k \le min(\text{nums.length}, 25)$
