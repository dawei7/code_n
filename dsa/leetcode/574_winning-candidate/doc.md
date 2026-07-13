# Winning Candidate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 574 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/winning-candidate/) |

## Problem Description
### Goal
Given a `Candidate` table containing candidate identifiers and names and a `Vote` table containing ballots, determine which candidate received the greatest number of votes. Each vote's `CandidateId` identifies the candidate chosen by that ballot, so votes must be counted by candidate rather than by the ballot's own identifier.

Return the winner's name in a column named `Name`. The input guarantees that exactly one candidate has the highest vote count, so no tie-breaking rule or multiple-winner output is required.

### Function Contract
**Inputs**

- `Candidate(id, Name)`: the available candidates
- `Vote(id, CandidateId)`: ballots, each associated with the candidate that received the vote

**Return value**

- A one-row result grid with column `Name` containing the election winner
- The input guarantees a unique winner

### Examples
**Example 1**

- Input: candidates `A`, `B`, and `C` receive two, three, and one votes
- Output: `B`

**Example 2**

- Input: one candidate receives the only vote
- Output: that candidate's name

**Example 3**

- Input: a candidate listed first receives fewer votes than a later candidate
- Output: the later candidate's name

### Required Complexity

- **Time:** $O(V + C \log C)$
- **Space:** $O(C)$

<details>
<summary>Approach</summary>

#### General

**Count ballots by candidate**

Join each `Vote.CandidateId` to the matching `Candidate.id`. Grouping the joined rows by candidate turns every ballot for one candidate into a single count.

**Rank the aggregate counts**

Order the candidate groups by descending `COUNT(*)`. Because the contract guarantees one candidate has strictly more votes than every other candidate, the first group is unambiguous; `LIMIT 1` returns only its name.

**Why the returned candidate is the winner**

The join associates every vote with exactly its chosen candidate, and grouping neither loses nor duplicates joined ballots. Each aggregate count therefore equals that candidate's true vote total. Descending order places the unique maximum first, so the selected row is precisely the winner.

#### Complexity detail

With `V` votes and `C` candidates, the join and aggregation take $O(V + C)$ expected work with indexed or hashed identifiers. Ordering at most `C` aggregate rows takes $O(C \log C)$ time. The groups require $O(C)$ working space.

#### Alternatives and edge cases

- **Aggregate votes before joining:** count `Vote` rows by `CandidateId`, select the largest count, then join that one identifier to `Candidate`; this has the same asymptotic bounds.
- **Window rank over counts:** `RANK()` can express maximum selection, but it is more machinery than needed when the winner is guaranteed unique.
- **Correlated count per candidate:** produces the right answer but may rescan the full vote table for every candidate and take $O(CV)$ time.
- **Candidate row order:** does not indicate popularity; only aggregated vote counts decide the result.
- **Candidates with no votes:** create no joined group and cannot be the winner while at least one ballot exists.
- **Unique winner guarantee:** means no tie-breaking rule should be invented.
- **Capitalized `Name` column:** preserve the requested output label exactly.

</details>
