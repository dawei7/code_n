### 1. Description

You are given a **0-indexed** 2D integer array `items` of length `n` and an integer `k`.

$\text{items}[i] = [\text{profit}_{i}, \text{category}_{i}]$, where $\text{profit}_{i}$ and $\text{category}_{i}$ denote the profit and category of the $$i^{\text{th}}$$ item respectively.

Let's define the **elegance** of a **subsequence** of `items` as $\text{total}_{profit} + \text{distinct}_{categories}^2$, where $\text{total}_{profit}$ is the sum of all profits in the subsequence, and $\text{distinct}_{categories}$ is the number of **distinct** categories from all the categories in the selected subsequence.

Your task is to find the **maximum elegance** from all subsequences of size `k` in `items`.

Return *an integer denoting the maximum elegance of a subsequence of *`items`* with size exactly *`k`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order.

### 4. Examples

#### Example 1

- **Input:** $items = [[3,2],[5,1],[10,1]], k = 2$
- **Output:** `17`
- **Explanation:** In this example, we have to select a subsequence of size 2.
We can select items[0] = [3,2] and items[2] = [10,1].
The total profit in this subsequence is 3 + 10 = 13, and the subsequence contains 2 distinct categories [2,1].
Hence, the elegance is 13 + $2^{2}$ = 17, and we can show that it is the maximum achievable elegance.
#### Example 2

- **Input:** $items = [[3,1],[3,1],[2,2],[5,3]], k = 3$
- **Output:** `19`
- **Explanation:** In this example, we have to select a subsequence of size 3.
We can select items[0] = [3,1], items[2] = [2,2], and items[3] = [5,3].
The total profit in this subsequence is 3 + 2 + 5 = 10, and the subsequence contains 3 distinct categories [1,2,3].
Hence, the elegance is 10 + $3^{2}$ = 19, and we can show that it is the maximum achievable elegance.
#### Example 3

- **Input:** $items = [[1,1],[2,1],[3,1]], k = 3$
- **Output:** `7`
- **Explanation:** In this example, we have to select a subsequence of size 3.
We should select all the items.
The total profit will be 1 + 2 + 3 = 6, and the subsequence contains 1 distinct category [1].
Hence, the maximum elegance is 6 + $1^{2}$ = 7.

### 5. Constraints

- $1 \le \text{items.length} = n \le 10^{5}$

- $\text{items}[i].length = 2$

- $\text{items}[i][0] = \text{profit}_{i}$

- $\text{items}[i][1] = \text{category}_{i}$

- $1 \le \text{profit}_{i} \le 10^{9}$

- $1 \le \text{category}_{i} \le n$

- $1 \le k \le n$