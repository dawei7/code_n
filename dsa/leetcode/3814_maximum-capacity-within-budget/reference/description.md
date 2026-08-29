### 1. Description

You are given two integer arrays `costs` and `capacity`, both of length `n`, where $\text{costs}[i]$ represents the purchase cost of the $i^{\text{th}}$ machine and $\text{capacity}[i]$ represents its performance capacity.

You are also given an integer `budget`.

You may select **at most two distinct** machines such that the **total cost** of the selected machines is **strictly less** than `budget`.

Return the **maximum** achievable total capacity of the selected machines.

### 2. Function Contract

**Inputs**

- `costs`: The purchase costs of the machines.
- `capacity`: The corresponding performance capacities; $\text{capacity}[i]$ belongs to the same machine as $\text{costs}[i]$.
- `budget`: The exclusive upper bound on the total purchase cost.

Let $N=\lvert\texttt{costs}\rvert=\lvert\texttt{capacity}\rvert$. A valid choice contains zero, one, or two different indices. For a two-machine choice `{i, j}`, validity requires $i\ne j$ and $\text{costs}[i] + \text{costs}[j] < budget$; equality with `budget` is not allowed.

**Return value**

Return the maximum sum of capacities among all valid choices. Return `0` if no individual machine costs strictly less than `budget`.

### 3. Examples

#### Example 1

- **Input:** costs = [4,8,5,3], capacity = [1,5,2,7], budget = 8

- **Output:** 8

- **Explanation:** 

- Choose two machines with $\text{costs}[0] = 4$ and $\text{costs}[3] = 3$.

- The total cost is $4 + 3 = 7$, which is strictly less than $budget = 8$.

- The maximum total capacity is $\text{capacity}[0] + \text{capacity}[3] = 1 + 7 = 8$.

#### Example 2

- **Input:** costs = [3,5,7,4], capacity = [2,4,3,6], budget = 7

- **Output:** 6

- **Explanation:** 

- Choose one machine with $\text{costs}[3] = 4$.

- The total cost is 4, which is strictly less than $budget = 7$.

- The maximum total capacity is $\text{capacity}[3] = 6$.

#### Example 3

- **Input:** costs = [2,2,2], capacity = [3,5,4], budget = 5

- **Output:** 9

- **Explanation:** 

- Choose two machines with $\text{costs}[1] = 2$ and $\text{costs}[2] = 2$.

- The total cost is $2 + 2 = 4$, which is strictly less than $budget = 5$.

- The maximum total capacity is $\text{capacity}[1] + \text{capacity}[2] = 5 + 4 = 9$.

### 4. Constraints

- $1 \le n = \text{costs.length} = \text{capacity.length} \le 10^{5}$

- $1 \le \text{costs}[i], \text{capacity}[i] \le 10^{5}$

- $1 \le budget \le 2 * 10^{5}$
