### 1. Description

You are given a ​​​​​​​circular integer array​​​​​​​ `nums` of length `n`.

An index `i` is a **peak** if its value is **strictly greater** than its neighbors:

- The **previous** neighbor of `i` is $nums[i - 1]$ if `i > 0`, otherwise $nums[n - 1]$.

- The **next** neighbor of `i` is $nums[i + 1]$ if $i < n - 1$, otherwise $\text{nums}[0]$.

You are allowed to perform the following operation **any** number of times:

- Choose any index `i` and **increase** $\text{nums}[i]$ by 1.

Return an integer denoting the **minimum** number of operations required to make the array contain **at least** `k` peaks. If it is impossible, return -1.

### 2. Function Contract

**Inputs**

- `nums`: A circular integer array of length $n$.
- `k`: The minimum number of peaks required in the final array.

Each operation increases one chosen array element by $1$. Values may become larger than their original constraint range after operations. Peak comparisons use the two circular neighbors and are strict.

**Return value**

Return the fewest unit increases that can produce at least `k` peaks, or $-1$ if the requested count is impossible.

### 3. Examples

#### Example 1

- **Input:** nums = [2,1,2], k = 1

- **Output:** 1

- **Explanation:** 

- To achieve at least $k = 1$ peak, we can increase $\text{nums}[2] = 2$ to 3.

- After this operation, $\text{nums}[2] = 3$ is strictly greater than its neighbors $\text{nums}[0] = 2$ and $\text{nums}[1] = 1$.

- Therefore, the minimum number of operations required is 1.

#### Example 2

- **Input:** nums = [4,5,3,6], k = 2

- **Output:** 0

- **Explanation:** 

- The array already contains at least $k = 2$ peaks with zero operations.

- Index 1: $\text{nums}[1] = 5$ is strictly greater than its neighbors $\text{nums}[0] = 4$ and $\text{nums}[2] = 3$.

- Index 3: $\text{nums}[3] = 6$ is strictly greater than its neighbors $\text{nums}[2] = 3$ and $\text{nums}[0] = 4$.

- Therefore, the minimum number of operations required is 0.

#### Example 3

- **Input:** nums = [3,7,3], k = 2

- **Output:** -1

- **Explanation:** It is impossible to have at least $k = 2$ peaks in this array. Therefore, the answer is -1.

### 4. Constraints

- $2 \le n = \text{nums.length} \le 5000$

- $-10^{5} \le \text{nums}[i] \le 10^{5}$

- $0 \le k \le n$​​​​​​​
