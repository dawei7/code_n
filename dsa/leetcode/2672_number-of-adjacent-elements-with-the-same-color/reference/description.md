### 1. Description

You are given an integer `n` representing an array `colors` of length `n` where all elements are set to 0's meaning **uncolored**. You are also given a 2D integer array `queries` where $\text{queries}[i] = [\text{index}_{i}, \text{color}_{i}]$. For the $$i^{\text{th}}$$ **query**:

- Set $colors[\text{index}_{i}]$ to $\text{color}_{i}$.

- Count the number of adjacent pairs in `colors` which have the same color (regardless of $\text{color}_{i}$).

Return an array `answer` of the same length as `queries` where $\text{answer}[i]$ is the answer to the $$i^{\text{th}}$$ query.

### 2. Function Contract

**Inputs**

- `n`: Input parameter (`int`).
- `queries`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]

- **Output:** [0,1,1,0,2]

- **Explanation:** 

- Initially array colors = [0,0,0,0], where 0 denotes uncolored elements of the array.

- After the 1^st query colors = [2,0,0,0]. The count of adjacent pairs with the same color is 0.

- After the 2^nd query colors = [2,2,0,0]. The count of adjacent pairs with the same color is 1.

- After the 3^rd query colors = [2,2,0,1]. The count of adjacent pairs with the same color is 1.

- After the 4^th query colors = [2,1,0,1]. The count of adjacent pairs with the same color is 0.

- After the 5^th query colors = [2,1,1,1]. The count of adjacent pairs with the same color is 2.

#### Example 2

- **Input:** n = 1, queries = [[0,100000]]

- **Output:** [0]

- **Explanation:** After the 1^st query colors = [100000]. The count of adjacent pairs with the same color is 0.

### 4. Constraints

- $1 \le n \le 10^{5}$

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i].length = 2$

- $0 \le \text{index}_{i} \le n - 1$

- $1 \le \text{color}_{i} \le 10^{5}$
