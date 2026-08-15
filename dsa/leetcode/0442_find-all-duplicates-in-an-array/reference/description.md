### 1. Description

Given an integer array `nums` of length `n` where all the integers of `nums` are in the range `[1, n]` and each integer appears **at most** **twice**, return *an array of all the integers that appears **twice***.

You must write an algorithm that runs in `O(n)` time and uses only *constant* auxiliary space, excluding the space needed to store the output

### 2. Function Contract

**Inputs**

- `nums`: An integer array of length $n$ whose values are all in $[1, n]$ and each occur once or twice.

**Return value**

- Return an array containing each value that occurs twice. The values may appear in any order.

The required complexity is $O(n)$ time and $O(1)$ auxiliary space, not counting the output array.

### 3. Examples

#### Example 1

- **Input:** `nums = [4,3,2,7,8,2,3,1]`
- **Output:** `[2,3]`

#### Example 2

- **Input:** `nums = [1,1,2]`
- **Output:** `[1]`

#### Example 3

- **Input:** `nums = [1]`
- **Output:** `[]`

### 4. Constraints

- $n = \text{nums.length}$

- $1 \le n \le 10^{5}$

- $1 \le \text{nums}[i] \le n$

- Each element in `nums` appears **once** or **twice**.
