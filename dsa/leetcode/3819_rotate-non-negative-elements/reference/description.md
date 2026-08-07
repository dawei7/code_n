## Description

You are given an integer array `nums` and an integer `k`.

Rotate only the **non-negative** elements of the array to the **left** by `k` positions, in a cyclic manner.

All **negative** elements must stay in their original positions and must not move.

After rotation, place the **non-negative** elements back into the array in the new order, filling only the positions that originally contained **non-negative** values and **skipping all negative** positions.

Return the resulting array.
### Function Contract

**Inputs**

- `nums`: A non-empty array of integers.
- `k`: A non-negative number of left-rotation positions.

Let $N=\lvert\texttt{nums}\rvert$, and let $M$ be the number of elements in `nums` whose value is at least zero. Read those $M$ values from left to right as a separate sequence. When $M>0$, a rotation by `k` has the same effect as a rotation by `k % M`; when $M=0$, no position is movable and the array remains unchanged.

For every index holding a negative value in the input, the output must contain that same value at that same index. The rotated non-negative sequence fills the remaining indices from left to right.

**Return value**

Return the array produced by rotating and reinserting only the non-negative values.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,-2,3,-4], k = 3

**Output:** [3,-2,1,-4]

**Explanation:**​​​​​​​

- The non-negative elements, in order, are `[1, 3]`.

- Left rotation with $k = 3$ results in:

		<li>`[1, 3] -> [3, 1] -> [1, 3] -> [3, 1]`

	</li>
- Placing them back into the non-negative indices results in `[3, -2, 1, -4]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [-3,-2,7], k = 1

**Output:** [-3,-2,7]

**Explanation:**

- The non-negative elements, in order, are `[7]`.

- Left rotation with $k = 1$ results in `[7]`.

- Placing them back into the non-negative indices results in `[-3, -2, 7]`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [5,4,-9,6], k = 2

**Output:** [6,5,-9,4]

**Explanation:**

- The non-negative elements, in order, are `[5, 4, 6]`.

- Left rotation with $k = 2$ results in `[6, 5, 4]`.

- Placing them back into the non-negative indices results in `[6, 5, -9, 4]`.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{5} \le \text{nums}[i] \le 10^{5}$

- $0 \le k \le 10^{5}$