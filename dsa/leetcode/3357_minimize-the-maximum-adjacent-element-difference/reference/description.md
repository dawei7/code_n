### 1. Description

You are given an array of integers `nums`. Some values in `nums` are **missing** and are denoted by -1.

You must choose a pair of **positive** integers `(x, y)` **exactly once** and replace each **missing** element with *either* `x` or `y`.

You need to **minimize**** **the** maximum** **absolute difference** between *adjacent* elements of `nums` after replacements.

Return the **minimum** possible difference.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,-1,10,8]

**Output:** 4

**Explanation:**

By choosing the pair as `(6, 7)`, nums can be changed to `[1, 2, 6, 10, 8]`.

The absolute differences between adjacent elements are:

- $|1 - 2| = 1$

- $|2 - 6| = 4$

- $|6 - 10| = 4$

- $|10 - 8| = 2$

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [-1,-1,-1]

**Output:** 0

**Explanation:**

By choosing the pair as `(4, 4)`, nums can be changed to `[4, 4, 4]`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [-1,10,-1,8]

**Output:** 1

**Explanation:**

By choosing the pair as `(11, 9)`, nums can be changed to `[11, 10, 9, 8]`.

</div>

### 4. Constraints

- $2 \le \text{nums.length} \le 10^{5}$

- $\text{nums}[i]$ is either -1 or in the range $[1, 10^{9}]$.