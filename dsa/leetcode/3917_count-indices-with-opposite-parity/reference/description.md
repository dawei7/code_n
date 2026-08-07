## Description

You are given an integer array `nums` of length `n`.

The **score** of an index `i` is defined as the number of indices `j` such that:

- `i < j < n`, and

- $\text{nums}[i]$ and $\text{nums}[j]$ have different parity (one is even and the other is odd).

Return an integer array `answer` of length `n`, where $\text{answer}[i]$ is the score of index `i`.
### Function Contract

**Inputs**

- `nums`: The non-empty integer array whose indices receive scores.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

Return a length-$n$ integer array. At each index `i`, store the number of indices strictly to its right whose values have parity different from $\text{nums}[i]$.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3,4]

**Output:** [2,1,1,0]

**Explanation:**

- $\text{nums}[0] = 1$, which is odd. Thus, the indices $j = 1$ and $j = 3$ satisfy the conditions, so the score of index 0 is 2.

- $\text{nums}[1] = 2$, which is even. Thus, the index $j = 2$ satisfies the conditions, so the score of index 1 is 1.

- $\text{nums}[2] = 3$, which is odd. Thus, the index $j = 3$ satisfies the conditions, so the score of index 2 is 1.

- $\text{nums}[3] = 4$, which is even. Thus, no index satisfies the conditions, so the score of index 3 is 0.

Thus, the $answer = [2, 1, 1, 0]$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1]

**Output:** [0]

**Explanation:**

There is only one element in `nums`. Thus, the score of index 0 is 0.

</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$