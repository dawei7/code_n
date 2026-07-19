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
