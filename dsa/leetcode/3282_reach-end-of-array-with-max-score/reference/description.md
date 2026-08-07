### 1. Description

You are given an integer array `nums` of length `n`.

Your goal is to start at index `0` and reach index $n - 1$. You can only jump to indices **greater** than your current index.

The score for a jump from index `i` to index `j` is calculated as $(j - i) * \text{nums}[i]$.

Return the **maximum** possible **total score** by the time you reach the last index.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,3,1,5]

**Output:** 7

**Explanation:**

First, jump to index 1 and then jump to the last index. The final score is $1 * 1 + 2 * 3 = 7$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,3,1,3,2]

**Output:** 16

**Explanation:**

Jump directly to the last index. The final score is $4 * 4 = 16$.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$