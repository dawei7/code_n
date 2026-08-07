### 1. Description

You are given an integer array `nums` of length `n`, where `nums` is a permutation of the integers in the range `[0, n - 1]`.

You are also given an integer array `pre`, where each $\text{pre}[i]$ is a valid prefix length.

In one operation, you may choose any length `x` from `pre` and reverse the first `x` elements of `nums`.

For example, applying a prefix reversal of length `3` on `[4, 1, 2, 3]` results in `[2, 1, 4, 3]`.

Return the minimum number of operations required to sort `nums` in ascending order. If it is impossible to sort `nums`, return `-1`.

### 2. Function Contract

**Inputs**

- `nums`: A permutation of the integers from $0$ through $n-1$.
- `pre`: The distinct prefix lengths that may be reversed.

Let $n = \lvert\texttt{nums}\rvert$, $q = \lvert\texttt{pre}\rvert$, and $P=n!$, the maximum number of permutation states.

Each operation chooses one value `x` from `pre` and replaces the prefix `nums[:x]` with its reverse. An allowed length may be used more than once. The operation is conceptual; the function only has to return the distance to the target permutation.

**Return value**

Return the fewest operations that transform `nums` into `[0, 1, ..., n - 1]`. Return `-1` if the target is unreachable.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,0,1], pre = [2,3]

**Output:** 2

**Explanation:**

- Reverse $\text{pre}[1] = 3$ elements to get `nums = [1, 0, 2]`.

- Then reverse $\text{pre}[0] = 2$ elements to get `nums = [0, 1, 2]`.

- Thus, the minimum number of prefix reversal required is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,0,2], pre = [1,3]

**Output:** -1

**Explanation:**

It is impossible to sort the array using the given prefix lengths, so the answer is -1.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [0,1], pre = [2]

**Output:** 0

**Explanation:**

Since `nums` is already sorted, no prefix reversals are needed. Thus, the answer is 0.

</div>

### 4. Constraints

- $1 \le n = \text{nums.length} \le 8$

- $0 \le \text{nums}[i] \le n - 1$

- $1 \le \text{pre.length} \le n$

- $1 \le \text{pre}[i] \le n$

- `​​​​​​​nums` is a permutation of integers from 0 to $n - 1$.

- `pre` consists of **unique** integers.