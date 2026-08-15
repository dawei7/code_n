### 1. Description

There are `n` windows open numbered from `1` to `n`, we want to simulate using alt + tab to navigate between the windows.

You are given an array `windows` which contains the initial order of the windows (the first element is at the top and the last one is at the bottom).

You are also given an array `queries` where for each query, the window $\text{queries}[i]$ is brought to the top.

Return the final state of the array `windows`.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

- **Input:** windows = [1,2,3], queries = [3,3,2]

- **Output:** [2,3,1]

- **Explanation:** Here is the window array after each query:

- Initial order: `[1,2,3]`

- After the first query: `[<u>**3**</u>,1,2]`

- After the second query: `[<u>**3**</u>,1,2]`

- After the last query: `[<u>**2**</u>,3,1]`

#### Example 2

- **Input:** windows = [1,4,2,3], queries = [4,1,3]

- **Output:** [3,1,4,2]

- **Explanation:** Here is the window array after each query:

- Initial order: `[1,4,2,3]`

- After the first query: `[<u>**4**</u>,1,2,3]`

- After the second query: `[<u>**1**</u>,4,2,3]`

- After the last query: `[<u>**3**</u>,1,4,2]`

### 4. Constraints

- $1 \le n = \text{windows.length} \le 10^{5}$

- `windows` is a permutation of `[1, n]`.

- $1 \le \text{queries.length} \le 10^{5}$

- $1 \le \text{queries}[i] \le n$
