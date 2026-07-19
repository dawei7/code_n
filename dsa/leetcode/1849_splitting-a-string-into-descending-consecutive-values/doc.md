# Splitting a String Into Descending Consecutive Values

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/) |
| Frontend ID | 1849 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given a string `s` containing only decimal digits. Split the entire string into at least two non-empty contiguous substrings. Interpret each substring as an integer; leading zeros are permitted and do not affect that numerical value.

The split is valid only when its values form a descending consecutive sequence: every value after the first must be exactly one less than the value immediately before it. Return whether any placement of split boundaries satisfies all of these conditions.

### Function Contract

**Inputs**

- `s`: a digit string with $1 \le \lvert\texttt{s}\rvert \le 20$.
- A substring such as `"0090"` has numerical value 90.
- Let $n=\lvert\texttt{s}\rvert$.

**Return value**

- Return `true` if all characters can be divided into at least two non-empty substrings with values $v_1,v_2,\ldots,v_k$ such that $k\ge 2$ and $v_{i+1}=v_i-1$ for every $1\le i<k$.
- Return `false` if no such complete split exists.

### Examples

**Example 1**

- Input: `s = "1234"`
- Output: `false`

No placement of boundaries produces the required descending consecutive values.

**Example 2**

- Input: `s = "050043"`
- Output: `true`

The substrings `"05"`, `"004"`, and `"3"` have values 5, 4, and 3.

**Example 3**

- Input: `s = "9080701"`
- Output: `false`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Choose only the first boundary**

The first substring can end at any position before the final character. Trying those $n-1$ possibilities guarantees that the first value of every legal split is considered while also enforcing the requirement of at least two pieces.

Once a first value `previous` is fixed, the next numerical value is forced to be `previous - 1`. Build the next value from consecutive digits until it either equals that target or exceeds it. Leading zeros merely delay the first positive contribution, so stopping at the first equality cannot discard a different valid value. If the constructed value exceeds the target or the input ends too early, that first boundary cannot work.

**Handle the final zero**

A descending sequence cannot continue below zero. When the required next value is zero, the entire remaining suffix must therefore consist of zeros. Consuming that suffix creates one final non-empty zero-valued substring; any nonzero digit means the candidate first boundary fails.

Each successful match advances to a non-empty substring and decreases the previous value by exactly one. If the scan reaches the end, the chosen pieces cover all of `s` and every adjacent pair satisfies the required relation. Conversely, any valid split begins at one of the tried first boundaries, and each of its later values is the unique forced predecessor minus one, so the scan follows that split to the end.

#### Complexity detail

There are $O(n)$ possible first boundaries. For each one, the remaining characters are scanned at most once, giving $O(n^2)$ time. The largest parsed integer and temporary decimal text can contain $O(n)$ digits, so the auxiliary space is $O(n)$ when arbitrary-precision integer storage is counted; the iterative control state itself is constant-sized.

#### Alternatives and edge cases

- **Depth-first search over all endpoints:** Recursively try every possible next substring and prune values that are not one less; this is direct but uses a recursion stack and explores unnecessary boundaries after the first value is fixed.
- **Enumerate every partition:** Test all $2^{n-1}$ boundary patterns; it is correct for the small source limit but does exponentially more work.
- **Leading zeros:** `"050043"` is valid because its values are 5, 4, and 3, not 5, 4, and 3 with width constraints.
- **At least two pieces:** A one-character string and the unsplit whole string are never valid answers.
- **Repeated equal values:** A difference of zero is invalid even though the sequence does not increase.
- **Transition to zero:** A suffix made entirely of zeros may be the final value, but no further value can equal $-1$.
- **Complete consumption:** Matching an early prefix is insufficient unless every character belongs to the valid sequence.
- **Large first value:** The 20-digit input limit may exceed fixed-width integer ranges in some languages, so implementations must avoid overflow or bound candidate construction safely.

</details>
