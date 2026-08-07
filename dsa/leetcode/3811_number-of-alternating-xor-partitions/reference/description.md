## Description

You are given an integer array `nums` and two **distinct** integers `target1` and `target2`.

A **partition** of `nums` splits it into one or more **contiguous, non-empty** blocks that cover the entire array without overlap.

A partition is **valid** if the **bitwise XOR** of elements in its blocks **alternates** between `target1` and `target2`, starting with `target1`.

Formally, for blocks `b1`, `b2`, …:

- $XOR(b1) = target1$

- $XOR(b2) = target2$ (if it exists)

- $XOR(b3) = target1$, and so on.

Return the number of valid partitions of `nums`, modulo $10^{9} + 7$.

**Note:** A single block is valid if its **XOR** equals `target1`.
### Function Contract

**Inputs**

- `nums`: A non-empty integer array to be partitioned.
- `target1`: The required XOR of the first block and every subsequent odd-numbered block.
- `target2`: The distinct required XOR of every even-numbered block.

Let $N=\lvert\texttt{nums}\rvert$. Every chosen block must contain at least one array element, and the ordered blocks must cover indices $0$ through $N-1$ exactly once.

**Return value**

Return the number of complete partitions whose block XOR values follow `target1`, `target2`, `target1`, and so on. Reduce the count modulo $1{,}000{,}000{,}007$.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,3,1,4], target1 = 1, target2 = 5

**Output:** 1

**Explanation:**​​​​​​​

- The XOR of `[2, 3]` is 1, which matches `target1`.

- The XOR of the remaining block `[1, 4]` is 5, which matches `target2`.

- This is the only valid alternating partition, so the answer is 1.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,0,0], target1 = 1, target2 = 0

**Output:** 3

**Explanation:**

- **​​​​​​​**The XOR of `[1, 0, 0]` is 1, which matches `target1`.

- The XOR of `[1]` and `[0, 0]` are 1 and 0, matching `target1` and `target2`.

- The XOR of `[1, 0]` and `[0]` are 1 and 0, matching `target1` and `target2`.

- Thus, the answer is 3.​​​​​​​

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [7], target1 = 1, target2 = 7

**Output:** 0

**Explanation:**

- The XOR of `[7]` is 7, which does not match `target1`, so no valid partition exists.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i], target1, target2 \le 10^{5}$

- $target1 \neq target2$