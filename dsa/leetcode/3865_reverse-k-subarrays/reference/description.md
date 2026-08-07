### 1. Description

You are given an integer array `nums` of length `n` and an integer `k`.

You must **partition** the array into `k` contiguous subarrays of **equal** length and **reverse** each subarray.

It is guaranteed that `n` is divisible by `k`.

Return the resulting array after performing the above operation.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of integers.
- `k`: The number of equal-length contiguous subarrays into which `nums` is partitioned.

Let $N=\lvert\texttt{nums}\rvert$ and $B=N/k$. The divisibility guarantee makes $B$ an integer. Block $b$, for $0 \le b < k$, consists of the original positions from $bB$ through $(b+1)B-1$, inclusive. Reversal changes order only within those boundaries.

**Return value**

Return the length-$N$ array formed by reversing each of the `k` blocks and concatenating the blocks from left to right.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,4,3,5,6], k = 3

**Output:** [2,1,3,4,6,5]

**Explanation:**

- The array is partitioned into $k = 3$ subarrays: `[1, 2]`, `[4, 3]`, and `[5, 6]`.

- After reversing each subarray: `[2, 1]`, `[3, 4]`, and `[6, 5]`.

- Combining them gives the final array `[2, 1, 3, 4, 6, 5]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [5,4,4,2], k = 1

**Output:** [2,4,4,5]

**Explanation:**

- The array is partitioned into $k = 1$ subarray: `[5, 4, 4, 2]`.

- Reversing it produces `[2, 4, 4, 5]`, which is the final array.

</div>

### 4. Constraints

- $1 \le n = \text{nums.length} \le 1000$

- $1 \le \text{nums}[i] \le 1000$

- $1 \le k \le n$

- `n` is divisible by `k`.