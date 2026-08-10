## General

**Describe a target by its deficits**

All operations only increase values, so any common target $T$ must satisfy

$$
T\ge M=\max(\texttt{nums}).
$$

For index $i$, define its deficit as $d_i=T-\texttt{nums}[i]$. Every unit of deficit must be supplied by an operation. Let

$$
D=\sum_i d_i=nT-S,
$$

where $S=\sum_i\texttt{nums}[i]$. Let

$$
L=\max_i d_i=T-m,
$$

where $m=\min(\texttt{nums})$. The largest deficit always belongs to a minimum element.

A single operation fills one deficit unit for `cost1`. A pair operation fills two units belonging to different indices for `cost2`.

**When pair operations are irrelevant**

If `cost2 >= 2 * cost1`, one pair operation costs at least as much as two single operations. Singles can reproduce its effect without restriction, so pairs never improve the answer.

For $n\le2$, raising the target above $M$ also cannot improve the cost. With two values, any paired increments above $M$ raise both sides together and do not eliminate the original gap; the smaller value's initial gap still needs singles. The cheapest target is $M$, where total deficit is `deficit_at_maximum = n * maximum - total`.

The early branch therefore returns

`deficit_at_maximum * cost1`

when either pairs are not cheaper than two singles or there are at most two elements.

**Maximum usable pairs for a fixed target**

Now assume $n\ge3$ and `cost2 < 2 * cost1`. We should use as many pair operations as possible.

Two independent limits apply:

1. Each pair consumes two of the $D$ units, so there can be at most $\lfloor D/2\rfloor$ pairs.
2. A pair cannot use the same index twice. If the largest-deficit index contributes one unit to a pair, the other unit must come from the remaining deficits, whose total is $D-L$. Thus there can be at most $D-L$ pairs when one index dominates.

Both limits are attainable by pairing deficit units from different indices, so

$$
P=\min\left(\left\lfloor\frac D2\right\rfloor,D-L\right).
$$

The remaining single units are

$$
R=D-2P.
$$

The nested `cost(target)` function implements exactly these formulas and returns

$$
P\cdot\texttt{cost2}+R\cdot\texttt{cost1}.
$$

**Why a target above the current maximum can help**

At $T=M$, one minimum element may have a much larger deficit than all other elements combined. Its excess cannot be paired with itself, so many expensive singles remain.

Increasing the common target by one adds one deficit unit to every index. It adds only one unit to the largest deficit but adds $n-1$ units across the other indices. For $n\ge3$, this can make the deficit distribution more balanced and convert formerly unavoidable singles into cheaper pairs. Eventually the largest deficit no longer dominates:

$$
L\le D-L.
$$

Substituting $L=T-m$ and $D=nT-S$ gives

$$
2(T-m)\le nT-S,
$$

or

$$
(n-2)T\ge S-2m.
$$

The smallest integer target satisfying this is

$$
B=\left\lceil\frac{S-2m}{n-2}\right\rceil.
$$

The code computes this ceiling as `(total - 2 * minimum + n - 3) // (n - 2)` and clamps it to at least `maximum`.

**Why only four targets need evaluation**

Below the balance boundary, the largest deficit dominates. Then $P=D-L$ and $R=2L-D$. Substituting the linear expressions for $D$ and $L$ makes the cost a linear function of $T$. A linear function on the integer interval from $M$ to the boundary reaches its minimum at an endpoint: either $M$ or immediately around $B$.

At and above the balance boundary, $P=\lfloor D/2\rfloor$ and $R=D\bmod2$. Increasing $T$ increases total deficit by $n$. Pair costs are positive, so the overall trend increases; only parity can make the first neighboring target slightly cheaper by replacing singles with pairs. Checking $B$ and $B+1$ covers both parities. Checking $B-1$ covers the final unbalanced integer and protects the exact transition caused by the ceiling.

Thus the set

`{maximum, max(maximum, balance - 1), balance, balance + 1}`

contains an optimal target. Duplicates are harmless because it is a set. The code computes exact integer costs, takes their minimum, and only then applies modulo $10^9+7$. Modulo must not be applied before minimization because residues do not preserve numeric ordering.

**Example of the deficit pairing**

For `nums = [2,3,3,3,5]` at target 5, deficits are `[3,2,2,2,0]`. Here $D=9$, $L=3$, so $P=\min(4,6)=4$ and $R=1$. Four pair operations and one single produce cost $4\cdot1+1\cdot2=6$, matching the example.

## Complexity detail

Let $n$ be the array length.

Computing the minimum, maximum, and sum performs three linear scans in the exact code. Their combined time is $O(n)$. Every later formula is constant time, and `cost` is evaluated for at most four targets. Total time is $O(n)$.

Only scalar integers and a set containing at most four target values are stored. Its size does not depend on $n$, so auxiliary space is $O(1)$.

Python uses arbitrary-precision integers, so intermediate products such as `n * target` and full costs do not overflow. Under the bounded problem inputs, conventional arithmetic is treated as constant time.

The final modulo affects only the representation of the required answer, not target selection. Exact costs must be compared first.

## Alternatives and edge cases

- **Try every target:** The optimum may lie above the maximum, and scanning an unbounded or large target range is unnecessary. The piecewise-linear analysis reduces it to four candidates.
- **Priority queue of deficits:** Repeatedly pair the two largest remaining deficits. It can realize the fixed-target pairing count but would be far slower than the closed formula and still needs target selection.
- **Use singles only:** This is optimal when `cost2 >= 2 * cost1`, but can be much more expensive when pairs are cheap.
- **Always target the maximum:** It fails when a dominant minimum deficit forces many singles and a slightly larger target creates enough other deficits for cheap pairing.
- **One element:** It is already equal to itself; `deficit_at_maximum` is zero and the result is zero.
- **Two elements:** Raising both toward a higher target cannot remove their original difference. Pair increments cover only equal extra growth, so the gap is optimally paid with singles at the current maximum.
- **All values already equal:** Deficit at the maximum is zero. Candidate evaluation also yields zero at that target.
- **Pair cost equal to two singles:** Pairing offers no benefit, so the early single-only branch is valid.
- **Dominant largest deficit:** Pair count is limited by $D-L$, because every pair using that index needs a unit from some other index.
- **Balanced deficits with odd total:** One single unit remains after $\lfloor D/2\rfloor$ pairs. This parity effect is why a neighbor of the balance target is checked.
- **Ceiling boundary:** Both `balance - 1` and `balance` are evaluated because the formula changes regimes at the first balanced integer.
- **Modulo timing:** Taking each candidate cost modulo before `min` could select a much larger true cost whose residue is small; the exact source correctly minimizes first.
- **Generated-source note:** The repository solution is marked AI-generated because its upstream source was unavailable. The mathematical derivation above validates the behavior of this exact implementation rather than relying on that provenance note.
