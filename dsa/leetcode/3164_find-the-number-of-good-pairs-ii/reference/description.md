### 1. Description

You are given 2 integer arrays `nums1` and `nums2` of lengths `n` and `m` respectively. You are also given a **positive** integer `k`.

A pair `(i, j)` is called **good** if $\text{nums1}[i]$ is divisible by $\text{nums2}[j] * k$ ($0 \le i \le n - 1$, $0 \le j \le m - 1$).

Return the total number of **good** pairs.

### 2. Function Contract

**Inputs**

- `nums1`: Input parameter (`List[int]`).
- `nums2`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums1 = [1,3,4], nums2 = [1,3,4], k = 1

- **Output:** 5

- **Explanation:** The 5 good pairs are `(0, 0)`, `(1, 0)`, `(1, 1)`, `(2, 0)`, and `(2, 2)`.

#### Example 2

- **Input:** nums1 = [1,2,4,12], nums2 = [2,4], k = 3

- **Output:** 2

- **Explanation:** The 2 good pairs are `(3, 0)` and `(3, 1)`.

### 4. Constraints

- $1 \le n, m \le 10^{5}$

- $1 \le \text{nums1}[i], \text{nums2}[j] \le 10^{6}$

- $1 \le k \le 10^{3}$
