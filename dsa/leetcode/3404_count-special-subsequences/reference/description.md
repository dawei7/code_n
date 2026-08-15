### 1. Description

You are given an array `nums` consisting of positive integers.

A **special subsequence** is defined as a subsequence of length 4, represented by indices `(p, q, r, s)`, where `p < q < r < s`. This subsequence **must** satisfy the following conditions:

- $\text{nums}[p] * \text{nums}[r] = \text{nums}[q] * \text{nums}[s]$

- There must be *at least* **one** element between each pair of indices. In other words, $q - p > 1$, $r - q > 1$ and $s - r > 1$.

Return the *number* of different **special** **subsequences** in `nums`.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [1,2,3,4,3,6,1]

- **Output:** 1

- **Explanation:** There is one special subsequence in `nums`.

- $(p, q, r, s) = (0, 2, 4, 6)$:

		- This corresponds to elements `(1, 3, 3, 1)`.

- $\text{nums}[p] * \text{nums}[r] = \text{nums}[0] * \text{nums}[4] = 1 * 3 = 3$

- $\text{nums}[q] * \text{nums}[s] = \text{nums}[2] * \text{nums}[6] = 3 * 1 = 3$

#### Example 2

- **Input:** nums = [3,4,3,4,3,4,3,4]

- **Output:** 3

- **Explanation:** There are three special subsequences in `nums`.

- $(p, q, r, s) = (0, 2, 4, 6)$:

		- This corresponds to elements `(3, 3, 3, 3)`.

- $\text{nums}[p] * \text{nums}[r] = \text{nums}[0] * \text{nums}[4] = 3 * 3 = 9$

- $\text{nums}[q] * \text{nums}[s] = \text{nums}[2] * \text{nums}[6] = 3 * 3 = 9$

- $(p, q, r, s) = (1, 3, 5, 7)$:

		- This corresponds to elements `(4, 4, 4, 4)`.

- $\text{nums}[p] * \text{nums}[r] = \text{nums}[1] * \text{nums}[5] = 4 * 4 = 16$

- $\text{nums}[q] * \text{nums}[s] = \text{nums}[3] * \text{nums}[7] = 4 * 4 = 16$

- $(p, q, r, s) = (0, 2, 5, 7)$:

		- This corresponds to elements `(3, 3, 4, 4)`.

- $\text{nums}[p] * \text{nums}[r] = \text{nums}[0] * \text{nums}[5] = 3 * 4 = 12$

- $\text{nums}[q] * \text{nums}[s] = \text{nums}[2] * \text{nums}[7] = 3 * 4 = 12$

### 4. Constraints

- $7 \le \text{nums.length} \le 1000$

- $1 \le \text{nums}[i] \le 1000$
