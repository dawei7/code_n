## General

For a fixed target residue, the cost of changing one element depends only on its current residue modulo `k`. The source first counts residue frequencies separately for even and odd indices, then computes the total adjustment cost to every possible target residue in linear time around the residue circle.

Finally, it chooses one target for even indices and a different target for odd indices.

**Distance on the residue circle**

If an element has residue $r$ and needs residue $t$, changing the integer by one moves its residue one step around a cycle of length $k$. The direct gap is $\lvert r-t\rvert$; moving the other way around the cycle costs $k-\lvert r-t\rvert$. Therefore:

$$
\operatorname{dist}(r,t)
=\min\bigl(\lvert r-t\rvert,\ k-\lvert r-t\rvert\bigr).
$$

The quotient of the original value by $k$ is irrelevant. `group_frequencies[0][r]` counts even-index values with residue $r$, and `group_frequencies[1][r]` counts odd-index values with that residue.

For one parity group with frequency array $f$, define

$$
C(t)=\sum_{r=0}^{k-1} f[r]\operatorname{dist}(r,t).
$$

The helper `build_costs` computes $C(t)$ for every $t$ without spending $O(k)$ per target.

**Compute the cost for target zero directly**

For $t=0$, the circular distance from remainder $r$ is $\min(r,k-r)$. The source evaluates the defining sum once:

`costs[0] = sum(count * min(remainder, k - remainder) ...)`.

This costs $O(k)$ and gives a starting point for rotating the target from zero through all later residues.

**How cost changes when the target advances**

Let

$$
h=\left\lfloor\frac{k}{2}\right\rfloor.
$$

For a current target $t$, `nearer_clockwise` counts elements at residues

$$
t+1,t+2,\ldots,t+h\pmod k.
$$

When the target moves one step clockwise from $t$ to $t+1$, every element in this clockwise half becomes one step closer, decreasing total cost by one per occurrence. Most elements outside that half become one step farther, increasing cost by one per occurrence.

If `total` is the group size and $q$ elements are in the closer half, the basic change is

$$
(total-q)-q=total-2q.
$$

That is the source's update:

`current += total - 2 * nearer_clockwise`.

**The odd-modulus neutral residue**

When $k$ is even, the residue exactly opposite $t$ is included in the clockwise half. Moving the target one step makes that residue one step closer, so the basic formula is complete.

When $k$ is odd, one residue changes from distance $h$ on one side to distance $h$ on the other side. Its distance does not change at all. The basic formula classified it among the “farther by one” elements, so the source subtracts its frequency once:

`current -= frequencies[(target + half + 1) % k]`.

This changes its contribution from the incorrectly assumed $+1$ to the correct $0$.

After recording `costs[target + 1]`, the clockwise window slides one residue. It removes `target + 1`, which is now the target itself, and adds `target + half + 1` at the far end:

`nearer_clockwise += entering_frequency - leaving_frequency`.

Every frequency enters and leaves this rotating half a constant number of times, so all $k$ costs are produced in $O(k)$.

**Build parity costs independently**

Calling `build_costs` on the even frequency array produces `even_costs[x]`, the minimum operations needed to make every even-index element congruent to $x$.

Calling it on the odd array similarly produces `odd_costs[y]`. For a fixed ordered pair $(x,y)$, the two index groups are disjoint, so the total is simply:

$$
\texttt{even\_costs}[x]+\texttt{odd\_costs}[y].
$$

The only coupling is the condition $x\ne y$.

**Enforce distinct residues with two odd minima**

The source scans `odd_costs` and records:

- the smallest odd-group cost and one remainder achieving it;
- the second-smallest cost from a different remainder.

Equal costs are handled correctly. If a later remainder ties the best cost, it can become the second-best value, giving two distinct residues with the same minimum.

For each even target `remainder`:

- if it differs from `best_odd_remainder`, combine it with `best_odd`;
- if it equals that remainder, combine it with `second_best_odd`.

This selects the cheapest allowed odd target for every even target. Taking the minimum of these $k$ totals examines the best valid ordered pair without an $O(k^2)$ nested loop.

Because $k\ge2$, a second distinct odd remainder always exists. If one parity group is empty, all of its target costs are zero, and the same selection logic still enforces distinct residue labels at no element-adjustment cost.

**Why the final result is globally minimal**

For each target residue, `build_costs` sums the independent shortest circular adjustment for every element in that parity. Thus its entry is exactly the least cost for that group.

For each even target, the two-minimum rule picks the least-cost odd target among all different residues. Therefore the final generator considers the optimum associated with every possible even target. Its minimum is exactly the optimum over all valid distinct pairs.

## Complexity detail

Let $N$ be the array length and $K=k$.

Building both residue-frequency arrays takes $O(N)$ time. Each `build_costs` call performs a constant number of $O(K)$ scans, and there are two calls. Finding the two odd minima and combining even choices are also $O(K)$. Total time is $O(N+K)$.

The two frequency arrays and two cost arrays each have length $K$. All other state is scalar, so additional space is $O(K)$.

These bounds match the manifest and improve substantially over checking every one of the $K(K-1)$ residue pairs against all $N$ elements.

## Alternatives and edge cases

- **Enumerate every distinct residue pair and rescan the array:** This is the straightforward problem-I method but costs $O(NK^2)$, which is infeasible when both $N$ and $K$ reach $10^5$.
- **Precompute costs with a nested residue loop:** Computing every $C(t)$ directly from all frequency entries costs $O(K^2)$. The rotating recurrence reduces it to $O(K)$.
- **Use ordinary absolute difference:** Residues live on a cycle. Near zero and `k - 1`, wrapping can be much cheaper.
- **Choose the independently cheapest even and odd targets without checking equality:** If their residues match, the result violates the modulo-alternating definition.
- **Track only one odd minimum:** When the even target equals that odd remainder, a second distinct choice is necessary.
- **Tied odd minima:** The scan allows the second-best cost to equal the best cost as long as it comes from another remainder.
- **Odd `k`:** One residue is equally distant before and after a target step; the explicit correction prevents an off-by-one cost.
- **Even `k`:** The antipodal residue becomes closer in one direction, so no neutral correction is applied.
- **Single-element array:** The odd group is empty. Any odd target different from the chosen even target costs zero, and the existing even residue yields answer zero.
- **Already modulo alternating:** The matching distinct pair has zero in both cost arrays, so the result is zero.
- **Distance exactly `k / 2` for even `k`:** Both directions are equally short. The initial formula and recurrence count that distance correctly.
- **Large original values:** Only `value % k` enters the frequency arrays, avoiding dependence on magnitude.
- **Residue groups with no elements:** Their cost array is all zero, and two-minimum selection remains well-defined because $K\ge2$.
