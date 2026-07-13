# Additive Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 306 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/additive-number/) |

## Problem Description
### Goal
Given a nonempty string of decimal digits, divide the entire string into at least three consecutive numbers. Beginning with the third number, every value must equal the sum of the two values immediately before it.

Return `True` when at least one complete additive partition exists and `False` otherwise. Number boundaries may have different widths, but a multi-digit number cannot begin with `0`; the single value `0` is allowed. Every input digit must be consumed in order with no separators or leftovers. Values may exceed fixed-width integer ranges, so their decimal substrings must be handled without overflow assumptions.

### Function Contract
**Inputs**

- `num`: a nonempty string of decimal digits

**Return value**

`True` when the complete string forms an additive sequence without illegal leading zeroes; otherwise `False`.

### Examples
**Example 1**

- Input: `num = "112358"`
- Output: `True`

**Example 2**

- Input: `num = "199100199"`
- Output: `True`

**Example 3**

- Input: `num = "1023"`
- Output: `False`

### Required Complexity

- **Time:** $O(n^3)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Only the first two boundaries are choices**

Once the first and second numbers are fixed, every later value is forced: compute their sum and require its decimal representation to occur exactly at the current string position. If it matches, advance and repeat with the second number and the sum. If it does not, that initial pair cannot produce an additive sequence.

Enumerate every nonempty first prefix and every following nonempty second segment while leaving at least one digit for the third number. Reject a multi-digit segment beginning with zero before converting it.

**Match forced sums directly against the remaining text**

For a candidate pair `first, second`, form `str(first + second)`. A prefix comparison at the current index simultaneously chooses the next boundary and verifies its value. There is no reason to try other third-number lengths because decimal notation for the required sum is unique.

For `"199100199"`, selecting `1` and `99` forces `100`, then `199`; both match and consume the string. For `"1023"`, the split `1,0` forces `1` rather than `2`, while a second number beginning with `0` cannot be extended to `02`.

**Exhausting initial pairs proves the decision**

Every valid additive sequence has one definite end for its first number and one definite end for its second. The nested boundary loops reach that pair unless it has an illegal leading zero, in which case it cannot belong to a valid sequence.

Given a legal pair, induction makes the verifier exact: before each step its two stored values are the previous two sequence members, so the only valid next text is their sum. Consuming the entire string proves a sequence of at least three numbers; any mismatch proves that chosen pair impossible. Therefore returning false after all pairs are rejected is complete.

#### Complexity detail

There are $O(n^2)$ initial boundary pairs. Verifying one pair may consume and compare $O(n)$ digits, giving the conservative $O(n^3)$ time bound, including decimal conversion and matching. Sum strings and integer representations may contain $O(n)$ digits, so auxiliary space is $O(n)$.

#### Alternatives and edge cases

- **Choose every later boundary recursively:** explores branches even though each next value is uniquely determined.
- **Try every possible third-number length:** adds an unnecessary factor; the sum fixes that length.
- The single digit `"0"` is valid as a number, but `"00"` is not. Thus `"000"` is additive as `0,0,0`, while leading-zero alternatives such as `"01"` are forbidden.

</details>
