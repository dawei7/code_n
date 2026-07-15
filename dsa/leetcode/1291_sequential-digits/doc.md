# Sequential Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1291 |
| Difficulty | Medium |
| Topics | Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/sequential-digits/) |

## Problem Description
### Goal
An integer has sequential digits exactly when every digit after the first is one greater than the digit immediately before it. For example, 1234 qualifies, while 1245 and 321 do not.

Given inclusive integer bounds `low` and `high`, return every sequential-digit integer in the closed range $[\texttt{low},\texttt{high}]$. The returned list must be sorted in ascending numeric order.

### Function Contract
**Inputs**

- `low` and `high`: integers satisfying $10 \le \texttt{low} \le \texttt{high} \le 10^9$.

**Return value**

A sorted list containing exactly the integers between the bounds, inclusive, whose adjacent decimal digits increase by one.

### Examples
**Example 1**

- Input: `low = 100`, `high = 300`
- Output: `[123,234]`

**Example 2**

- Input: `low = 1000`, `high = 13000`
- Output: `[1234,2345,3456,4567,5678,6789,12345]`

**Example 3**

- Input: `low = 90`, `high = 100`
- Output: `[]`

### Required Complexity
- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Every sequential-digit integer is a contiguous substring of `"123456789"`. No zero can appear: a preceding digit would have to be $-1$ for zero to start a valid sequence, or nine would need a successor digit ten. Thus the complete legal candidate set consists of the 36 substrings of lengths two through nine.

Enumerate substring lengths in increasing order and, within one length, move the start from left to right. This visits candidates in ascending numeric order: shorter valid numbers precede longer ones, and equal-length decimal strings have the same order lexicographically and numerically. Convert each substring to an integer and append it exactly when it lies within the inclusive bounds. Because the enumeration contains every possible sequential-digit number once, filtering it produces exactly the required sorted list.

#### Complexity detail

There are always exactly 36 possible candidates, each with at most nine digits. Their enumeration and filtering therefore take $O(1)$ time relative to the input bounds, and the result has constant maximum size. Aside from the returned list, the loop uses $O(1)$ auxiliary space. This fixed source domain is verified by a bounded-domain certificate rather than runtime scaling.

#### Alternatives and edge cases

- **Breadth-first generation:** Start with digits one through nine and repeatedly append the next digit; this is correct but more machinery than fixed substring enumeration.
- **Scan the numeric interval:** Testing every integer between the bounds can take $O(\texttt{high}-\texttt{low})$ time.
- **Inclusive endpoints:** A sequential value equal to either bound must be included.
- **Empty result:** Some ranges, such as $[90,100]$, contain no sequential-digit value.
- **Nine-digit maximum:** `123456789` is the only nine-digit candidate; no valid sequence can continue after nine.

</details>
