# Count of Matches in Tournament

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1688 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-of-matches-in-tournament/) |

## Problem Description
### Goal

A single-elimination tournament begins with `n` teams. In a round with an even number of teams, every team is paired, half as many matches are played, and one winner from each match advances. In a round with an odd number, one team advances without playing while all other teams are paired; the winners and the team receiving the bye form the next round.

Rounds continue until only one team remains and becomes the champion. Return the total number of matches played across every round. A bye neither plays a match nor eliminates a team, and the identity of the team receiving it does not affect the requested count.

### Function Contract
**Inputs**

- `n`: the initial number of teams, with $1 \le n \le 200$

**Return value**

The total number of matches required to leave exactly one tournament winner.

### Examples
**Example 1**

- Input: `n = 7`
- Output: `6`

The three rounds play 3, 2, and 1 matches.

**Example 2**

- Input: `n = 14`
- Output: `13`

The rounds play 7, 3, 2, and 1 matches.

**Example 3**

- Input: `n = 1`
- Output: `0`

The sole team is already the winner, so no match is necessary.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Every played match has exactly one losing team, so each match reduces the number of teams still eligible to win by one. A bye advances a team without changing that count and therefore does not alter this elimination invariant.

The tournament starts with `n` eligible teams and finishes with one. Exactly $n-1$ teams must be eliminated, and no match eliminates more or fewer than one team. Consequently, exactly $n-1$ matches are necessary and sufficient under the stated round rules. Return that value directly without simulating how the teams are paired.

#### Complexity detail

One subtraction computes the answer, taking $O(1)$ time and $O(1)$ auxiliary space regardless of `n`.

#### Alternatives and edge cases

- **Round-by-round simulation:** add `teams // 2` matches and replace the team count by `(teams + 1) // 2` until one remains; this is correct but takes $O(\log n)$ iterations.
- **Eliminate one team per loop:** directly model each match by decrementing the team count; it exposes the invariant but takes $O(n)$ time.
- **Odd rounds:** the unpaired team creates no match and no elimination, so it does not change the total formula.
- **One team:** no elimination is needed, producing zero matches.
- **Power-of-two counts:** all teams pair in every round, but the same $n-1$ total still results.

</details>
