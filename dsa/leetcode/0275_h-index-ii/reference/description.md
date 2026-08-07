## Description

Given an array of integers `citations` where $\text{citations}[i]$ is the number of citations a researcher received for their $$i^{\text{th}}$$ paper and `citations` is sorted in **non-descending order**, return *the researcher's h-index*.

According to the <a href="https://en.wikipedia.org/wiki/H-index" target="_blank">definition of h-index on Wikipedia</a>: The h-index is defined as the maximum value of `h` such that the given researcher has published at least `h` papers that have each been cited at least `h` times.

You must write an algorithm that runs in logarithmic time.
### Function Contract

**Inputs**

- `citations`: Non-negative paper citation counts sorted in non-decreasing order.

Let $n = \texttt{citations.length}$.

**Return value**

Return the greatest $h$ such that at least $h$ entries in `citations` are at least $h$.

### Examples
#### Example 1

- **Input:** $citations = [0,1,3,5,6]$
- **Output:** `3`
- **Explanation:** [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
#### Example 2

- **Input:** $citations = [1,2,100]$
- **Output:** `2`
### Constraints

- $n = \text{citations.length}$

- $1 \le n \le 10^{5}$

- $0 \le \text{citations}[i] \le 1000$

- `citations` is sorted in **ascending order**.