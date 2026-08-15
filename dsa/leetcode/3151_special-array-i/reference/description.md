### 1. Description

An array is considered **special** if the *parity* of every pair of adjacent elements is different. In other words, one element in each pair **must** be even, and the other **must** be odd.

You are given an array of integers `nums`. Return `true` if `nums` is a **special** array, otherwise, return `false`.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `bool`.

### 3. Examples

#### Example 1

- **Input:** nums = [1]

- **Output:** true

- **Explanation:** There is only one element. So the answer is `true`.

#### Example 2

- **Input:** nums = [2,1,4]

- **Output:** true

- **Explanation:** There is only two pairs: `(2,1)` and `(1,4)`, and both of them contain numbers with different parity. So the answer is `true`.

#### Example 3

- **Input:** nums = [4,3,1,6]

- **Output:** false

- **Explanation:** $\text{nums}[1]$ and $\text{nums}[2]$ are both odd. So the answer is `false`.

### 4. Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$
