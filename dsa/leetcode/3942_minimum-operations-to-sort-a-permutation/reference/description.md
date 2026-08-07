### 1. Description

You are given an integer array `nums` of length `n`, where `nums` is a permutation of the integers from 0 to $n - 1$.

You may perform **only** the following operations:

- **Reverse** the entire array.

- **Rotate Left by One**: Move the first element to the end of the array, and rest elements to left by one position.

Return an integer denoting the **minimum** number of operations required to sort the array in **increasing** order. If it is **not possible** to sort the array using only the given operations, return -1.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty permutation of the integers from $0$ through $n-1$.

**Return value**

Return the fewest whole-array reversals and one-position left rotations needed to transform `nums` into increasing order, or `-1` if the target is unreachable.

The function observes `nums` without modifying it.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [0,2,1]

**Output:** 2

**Explanation:**

- Rotate Left by one: `[2, 1, 0]`

- Reverse the array: `[0, 1, 2]`

The array becomes sorted in 2 operations, which is minimal

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,0,2]

**Output:** 2

**Explanation:**

- Reverse the array: `[2, 0, 1]`

- Rotate Left by one: `[0, 1, 2]`

The array becomes sorted in 2 operations, which is minimal.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [2,0,1,3]

**Output:** -1

**Explanation:**

It is impossible to reach `[2, 0, 1, 3]`. Thus, the answer is -1.

</div>

### 4. Constraints

- $1 \le n = \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le n - 1$

- `nums` is a permutation of integers from 0 to $n - 1$.