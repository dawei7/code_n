## General

**Translate complete rows into a triangular-number inequality**

Row 1 needs one coin, row 2 needs two, and row $k$ needs $k$. Completing the first $k$ rows consumes

$$
1+2+\cdots+k=\frac{k(k+1)}{2}
$$

coins. Therefore $k$ rows are possible exactly when

$$
\frac{k(k+1)}{2}\le n.
$$

The answer is the greatest integer $k$ satisfying this inequality. Any leftover coins fewer than $k+1$ begin an incomplete next row and do not increase the answer.

**Solve the boundary equation**

First consider equality:

$$
k^2+k-2n=0.
$$

The quadratic formula gives roots

$$
k=\frac{-1\pm\sqrt{1+8n}}{2}.
$$

Only the positive root is relevant because a row count cannot be negative:

$$
r=\frac{\sqrt{1+8n}-1}{2}.
$$

The function $k(k+1)/2$ is strictly increasing for nonnegative $k$. All real values at or below $r$ satisfy the coin budget, and values above $r$ exceed it. Consequently, the greatest valid integer row count is $\lfloor r\rfloor$.

**Connect the code's expression to the standard root**

The exact solution returns

`int(math.sqrt(2) * math.sqrt(n + 0.125) - 0.5)`.

At first this may look different from the quadratic formula. Algebra shows they are identical:

$$
\sqrt{2}\sqrt{n+\frac18}
=\sqrt{2n+\frac14}
=\frac{\sqrt{8n+1}}{2}.
$$

Subtracting $1/2$ gives

$$
\frac{\sqrt{8n+1}-1}{2}=r.
$$

Thus the code computes the positive boundary root using a factored equivalent expression.

**Why `int` performs the required floor**

Python's `int` conversion truncates a positive floating-point value toward zero. Since $n\ge1$, the computed root is nonnegative, so truncation equals mathematical floor. The conversion therefore returns $\lfloor r\rfloor$.

For `n = 5`, the positive root is slightly above 2 but below 3. Flooring gives 2: rows needing 1 and 2 coins consume 3, while adding the third row would require 6 coins.

For `n = 8`, the root lies between 3 and 4. Three rows consume 6 coins; the two leftovers cannot complete the four-coin next row.

When `n` itself is triangular, such as `n = 6`, the root is exactly 3 and the conversion returns 3.

**Why flooring the root is correct**

Let $k=\lfloor r\rfloor$. Since $k\le r$ and the triangular-number expression increases with nonnegative input,

$$
\frac{k(k+1)}2\le n.
$$

So $k$ rows are achievable. The next integer satisfies $k+1>r$, which places it beyond the equality boundary, so

$$
\frac{(k+1)(k+2)}2>n.
$$

The next row cannot be completed. This proves $k$ is both feasible and maximal.

**Why the answer changes only at triangular numbers**

The staircase total after each completed row forms the sequence `1, 3, 6, 10, 15, ...`. Between two consecutive totals, adding another coin merely adds to the unfinished next row. For example, `n = 6`, `7`, `8`, and `9` all produce three complete rows; the answer becomes four only when `n` reaches `10`. The formula finds the interval containing `n` without visiting any earlier total. Inverting the increasing triangular-number function gives the real boundary `r`, and flooring selects the interval's lower row number. This perspective also explains why checking only whether the formula is close to an integer would be wrong: most inputs are not triangular numbers, yet each still has a well-defined greatest completed row.

**Floating-point considerations**

The implementation uses binary floating-point square roots. For the stated bound $n\le2^{31}-1$, the involved magnitudes are small enough for standard double-precision evaluation to provide the accepted integer result. An integer binary search avoids any dependence on rounding and is a robust alternative for much larger arbitrary-precision inputs.

The chosen expression performs no loop and does not construct the staircase; it extracts the boundary directly from the sum formula.

## Complexity detail

Under the standard machine-arithmetic model, a fixed number of additions, multiplications, square roots, and one conversion are performed. Time complexity is $O(1)$ and auxiliary space is $O(1)$.

In a bit-complexity model with unbounded integers, arithmetic cost depends on the number of bits in `n`. The manifest and customary interview analysis use the fixed-width model consistent with the 32-bit input constraint.

## Alternatives and edge cases

- **Binary search for the largest feasible `k`:** Search `0..n` using `k*(k+1)//2 <= n`. It takes $O(\log n)$ time, $O(1)$ space, and uses exact integer arithmetic.
- **Subtract row sizes iteratively:** Repeatedly subtract `1,2,3,...` until the next row does not fit. It is simple but takes $O(\sqrt n)$ iterations.
- **Use the direct formula `(sqrt(8*n+1)-1)/2`:** It is algebraically identical to the exact code and perhaps more recognizable.
- **Round instead of floor:** Rounding can select an incomplete next row. The maximal-feasible inequality specifically requires floor.
- **`n == 1`:** The root floors to one; the first row is complete.
- **Exact triangular number:** The root is an integer and all corresponding rows are complete with no remainder.
- **One less than a triangular number:** Flooring remains at the preceding complete row count.
- **Maximum input:** Constant-time arithmetic avoids a long simulation; Python also avoids integer overflow in intermediate expressions.
- **Floating precision beyond constraints:** For much larger values, prefer integer binary search or an integer square-root formula.
