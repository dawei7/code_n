## General

**Two independent limits bound the container count.** An $n\times n$ deck has exactly

$$
n^2
$$

cells, and each cell can hold at most one container. Therefore, no loading plan can use more than $n^2$ containers.

Every container weighs exactly $w$. If $c$ containers are loaded, the weight constraint is

$$
cw\le maxWeight.
$$

Since $c$ must be an integer, this implies

$$
c\le\left\lfloor\frac{maxWeight}{w}\right\rfloor.
$$

The maximum feasible count is the smaller of these limits:

$$
\min\left(
n^2,
\left\lfloor\frac{maxWeight}{w}\right\rfloor
\right).
$$

There is no placement geometry beyond the number of cells. All cells and containers are interchangeable, so meeting both scalar limits is sufficient.

**Understand the source's algebraically equivalent expression.** The protected code returns

`min(n * n * w, maxWeight) // w`.

`n * n * w` is the total weight of filling every deck cell. Taking the minimum with `maxWeight` chooses the smaller total weight ceiling: either the full-deck weight or the ship's capacity.

Integer-dividing that chosen weight by `w` converts it back to a whole-container count.

To see the equivalence, let $C=n^2$. If $Cw\le maxWeight$, the minimum is $Cw$, and division returns $C$: every cell can be filled. If $Cw>maxWeight$, the minimum is `maxWeight`, and division returns $\lfloor maxWeight/w\rfloor$: weight is the limiting factor. These are exactly the two cases of the displayed minimum-count formula.

For $n=2,w=3,maxWeight=15$, the full-deck weight is $4\cdot3=12$. The source takes $\min(12,15)=12$ and divides by three, returning four.

For $n=3,w=5,maxWeight=20$, filling all nine cells would weigh $45$. The source takes $20$ and integer-divides by five, returning four containers.

**Why the upper bound is attainable.** If deck capacity is smaller, place one container in each of the chosen cells; their total weight $n^2w$ is within the ship limit by that case's condition. If weight capacity is smaller, the floor quotient gives a count whose weight is at most `maxWeight`, and the case condition ensures this count is below $n^2$, so enough cells exist. Thus the smaller upper bound is not only necessary but always feasible.

No search, simulation, sorting, or dynamic programming is required because containers have identical weight and cells have identical capacity.

It is useful to keep the units straight. `n * n` is measured in cells or containers, while `n * n * w` and `maxWeight` are both measured in weight. The source first compares quantities in the same weight unit, then divides by the per-container weight to return to a count. Comparing `n * n` directly with `maxWeight` would be dimensionally wrong: one side counts positions and the other measures weight.

The answer also cannot use a fraction of a container. If the limiting weight after `min` is $M$, exactly $\lfloor M/w\rfloor$ complete containers fit. The unused remainder $M\bmod w$ is strictly smaller than one container's weight. Because every cell accepts one whole container of exactly $w$, there is no way to combine that remainder with spare deck cells to improve the count.

Another algebraic verification starts from monotonicity. For nonnegative $A$ and positive $w$,

$$
\left\lfloor\frac{\min(Aw,M)}{w}\right\rfloor
=
\min\left(A,\left\lfloor\frac{M}{w}\right\rfloor\right).
$$

Setting $A=n^2$ and $M=maxWeight$ produces the direct count formula. This identity explains why taking `min` before floor division cannot introduce an off-by-one error.

**Integer division handles unused capacity correctly.** When `maxWeight` is not a multiple of $w$, the remainder cannot support another whole container. Floor division discards it. For example, capacity fourteen with weight three supports four containers weighing twelve, not five weighing fifteen.

The inputs are positive, so division by zero and negative-count behavior cannot occur.

## Complexity detail

The source performs a fixed number of integer multiplications, one comparison through `min`, and one integer division. Time complexity is $O(1)$ and auxiliary space is $O(1)$, matching the manifest.

Under the stated bounds, `n * n * w` is at most $1000^3=10^9$. It fits in a signed 32-bit range, while Python integers would remain safe even beyond that.

The method is asymptotically optimal because producing the scalar answer itself requires constant work and there is no input collection to inspect.

## Alternatives and edge cases

- **Simulate filling cells:** Repeating up to $n^2$ placements produces the same minimum but wastes $O(n^2)$ time.
- **Binary-search the number of containers:** Feasibility is monotone, but the exact quotient gives the boundary directly.
- **Use only `maxWeight // w`:** This can exceed the number of deck cells when the ship has large weight capacity.
- **Use only `n * n`:** This can violate the ship's weight limit.
- **Capacity not divisible by weight:** Floor division correctly leaves unusable remainder capacity.
- **Capacity below one container weight:** The result is zero even though the deck has cells.
- **Exactly full-deck weight:** Both limits agree and every cell is filled.
- **Capacity greater than full-deck weight:** Extra ship capacity cannot create more cells, so the deck limit wins.
- **One-cell deck:** The answer is one if capacity reaches $w$, otherwise zero.
- **Identical container weights:** This uniformity is why only the count matters; varying weights would require a selection problem.
- **Positive inputs:** They guarantee meaningful cell count, weight, and safe division.
- **Equivalent formula:** `min(n*n, maxWeight//w)` may look more direct, while the protected source takes the minimum in weight units before dividing.
