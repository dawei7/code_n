## Description

You are given an array `colors`, in which there are three colors: `1`, `2` and `3`.

You are also given some queries. Each query consists of two integers `i` and `c`, return the shortest distance between the given index `i` and the target color `c`. If there is no solution return `-1`.
### Function Contract

**Inputs**

- `colors`: A list of color values from the set `{1, 2, 3}`.
- `queries`: A list of pairs `[i, c]`, where `i` is a valid zero-based position in `colors` and `c` is one of the three color values.

Let $n = \lvert\texttt{colors}\rvert$ and $q = \lvert\texttt{queries}\rvert$. For a query `[i, c]`, the distance to a matching position $j$ is $\lvert i-j\rvert$.

**Return value**

- Return a list of $q$ integers in query order. For each `[i, c]`, return the minimum distance to a position `j` satisfying $\text{colors}[j] = c$, or `-1` when no such position exists.

### Examples

#### Example 1

- **Input:** $colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]$
- **Output:** `[3,0,3]`
- **Explanation:**
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
#### Example 2

- **Input:** $colors = [1,2], queries = [[0,3]]$
- **Output:** `[-1]`
- **Explanation:** There is no 3 in the array.
### Constraints

- $1 \le \text{colors.length} \le 5*10^{4}$

- $1 \le \text{colors}[i] \le 3$

- $1 \le \text{queries.length} \le 5*10^{4}$

- $\text{queries}[i].length = 2$

- $0 \le \text{queries}[i][0] < \text{colors.length}$

- $1 \le \text{queries}[i][1] \le 3$