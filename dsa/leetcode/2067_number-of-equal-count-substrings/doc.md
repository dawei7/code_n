# Number of Equal Count Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2067 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-equal-count-substrings/) |

## Problem Description

### Goal

An equal count substring is a nonempty contiguous part of a lowercase English string in which every distinct letter that appears has the same prescribed frequency `count`. Letters absent from that substring impose no requirement.

Given `s` and the positive integer `count`, return the number of index ranges that form equal count substrings. Count ranges separately even when they contain identical text, and reject any range where at least one present letter occurs either fewer or more than `count` times.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $n$, where $1 \le n \le 3\cdot 10^4$.
- `count`: the exact required frequency for every distinct letter in a valid substring, where $1 \le \texttt{count} \le 3\cdot 10^4$.

**Return value**

- Return the number of nonempty contiguous substrings whose every present letter occurs exactly `count` times.

### Examples

**Example 1**

- Input: `s = "aaabcbbcc", count = 3`
- Output: `3`
- Explanation: `"aaa"`, `"bcbbcc"`, and the complete string have one, two, and three distinct letters, respectively, each occurring three times.

**Example 2**

- Input: `s = "abcd", count = 2`
- Output: `0`
- Explanation: No letter occurs twice inside any candidate range.

**Example 3**

- Input: `s = "a", count = 5`
- Output: `0`
- Explanation: The string is shorter than the required frequency.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**A distinct-letter count determines the window length**

If a valid substring contains exactly $d$ distinct letters, its length must be $d\cdot\texttt{count}$. The lowercase alphabet limits $d$ to the integers from $1$ through $26$. For each feasible $d$, slide a fixed-width window of that length across `s`.

**Maintain how many letters meet the target**

Keep a 26-entry frequency array and a counter for letters whose current frequency equals `count`. When a character enters or leaves the window, remove its old contribution to that counter, update its frequency, and add its new contribution. A full window is valid exactly when the counter equals $d$: those $d$ letters already account for all $d\cdot\texttt{count}$ positions, so no additional letter or excess occurrence can be present.

Every valid substring has one definite number $d$ of distinct letters and is examined once by the window width associated with that $d$. The maintained condition accepts it because all $d$ frequencies equal the target. Conversely, an accepted window has exactly the required total length supplied by $d$ target-frequency letters, proving that every present letter meets the rule.

#### Complexity detail

There are at most 26 window widths, and each width scans the $n$ characters with constant work per movement. Thus the time is $O(26n)=O(n)$. The 26 frequency counters use $O(26)=O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate every start and end:** Incremental frequencies make the test correct, but there can be $O(n^2)$ candidate ranges.
- **Prefix counts for every letter:** Any substring frequency can be queried in constant time per letter, yet checking all index ranges remains quadratic.
- When `count == 1`, valid substrings are precisely ranges with no repeated letter.
- A letter occurring more than `count` times invalidates the range just as surely as one occurring fewer times.
- Different valid ranges containing the same characters are counted separately.
- If `count > n`, no nonempty substring can qualify.
- Only values of $d$ with $d\cdot\texttt{count}\le n$ need a sliding window.

</details>
