### 1. Description

You are given an integer array `nums`.

Rearrange elements of `nums` in **non-decreasing** order of their absolute value.

Return **any** rearranged array that satisfies this condition.

### 2. Function Contract

- Refer to method signature.

### 3. Note

: The absolute value of an integer x is defined as:

- `x` if $x \ge 0$

- `-x` if `x < 0`

### 4. Examples

#### Example 1

- **Input:** nums = [3,-1,-4,1,5]

- **Output:** [-1,1,3,-4,5]

- **Explanation:** 

- The absolute values of elements in `nums` are 3, 1, 4, 1, 5 respectively.

- Rearranging them in increasing order, we get 1, 1, 3, 4, 5.

- This corresponds to `[-1, 1, 3, -4, 5]`. Another possible rearrangement is $[1, -1, 3, -4, 5].$

#### Example 2

- **Input:** nums = [-100,100]

- **Output:** [-100,100]

- **Explanation:** 

- The absolute values of elements in `nums` are 100, 100 respectively.

- Rearranging them in increasing order, we get 100, 100.

- This corresponds to `[-100, 100]`. Another possible rearrangement is `[100, -100]`.

### 5. Constraints

- $1 \le \text{nums.length} \le 100$

- $-100 \le \text{nums}[i] \le 100$
