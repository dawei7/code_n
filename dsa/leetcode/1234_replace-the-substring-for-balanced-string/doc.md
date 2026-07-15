# Replace the Substring for Balanced String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1234 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/replace-the-substring-for-balanced-string/) |

## Problem Description

### Goal

You are given a string `s` of length $n$ containing only the four characters `"Q"`, `"W"`, `"E"`, and `"R"`. The length is a multiple of four. The string is balanced when each of those four characters appears exactly $n/4$ times.

Choose one contiguous substring and replace it with any other string having the same length. Return the minimum possible length of a replacement that can make the entire string balanced. The replacement may contain any of the four permitted characters; if `s` is already balanced, return `0` without replacing anything.

### Function Contract

**Inputs**

- `s`: A string of length $n$, where $4\le n\le10^5$, $n$ is divisible by $4$, and every character belongs to `"QWER"`.

**Return value**

- The minimum length of a substring that can be replaced to make every character occur exactly $n/4$ times.

### Examples

**Example 1**

- Input: `s = "QWER"`
- Output: `0`

Every character already appears once.

**Example 2**

- Input: `s = "QQWE"`
- Output: `1`

Replacing one `"Q"` with `"R"` balances the string.

**Example 3**

- Input: `s = "QQQW"`
- Output: `2`

The first `"QQ"` can be replaced by `"ER"`.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Describe a replacement by what remains outside it.** Once a window is selected for replacement, characters outside that window cannot change. A valid replacement exists exactly when the outside count of every character is at most `n // 4`: the new window can supply each missing count, and those deficits sum to the window length.

**Maintain outside counts with a sliding window.** Begin with counts for the full string and an empty window. Move `right` across `s`, subtracting the newly included character from its outside count. Whenever all four outside counts are at most the target, the current window is replaceable. Record its length, then advance `left` and restore that departing character to the outside counts while feasibility remains true.

For each fixed `right`, shrinking finds the shortest feasible window ending there. If restoring the left character makes an outside count exceed the target, every still-shorter window with that right endpoint would leave at least as much excess outside and cannot work. Both pointers only move forward, so considering all right endpoints finds the globally shortest valid replacement.

#### Complexity detail

Each character enters the window once and leaves it at most once, so the two-pointer scan takes $O(n)$ time. The count map has exactly four entries, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Try every substring:** Recounting or checking all window boundaries takes at least $O(n^2)$ time.
- **Binary search on window length:** Feasibility can be checked in $O(n)$ for a fixed length, producing $O(n\log n)$ time, but the direct sliding window is simpler and faster.
- **Already balanced:** The empty window immediately satisfies the outside-count condition, so the answer is `0`.
- **Only one character:** If all $n$ positions match, exactly $3n/4$ positions must be replaced.
- **Replacement contents:** The algorithm need not construct them; outside deficits uniquely determine how many of each character the window must provide.
- **Exact boundary:** An outside count equal to $n/4$ is allowed; only a count strictly above the target makes a window infeasible.

</details>
