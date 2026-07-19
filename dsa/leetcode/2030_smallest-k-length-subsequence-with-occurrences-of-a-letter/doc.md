# Smallest K-Length Subsequence With Occurrences of a Letter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2030 |
| Difficulty | Hard |
| Topics | String, Stack, Greedy, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/) |

## Problem Description

### Goal

Given a lowercase string `s`, select a subsequence of exactly `k` characters.
The distinguished character `letter` must occur in the selected subsequence at
least `repetition` times. The input guarantees that `s` contains enough copies
of `letter` for this requirement to be possible.

Among all qualifying length-`k` subsequences, return the lexicographically
smallest one. Deleting characters must preserve the relative order of every
character that remains.

### Function Contract

Let $N$ be the length of `s`.

**Inputs**

- `s`: a string of $N$ lowercase English letters, where
  $1 \le N \le 5 \cdot 10^4$.
- `k`: the required subsequence length, where $1 \le k \le N$.
- `letter`: one lowercase English character.
- `repetition`: the minimum number of selected occurrences of `letter`, where
  $1 \le \text{repetition} \le k$ and `s` contains at least that many copies.

**Return value**

- The lexicographically smallest length-`k` subsequence containing `letter` at
  least `repetition` times.

### Examples

**Example 1**

- Input: `s = "leet", k = 3, letter = "e", repetition = 1`
- Output: `"eet"`

**Example 2**

- Input: `s = "leetcode", k = 4, letter = "e", repetition = 2`
- Output: `"ecde"`

**Example 3**

- Input: `s = "bb", k = 2, letter = "b", repetition = 2`
- Output: `"bb"`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Build the lexicographically smallest feasible prefix**

Scan `s` from left to right while maintaining the chosen characters as a
monotonic stack. When the current character is smaller than the stack top,
removing the top improves the first position where the candidate changes.
Such a removal is allowed only if the current and remaining source characters
can still fill the stack to length `k`.

**Protect the required letter count while popping**

Track how many copies of `letter` are already selected and how many remain at
or after the current position. A non-`letter` stack top may be removed whenever
the length guard permits. A `letter` top may be removed only when the selected
copies left behind plus all remaining copies can still reach `repetition`.
This prevents a lexicographic improvement from destroying feasibility.

**Reserve enough output slots while pushing**

If the stack has room, always admit the current character when it equals
`letter`. A different character is admitted only when the number of open
output slots is strictly greater than the number of required `letter` copies
still missing. Otherwise, that slot must be reserved for a future required
copy.

Every pop replaces an earlier, larger character with a smaller feasible one,
so it improves the candidate without eliminating any valid completion. Every
skipped non-`letter` is either unnecessary for length or would occupy a slot
reserved by the repetition constraint. Because each decision preserves at
least one completion and greedily minimizes the earliest undecided position,
the final length-`k` stack is the lexicographically smallest valid
subsequence.

#### Complexity detail

Each of the $N$ characters is pushed at most once and popped at most once.
Counting remaining copies and joining the result are also linear, so the total
time is $O(N)$. The stack can contain up to `k` characters and therefore uses
$O(N)$ space in the worst case.

#### Alternatives and edge cases

- **Greedy suffix scan per position:** For each output slot, scan all possible
  next indices and select the smallest character that leaves a feasible
  suffix. This is correct but can take $O(Nk)$ time.
- **Dynamic programming:** States for source position, selected length, and
  required copies can recover the optimum but require prohibitive
  $O(Nk \cdot \text{repetition})$ work.
- When `repetition == k`, every selected character must equal `letter`.
- Extra copies of `letter` beyond the minimum are allowed and may be
  lexicographically beneficial.
- A selected required copy cannot be popped after too few copies remain in the
  suffix.
- Non-`letter` characters must be rejected once every open slot is needed for
  the repetition requirement.
- When `k == N`, the only subsequence is the entire source string.

</details>
