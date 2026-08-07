## Description

In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

- The town judge trusts nobody.

- Everybody (except for the town judge) trusts the town judge.

- There is exactly one person that satisfies properties **1** and **2**.

You are given an array `trust` where $\text{trust}[i] = [a_{i}, b_{i}]$ representing that the person labeled $a_{i}$ trusts the person labeled $b_{i}$. If a trust relationship does not exist in `trust` array, then such a trust relationship does not exist.

Return *the label of the town judge if the town judge exists and can be identified, or return *`-1`* otherwise*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $n = 2, trust = [[1,2]]$
- **Output:** `2`
#### Example 2

- **Input:** $n = 3, trust = [[1,3],[2,3]]$
- **Output:** `3`
#### Example 3

- **Input:** $n = 3, trust = [[1,3],[2,3],[3,1]]$
- **Output:** `-1`
### Constraints

- $1 \le n \le 1000$

- $0 \le \text{trust.length} \le 10^{4}$

- $\text{trust}[i].length = 2$

- All the pairs of `trust` are **unique**.

- $a_{i} \neq b_{i}$

- $1 \le a_{i}, b_{i} \le n$