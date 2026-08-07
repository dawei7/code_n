### 1. Description

Given a binary array `data`, return the minimum number of swaps required to group all `1`’s present in the array together in **any place** in the array.

### 2. Function Contract

**Input**

- `data`: a binary array of length $n$.

Let $k$ be the number of `1` values in `data`. One swap exchanges the values stored at any two positions.

**Return value**

- The minimum number of swaps needed to make all $k$ ones occupy one contiguous block. Return `0` when no swap is necessary, including when $k \le 1$.

### 3. Examples

#### Example 1

- **Input:** $data = [1,0,1,0,1]$
- **Output:** `1`
- **Explanation:** There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
#### Example 2

- **Input:** $data = [0,0,0,1,0]$
- **Output:** `0`
- **Explanation:** Since there is only one 1 in the array, no swaps are needed.
#### Example 3

- **Input:** $data = [1,0,1,0,1,0,0,1,1,0,1]$
- **Output:** `3`
- **Explanation:** One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].

### 4. Constraints

- $1 \le \text{data.length} \le 10^{5}$

- $\text{data}[i]$ is either `0` or `1`.