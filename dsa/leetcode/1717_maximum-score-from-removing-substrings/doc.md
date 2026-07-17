# Maximum Score From Removing Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1717 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-score-from-removing-substrings/) |

## Problem Description

### Goal

You are given a lowercase English string `s` and two positive scores, `x` and `y`. At any time, you may delete an adjacent occurrence of `ab` and add `x` points, or delete an adjacent occurrence of `ba` and add `y` points. A deletion joins the characters on its two sides, so it can create another removable pair.

Choose both the order and locations of the deletions. Return the greatest total score obtainable after performing either operation any number of times; characters other than `a` and `b` cannot be removed and therefore separate the string into independent regions.

### Function Contract

**Inputs**

- `s`: a string of lowercase English letters, with $1 \le \lvert \texttt{s} \rvert \le 10^5$.
- `x`: the points gained for removing `ab`, with $1 \le x \le 10^4$.
- `y`: the points gained for removing `ba`, with $1 \le y \le 10^4$.

**Return value**

- Return the maximum total points obtainable by repeatedly removing `ab` and `ba`.

### Examples

**Example 1**

- Input: `s = "cdbcbbaaabab", x = 4, y = 5`
- Output: `19`
- Explanation: Removing three `ba` pairs and one `ab` pair yields $3 \cdot 5 + 4 = 19$ points.

**Example 2**

- Input: `s = "aabbaaxybbaabb", x = 5, y = 4`
- Output: `20`
- Explanation: The characters `x` and `y` separate independent `a`/`b` regions; four profitable removals are available in total.

**Example 3**

- Input: `s = "abba", x = 10, y = 1`
- Output: `11`
- Explanation: Delete the higher-valued `ab` first, leaving `ba`; both pairs can then be scored.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Remove the more valuable pair first**

Suppose `ab` is worth at least as much as `ba`; otherwise exchange the roles of the two patterns and their scores. Process `s` from left to right with a stack. Whenever the stack top and current character form `ab`, remove that pair immediately and add `x`; otherwise push the character. This single pass removes every possible occurrence of the higher-valued pattern, including occurrences created by earlier removals.

**Resolve every competing deletion in the profitable direction**

The only local competition between the two operations occurs around three alternating characters: deleting one adjacent pair can destroy the opportunity to delete the other. Giving that choice to the higher-valued pair never lowers the score. Any sequence that takes the cheaper pair at such a conflict can be exchanged for one that takes the expensive pair, while preserving all removals outside that local `a`/`b` region. Consequently, some optimal sequence removes all possible higher-valued pairs before using the cheaper operation.

**Collect the remaining lower-value pairs**

Run the same stack procedure over the remaining characters for the other pattern. The first pass has left no higher-valued pair, and the second pass extracts every remaining cheaper pair. Characters other than `a` and `b` are simply pushed and can never match either pattern, so the procedure also respects the independent-region boundaries automatically.

#### Complexity detail

Let $n = \lvert \texttt{s} \rvert$. Each pass pushes and pops every character at most once, so the two passes take $O(n)$ time. The stacks and the intermediate remaining string contain at most $n$ characters, requiring $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Count within `a`/`b` blocks:** The same greedy order can be implemented by counting unmatched endpoint characters in each block, but the stack version makes newly adjacent pairs and separators more direct.
- **Repeated substring search and deletion:** Searching for one occurrence and rebuilding the string after every removal is correct when the valuable pattern is exhausted first, but it can require $O(n^2)$ time.
- **Equal scores:** When $x = y$, either pair may be processed first because every removal contributes the same value.
- **Separating characters:** Any character other than `a` or `b` prevents a removable pair from crossing it, even after all possible deletions on either side.
- **No removable pair:** A one-character string or a region containing only one of `a` and `b` contributes zero.

</details>
