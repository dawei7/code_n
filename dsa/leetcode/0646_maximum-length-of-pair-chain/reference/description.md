### 1. Description

You are given an array of `n` pairs `pairs` where $\text{pairs}[i] = [\text{left}_{i}, \text{right}_{i}]$ and $\text{left}_{i} < \text{right}_{i}$.

A pair $p2 = [c, d]$ **follows** a pair $p1 = [a, b]$ if `b < c`. A **chain** of pairs can be formed in this fashion.

Return *the length longest chain which can be formed*.

You do not need to use up all the given intervals. You can select pairs in any order.

### 2. Function Contract

**Inputs**

- `pairs`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $pairs = [[1,2],[2,3],[3,4]]$
- **Output:** `2`
- **Explanation:** The longest chain is [1,2] -> [3,4].

#### Example 2

- **Input:** $pairs = [[1,2],[7,8],[4,5]]$
- **Output:** `3`
- **Explanation:** The longest chain is [1,2] -> [4,5] -> [7,8].

### 4. Constraints

- $n = \text{pairs.length}$

- $1 \le n \le 1000$

- $-1000 \le \text{left}_{i} < \text{right}_{i} \le 1000$
