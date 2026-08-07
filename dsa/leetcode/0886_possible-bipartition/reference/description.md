## Description

We want to split a group of `n` people (labeled from `1` to `n`) into two groups of **any size**. Each person may dislike some other people, and they should not go into the same group.

Given the integer `n` and the array `dislikes` where $\text{dislikes}[i] = [a_{i}, b_{i}]$ indicates that the person labeled $a_{i}$ does not like the person labeled $b_{i}$, return `true` *if it is possible to split everyone into two groups in this way*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $n = 4, dislikes = [[1,2],[1,3],[2,4]]$
- **Output:** `true`
- **Explanation:** The first group has [1,4], and the second group has [2,3].
#### Example 2

- **Input:** $n = 3, dislikes = [[1,2],[1,3],[2,3]]$
- **Output:** `false`
- **Explanation:** We need at least 3 groups to divide them. We cannot put them in two groups.
### Constraints

- $1 \le n \le 2000$

- $0 \le \text{dislikes.length} \le 10^{4}$

- $\text{dislikes}[i].length = 2$

- $1 \le a_{i} < b_{i} \le n$

- All the pairs of `dislikes` are **unique**.