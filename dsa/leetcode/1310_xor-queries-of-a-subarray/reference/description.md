### 1. Description

You are given an array `arr` of positive integers. You are also given the array `queries` where $\text{queries}[i] = [\text{left}_{i}, \text{right}_{i}]$.

For each query `i` compute the **XOR** of elements from $\text{left}_{i}$ to $\text{right}_{i}$ (that is, $arr[\text{left}_{i}] XOR arr[\text{left}_{i} + 1] XOR ... XOR arr[\text{right}_{i}]$ ).

Return an array `answer` where $\text{answer}[i]$ is the answer to the $$i^{\text{th}}$$ query.

### 2. Function Contract

**Inputs**

- `arr`: Input parameter (`List[int]`).
- `queries`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** `arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]`
- **Output:** `[2,7,14,8]`
- **Explanation:** The binary representation of the elements in the array are:
1 = 0001
3 = 0011
4 = 0100
8 = 1000
The XOR values for queries are:
[0,1] = 1 xor 3 = 2
[1,2] = 3 xor 4 = 7
[0,3] = 1 xor 3 xor 4 xor 8 = 14
[3,3] = 8

#### Example 2

- **Input:** `arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]`
- **Output:** `[8,0,4,4]`

### 4. Constraints

- $1 \le \text{arr.length}, \text{queries.length} \le 3 * 10^{4}$

- $1 \le \text{arr}[i] \le 10^{9}$

- $\text{queries}[i].length = 2$

- $0 \le \text{left}_{i} \le \text{right}_{i} < \text{arr.length}$
