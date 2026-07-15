# Digit Count in Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1067 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/digit-count-in-range/) |

## Problem Description

### Goal

Given one decimal digit `d` and two positive integers `low` and `high`, inspect the ordinary decimal representations of every integer in the inclusive range from `low` through `high`.

Return the total number of times digit `d` occurs across all those representations. Count every position separately when a number contains the digit more than once, and do not treat omitted leading zeros as written digits.

### Function Contract

**Inputs**

- `d`: an integer digit satisfying $0 \le d \le 9$.
- `low` and `high`: inclusive bounds satisfying $1 \le \texttt{low} \le \texttt{high} \le 2 \cdot 10^8$.
- Let $H=\texttt{high}$.

**Return value**

- The number of occurrences of `d` in all decimal representations from `low` through `high`.

### Examples

**Example 1**

- Input: `d = 1, low = 1, high = 13`
- Output: `6`
- Explanation: The digit appears in `1`, `10`, twice in `11`, `12`, and `13`.

**Example 2**

- Input: `d = 3, low = 100, high = 250`
- Output: `35`

**Example 3**

- Input: `d = 0, low = 1, high = 10`
- Output: `1`
- Explanation: Only the ones position of `10` contributes a written zero.

### Required Complexity

- **Time:** $O(\log H)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce the interval to two prefixes:** Define a helper that counts occurrences of `d` from 1 through `n`. The required inclusive-range result is `count_up_to(high) - count_up_to(low - 1)`, so each bound can be processed independently.

**Analyze one decimal position:** For a position with place value $f$, split `n` into the digits above it, the current digit, and the value below it. For nonzero `d`, every complete higher-digit cycle contributes $f$ occurrences. The partial cycle contributes zero, $f$, or `lower + 1` depending on whether the current digit is below, above, or equal to `d`.

**Exclude leading zeros:** The same cycle formula would count zero in positions that a shorter number does not write. When `d == 0`, remove one full higher-digit cycle at every position. If the higher part is zero, that position has not yet appeared in any number and contributes nothing.

Each positive integer up to `n` belongs to exactly one complete or partial cycle at every written position, so the positional contributions count each occurrence once. Subtracting the two prefix totals removes precisely the values below `low`.

#### Complexity detail

The place value is multiplied by ten after each iteration, so each prefix helper examines one position per decimal digit. Processing `high` and `low - 1` therefore takes $O(\log H)$ time and $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate the range:** Convert every integer to a string and count characters. It is simple but takes time proportional to the range size and number of written digits.
- **Digit DP:** A tight-prefix dynamic program generalizes to richer digit constraints, but positional arithmetic is smaller and constant-space for counting one digit.
- **Digit zero:** Leading zeros are not part of ordinary decimal notation and must never be counted.
- **Single-number range:** Prefix subtraction still returns the number of occurrences within that one representation.
- **Repeated digit in one number:** Every matching decimal position contributes separately.
- **Power-of-ten boundary:** The new highest position is handled when its place value first becomes no greater than the bound.
- **Prefix below one:** `count_up_to(0)` is zero, which handles `low == 1` directly.

</details>
