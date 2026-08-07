### 1. Description

You are given an integer `n` and a 2D array `requirements`, where $\text{requirements}[i] = [\text{end}_{i}, \text{cnt}_{i}]$ represents the end index and the **inversion** count of each requirement.

A pair of indices `(i, j)` from an integer array `nums` is called an **inversion** if:

- `i < j` and $\text{nums}[i] > \text{nums}[j]$

Return the number of permutations `perm` of `[0, 1, 2, ..., n - 1]` such that for **all** $\text{requirements}[i]$, $perm[0..\text{end}_{i}]$ has exactly $\text{cnt}_{i}$ inversions.

Since the answer may be very large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 3, requirements = [[2,2],[0,0]]

**Output:** 2

**Explanation:**

The two permutations are:

- `[2, 0, 1]`

		<li>Prefix `[2, 0, 1]` has inversions `(0, 1)` and `(0, 2)`.

- Prefix `[2]` has 0 inversions.

	</li>
- `[1, 2, 0]`

		<li>Prefix `[1, 2, 0]` has inversions `(0, 2)` and `(1, 2)`.

- Prefix `[1]` has 0 inversions.

	</li>

</div>
#### Example 2

<div class="example-block">
**Input:** n = 3, requirements = [[2,2],[1,1],[0,0]]

**Output:** 1

**Explanation:**

The only satisfying permutation is `[2, 0, 1]`:

- Prefix `[2, 0, 1]` has inversions `(0, 1)` and `(0, 2)`.

- Prefix `[2, 0]` has an inversion `(0, 1)`.

- Prefix `[2]` has 0 inversions.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 2, requirements = [[0,0],[1,0]]

**Output:** 1

**Explanation:**

The only satisfying permutation is `[0, 1]`:

- Prefix `[0]` has 0 inversions.

- Prefix `[0, 1]` has no inversions.

</div>

### 4. Constraints

- $2 \le n \le 300$

- $1 \le \text{requirements.length} \le n$

- $\text{requirements}[i] = [\text{end}_{i}, \text{cnt}_{i}]$

- $0 \le \text{end}_{i} \le n - 1$

- $0 \le \text{cnt}_{i} \le 400$

- The input is generated such that there is at least one `i` such that $\text{end}_{i} = n - 1$.

- The input is generated such that all $\text{end}_{i}$ are unique.