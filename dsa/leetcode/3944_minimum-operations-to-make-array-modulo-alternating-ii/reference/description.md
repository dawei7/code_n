## Description

You are given an integer array `nums` and an integer `k`.

In one operation, you can **increase** or **decrease** any element of `nums` by 1.

An array is called **modulo alternating** if there exist two **distinct** integers `x` and `y` ($0 \le x, y < k$) such that:

- For every **even** index `i`, $\text{nums}[i] \% k = x$

- For every **odd** index `i`, $\text{nums}[i] \% k = y$

Return the **minimum** number of operations required to make `nums` **modulo alternating**.
### Function Contract

**Inputs**

- `nums`: A nonempty integer array. Indices are zero-based, so index `0` belongs to the even-index group.
- `k`: The modulus. Every selected target residue lies in `[0, k)`, and the even-index and odd-index target residues must be different.

Let $n = \lvert\texttt{nums}\rvert$. Increasing or decreasing one element by `1` costs one operation; any element may be changed repeatedly. Only each final value's remainder modulo `k` matters to the alternating condition.

**Return value**

Return the minimum total number of unit increment or decrement operations needed to make all even-index elements share one residue and all odd-index elements share a different residue.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,4,2,8], k = 3

**Output:** 2

**Explanation:**

- Let's choose $x = 1$ for even indices and $y = 2$ for odd indices.

- Perform the following operations:

		<li>Increment $\text{nums}[1] = 4$ by 1, giving `nums = [1, 5, 2, 8]`.

- Decrement $\text{nums}[2] = 2$ by 1, giving `nums = [1, 5, 1, 8]`.

	</li>
- Now, for even indices, $\text{nums}[i] \% k = 1$, and for odd indices, $\text{nums}[i] \% k = 2$.

- Thus, the total number of operations required is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,1,1], k = 3

**Output:** 1

**Explanation:**

- Incrementing $\text{nums}[1]$ by 1 gives `nums = [1, 2, 1]`, which satisfies the condition with $x = 1$ and $y = 2$.

- Thus, the total number of operations required is 1.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [6,7,8], k = 2

**Output:** 0

**Explanation:**

The array already satisfies the condition with $x = 0$ and $y = 1$. Thus, no operations are required.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $2 \le k \le 10^{5}$