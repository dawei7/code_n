## General

Represent a distribution by ordered nonnegative integers $(x,y,z)$, one amount for each of the three children. We need

$$
x+y+z=n
\quad\text{and}\quad
x,y,z\le\texttt{limit}.
$$

Although this first version has small limits, the exact Optimal source uses a direct inclusion–exclusion formula rather than enumeration.

**Capacity check**

Together the children can receive at most $3\cdot\texttt{limit}$ candies. If $n$ is larger, the source returns zero immediately.

After this check succeeds, it is impossible for all three children to violate the limit at once. Such a triple violation would require at least $3(\texttt{limit}+1)$ candies, which is more than the allowed total range reaching the formula.

**Begin with every nonnegative distribution**

Without upper bounds, stars and bars gives

$$
\#\{(x,y,z)\mid x+y+z=n,\ x,y,z\ge0\}
=
\binom{n+2}{2}.
$$

The two selected separator positions divide $n$ identical candies into three labeled shares. The source stores this unrestricted count in `ans`.

**Remove one-child violations**

Suppose the first child receives at least `limit + 1`. Reserve that minimum excessive amount, then distribute the remaining $n-\texttt{limit}-1$ candies freely among all three children. The count is

$$
\binom{(n-\texttt{limit}-1)+2}{2}
=
\binom{n-\texttt{limit}+1}{2}.
$$

Any of the three children might be the excessive one, so subtract three times this number. The term is evaluated only for `n > limit`, precisely when a violation is possible.

**Correct double subtraction**

A distribution in which two children exceed the limit belongs to two of the bad sets and was subtracted twice. It should be excluded only once, so add it back once.

There are three pairs of children. Reserving `limit + 1` for both leaves `n - 2(limit + 1)` candies. Stars and bars gives

$$
\binom{n-2\texttt{limit}}{2}
$$

for each pair. The source adds three times this term when `n - 2 >= 2 * limit`, the integer form of $n\ge2(\texttt{limit}+1)$.

**Why the formula stops here**

General inclusion–exclusion would next subtract distributions where all three children exceed the limit. None can reach this point: the earlier capacity guard ensures $n\le3\texttt{limit}$, while a triple violation requires at least $3\texttt{limit}+3$ candies. Its count is zero, so omitting that term is exact.

Every unrestricted triple is now treated correctly. A valid triple belongs to no bad set and remains once. A triple with one excessive child is subtracted once. A triple with two excessive children is initially counted once, subtracted twice, then added once, leaving zero.

For $n=5$ and `limit=2`, the unrestricted count is $\binom72=21$. Single violations contribute $3\binom42=18$. Two children cannot both receive at least three because that would need six candies. The answer is $21-18=3$.

## Complexity detail

Only a fixed number of arithmetic expressions and `comb(..., 2)` calls are evaluated. Time complexity is $O(1)$ and auxiliary space is $O(1)$ in the standard unit-cost arithmetic model.

The result is exact rather than modular. Python's arbitrary-precision integers safely hold all counts in this version.

## Alternatives and edge cases

- **Enumerate $x$ and $y$:** Small version-I constraints permit it, but the inclusion–exclusion formula is both faster and the exact checked-in approach.
- **Enumerate only $x$:** Derive an interval for $y$ after fixing the first child. This takes $O(\min(n,\texttt{limit}))$ time.
- **Unordered partitions:** They would merge assignments to different children. The problem counts ordered triples because children are distinct.
- **$n > 3limit$:** Combined capacity is insufficient, so returning zero before calling combinations is necessary.
- **$n = 3limit$:** Every child must receive exactly `limit`, producing one distribution.
- **`limit >= n`:** The cap cannot be violated and the unrestricted stars-and-bars count is the answer.
- **Zero share:** A child may receive no candy; nonnegative stars and bars includes these cases.
- **Exact thresholds:** The single-overflow term starts at `n = limit + 1`, while the double-overflow term starts at `n = 2(limit + 1)`.
- **Combination guards:** Calling `comb` only when a bad set can exist avoids invalid arguments and documents the boundary logic.
- **Identical implementation across versions:** The small constraints do not change the mathematics; this source deliberately uses the same constant-time formula as the larger variants.
- **Why subtract exactly three times:** Each of the three labeled children defines one bad set of assignments exceeding the cap. Symmetry makes their individual sizes equal, but does not merge their identities.
- **Pair overlap coefficient:** There are $\binom32=3$ choices of two excessive children, explaining the coefficient on the add-back term.
- **Combination meaning at a boundary:** When the residual candy count is zero, `comb(2, 2) == 1` represents assigning zero residual candies to every child.
- **Formula versus example listing:** The computation counts distributions without constructing them, but every listed ordered triple corresponds to exactly one stars-and-bars separator placement.
- **Exact return value:** The source performs no modulo reduction because this version asks for the complete number of valid assignments.
