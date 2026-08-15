### 1. Description

You are given a **0-indexed** integer array `nums` and a positive integer `k`.

We call an index `i` **k-big** if the following conditions are satisfied:

- There exist at least `k` different indices `idx1` such that `idx1 < i` and $\text{nums}[idx1] < \text{nums}[i]$.

- There exist at least `k` different indices `idx2` such that `idx2 > i` and $\text{nums}[idx2] < \text{nums}[i]$.

Return *the number of k-big indices*.

### 2. Function Contract

**Inputs**

- `nums`: A list of $n$ integers ($1 \le n \le 10^5$, $1 \le \text{nums}[i] \le n$).
- `k`: A positive integer ($1 \le k \le n$).

**Return value**

Return an integer representing the number of `k`-big indices in `nums`.

### 3. Examples

#### Example 1

- **Input:** `nums = [2,3,6,5,2,3], k = 2`
- **Output:** `2`
- **Explanation:** There are only two 2-big indices in nums:
- i = 2 --> There are two valid idx1: 0 and 1. There are three valid idx2: 2, 3, and 4.
- i = 3 --> There are two valid idx1: 0 and 1. There are two valid idx2: 3 and 4.

#### Example 2

- **Input:** `nums = [1,1,1], k = 3`
- **Output:** `0`
- **Explanation:** There are no 3-big indices in nums.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i], k \le \text{nums.length}$
