## Description

You are given an integer array `score` of size `n`, where $\text{score}[i]$ is the score of the $$i^{\text{th}}$$ athlete in a competition. All the scores are guaranteed to be **unique**.

The athletes are **placed** based on their scores, where the $1^st$ place athlete has the highest score, the $2^nd$ place athlete has the $2^nd$ highest score, and so on. The placement of each athlete determines their rank:

- The $1^st$ place athlete's rank is `"Gold Medal"`.

- The $2^nd$ place athlete's rank is `"Silver Medal"`.

- The $3^rd$ place athlete's rank is `"Bronze Medal"`.

- For the $4^th$ place to the $$n^{\text{th}}$$place athlete, their rank is their placement number (i.e., the$$x^{\text{th}}$$ place athlete's rank is `"x"`).

Return an array `answer` of size `n` where $\text{answer}[i]$ is the **rank** of the $$i^{\text{th}}$$ athlete.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $score = [5,4,3,2,1]$
- **Output:** `["Gold Medal","Silver Medal","Bronze Medal","4","5"]`
- **Explanation:** The placements are [1^st, 2^nd, 3^rd, 4^th, 5^th].
#### Example 2

- **Input:** $score = [10,3,8,9,4]$
- **Output:** `["Gold Medal","5","Bronze Medal","Silver Medal","4"]`
- **Explanation:** The placements are [1^st, 5^th, 3^rd, 2^nd, 4^th].
### Constraints

- $n = \text{score.length}$

- $1 \le n \le 10^{4}$

- $0 \le \text{score}[i] \le 10^{6}$

- All the values in `score` are **unique**.