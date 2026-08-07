## Description

Given an integer `n`, return all the **strobogrammatic numbers** that are of length `n`. You may return the answer in **any order**.

A **strobogrammatic number** is a number that looks the same when rotated `180` degrees (looked at upside down).
### Function Contract

**Inputs**

- `n`: Target length integer.

**Return value**

Return $\text{List}[str]$ containing all strobogrammatic numbers of length `n`.

### Examples

#### Example 1

- **Input:** $n = 2$
- **Output:** `["11","69","88","96"]`
#### Example 2

- **Input:** $n = 1$
- **Output:** `["0","1","8"]`
### Constraints

- $1 \le n \le 14$