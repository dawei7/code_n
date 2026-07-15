# Rank Teams by Votes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1366 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/rank-teams-by-votes/) |

## Problem Description

### Goal

Each string in `votes` is one ballot ranking the same set of teams from highest to lowest. Every team appears exactly once in every ballot, and uppercase letters identify the teams.

Rank the teams by comparing how many first-place votes they received. If two teams tie, compare their second-place counts, then third-place counts, and continue through every rank until they differ. If their complete count vectors are identical, the alphabetically smaller team comes first. Return all teams in final best-to-worst order.

### Function Contract

**Inputs**

- `votes`: $V$ equal-length ballot strings.
- Each ballot contains the same $T$ distinct uppercase team letters exactly once.

**Return value**

- One string containing all $T$ teams ordered by the positional vote rules and then alphabetical tie-breaking.

### Examples

**Example 1**

- Input: `votes = ["ABC","ACB","ABC","ACB","ACB"]`
- Output: `"ACB"`

**Example 2**

- Input: `votes = ["WXYZ","XYZW"]`
- Output: `"XWYZ"`

**Example 3**

- Input: `votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]`
- Output: `"ZMNAGUEDSJYLBOPHRQICWFXTVK"`

### Required Complexity

- **Time:** $O(VT+T^2\log T)$
- **Space:** $O(T^2)$

<details>
<summary>Approach</summary>

#### General

**Build one positional vector per team.** Initialize a length-$T$ counter vector for every team in the first ballot. Traverse each ballot; when a team appears at position $p$, increment that team's counter at $p$.

**Sort by the complete rule in one key.** A better team has a larger count at the earliest position where two vectors differ. Store counts negated, or negate them in the sort key, so ordinary ascending lexicographic comparison implements descending vote counts. Append the team letter to the key to make alphabetical order the final tie-breaker.

Lexicographic vector comparison examines rank positions in exactly the specified priority order. Therefore the first unequal count determines the same winner as the voting rule, and the appended letter resolves precisely the otherwise complete ties. Sorting all teams by these keys yields the required ranking.

#### Complexity detail

Counting visits all $VT$ ballot positions. Constructing $T$ keys of length $T$ uses $O(T^2)$ work, and comparison sorting may examine $T$ key entries in each of $O(T\log T)$ comparisons, for $O(T^2\log T)$ work. Total time is $O(VT+T^2\log T)$ and the rank vectors occupy $O(T^2)$ space.

#### Alternatives and edge cases

- **Custom comparator:** Compare rank vectors position by position and then letters. It is correct, but a key is simpler and avoids recomputing counts during comparisons.
- **Recount inside sorting:** Re-scan positional vote columns whenever two teams are compared. This preserves the rule but repeats substantial work.
- **Pairwise bubble sort:** Apply the same comparator to adjacent teams in $O(T^2)$ comparisons rather than $O(T\log T)$.
- **Complete count tie:** Alphabetical order applies only after every positional count is equal.
- **One ballot:** Its listed order is already the final ranking because every position has one unique vote.
- **One team:** Every ballot contains that team, so the result is the one-letter identifier.
- **Ballot order:** Reordering voters cannot affect any positional count.

</details>
