### 1. Description

You are given an integer array `nums`.

Return the length of the **longest subsequence** in `nums` whose bitwise **XOR** is **non-zero**. If no such **subsequence** exists, return 0.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of nonnegative integers.

A subsequence retains the relative order of its selected elements and may omit any number of elements. The selected subsequence must have a bitwise XOR different from zero.

**Return value**

Return the greatest attainable subsequence length, or `0` when no qualifying subsequence exists.

### 3. Examples

#### Example 1

- **Input:** nums = [1,2,3]

- **Output:** 2

- **Explanation:** One longest subsequence is `[2, 3]`. The bitwise XOR is computed as $2 XOR 3 = 1$, which is non-zero.

#### Example 2

- **Input:** nums = [2,3,4]

- **Output:** 3

- **Explanation:** The longest subsequence is `[2, 3, 4]`. The bitwise XOR is computed as $2 XOR 3 XOR 4 = 5$, which is non-zero.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 10^{9}$
