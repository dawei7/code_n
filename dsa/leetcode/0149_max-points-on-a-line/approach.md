## General

**Define a line by two distinct points**

All input coordinates are distinct, so any pair `points[i]` and `points[j]` determines exactly one straight line.

The selected source tries every pair with `i < j`. It starts `cnt = 2` for the two defining points, then checks later points `k > j` and adds one whenever the third point is collinear with the pair.

This is a direct enumeration approach. It avoids hash maps and avoids representing slopes as floating-point numbers.

**Derive the cross-product equality**

Let:

- the first point be $(x_1,y_1)$;
- the second be $(x_2,y_2)$;
- the candidate third point be $(x_3,y_3)$.

The slopes from the first point would be:

$$
\frac{y_2-y_1}{x_2-x_1}
\quad\text{and}\quad
\frac{y_3-y_1}{x_3-x_1}.
$$

Equal slopes indicate collinearity, but either denominator may be zero for a vertical line. Cross multiplication removes division:

$$
(y_2-y_1)(x_3-x_1)
=
(y_3-y_1)(x_2-x_1).
$$

The source stores the two products as `a` and `b` and tests `a == b`.

This formula naturally handles every orientation:

- vertical lines make both products zero in the corresponding way;
- horizontal lines make both vertical differences zero;
- negative slopes retain their signs;
- no special representation is needed for infinity.

Python integer multiplication is exact, so the comparison has no floating-point rounding risk.

**Why a Boolean can be added to the count**

In Python, `bool` is an integer subtype: `True` behaves like one and `False` like zero. Therefore:

`cnt += a == b`

increments exactly for a collinear third point.

Writing an explicit `if a == b: cnt += 1` would be equivalent and perhaps more obvious, but the compact expression is valid.

**Why checking only `k > j` still finds the maximum**

For one arbitrary pair, `cnt` may not count every point on its line. A collinear point whose index lies between `i` and `j` is omitted because the inner loop begins at `j + 1`.

That does not prevent finding the global maximum. Consider a line containing the maximum number of input points. Choose `i` as the smallest input index among points on that line, and choose `j` as the second-smallest such index. Every other point on the line then has index greater than `j`, so the `k` loop counts all of them.

Thus at least one enumerated pair counts the complete maximum line. Other pairs may undercount, but `ans = max(ans, cnt)` preserves the complete count once found.

No count can exceed the true number of points on its defining line, because only points satisfying the exact collinearity equation are added. The maximum recorded value is therefore exactly the answer.

**Small inputs and initialization**

`ans` begins at one. The constraints guarantee at least one point, and one point alone defines the minimum possible answer.

For one point, no pair loop runs and one is returned. For two points, their pair begins at two, no third-point check is needed, and two is returned.

For `[[1,1],[2,2],[3,3]]`, the pair of the first two points satisfies the cross-product equality with the third, raising `cnt` from two to three.

**Distinctness is part of the proof**

If two defining points were identical, they would not determine a unique line, and the cross-product equality would be true for every third point. The Reference explicitly guarantees unique points, so the source needs no duplicate handling.

The input arrays are read only.

## Complexity detail

Let $n$ be the number of points.

The code enumerates all pairs `(i, j)` and, for each pair, up to $O(n)$ later points. The number of triple checks is on the order of:

$$
\binom{n}{3}=O(n^3).
$$

Therefore, this exact source runs in $O(n^3)$ time, not the manifest’s $O(n^2)$.

It stores a fixed number of coordinates, products, counters, and indices. Auxiliary space is $O(1)$, which is tighter than the manifest’s $O(n)$ claim.

Python avoids multiplication overflow. In a fixed-width language, coordinate differences reach $2\cdot10^4$ and products reach $4\cdot10^8$, which still fit signed 32-bit arithmetic under these constraints, though wider types are a safer general habit.

## Alternatives and edge cases

- **Normalized rational slopes per anchor:** Divide `dy` and `dx` by their greatest common divisor and normalize signs, then count pairs in a map. It gives $O(n^2)$ time and $O(n)$ space with exact arithmetic.
- **Floating slopes per anchor:** Count `dy / dx` and use a special vertical key. It is concise but can be vulnerable to rounding outside tightly bounded domains.
- **Line equation keys:** Normalize coefficients in $Ax+By+C=0$. This can count global lines but requires careful common-factor and sign normalization.
- **One or two points:** Initialization and pair counting return one or two directly.
- **Vertical line:** Cross multiplication works without division by zero.
- **Negative coordinates:** Differences and exact products preserve the equation.
- **Duplicate points outside the contract:** A duplicate defining pair would make every third point appear collinear; this source relies on uniqueness.
- **Index-order undercount:** Individual later pairs may omit earlier collinear points, but the two smallest indices on a maximum line provide a complete witness pair.
- **Runtime dependency:** The source uses nested `List` annotations without importing the type. Standalone Python needs `from typing import List`.
- **Manifest mismatch:** Its actual tradeoff is cubic time with constant auxiliary storage.
