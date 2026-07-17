# Second Largest Digit in a String

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/second-largest-digit-in-a-string/) |
| Frontend ID | 1796 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given an alphanumeric string `s`, meaning that every character is either a lowercase English letter or a decimal digit.

Consider the distinct numerical digit values that occur in the string. Return the second largest of those values. Repeated appearances of one digit count as the same value, and letters do not participate in the ranking. If fewer than two distinct digits occur, return `-1`.

### Function Contract

**Inputs**

- `s`: an alphanumeric string of length $n$, where $1 \le n \le 500$.

**Return value**

- Return the second largest distinct integer digit from `0` through `9` that appears in `s`.
- Return `-1` when no second distinct digit exists.

### Examples

**Example 1**

- Input: `s = "dfa12321afd"`
- Output: `2`

The distinct digits are `1`, `2`, and `3`, so `2` is second largest.

**Example 2**

- Input: `s = "abc1111"`
- Output: `-1`

Only digit `1` appears, regardless of its repetitions.

**Example 3**

- Input: `s = "ck077"`
- Output: `0`

The distinct digits are `0` and `7`; therefore zero is the second largest.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate digits from letters**

Scan `s` once. Ignore every lowercase letter. For a character between `"0"` and `"9"`, convert it to its integer value before comparing ranks; lexical and numerical order agree for these ten characters, but integer sentinels make the missing-value result direct.

**Maintain two distinct ranks**

Keep `largest` and `second_largest`, both initialized to `-1`. When a digit exceeds `largest`, move the old largest into second place and install the new value as the largest. Otherwise, replace `second_largest` only when the digit lies strictly between the two stored values.

The strict comparisons matter. A digit equal to `largest` or `second_largest` is a duplicate and must not occupy another rank.

**Preserve the prefix invariant**

After each processed prefix, `largest` is its greatest digit value and `second_largest` is its greatest distinct value below `largest`, or `-1` if none exists. A new maximum performs the necessary demotion. A nonmaximum digit can affect only second place, and exactly the strict-between test identifies when it improves that rank.

These cases cover every incoming digit and preserve the invariant through the full string. The final `second_largest` is consequently the requested value, with the sentinel already representing the missing case.

#### Complexity detail

The scan performs constant work for each of the $n$ characters, taking $O(n)$ time. It stores two integer ranks and uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Digit set plus sorting:** Collecting distinct digit values and sorting them is concise and still uses only fixed-domain storage, but it does more work than maintaining the top two directly.
- **Boolean presence array:** Mark ten possible digits, then scan from `9` downward for the second marked value; this is also $O(n)$ time and $O(1)$ space.
- **Sort every digit occurrence:** Sorting all occurrences takes $O(n\log n)$ time and still requires explicit duplicate removal.
- **Letters only:** No digit exists, so the result remains `-1`.
- **One distinct repeated digit:** Repetition does not create a second rank.
- **Zero as the answer:** The `-1` sentinel keeps a legitimate digit zero distinguishable from absence.
- **Arrival order:** The largest value may appear before or after the eventual second largest; both update paths must work.

</details>
