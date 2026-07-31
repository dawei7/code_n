## General

**Reduce each value to a circular residue distance.** Suppose a value currently has remainder $r$ and must reach target remainder $t$. Increasing can cover $(t-r)\bmod K$ unit steps, while decreasing can cover $(r-t)\bmod K$ steps. The cheapest valid change therefore costs

$$
d_K(r,t)=\min\bigl((t-r)\bmod K,(r-t)\bmod K\bigr)
=\min\bigl(\lvert r-t\rvert,K-\lvert r-t\rvert\bigr).
$$

For each of the $K$ possible target residues, independently sum this distance over the even-indexed elements and over the odd-indexed elements. This produces arrays `costs[0]` and `costs[1]`, where `costs[0][x] + costs[1][y]` is the exact operation count for the fixed pair $(x,y)$. Elements contribute independently once the pair is fixed, so no interaction or operation ordering can improve that sum.

**Enforce distinct targets with two odd-side minima.** Find the cheapest and second-cheapest entries of the odd-index cost array. For each possible even residue $x$, use the cheapest odd residue unless it equals $x$; in that one case use the second-cheapest residue. Because $K\ge2$, a second distinct choice always exists. Taking the minimum over every $x$ examines the best feasible partner for every even residue and therefore the best feasible pair overall.

This reasoning also covers a one-element array. Its odd-index group is empty, so every odd residue has zero cost; the second-minimum rule can always choose one that differs from the even residue.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$ and $K=k$. Each of the $N$ values contributes to all $K$ target costs, taking $O(NK)$ time. Finding the two odd-side minima and scanning the even-side choices take another $O(K)$ time, which is absorbed by $O(NK)$ because $N\ge1$. The two cost arrays use $O(K)$ auxiliary space.

For scaling evidence, define the workload variable

$$
S=NK.
$$

The three legal benchmark tiers keep $N=4$, set $K$ to 16, 40, and 100, and use $S=64$, $160$, and $400$. The accepted method is linear in $S$. A correct implementation that precomputes the same costs but then checks every distinct pair takes $O(NK+K^2)$ time. With fixed $N$, its quadratic pair-selection term grows one full exponent faster than the reference while remaining small enough to reach the complexity verdict safely.

## Alternatives and edge cases

- **Enumerate every residue pair directly:** Trying all $K(K-1)$ pairs and scanning all $N$ values for each is straightforward and correct, but costs $O(NK^2)$ time.
- **Precompute costs, then enumerate pairs:** Building the same two cost arrays and checking all distinct pairs takes $O(NK+K^2)$ time. Keeping the two cheapest odd residues removes the avoidable quadratic selection step.
- **Group equal remainders first:** Frequency arrays can replace the $N$ values with at most $K$ residue buckets. This gives $O(N+K^2)$ time, which is useful for a different relationship between $N$ and $K$ but does not dominate the direct $O(NK)$ accumulation throughout this bounded source domain.
- **Ordinary absolute difference only:** Using just $\lvert r-t\rvert$ misses cheaper changes across the residue boundary; residues zero and $K-1$ are one operation apart.
- **Distinctness is mandatory:** The individually cheapest even and odd residues cannot both be used when they are equal; the second-best fallback is essential.
- **Minimum array length:** With no odd-indexed element, all odd targets cost zero, but a residue distinct from the even target must still be selected.
- **Modulus two:** Exactly two residues exist, so choosing one parity's target determines the other parity's target.
