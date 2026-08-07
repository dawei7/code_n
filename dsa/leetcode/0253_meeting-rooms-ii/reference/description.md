## Description

Given an array of meeting time intervals `intervals` where $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$, return *the minimum number of conference rooms required*.
### Function Contract

**Inputs**

- `intervals`: List of meeting intervals $List[\text{List}[int]]$.

**Return value**

Return integer minimum number of conference rooms required.

### Examples

#### Example 1

- **Input:** $intervals = [[0,30],[5,10],[15,20]]$
- **Output:** `2`
#### Example 2

- **Input:** $intervals = [[7,10],[2,4]]$
- **Output:** `1`
### Constraints

- $1 \le \text{intervals.length} \le 10^{4}$

- $0 \le \text{start}_{i} < \text{end}_{i} \le 10^{6}$