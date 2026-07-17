# Minimum Deletions to Make String Balanced

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1653 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/) |

## Problem Description
### Goal
Given a string `s` containing only `a` and `b`, delete as few characters as possible so that it becomes balanced. A balanced string has no earlier `b` followed by a later `a`; equivalently, every remaining `a` appears before every remaining `b`.

Any number of characters may be deleted, including none. Deletions preserve the relative order of the characters that remain. Return only the minimum deletion count.

### Function Contract
**Inputs**

- `s`: a string of length $n$ containing only `a` and `b`, where $1 \le n \le 10^5$.

**Return value**

Return the minimum number of deletions needed to leave a string with no index pair $i<j$ such that `s[i] == "b"` and `s[j] == "a"`.

### Examples
**Example 1**

- Input: `s = "aababbab"`
- Output: `2`

Deleting two conflicting characters can leave either `aaabbb` or `aabbbb`.

**Example 2**

- Input: `s = "bbaaaaabb"`
- Output: `2`

Deleting the first two `b` characters leaves all `a` characters before the final `b` characters.

**Example 3**

- Input: `s = "abab"`
- Output: `1`

Removing the middle `b` leaves `aab`.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce every balanced result to a split.** Any balanced subsequence has some boundary with only retained `a` characters on its left and only retained `b` characters on its right. For a chosen split, every original `b` before the boundary and every original `a` after it must be deleted. Minimizing that sum over all boundaries characterizes the answer.

**Maintain the best cost for the processed prefix.** Scan from left to right. `seen_b` counts the `b` characters encountered so far. `deletions` is the minimum deletions needed to balance the processed prefix. Reading another `b` never harms a balanced prefix because it can remain at the end, so only `seen_b` changes.

**Resolve a newly read `a`.** If the next character is `a`, there are exactly two optimal forms worth considering. Delete this `a`, which costs `deletions + 1`, or retain it and delete every earlier `b`, which costs `seen_b`. Set `deletions` to the smaller value. No third choice can do better: a retained `a` cannot coexist with any retained earlier `b`, while a deleted `a` leaves the previously optimal prefix unchanged.

This recurrence considers the two possible sides of the balance boundary whenever an `a` creates a conflict. By induction, `deletions` remains optimal for every prefix and therefore for the complete string.

#### Complexity detail

The scan processes each of the $n$ characters once with constant work, for $O(n)$ time. Two integer counters use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate every split with prefix/suffix counts:** Precomputing `b` prefixes and `a` suffixes also yields $O(n)$ time but uses $O(n)$ space.
- **Recount each split:** Directly counting left-side `b` and right-side `a` for all $n+1$ boundaries is correct but costs $O(n^2)$ time.
- **Stack cancellation:** Treat each `ba` conflict as a removable pair and count cancellations. This can run in $O(n)$ time but uses up to $O(n)$ stack space unless reduced to counters.
- A string containing only one character type is already balanced.
- An `a`-only prefix followed by a `b`-only suffix requires zero deletions.
- A `b`-only prefix followed by an `a`-only suffix requires deleting the smaller side.
- The empty string can result from deletions and is balanced, although an optimal solution never needs more than $n$ deletions.
- Equal optimal choices in the recurrence may represent different deletion sets but have the same minimum count.

</details>
