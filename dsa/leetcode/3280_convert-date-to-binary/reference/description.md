## Description

You are given a string `date` representing a Gregorian calendar date in the `yyyy-mm-dd` format.

`date` can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in `year-month-day` format.

Return the **binary** representation of `date`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** date = "2080-02-29"

**Output:** "100000100000-10-11101"

**Explanation:**

100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.

</div>
#### Example 2

<div class="example-block">
**Input:** date = "1900-01-01"

**Output:** "11101101100-1-1"

**Explanation:**

11101101100, 1, and 1 are the binary representations of 1900, 1, and 1 respectively.

</div>
### Constraints

- $\text{date.length} = 10$

- $\text{date}[4] = \text{date}[7] = '-'$, and all other $\text{date}[i]$'s are digits.

- The input is generated such that `date` represents a valid Gregorian calendar date between Jan 1^st, 1900 and Dec 31^st, 2100 (both inclusive).