### 1. Description

Given two strings low and high that represent two integers `low` and `high` where $low \le high$, return *the number of **strobogrammatic numbers** in the range* `[low, high]`.

A **strobogrammatic number** is a number that looks the same when rotated `180` degrees (looked at upside down).

### 2. Function Contract

**Inputs**

- `low`: String representing lower bound integer.
- `high`: String representing upper bound integer.

**Return value**

Return integer count of strobogrammatic numbers in `[low, high]`.

### 3. Examples

#### Example 1

- **Input:** $low = "50", high = "100"$
- **Output:** `3`

#### Example 2

- **Input:** $low = "0", high = "0"$
- **Output:** `1`

### 4. Constraints

- $1 \le \text{low.length}, \text{high.length} \le 15$

- `low` and `high` consist of only digits.

- $low \le high$

- `low` and `high` do not contain any leading zeros except for zero itself.
