### 1. Description

You are given an array of non-overlapping intervals `intervals` where $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$ represent the start and the end of the $$i^{\text{th}}$$ interval and `intervals` is sorted in ascending order by $\text{start}_{i}$. You are also given an interval $newInterval = [start, end]$ that represents the start and end of another interval.

Two intervals are considered overlapping if they share **at least** one point.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by $\text{start}_{i}$ and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals`* after the insertion*.

### 2. Function Contract

**Inputs**

- `intervals`: Non-overlapping closed intervals sorted by ascending start value.
- `newInterval`: The closed interval to insert and merge as necessary.

**Return value**

Return the sorted, non-overlapping intervals after insertion.

### 3. Note

that you don't need to modify `intervals` in-place. You can make a new array and return it.

### 4. Examples

#### Example 1

- **Input:** $intervals = [[1,3],[6,9]], newInterval = [2,5]$
- **Output:** `[[1,5],[6,9]]`
#### Example 2

- **Input:** $intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]$
- **Output:** `[[1,2],[3,10],[12,16]]`
- **Explanation:** Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

### 5. Constraints

- $0 \le \text{intervals.length} \le 10^{4}$

- $\text{intervals}[i].length = 2$

- $0 \le \text{start}_{i} \le \text{end}_{i} \le 10^{5}$

- `intervals` is sorted by $\text{start}_{i}$ in **ascending** order.

- $\text{newInterval.length} = 2$

- $0 \le start \le end \le 10^{5}$