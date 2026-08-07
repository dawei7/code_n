## Description

You are given an array `nums`, where each number in the array appears **either*** *once* *or* *twice.

Return the bitwise* *`XOR` of all the numbers that appear twice in the array, or 0 if no number appears twice.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,2,1,3]

**Output:** 1

**Explanation:**

The only number that appears twice in `nums` is 1.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,3]

**Output:** 0

**Explanation:**

No number appears twice in `nums`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,2,1]

**Output:** 3

**Explanation:**

Numbers 1 and 2 appeared twice. $1 XOR 2 = 3$.

</div>
### Constraints

- $1 \le \text{nums.length} \le 50$

- $1 \le \text{nums}[i] \le 50$

- Each number in `nums` appears either once or twice.