### 1. Description

You are given an integer array `nums` of length `n` where `nums` is a permutation of the numbers in the range `[0, n - 1]`.

You should build a set $s[k] = {\text{nums}[k], nums[\text{nums}[k]], nums[nums[\text{nums}[k]]], ... }$ subjected to the following rule:

- The first element in $s[k]$ starts with the selection of the element $\text{nums}[k]$ of $index = k$.

- The next element in $s[k]$ should be $nums[\text{nums}[k]]$, and then $nums[nums[\text{nums}[k]]]$, and so on.

- We stop adding right before a duplicate element occurs in $s[k]$.

Return *the longest length of a set* $s[k]$.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [5,4,0,3,1,6,2]`
- **Output:** `4`
- **Explanation:** nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
One of the longest sets s[k]:
s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}

#### Example 2

- **Input:** `nums = [0,1,2]`
- **Output:** `1`

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] < \text{nums.length}$

- All the values of `nums` are **unique**.
