## Description

You are given three arrays of length `n` that describe the properties of `n` coupons: `code`, `businessLine`, and `isActive`. The $$i^{\text{th}}$$coupon has:

- $\text{code}[i]$: a **string** representing the coupon identifier.

- $\text{businessLine}[i]$: a **string** denoting the business category of the coupon.

- $\text{isActive}[i]$: a **boolean** indicating whether the coupon is currently active.

A coupon is considered **valid** if all of the following conditions hold:

- $\text{code}[i]$ is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (`_`).

- $\text{businessLine}[i]$ is one of the following four categories: `"electronics"`, `"grocery"`, `"pharmacy"`, `"restaurant"`.

- $\text{isActive}[i]$ is **true**.

Return an array of the **codes** of all valid coupons, **sorted** first by their **businessLine** in the order: `"electronics"`, `"grocery"`, `"pharmacy", "restaurant"`, and then by **code** in lexicographical (ascending) order within each category.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]

**Output:** ["PHARMA5","SAVE20"]

**Explanation:**

- First coupon is valid.

- Second coupon has empty code (invalid).

- Third coupon is valid.

- Fourth coupon has special character `@` (invalid).

</div>
#### Example 2

<div class="example-block">
**Input:** code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]

**Output:** ["ELECTRONICS_50"]

**Explanation:**

- First coupon is inactive (invalid).

- Second coupon is valid.

- Third coupon has invalid business line (invalid).

</div>
### Constraints

- $n = \text{code.length} = \text{businessLine.length} = \text{isActive.length}$

- $1 \le n \le 100$

- $0 \le \text{code}[i].length, \text{businessLine}[i].length \le 100$

- $\text{code}[i]$ and $\text{businessLine}[i]$ consist of printable ASCII characters.

- $\text{isActive}[i]$ is either `true` or `false`.