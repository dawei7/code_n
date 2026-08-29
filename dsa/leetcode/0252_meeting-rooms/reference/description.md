### 1. Description

You are given an array of meeting times `intervals` where $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$.

A person can attend all meetings if no two meeting intervals overlap. Meetings ending at time `t` and starting at time `t` **do not** overlap.

Return `true` if a person can attend all meetings. Otherwise, return `false`.

### 2. Function Contract

**Inputs**

- `intervals`: List of meeting intervals $List[\text{List}[int]]$.

**Return value**

Return `true` if a person could attend all meetings without overlap, otherwise `false`.

### 3. Examples

#### Example 1

- **Input:** $intervals = [[0,30],[5,10],[15,20]]$
- **Output:** `false`

#### Example 2

- **Input:** $intervals = [[7,10],[2,4]]$
- **Output:** `true`

### 4. Constraints

- $0 \le \text{intervals.length} \le 10^{4}$

- $\text{intervals}[i].length = 2$

- $0 \le \text{start}_{i} < \text{end}_{i} \le 10^{6}$
