# Top Percentile Fraud

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3055 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/top-percentile-fraud/) |

## Problem Description

### Goal

An insurance fraud model assigns every policy a `fraud_score`, and policies
belong to states. Experienced adjusters should review the highest-scoring five
percent of claims independently within each state; one state's population and
scores must not affect another state's cutoff.

For a state containing $n$ policies, retain the first $\lceil 0.05n\rceil$
ranked positions after sorting scores from greatest to least. Policies tied at
the score occupying the final selected position share its rank and must all be
included. Return the original policy ID, state, and score, ordered by `state`
ascending, `fraud_score` descending, and `policy_id` ascending.

### Function Contract

**Inputs**

- `Fraud(policy_id, state, fraud_score)`: `policy_id` is unique; each row
  records a policy's state and predictive fraud score.

Let $n$ be the total row count and $n_s$ the row count of state $s$.

**Return value**

- An ordered table with columns `policy_id`, `state`, and `fraud_score`,
  containing each state's top five-percent ranked positions with boundary ties.

### Examples

**Example 1**

California, Florida, New York, and Texas each have fewer than twenty policies,
so each contributes its single highest-scoring policy. The result begins with
California policy `1`, followed by Florida policy `11` under state ordering.

**Example 2**

A state with exactly twenty policies contributes the one highest-scoring
position because $\lceil 20\cdot0.05\rceil=1$.

**Example 3**

A state with twenty-one policies contributes two ranked positions. If two
policies tie for the second-highest score, both are returned along with the
highest policy.
