## Description

You are given an integer `n`.

Return the **total** number of commas used when writing all integers from `[1, n]` (inclusive) in **standard** number formatting.

In **standard** formatting:

	- A comma is inserted after **every three** digits from the right.

	- Numbers with **fewer** than 4 digits contain no commas.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 1002</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The numbers `"1,000"`, `"1,001"`, and `"1,002"` each contain one comma, giving a total of 3.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 998</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

**​​​​​​​**All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

</div>

**Constraints:**

	- `1 <= n <= 10^15`
