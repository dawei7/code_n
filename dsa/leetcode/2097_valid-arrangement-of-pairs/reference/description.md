### 1. Description

You are given a **0-indexed** 2D integer array `pairs` where $\text{pairs}[i] = [\text{start}_{i}, \text{end}_{i}]$. An arrangement of `pairs` is **valid** if for every index `i` where $1 \le i < \text{pairs.length}$, we have $\text{end}_{i}-1 = \text{start}_{i}$.

Return ***any** valid arrangement of *`pairs`.

### 2. Function Contract

**Inputs**

- `pairs`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `List[List[int]]`.

### 3. Note

The inputs will be generated such that there exists a valid arrangement of `pairs`.

### 4. Examples

#### Example 1

- **Input:** $pairs = [[5,1],[4,5],[11,9],[9,4]]$
- **Output:** `[[11,9],[9,4],[4,5],[5,1]]`
- **Explanation:** 
**This is a valid arrangement since end_i-1 always equals start_i.
end_0 = 9 == 9 = start_1
end_1 = 4 == 4 = start_2
end_2 = 5 == 5 = start_3

#### Example 2

- **Input:** $pairs = [[1,3],[3,2],[2,1]]$
- **Output:** `[[1,3],[3,2],[2,1]]`
- **Explanation:** This is a valid arrangement since end_i-1 always equals start_i.
end_0 = 3 == 3 = start_1
end_1 = 2 == 2 = start_2
The arrangements [[2,1],[1,3],[3,2]] and [[3,2],[2,1],[1,3]] are also valid.

#### Example 3

- **Input:** $pairs = [[1,2],[1,3],[2,1]]$
- **Output:** `[[1,2],[2,1],[1,3]]`
- **Explanation:** This is a valid arrangement since end_i-1 always equals start_i.
end_0 = 2 == 2 = start_1
end_1 = 1 == 1 = start_2

### 5. Constraints

- $1 \le \text{pairs.length} \le 10^{5}$

- $\text{pairs}[i].length = 2$

- $0 \le \text{start}_{i}, \text{end}_{i} \le 10^{9}$

- $\text{start}_{i} \neq \text{end}_{i}$

- No two pairs are exactly the same.

- There **exists** a valid arrangement of `pairs`.
