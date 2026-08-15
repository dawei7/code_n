### 1. Description

You are given two integer arrays, `nums` and `forbidden`, each of length `n`.

You may perform the following operation any number of times (including zero):

- Choose two **distinct** indices `i` and `j`, and swap $\text{nums}[i]$ with $\text{nums}[j]$.

Return the **minimum** number of swaps required such that, for every index `i`, the value of $\text{nums}[i]$ is **not equal** to $\text{forbidden}[i]$. If no amount of swaps can ensure that every index avoids its forbidden value, return -1.

### 2. Function Contract

**Inputs**

- `nums`: The integer array whose elements may be swapped.
- `forbidden`: An equally long array specifying the disallowed value at each index.

Let $N=\lvert\texttt{nums}\rvert=\lvert\texttt{forbidden}\rvert$. A swap must use distinct indices and changes only the order of `nums`; it does not alter `forbidden` or the multiset of values in `nums`.

**Return value**

Return the fewest swaps that produce $\text{nums}[i] \neq \text{forbidden}[i]$ for every $0 \le i < N$. Return `-1` when no permutation of the available `nums` values can meet that condition.

### 3. Examples

#### Example 1

- **Input:** nums = [1,2,3], forbidden = [3,2,1]

- **Output:** 1

- **Explanation:** One optimal set of swaps:

- Select indices $i = 0$ and $j = 1$ in `nums` and swap them, resulting in `nums = [2, 1, 3]`.

- After this swap, for every index `i`, $\text{nums}[i]$ is not equal to $\text{forbidden}[i]$.

#### Example 2

- **Input:** nums = [4,6,6,5], forbidden = [4,6,5,5]

- **Output:** 2

- **Explanation:** One optimal set of swaps:

- Select indices $i = 0$ and $j = 2$ in `nums` and swap them, resulting in `nums = [6, 6, 4, 5]`.

- Select indices $i = 1$ and $j = 3$ in `nums` and swap them, resulting in `nums = [6, 5, 4, 6]`.

- After these swaps, for every index `i`, $\text{nums}[i]$ is not equal to $\text{forbidden}[i]$.

#### Example 3

- **Input:** nums = [7,7], forbidden = [8,7]

- **Output:** -1

- **Explanation:** It is not possible to make $\text{nums}[i]$ different from $\text{forbidden}[i]$ for all indices.

#### Example 4

- **Input:** nums = [1,2], forbidden = [2,1]

- **Output:** 0

- **Explanation:** No swaps are required because $\text{nums}[i]$ is already different from $\text{forbidden}[i]$ for all indices, so the answer is 0.

### 4. Constraints

- $1 \le n = \text{nums.length} = \text{forbidden.length} \le 10^{5}$

- $1 \le \text{nums}[i], \text{forbidden}[i] \le 10^{9}$
