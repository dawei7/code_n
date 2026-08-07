## Description

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.
### Function Contract

**Inputs**

- `candidates`: A collection of positive integers that may contain repeated values.
- `target`: The required sum.

Let $n = \lvert\texttt{candidates}\rvert$.

**Return value**

Return all unique combinations that sum to `target`. Each input position may be used at most once.

### Examples
#### Example 1

- **Input:** $candidates = [10,1,2,7,6,1,5], target = 8$
- **Output:** ``
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
#### Example 2

- **Input:** $candidates = [2,5,2,1,2], target = 5$
- **Output:** ``
[
[1,2,2],
[5]
]
### Constraints

- $1 \le \text{candidates.length} \le 100$

- $1 \le \text{candidates}[i] \le 50$

- $1 \le target \le 30$