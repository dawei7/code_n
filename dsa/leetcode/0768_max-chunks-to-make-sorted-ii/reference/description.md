### 1. Description

You are given an integer array `arr`.

We split `arr` into some number of **chunks** (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return *the largest number of chunks we can make to sort the array*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `arr = [5,4,3,2,1]`
- **Output:** `1`
- **Explanation:**
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
#### Example 2

- **Input:** `arr = [2,1,3,4,4]`
- **Output:** `4`
- **Explanation:**
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.

### 4. Constraints

- $1 \le \text{arr.length} \le 2000$

- $0 \le \text{arr}[i] \le 10^{8}$