### 1. Description

You are given an integer array `nums`.

You can perform the following operation any number of times:

- Choose two indices `a` and `b` such that $\text{nums}[a] \% \text{nums}[b] = 0$.

- Replace $\text{nums}[a]$ with $\text{nums}[b]$.

Return the **minimum** possible sum of the array after performing any number of operations.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.

Let $n = \texttt{nums.length}$, let $V = \max(\texttt{nums})$, and define $N = \max(n,V)$.

At any moment, position `a` may be assigned the current value at position `b` exactly when $\text{nums}[a] \% \text{nums}[b] = 0$. Operations are optional and may be repeated.

**Return value**

Return the minimum possible sum of all array elements. The result may exceed the range of a 32-bit signed integer.

### 3. Examples

#### Example 1

- **Input:** nums = [3,6,2]

- **Output:** 7

- **Explanation:** 

- Choose $a = 1$, $b = 2$, where $\text{nums}[a] = 6$ and $\text{nums}[b] = 2$. Since $6 \% 2 = 0$, replace $\text{nums}[1]$ with $\text{nums}[2]$.

- The array becomes `[3, 2, 2]`.

- No further operation reduces the sum. Thus, the final sum is $3 + 2 + 2 = 7$.

#### Example 2

- **Input:** nums = [4,2,8,3]

- **Output:** 9

- **Explanation:** 

- Choose $a = 0$, $b = 1$, where $\text{nums}[a] = 4$ and $\text{nums}[b] = 2$. Since $4 \% 2 = 0$, replace $\text{nums}[0]$ with $\text{nums}[1]$.

- Choose $a = 2$, $b = 1$, where $\text{nums}[a] = 8$ and $\text{nums}[b] = 2$. Since $8 \% 2 = 0$, replace $\text{nums}[2]$ with $\text{nums}[1]$.

- The array becomes `[2, 2, 2, 3]`.

- No further operation reduces the sum. Thus, the final sum is $2 + 2 + 2 + 3 = 9$.

#### Example 3

- **Input:** nums = [7,5,9]

- **Output:** 21

- **Explanation:** 

- There is no pair `(a, b)` such that $\text{nums}[a] \% \text{nums}[b] = 0$.

- Hence, no operation can be performed. The sum remains $7 + 5 + 9 = 21$.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^5$
