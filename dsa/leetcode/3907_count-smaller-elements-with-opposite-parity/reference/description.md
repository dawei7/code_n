### 1. Description

You are given an integer array `nums` of length `n`.

The **score** of an index `i` is defined as the number of indices `j` such that:

- `i < j < n`

- $\text{nums}[j] < \text{nums}[i]$

- $\text{nums}[i]$ and $\text{nums}[j]$ have different parity (one is even and the other is odd).

Return an integer array `answer` of length `n`, where $\text{answer}[i]$ is the score of index `i`.

### 2. Function Contract

**Inputs**

- `nums`: A non-empty array of positive integers.

Let $n=\lvert\texttt{nums}\rvert$. Each score is based only on positions $j$ with $i<j<n$. Equal values never qualify because the comparison is strict, even if a later value were otherwise eligible. Parity is determined by divisibility by $2$.

**Return value**

Return an integer array `answer` of length $n$, where $\text{answer}[i]$ counts the indices $j$ to the right of $i$ for which $\text{nums}[j] < \text{nums}[i]$ and exactly one of $\text{nums}[i]$ and $\text{nums}[j]$ is even.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [5,2,4,1,3]

**Output:** [2,1,2,0,0]

**Explanation:**

- For $i = 0$, the elements $\text{nums}[1] = 2$ and $\text{nums}[2] = 4$ are smaller and have different parity.

- For $i = 1$, the element $\text{nums}[3] = 1$ is smaller and has different parity.

- For $i = 2$, the elements $\text{nums}[3] = 1$ and $\text{nums}[4] = 3$ are smaller and have different parity.

- No valid elements exist for the remaining indices.

Thus, the $answer = [2, 1, 2, 0, 0]$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,4,1]

**Output:** [1,1,0]

**Explanation:**​​​​​​​

For $i = 0$ and $i = 1$, the element $\text{nums}[2] = 1$ is smaller and has different parity. Thus, the $answer = [1, 1, 0]$.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [7]

**Output:** [0]

**Explanation:**

No elements exist to the right of index 0, so its score is 0. Thus, the $answer = [0]$.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$​​​​​​​