### 1. Description

Given an array of `n` integers `nums`, a **132 pattern** is a subsequence of three integers $\text{nums}[i]$, $\text{nums}[j]$ and $\text{nums}[k]$ such that `i < j < k` and $\text{nums}[i] < \text{nums}[k] < \text{nums}[j]$.

Return `true`* if there is a **132 pattern** in *`nums`*, otherwise, return *`false`*.*

### 2. Function Contract

**Inputs**

- `nums`: A nonempty integer array of length $n$.

**Return value**

- Return `True` when there are positions $i < j < k$ with $\text{nums}[i] < \text{nums}[k] < \text{nums}[j]$; otherwise, return `False`.

Equal values cannot satisfy either strict inequality.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,3,4]`
- **Output:** `false`
- **Explanation:** There is no 132 pattern in the sequence.
#### Example 2

- **Input:** `nums = [3,1,4,2]`
- **Output:** `true`
- **Explanation:** There is a 132 pattern in the sequence: [1, 4, 2].
#### Example 3

- **Input:** `nums = [-1,3,2,0]`
- **Output:** `true`
- **Explanation:** There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

### 4. Constraints

- $n = \text{nums.length}$

- $1 \le n \le 2 * 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$