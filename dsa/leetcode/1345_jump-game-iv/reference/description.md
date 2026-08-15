### 1. Description

Given an array of integers `arr`, you are initially positioned at the first index of the array.

In one step you can jump from index `i` to index:

- $i + 1$ where: $i + 1 < \text{arr.length}$.

- $i - 1$ where: $i - 1 \ge 0$.

- `j` where: $\text{arr}[i] = \text{arr}[j]$ and $i \neq j$.

Return *the minimum number of steps* to reach the **last index** of the array.

Notice that you can not jump outside of the array at any time.

### 2. Function Contract

**Inputs**

- `arr`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `arr = [100,-23,-23,404,100,23,23,23,3,404]`
- **Output:** `3`
- **Explanation:** You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

#### Example 2

- **Input:** `arr = [7]`
- **Output:** `0`
- **Explanation:** Start index is the last index. You do not need to jump.

#### Example 3

- **Input:** `arr = [7,6,9,6,9,6,9,7]`
- **Output:** `1`
- **Explanation:** You can jump directly from index 0 to index 7 which is last index of the array.

### 4. Constraints

- $1 \le \text{arr.length} \le 5 * 10^{4}$

- $-10^{8} \le \text{arr}[i] \le 10^{8}$
