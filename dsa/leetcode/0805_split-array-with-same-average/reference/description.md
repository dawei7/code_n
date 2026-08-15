### 1. Description

You are given an integer array `nums`.

You should move each element of `nums` into one of the two arrays `A` and `B` such that `A` and `B` are non-empty, and $average(A) = average(B)$.

Return `true` if it is possible to achieve that and `false` otherwise.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `bool`.

### 3. Note

that for an array `arr`, `average(arr)` is the sum of all the elements of `arr` over the length of `arr`.

### 4. Examples

#### Example 1

- **Input:** `nums = [1,2,3,4,5,6,7,8]`
- **Output:** `true`
- **Explanation:** We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.

#### Example 2

- **Input:** `nums = [3,1]`
- **Output:** `false`

### 5. Constraints

- $1 \le \text{nums.length} \le 30$

- $0 \le \text{nums}[i] \le 10^{4}$
