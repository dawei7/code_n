### 1. Description

You are given an integer array `nums` and two integers `limit` and `goal`. The array `nums` has an interesting property that $abs(\text{nums}[i]) \le limit$.

Return *the minimum number of elements you need to add to make the sum of the array equal to *`goal`. The array must maintain its property that $abs(\text{nums}[i]) \le limit$.

Note that `abs(x)` equals `x` if $x \ge 0$, and `-x` otherwise.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `limit`: Input parameter (`int`).
- `goal`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,-1,1], limit = 3, goal = -4`
- **Output:** `2`
- **Explanation:** You can add -2 and -3, then the sum of the array will be 1 - 1 + 1 - 2 - 3 = -4.

#### Example 2

- **Input:** `nums = [1,-10,9,1], limit = 100, goal = 0`
- **Output:** `1`

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le limit \le 10^{6}$

- $-limit \le \text{nums}[i] \le limit$

- $-10^{9} \le goal \le 10^{9}$
