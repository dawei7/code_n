## Description

You are given three arrays of length `n` that describe the properties of `n` coupons: `code`, `businessLine`, and `isActive`. The `i^th `coupon has:

	- `code[i]`: a **string** representing the coupon identifier.

	- `businessLine[i]`: a **string** denoting the business category of the coupon.

	- `isActive[i]`: a **boolean** indicating whether the coupon is currently active.

A coupon is considered **valid** if all of the following conditions hold:

	- `code[i]` is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (`_`).

	- `businessLine[i]` is one of the following four categories: `"electronics"`, `"grocery"`, `"pharmacy"`, `"restaurant"`.

	- `isActive[i]` is **true**.

Return an array of the **codes** of all valid coupons, **sorted** first by their **businessLine** in the order: `"electronics"`, `"grocery"`, `"pharmacy", "restaurant"`, and then by **code** in lexicographical (ascending) order within each category.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]</span>

**Output:** <span class="example-io">["PHARMA5","SAVE20"]</span>

**Explanation:**

	- First coupon is valid.

	- Second coupon has empty code (invalid).

	- Third coupon is valid.

	- Fourth coupon has special character `@` (invalid).

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]</span>

**Output:** <span class="example-io">["ELECTRONICS_50"]</span>

**Explanation:**

	- First coupon is inactive (invalid).

	- Second coupon is valid.

	- Third coupon has invalid business line (invalid).

</div>

**Constraints:**

	- `n == code.length == businessLine.length == isActive.length`

	- `1 <= n <= 100`

	- `0 <= code[i].length, businessLine[i].length <= 100`

	- `code[i]` and `businessLine[i]` consist of printable ASCII characters.

	- `isActive[i]` is either `true` or `false`.
