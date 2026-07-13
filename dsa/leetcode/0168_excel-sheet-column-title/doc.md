# Excel Sheet Column Title

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 168 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/excel-sheet-column-title/) |

## Problem Description
### Goal
Spreadsheet columns are labeled `A` through `Z`, then `AA`, `AB`, and onward, using uppercase letters as a one-based alphabetic numeral system. Given a positive integer `column_number`, determine the label assigned to that numbered column.

Return the complete Excel-style title as a string. Each letter represents a value from `1` through `26`; there is no zero digit, so boundaries such as $26 \to Z$ and `27 -> AA` do not behave like ordinary zero-based base conversion. Preserve the most-significant-to-least-significant letter order and support titles containing as many characters as the input requires.

### Function Contract
**Inputs**

- `column_number`: positive integer column number

**Return value**

Its Excel-style column title.

### Examples
**Example 1**

- Input: `column_number = 1`
- Output: `"A"`

**Example 2**

- Input: `column_number = 28`
- Output: `"AB"`

**Example 3**

- Input: `column_number = 701`
- Output: `"ZY"`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(\log n)$

<details>
<summary>Approach</summary>

#### General

Excel titles resemble base 26, but they are **bijective base 26**: the symbols represent values `1` through `26`, and there is no symbol for zero. That missing zero is why ordinary remainder arithmetic fails at boundaries such as `26`, which must become `Z` rather than something ending in a zero digit.

Before extracting each digit, subtract one from the current number. This shifts the valid digit range `1..26` onto the ordinary remainder range `0..25`. Then

`quotient, remainder = divmod(column_number - 1, 26)`

maps remainder `0` to `A`, remainder `1` to `B`, and so on through remainder `25` to `Z`. Append that letter and continue with the quotient. As with ordinary positional conversion, division discovers the least-significant character first, so reverse the accumulated characters at the end.

Trace `701`: subtracting one and dividing by 26 gives quotient `26`, remainder `24`, so the last character is `Y`. Repeating with `26` gives quotient `0`, remainder `25`, so the preceding character is `Z`. Reversing the generated `"YZ"` yields `"ZY"`.

The subtraction can also be understood as borrowing across a system without zero. At the transition from `Z` to `AA`, value `26` consumes the final one-character title; value `27` becomes one `A` in the next position plus one `A` in the current position.

For every positive current value, subtracting one creates a unique quotient and remainder with remainder in `0..25`. Adding one to that remainder identifies exactly one title letter, while the quotient represents the still-unprocessed prefix in the same bijective system. Repeating until the quotient is zero therefore extracts every title character exactly once from right to left. Reversing those characters reconstructs the unique Excel column title for the original number.

#### Complexity detail

Each iteration divides the remaining value by approximately 26, so a title of length $k = O(\log_{26} n)$ requires $O(k)$ time. The character buffer and returned string use $O(k)$ space; excluding the required output, the arithmetic state is $O(1)$.

#### Alternatives and edge cases

- Ordinary base-26 conversion without the decrement invents a zero digit and fails at every multiple of 26.
- A recursive implementation expresses the prefix/suffix relationship neatly but consumes $O(\log n)$ call-stack space.
- Precomputing or enumerating column titles performs work proportional to the input value rather than its logarithm.
- Boundary cases `1 -> A`, `26 -> Z`, `27 -> AA`, and `702 -> ZZ`, `703 -> AAA` are useful tests of the one-based digit rule.

</details>
