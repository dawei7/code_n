### 1. Description

You are given an integer array `nums` and an integer `digit`.

Return the total number of times `digit` appears in the decimal representation of all elements in `nums`.

### 2. Function Contract

**Inputs**

- `nums`: A non-empty array of positive integers whose decimal digits are inspected.
- `digit`: The single decimal digit, from $0$ through $9$, whose appearances must be counted.

Let $S$ denote the total number of decimal digit positions across every value in `nums`.

**Return value**

Return the number of positions among those $S$ positions whose value equals `digit`.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [12,54,32,22], digit = 2

**Output:** 4

**Explanation:**

The digit 2 appears once in 12 and 32, and twice in 22. Thus, the total number of times digit 2 appears is 4.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,34,7], digit = 9

**Output:** 0

**Explanation:**

The digit 9 does not appear in the decimal representation of any element in `nums`, so the total number of times digit 9 appears is 0.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 1000$

- $1 \le \text{nums}[i] \le 10^{6}​​​​​​​$

- $0 \le digit \le 9$