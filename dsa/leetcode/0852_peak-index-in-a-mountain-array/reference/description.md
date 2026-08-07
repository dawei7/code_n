### 1. Description

You are given an integer **mountain** array `arr` of length `n` where the values increase to a **peak element** and then decrease.

Return the index of the peak element.

Your task is to solve it in `O(log(n))` time complexity.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** arr = [0,1,0]

**Output:** 1

</div>
#### Example 2

<div class="example-block">
**Input:** arr = [0,2,1,0]

**Output:** 1

</div>
#### Example 3

<div class="example-block">
**Input:** arr = [0,10,5,2]

**Output:** 1

</div>

### 4. Constraints

- $3 \le \text{arr.length} \le 10^{5}$

- $0 \le \text{arr}[i] \le 10^{6}$

- `arr` is **guaranteed** to be a mountain array.