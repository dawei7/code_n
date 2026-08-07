### 1. Description

Given an array of `intervals` where $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

### 2. Function Contract

**Inputs**

- `intervals`: Closed integer intervals represented by start-and-end pairs.

**Return value**

Return the merged, mutually non-overlapping intervals covering the complete input union.

### 3. Examples

#### Example 1

- **Input:** $intervals = [[1,3],[2,6],[8,10],[15,18]]$
- **Output:** `[[1,6],[8,10],[15,18]]`
- **Explanation:** Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#### Example 2

- **Input:** $intervals = [[1,4],[4,5]]$
- **Output:** `[[1,5]]`
- **Explanation:** Intervals [1,4] and [4,5] are considered overlapping.
#### Example 3

- **Input:** $intervals = [[4,7],[1,4]]$
- **Output:** `[[1,7]]`
- **Explanation:** Intervals [1,4] and [4,7] are considered overlapping.

### 4. Constraints

- $1 \le \text{intervals.length} \le 10^{4}$

- $\text{intervals}[i].length = 2$

- $0 \le \text{start}_{i} \le \text{end}_{i} \le 10^{4}$