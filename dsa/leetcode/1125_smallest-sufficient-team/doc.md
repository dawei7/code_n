# Smallest Sufficient Team

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1125 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/smallest-sufficient-team/) |

## Problem Description

### Goal

A project has a list `req_skills` of required skills and a list `people`, where `people[i]` contains every required skill possessed by person `i`. A team is sufficient when, for each skill in `req_skills`, at least one selected person has that skill. Represent a team by the indices of its selected people; for example, `[0,1,3]` selects `people[0]`, `people[1]`, and `people[3]`.

Return any sufficient team having the smallest possible number of people. The indices may appear in any order, and more than one minimum team may be valid. Every person's listed skills belong to `req_skills`, skill names are unique within each relevant list, and a sufficient team is guaranteed to exist.

### Function Contract

**Inputs**

- `req_skills`: a list of $s$ distinct lowercase skill names, where $1 \le s \le 16$ and each name has length from $1$ through $16$.
- `people`: a list of $p$ people, where $1 \le p \le 60$; `people[i]` contains between $0$ and $16$ distinct names drawn from `req_skills`.

**Return value**

The indices of any smallest sufficient team, in any order.

### Examples

**Example 1**

- Input: `req_skills = ["java","nodejs","reactjs"]`, `people = [["java"],["nodejs"],["nodejs","reactjs"]]`
- Output: `[0,2]`

**Example 2**

- Input: `req_skills = ["algorithms","math","java","reactjs","csharp","aws"]`, `people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]`
- Output: `[1,2]`

### Required Complexity

- **Time:** $O(p2^s)$
- **Space:** $O(p2^s)$

<details>
<summary>Approach</summary>

#### General

**Encode coverage, not team order.** Assign each required skill one bit. Convert every person's skills into an $s$-bit mask, so bitwise OR gives the combined coverage of a team. The target is `full_mask = (1 << s) - 1`.

**Keep the smallest team for each coverage state.** Start with coverage `0` represented by the empty team. Process people one at a time. For every state that existed before considering person `i`, OR its coverage with that person's mask. If the new coverage has no recorded team, or adding `i` produces fewer selected people, replace the state. Iterating over a snapshot prevents one person from being selected repeatedly during the same update.

**Why dominated teams can be discarded.** Two teams with the same skill mask are interchangeable for every future person: any later mask adds exactly the same new coverage to both. Therefore only the smaller team can belong to an optimum. Inductively, after processing each prefix of `people`, every stored state has minimum size among teams drawn from that prefix. The state for `full_mask` at the end is consequently a globally smallest sufficient team.

The implementation stores a selected team as a $p$-bit integer. `team.bit_count()` gives its size, and the set bits are converted back to person indices only once for the final answer.

#### Complexity detail

There are at most $2^s$ coverage masks. Each of the $p$ people updates a snapshot of those states with constant-time mask operations, giving $O(p2^s)$ time under the bounded machine-word model used by the constraints. Up to $2^s$ team bitsets are stored, each containing up to $p$ bits, for $O(p2^s)$ bits of space.

#### Alternatives and edge cases

- **Enumerate subsets of people:** Testing all $2^p$ teams is correct but depends exponentially on as many as $60$ people instead of at most $16$ skills.
- **Backtracking with pruning:** Skill rarity and dominance pruning can work well on some inputs, but its worst case remains exponential in the number of people and is harder to bound.
- **Person with no skills:** Their mask is zero, so adding them never improves coverage or team size and they can be skipped.
- **Duplicate person masks:** Both indices may be considered, but the DP retains only a minimum-size representative for each resulting coverage.
- **One person covers every skill:** Processing that person creates the full mask with a one-person team, which is immediately optimal.
- **Multiple minimum teams:** The semantic contract accepts any sufficient team whose size is minimum; neither index order nor a particular tie-breaking choice is required.

</details>
