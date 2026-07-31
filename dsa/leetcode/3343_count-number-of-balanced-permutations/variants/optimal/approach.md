## General

Let $e=\lceil n/2\rceil$ and $o=\lfloor n/2\rfloor$ be the numbers of even- and odd-index positions. If the total digit sum is odd, two equal side sums are impossible. Otherwise, each side must sum to half the total; call that target $T$.

For a digit value $d$ occurring $c_d$ times, choose $k_d$ copies for even positions and leave $c_d-k_d$ copies for odd positions. A complete choice is feasible exactly when

$$
\sum_d k_d=e
\qquad\text{and}\qquad
\sum_d d k_d=T.
$$

Dynamic programming processes the ten digit values. State `(used_even, current_sum)` accumulates feasible allocations, and choosing $k_d$ adds `k_d` positions and $d k_d$ to the even-index sum.

Repeated copies must remain indistinguishable. For one allocation, the even positions can be filled in $e!/\prod_d k_d!$ ways and the odd positions in $o!/\prod_d(c_d-k_d)!$ ways. The transition therefore contributes the inverse-factorial weight

$$
\frac{1}{k_d!(c_d-k_d)!}.
$$

After all digits, multiplying state `(e, T)` by $e!o!$ produces exactly the number of distinct balanced permutations. Factorials and inverse factorials modulo $10^9+7$ make every division valid through Fermat's little theorem.

## Complexity detail

Let $T$ be half the total digit sum, so $T=O(n)$. The table contains $O(nT)$ states. Across the ten digit groups, the total number of possible multiplicity choices is $O(n)$, giving $O(n^2T)=O(n^3)$ time in the worst case. Two table layers use $O(nT)=O(n^2)$ auxiliary space.

The benchmark size is $n$. Its repeated full digit cycles keep the total sum even, create many feasible partial sums, and exercise duplicate corrections. The calibrated slower class performs the same correct transitions but recomputes factorial denominators inside every state transition, adding another factor of $n$.

## Alternatives and edge cases

- **Enumerate distinct permutations:** Direct generation grows factorially and is infeasible at length 80.
- **Treat copies as labeled:** Counting labeled digit occurrences overcounts every result by the factorials of its duplicate multiplicities.
- **Track both side sums:** Once the processed multiplicities and even sum are known, the odd sum is determined, so a second sum dimension is redundant.
- **Odd total sum:** No integer can equal half an odd total, so the answer is immediately zero.
- **Odd length:** Even indices contain one more slot; equality concerns digit sums, not slot counts.
- **Zero digits:** They do not change a sum but still consume positions and affect multiplicity denominators.
- **Modulo division:** Ordinary integer division is invalid after reduction; inverse factorials must be computed modulo the prime.
