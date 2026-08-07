## Description

You are given an array of strings `names`, and an array `heights` that consists of **distinct** positive integers. Both arrays are of length `n`.

For each index `i`, $\text{names}[i]$ and $\text{heights}[i]$ denote the name and height of the $$i^{\text{th}}$$ person.

Return `names`* sorted in **descending** order by the people's heights*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $names = ["Mary","John","Emma"], heights = [180,165,170]$
- **Output:** `["Mary","Emma","John"]`
- **Explanation:** Mary is the tallest, followed by Emma and John.
#### Example 2

- **Input:** $names = ["Alice","Bob","Bob"], heights = [155,185,150]$
- **Output:** `["Bob","Alice","Bob"]`
- **Explanation:** The first Bob is the tallest, followed by Alice and the second Bob.
### Constraints

- $n = \text{names.length} = \text{heights.length}$

- $1 \le n \le 10^{3}$

- $1 \le \text{names}[i].length \le 20$

- $1 \le \text{heights}[i] \le 10^{5}$

- $\text{names}[i]$ consists of lower and upper case English letters.

- All the values of `heights` are distinct.