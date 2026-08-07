### 1. Description

You are given two 2D integer arrays, `items1` and `items2`, representing two sets of items. Each array `items` has the following properties:

- $\text{items}[i] = [\text{value}_{i}, \text{weight}_{i}]$ where $\text{value}_{i}$ represents the **value** and $\text{weight}_{i}$ represents the **weight **of the $$i^{\text{th}}$$ item.

- The value of each item in `items` is **unique**.

Return *a 2D integer array* `ret` *where* $\text{ret}[i] = [\text{value}_{i}, \text{weight}_{i}]$*,* *with* $\text{weight}_{i}$ *being the **sum of weights** of all items with value* $\text{value}_{i}$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

`ret` should be returned in **ascending** order by value.

### 4. Examples

#### Example 1

- **Input:** $items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]$
- **Output:** `[[1,6],[3,9],[4,5]]`
- **Explanation:**
The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 5, total weight = 1 + 5 = 6.
The item with value = 3 occurs in items1 with weight = 8 and in items2 with weight = 1, total weight = 8 + 1 = 9.
The item with value = 4 occurs in items1 with weight = 5, total weight = 5.
Therefore, we return [[1,6],[3,9],[4,5]].
#### Example 2

- **Input:** $items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]$
- **Output:** `[[1,4],[2,4],[3,4]]`
- **Explanation:**
The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 3, total weight = 1 + 3 = 4.
The item with value = 2 occurs in items1 with weight = 3 and in items2 with weight = 1, total weight = 3 + 1 = 4.
The item with value = 3 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4.
Therefore, we return [[1,4],[2,4],[3,4]].
#### Example 3

- **Input:** $items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]$
- **Output:** `[[1,7],[2,4],[7,1]]`
- **Explanation:**
**The item with value = 1 occurs in items1 with weight = 3 and in items2 with weight = 4, total weight = 3 + 4 = 7.
The item with value = 2 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4.
The item with value = 7 occurs in items2 with weight = 1, total weight = 1.
Therefore, we return [[1,7],[2,4],[7,1]].

### 5. Constraints

- $1 \le \text{items1.length}, \text{items2.length} \le 1000$

- $\text{items1}[i].length = \text{items2}[i].length = 2$

- $1 \le \text{value}_{i}, \text{weight}_{i} \le 1000$

- Each $\text{value}_{i}$ in `items1` is **unique**.

- Each $\text{value}_{i}$ in `items2` is **unique**.