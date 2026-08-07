## Description

You are given a string `date` representing a Gregorian calendar date in the `yyyy-mm-dd` format.

`date` can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in `year-month-day` format.

Return the **binary** representation of `date`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">date = "2080-02-29"</span>

**Output:** <span class="example-io">"100000100000-10-11101"</span>

**Explanation:**

<span class="example-io">100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.</span>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">date = "1900-01-01"</span>

**Output:** <span class="example-io">"11101101100-1-1"</span>

**Explanation:**

<span class="example-io">11101101100, 1, and 1 are the binary representations of 1900, 1, and 1 respectively.</span>

</div>

**Constraints:**

	- `date.length == 10`

	- `date[4] == date[7] == '-'`, and all other `date[i]`'s are digits.

	- The input is generated such that `date` represents a valid Gregorian calendar date between Jan 1^st, 1900 and Dec 31^st, 2100 (both inclusive).
