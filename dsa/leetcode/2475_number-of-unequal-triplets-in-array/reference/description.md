### 1. Description

You are given a **0-indexed** array of positive integers `nums`. Find the number of triplets `(i, j, k)` that meet the following conditions:

- $0 \le i < j < k < \text{nums.length}$

- $\text{nums}[i]$, $\text{nums}[j]$, and $\text{nums}[k]$ are **pairwise distinct**.

		- In other words, $\text{nums}[i] \neq \text{nums}[j]$, $\text{nums}[i] \neq \text{nums}[k]$, and $\text{nums}[j] \neq \text{nums}[k]$.

Return *the number of triplets that meet the conditions.*

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [4,4,2,4,3]`
- **Output:** `3`
- **Explanation:** The following triplets meet the conditions:
- (0, 2, 4) because 4 != 2 != 3
- (1, 2, 4) because 4 != 2 != 3
- (2, 3, 4) because 2 != 4 != 3
Since there are 3 triplets, we return 3.
Note that (2, 0, 4) is not a valid triplet because 2 > 0.

#### Example 2

- **Input:** `nums = [1,1,1,1,1]`
- **Output:** `0`
- **Explanation:** No triplets meet the conditions so we return 0.

### 4. Constraints

- $3 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 1000$
