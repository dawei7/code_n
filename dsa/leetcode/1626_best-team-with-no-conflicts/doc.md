# Best Team With No Conflicts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1626 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/best-team-with-no-conflicts/) |

## Problem Description
### Goal
Choose players for a basketball tournament so that their total score is as large as possible. Player `i` has score `scores[i]` and age `ages[i]`, and any subset of the available players may form the team.

The selected team must contain no conflict: a younger selected player may not have a strictly higher score than an older selected player. Players of the same age never conflict with one another, regardless of their scores. Return the maximum sum of scores among all conflict-free teams.

### Function Contract
**Inputs**

- `scores`: an integer array of length $n$, where $1 \le n \le 1000$ and $1 \le \texttt{scores[i]} \le 10^6$.
- `ages`: an integer array of the same length, where $1 \le \texttt{ages[i]} \le 1000$.
- Entries at the same index describe the same player.

**Return value**

Return the greatest possible sum of selected player scores subject to the no-conflict rule.

### Examples
**Example 1**

- Input: `scores = [1,3,5,10,15], ages = [1,2,3,4,5]`
- Output: `34`

Every player can be selected because scores rise with ages.

**Example 2**

- Input: `scores = [4,5,6,5], ages = [2,1,2,1]`
- Output: `16`

The two players of age 1 with score 5 and the age-2 player with score 6 form an optimal team.

**Example 3**

- Input: `scores = [1,2,3,5], ages = [8,9,10,1]`
- Output: `6`

Choosing the three older players avoids the conflict created by the younger score-5 player.

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Turn conflicts into an ordering condition.** Sort players by `(age, score)`. Ages are then non-decreasing. Within one age, sorting scores in non-decreasing order permits every equal-age player to follow another; this is necessary because equal ages never conflict. Across different ages, a conflict-free selected sequence must also have non-decreasing scores. The problem therefore becomes finding a maximum-weight non-decreasing subsequence of scores, where each selected score is its own weight.

**Query the best compatible prefix.** Coordinate-compress the distinct score values. Maintain a Fenwick tree whose prefix maximum through rank `r` is the greatest total of any processed team ending with a score at most the score of rank `r`. For the current player with score `x`, query through `rank(x)`, add `x`, and update that rank with the resulting team total.

**Why immediate updates handle equal ages.** Equal-age players are processed in ascending score order. An update from one such player can therefore contribute to a later player of the same age, including all of them in a team. This never introduces a conflict because the rule explicitly exempts equal ages. For a strictly older player, the prefix query admits only earlier team endings whose scores are no greater, exactly enforcing the remaining conflict condition.

Every team represented by a tree value is conflict-free by construction. Conversely, sort any conflict-free team by age and score. Its scores are non-decreasing, so each player extends the prefix state containing all earlier team members. Inductively, the dynamic program considers a total at least as large as that team's score. The maximum tree update is therefore the optimum.

#### Complexity detail

Sorting the $n$ players and compressing scores take $O(n\log n)$ time. Each player performs one Fenwick prefix query and one point update in $O(\log n)$ time, so total time is $O(n\log n)$. The sorted players, compressed ranks, and tree use $O(n)$ space.

#### Alternatives and edge cases

- **Quadratic dynamic programming:** Let `dp[i]` be the best total ending at sorted player `i` and scan every compatible predecessor. This is simpler and takes $O(n^2)$ time and $O(n)$ space.
- **Segment tree:** Range-maximum queries and point updates give the same $O(n\log n)$ bound but use a larger and more involved data structure.
- **Sort by score first:** Sorting by `(score, age)` and building a non-decreasing age sequence is symmetric, but tie ordering must still preserve the equal-score and equal-age exemptions.
- Players of the same age may all be selected even when their scores differ sharply.
- Players with equal scores never form a strict score inversion and can coexist across ages.
- Input order is irrelevant; `scores[i]` and `ages[i]` must remain paired during sorting.
- Since every score is positive, an optimal team is nonempty.

</details>
