### 1. Description

You are given an integer array `nums` and an integer `k`.

In one operation, you can **increase** or **decrease** any element of `nums` by 1.

An array is called **modulo alternating** if there exist two **distinct** integers `x` and `y` ($0 \le x, y < k$) such that:

- For every **even** index `i`, $\text{nums}[i] \% k = x$

- For every **odd** index `i`, $\text{nums}[i] \% k = y$

Return the **minimum** number of operations required to make `nums` **modulo alternating**.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty integer array whose elements may be increased or decreased by unit operations.
- `k`: The modulus that defines the allowed target residues.

Let $N=\lvert\texttt{nums}\rvert$ and $K=k$. A feasible result chooses residues $x,y\in\{0,\ldots,K-1\}$ with $x\ne y$. Every even-indexed element must become congruent to $x$ modulo $K$, and every odd-indexed element must become congruent to $y$ modulo $K$.

**Return value**

Return the minimum number of single-element increments and decrements required over all feasible distinct residue pairs.

### 3. Examples

#### Example 1

- **Input:** nums = [1,4,2,8], k = 3

- **Output:** 2

- **Explanation:** 

- Let's choose $x = 1$ for even indices and $y = 2$ for odd indices.

- Perform the following operations:

		- Increment $\text{nums}[1] = 4$ by 1, giving `nums = [1, 5, 2, 8]`.

- Decrement $\text{nums}[2] = 2$ by 1, giving `nums = [1, 5, 1, 8]`.

- Now, for even indices, $\text{nums}[i] \% k = 1$, and for odd indices, $\text{nums}[i] \% k = 2$.

- Thus, the total number of operations required is 2.

#### Example 2

- **Input:** nums = [1,1,1], k = 3

- **Output:** 1

- **Explanation:** 

- Incrementing $\text{nums}[1]$ by 1 gives `nums = [1, 2, 1]`, which satisfies the condition with $x = 1$ and $y = 2$.

- Thus, the total number of operations required is 1.

### 4. Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 10^{9}$

- $2 \le k \le 100$
