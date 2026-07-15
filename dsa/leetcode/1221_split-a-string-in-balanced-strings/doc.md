# Split a String in Balanced Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1221 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/split-a-string-in-balanced-strings/) |

## Problem Description

### Goal

A string is **balanced** when it contains the same number of `L` and `R` characters. You are given a balanced string `s` containing only those two characters.

Split `s` into nonempty, contiguous balanced strings so that every character belongs to exactly one piece and the pieces retain their original order. Return the maximum number of balanced strings obtainable in such a split.

### Function Contract

**Inputs**

- `s`: A balanced string of length $n$ containing only `L` and `R`, where $2\le n\le1000$.

**Return value**

- The greatest possible number of nonempty balanced pieces in a complete split of `s`.

### Examples

**Example 1**

- Input: `s = "RLRRLLRLRL"`
- Output: `4`

One maximum split is `RL | RRLL | RL | RL`.

**Example 2**

- Input: `s = "RLRRRLLRLL"`
- Output: `2`

It may be split as `RL | RRRLLRLL`.

**Example 3**

- Input: `s = "LLLLRRRR"`
- Output: `1`

No proper prefix is balanced, so the entire string is the only piece.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track the unmatched character difference.** Scan from left to right, adding one for `L` and subtracting one for `R`. The balance is zero exactly when the current segment since the last cut contains equal counts of the two characters.

**Cut at every earliest zero.** Whenever the balance returns to zero, finish the current piece immediately and increment the answer. The next character begins a fresh segment with balance zero, so the same rule can be applied independently to the remaining suffix.

**Why earliest cuts maximize the number of pieces.** Any balanced piece must end at an index where the cumulative balance relative to its start is zero. Choosing the first such index creates one valid piece and leaves the longest possible suffix for additional pieces. Delaying that cut can only merge this piece with one or more later balanced portions; it cannot create an extra boundary before the first zero. Applying the exchange argument at every boundary proves the greedy count is maximal. The input's global balance guarantees the final character closes the last piece.

#### Complexity detail

The scan examines each of the $n$ characters once, taking $O(n)$ time. The balance and piece count are the only stored values, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Repeated prefix extraction:** Searching for the first balanced prefix and copying the remaining suffix is correct, but repeated scans or copies can take $O(n^2)$ time.
- **Dynamic programming over cut positions:** It can model all balanced prefixes, but the earliest-zero property makes the extra states unnecessary.
- **Single piece:** A string such as `LLLLRRRR` has no earlier zero balance and must remain whole.
- **Alternating characters:** Every adjacent `LR` or `RL` pair can become its own piece, attaining $n/2$ pieces.
- **Nested imbalance:** A large positive or negative balance does not permit a cut until it returns exactly to zero.
- **Even length:** Global balance implies an even number of characters, though no separate validation is needed.

</details>
