# Accepted Candidates From the Interviews

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2041 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/accepted-candidates-from-the-interviews/) |

## Problem Description

### Goal

The `Candidates` table stores each candidate's identifier, name, years of
experience, and interview identifier. The `Rounds` table stores the score for
each round belonging to an interview.

Report the identifier of every candidate who has at least two years of
experience and whose interview's round scores sum to strictly more than `15`.
Return one row per qualifying candidate; the problem permits any row order.

### Function Contract

Let $C$ be the number of candidate rows and $R$ the number of round rows.

**Input tables**

- `Candidates(candidate_id, name, years_of_exp, interview_id)`, with
  `candidate_id` as its primary key.
- `Rounds(interview_id, round_id, score)`, with
  `(interview_id, round_id)` as its composite primary key.

**Return value**

- A table with the single column `candidate_id`, containing candidates for whom
  `years_of_exp >= 2` and the sum of all matching `score` values is greater
  than `15`.

### Examples

**Example 1**

- Input: candidates `[(11, "Atticus", 1, 101), (9, "Ruben", 6, 104), (6, "Aliza", 10, 109), (8, "Alfredo", 0, 107)]`, with interview totals `16`, `22`, `10`, and `6`
- Output: `candidate_id = 9`
- Explanation: Candidate `9` satisfies both thresholds. Candidate `11` has
  enough score but not enough experience.

**Example 2**

- Input: one candidate with `years_of_exp = 2` and round scores `[8, 8]`
- Output: that candidate's identifier
- Explanation: Exactly two years is included, and the total `16` is above the
  score threshold.

**Example 3**

- Input: one experienced candidate with round scores `[7, 8]`
- Output: no rows
- Explanation: A total of exactly `15` is not strictly greater than `15`.
