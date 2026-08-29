### 1. Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed and is protected by a security system with a color code.

You are given two integer arrays `nums` and `colors`, both of length `n`, where $\text{nums}[i]$ is the amount of money in the $i^{\text{th}}$ house and $\text{colors}[i]$ is the color code of that house.

You **cannot rob two adjacent** houses if they share the **same color** code.

Return the **maximum** amount of money you can rob.

### 2. Function Contract

**Inputs**

- `nums`: The money stored in the houses, in street order.
- `colors`: The corresponding security color code for every house.

Let $N=\lvert\texttt{nums}\rvert=\lvert\texttt{colors}\rvert$. A chosen index set $S\subseteq\{0,\ldots,N-1\}$ is valid exactly when

$$
i\in S \text{ and } i+1\in S
\quad\Longrightarrow\quad
\texttt{colors}[i]\ne\texttt{colors}[i+1].
$$

Thus, equality of color codes matters only for two consecutive selected indices that are also adjacent houses; the same color may occur at any distance elsewhere.

**Return value**

Return the maximum possible value of $\sum_{i\in S}\texttt{nums}[i]$ over all valid choices $S$.

### 3. Examples

#### Example 1

- **Input:** nums = [1,4,3,5], colors = [1,1,2,2]

- **Output:** 9

- **Explanation:** 

- Choose houses $i = 1$ with $\text{nums}[1] = 4$ and $i = 3$ with $\text{nums}[3] = 5$ because they are non-adjacent.

- Thus, the total amount robbed is $4 + 5 = 9$.

#### Example 2

- **Input:** nums = [3,1,2,4], colors = [2,3,2,2]

- **Output:** 8

- **Explanation:** 

- Choose houses $i = 0$ with $\text{nums}[0] = 3$, $i = 1$ with $\text{nums}[1] = 1$, and $i = 3$ with $\text{nums}[3] = 4$.

- This selection is valid because houses $i = 0$ and $i = 1$ have different colors, and house $i = 3$ is non-adjacent to $i = 1$.

- Thus, the total amount robbed is $3 + 1 + 4 = 8$.

#### Example 3

- **Input:** nums = [10,1,3,9], colors = [1,1,1,2]

- **Output:** 22

- **Explanation:** 

- Choose houses $i = 0$ with $\text{nums}[0] = 10$, $i = 2$ with $\text{nums}[2] = 3$, and $i = 3$ with $\text{nums}[3] = 9$.

- This selection is valid because houses $i = 0$ and $i = 2$ are non-adjacent, and houses $i = 2$ and $i = 3$ have different colors.

- Thus, the total amount robbed is $10 + 3 + 9 = 22$.

### 4. Constraints

- $1 \le n = \text{nums.length} = \text{colors.length} \le 10^{5}$

- $1 \le \text{nums}[i], \text{colors}[i] \le 10^{5}$
