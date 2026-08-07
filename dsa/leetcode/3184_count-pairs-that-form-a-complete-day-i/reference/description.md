### 1. Description

Given an integer array `hours` representing times in **hours**, return an integer denoting the number of pairs `i`, `j` where `i < j` and $\text{hours}[i] + \text{hours}[j]$ forms a **complete day**.

A **complete day** is defined as a time duration that is an **exact** **multiple** of 24 hours.

For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** hours = [12,12,30,24,24]

**Output:** 2

**Explanation:**

The pairs of indices that form a complete day are `(0, 1)` and `(3, 4)`.

</div>
#### Example 2

<div class="example-block">
**Input:** hours = [72,48,24,3]

**Output:** 3

**Explanation:**

The pairs of indices that form a complete day are `(0, 1)`, `(0, 2)`, and `(1, 2)`.

</div>

### 4. Constraints

- $1 \le \text{hours.length} \le 100$

- $1 \le \text{hours}[i] \le 10^{9}$