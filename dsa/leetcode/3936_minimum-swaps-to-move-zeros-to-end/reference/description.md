## Description

You are given an integer array `nums`.

In one operation, you can choose any two **distinct** indices `i` and `j` and swap $\text{nums}[i]$ and $\text{nums}[j]$.

Return an integer denoting the **minimum** number of operations required to move all 0s to the end of the array.
### Function Contract

**Inputs**

- `nums`: A nonempty integer array whose zero values must be moved into one suffix.

Let $N=\lvert\texttt{nums}\rvert$ and let $Z$ be the number of zeroes in `nums`. One operation exchanges $\text{nums}[i]$ and $\text{nums}[j]$ for any distinct indices $i$ and $j$; adjacent positions are not required. Only the zero-versus-nonzero distinction affects the answer.

**Return value**

Return the minimum number of allowed swaps needed to make the last $Z$ positions zero and the first $N-Z$ positions nonzero.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [0,1,0,3,12]

**Output:** 2

**Explanation:**

We perform the following swap operations:

- Swap $\text{nums}[0]$ and $\text{nums}[3]$, giving `nums = [3, 1, 0, 0, 12]`.

- Swap $\text{nums}[2]$ and $\text{nums}[4]$, giving `nums = [3, 1, 12, 0, 0]`.

Thus, the answer is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [0,1,0,2]

**Output:** 1

**Explanation:**

We perform the following swap operations:

- Swap $\text{nums}[0]$ and $\text{nums}[3]$, giving `nums = [2, 1, 0, 0]`.

Thus, the answer is 1.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,0]

**Output:** 0

**Explanation:**

The array already satisfies the condition. Therefore, no swap operations are needed.

</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $0 \le \text{nums}[i] \le 100$