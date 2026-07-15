# Max Difference You Can Get From Changing an Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1432 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/) |

## Problem Description

### Goal

Start with the positive integer `num`. One replacement operation chooses a decimal digit `x` and another digit `y`, then changes every occurrence of `x` in `num` to `y`. Apply this operation independently twice to produce integers `a` and `b`; the two operations may choose different digit pairs.

Neither result may have a leading zero or equal zero. The chosen digits may be equal, so an operation is allowed to leave the number unchanged. Return the greatest possible value of `a - b` over all valid choices.

### Function Contract

**Inputs**

- `num`: an integer satisfying $1 \le \texttt{num} \le 10^8$.
- Let $d$ be the number of decimal digits in `num`.

**Return value**

- The maximum difference between a valid independently maximized replacement result and a valid independently minimized replacement result.

### Examples

**Example 1**

- Input: `num = 555`
- Output: `888`

**Example 2**

- Input: `num = 9`
- Output: `8`

**Example 3**

- Input: `num = 123456`
- Output: `820000`

### Required Complexity

- **Time:** $O(d)$
- **Space:** $O(d)$

<details>
<summary>Approach</summary>

#### General

**Maximize at the first improvable digit.** Read the decimal digits from left to right. If every digit is `9`, the maximum is already `num`. Otherwise, take the first digit that is not `9` and replace every occurrence of it with `9`. Changing that earliest position gives the largest possible positional gain; once its replacement is fixed to the greatest digit, changing all equal occurrences can only increase the result further.

**Minimize a leading digit without creating zero.** If the first digit is not `1`, replace every occurrence of that leading digit with `1`. The leading position has the greatest place value, and `1` is the smallest digit allowed there, so no valid choice can produce a smaller most-significant digit.

**Minimize after a leading one.** When the number already starts with `1`, replacing that digit cannot lower the leading position: changing it to `0` is invalid and any other digit is no smaller. Instead, find the first later digit that is neither `0` nor `1` and replace all of its occurrences with `0`. Earlier later digits already have their smallest usable values, so this is the earliest position that can be reduced. If no such digit exists, the minimum remains unchanged.

**Why the two greedy extremes maximize the difference.** The two operations are independent, so choosing the greatest valid `a` cannot restrict the choice of `b`, and choosing the smallest valid `b` cannot restrict `a`. The positional arguments above establish those separate extremes. Their difference is therefore at least every other valid `a - b` and is the requested maximum.

#### Complexity detail

Each extreme requires at most a constant number of scans over the $d$ decimal digits, and replacement constructs two length-$d$ strings. The total time is $O(d)$ and the string representations use $O(d)$ space. Under the public constraint, $d \le 9$; the package records bounded-domain evidence instead of claiming a meaningful runtime scaling measurement across only nine legal sizes.

#### Alternatives and edge cases

- **Enumerate digit pairs:** Trying all 100 choices of source and replacement digits is correct after rejecting leading zeroes, but it obscures the positional greedy reasoning and repeats work.
- **All nines:** The maximum is unchanged because no digit can increase; the minimum replaces the leading `9` with `1`.
- **Leading one followed only by zeroes and ones:** No valid replacement lowers the number, so the minimum is the original value.
- **Repeated selected digit:** Every occurrence must be replaced, not only the first one that motivated the greedy choice.
- **Single digit:** The greatest valid result is `9` and the smallest is `1`.
- **Result length:** Replacement never adds or removes a digit, and the leading-zero rule preserves the original digit count.

</details>
