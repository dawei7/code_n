### 1. Description

Given an integer array `nums` of size `n`, return *the minimum number of moves required to make all array elements equal*.

In one move, you can increment $n - 1$ elements of the array by `1`.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty integer array of length $n$.

**Return value**

- Return the minimum number of moves needed to make all elements equal, where each move increments exactly $n - 1$ elements by `1`.

The result is guaranteed to fit in a 32-bit integer.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,3]`
- **Output:** `3`
- **Explanation:** Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
#### Example 2

- **Input:** `nums = [1,1,1]`
- **Output:** `0`

### 4. Constraints

- $n = \text{nums.length}$

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$

- The answer is guaranteed to fit in a **32-bit** integer.