### 1. Description

Given a string `num` which represents an integer, return `true` *if* `num` *is a **strobogrammatic number***.

A **strobogrammatic number** is a number that looks the same when rotated `180` degrees (looked at upside down).

### 2. Function Contract

**Inputs**

- `num`: String representing an integer.

**Return value**

Return `true` if `num` looks identical when rotated 180 degrees, otherwise `false`.

### 3. Examples

#### Example 1

- **Input:** $num = "69"$
- **Output:** `true`

#### Example 2

- **Input:** $num = "88"$
- **Output:** `true`

#### Example 3

- **Input:** $num = "962"$
- **Output:** `false`

### 4. Constraints

- $1 \le \text{num.length} \le 50$

- `num` consists of only digits.

- `num` does not contain any leading zeros except for zero itself.
