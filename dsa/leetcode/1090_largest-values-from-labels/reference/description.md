### 1. Description

You are given `n` item's value and label as two integer arrays `values` and `labels`. You are also given two integers `numWanted` and `useLimit`.

Your task is to find a subset of items with the **maximum sum** of their values such that:

- The number of items is **at most** `numWanted`.

- The number of items with the same label is **at most** `useLimit`.

Return the maximum sum.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1

**Output:** 9

**Explanation:**

The subset chosen is the first, third, and fifth items with the sum of values 5 + 3 + 1.

</div>
#### Example 2

<div class="example-block">
**Input:** values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2

**Output:** 12

**Explanation:**

The subset chosen is the first, second, and third items with the sum of values 5 + 4 + 3.

</div>
#### Example 3

<div class="example-block">
**Input:** values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1

**Output:** 16

**Explanation:**

The subset chosen is the first and fourth items with the sum of values 9 + 7.

</div>

### 4. Constraints

- $n = \text{values.length} = \text{labels.length}$

- $1 \le n \le 2 * 10^{4}$

- $0 \le \text{values}[i], \text{labels}[i] \le 2 * 10^{4}$

- $1 \le numWanted, useLimit \le n$