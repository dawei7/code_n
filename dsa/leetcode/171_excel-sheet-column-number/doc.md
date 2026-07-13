# Excel Sheet Column Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 171 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/excel-sheet-column-number/) |

## Problem Description
### Goal
Spreadsheet columns use titles `A` through `Z`, followed by `AA`, `AB`, and longer uppercase sequences. Given a nonempty valid `column_title`, convert that label to its positive one-based column number.

Interpret the letters as digits valued `1` through `26` in a positional alphabetic system: `A` is `1`, `Z` is `26`, and the next title `AA` is `27`. Letter order is significant, with the leftmost character carrying the greatest place value. Return the integer column number only, without normalizing, reordering, or treating the system as ordinary base 26 with a zero digit.

### Function Contract
**Inputs**

- `column_title`: a nonempty string of uppercase letters `A` through `Z`

**Return value**

The corresponding one-based Excel column number.

### Examples
**Example 1**

- Input: `column_title = "A"`
- Output: `1`

**Example 2**

- Input: `column_title = "AB"`
- Output: `28`

**Example 3**

- Input: `column_title = "ZY"`
- Output: `701`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Interpret the title as a positional numeral with base 26 and digit values $A = 1$ through $Z = 26$. Although this alphabet has no zero digit, left-to-right evaluation works like an ordinary base representation once each character has been mapped to its one-based value.

Maintain a running `total`. For each letter with value `digit`, update

`total = total * 26 + digit`.

Multiplication shifts the previously processed prefix one position to the left, and addition installs the new least-significant digit. This is Horner's rule applied to the title's positional polynomial.

For `"ZY"`, processing `Z` gives `26`; processing `Y` gives $26 \cdot 26 + 25 = 701$. For `"AB"`, the calculation is $1 \cdot 26 + 2 = 28$, explaining why `AA` begins at 27 rather than at 26.

After processing any prefix, `total` equals the numeric value represented by that prefix. This is true for the empty prefix, whose value is zero. Appending a letter shifts every existing digit one base-26 position and adds the new digit, exactly the update `26 * total + digit`; therefore the property is preserved. By induction, after the final character, `total` is the value of the complete column title.

#### Complexity detail

Each of the `n` characters is converted and accumulated once, so time is $O(n)$. The running total and current digit use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- Explicitly summing `digit * 26 ^ position` is correct but requires powers and more bookkeeping than Horner's rule.
- Mapping `A` to zero produces incorrect values because Excel's notation is bijective and has no zero symbol.
- Generating titles until the input is reached takes time proportional to the numeric answer instead of the title length.
- Single letters map to `1..26`; `AA`, `ZZ`, and `AAA` are useful boundary tests.
- Fixed-width languages should ensure the accumulator type can hold the maximum permitted result.

</details>
