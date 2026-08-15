### 1. Description

An array `nums` of length `n` is **beautiful** if:

- `nums` is a permutation of the integers in the range `[1, n]`.

- For every $0 \le i < j < n$, there is no index `k` with `i < k < j` where $2 * \text{nums}[k] = \text{nums}[i] + \text{nums}[j]$.

Given the integer `n`, return *any **beautiful** array *`nums`* of length *`n`. There will be at least one valid answer for the given `n`.

### 2. Function Contract

**Inputs**

- `n`: Input parameter (`int`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** $n = 4$
- **Output:** `[2,1,4,3]`

#### Example 2

- **Input:** $n = 5$
- **Output:** `[3,1,2,5,4]`

### 4. Constraints

- $1 \le n \le 1000$
