### 1. Description

Given an integer array `nums` of size `n`, return *the minimum number of moves required to make all array elements equal*.

In one move, you can increment or decrement an element of the array by `1`.

Test cases are designed so that the answer will fit in a **32-bit** integer.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty integer array of length $n$.

**Return value**

- Return the minimum number of single-element `+1` or `-1` moves needed to make every value equal.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,3]`
- **Output:** `2`
- **Explanation:** Only two moves are needed (remember each move increments or decrements one element):
[<u>1</u>,2,3]  =>  [2,2,<u>3</u>]  =>  [2,2,2]

#### Example 2

- **Input:** `nums = [1,10,2,9]`
- **Output:** `16`

### 4. Constraints

- $n = \text{nums.length}$

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$
