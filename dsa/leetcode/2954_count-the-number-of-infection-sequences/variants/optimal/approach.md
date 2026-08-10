## General

Initially sick people divide the healthy positions into independent gaps. The source constructs gap lengths with

`pairwise([-1] + sick + [n])`

and `b - a - 1`:

- the first gap lies before the first sick position;
- internal gaps lie between consecutive sick positions;
- the final gap lies after the last sick position.

Let these lengths be $g_0,g_1,\ldots,g_t$, and let

$$
S=\sum g_i=n-|\texttt{sick}|
$$

be the number of people who will become infected during the sequence.

The counting has two layers: possible order inside each gap and possible interleaving between different gaps.

**Orders inside an exterior gap**

In the leading gap, infection begins from its right boundary, next to the first initially sick person. People must become infected from right to left in one forced order.

The trailing gap is symmetric: infection progresses from left to right from the last initially sick person. Each exterior gap therefore has exactly one internal order, regardless of length.

**Orders inside an internal gap**

An internal gap has infected people on both ends. At any stage, the next infected person in that gap can be the leftmost remaining healthy position or the rightmost remaining healthy position.

For a gap of length $x$:

- during the first $x-1$ infections, choose left or right independently;
- after those choices, only one person remains, so the final infection is forced.

This gives

$$
2^{x-1}
$$

orders when $x>0$. For $x=1$, this is one. The source multiplies `pow(2, x - 1, mod)` only when `x > 1` because factors of one need no work.

Different left/right choice sequences produce different infection orders, and every legal order must repeatedly choose one of those two frontiers, so the count is exact.

**Interleave the gaps**

Fix one legal internal order for every gap. Infections belonging to different gaps do not constrain each other: at any moment, each nonempty gap's next frontier person is adjacent to an infected person within that gap.

We may therefore merge the gap-specific sequences while preserving order inside each gap. The number of such interleavings is the multinomial coefficient

$$
\binom{S}{g_0,g_1,\ldots,g_t}
=
\frac{S!}{\prod_i g_i!}.
$$

The source starts with `fac[S]` and multiplies by the modular inverse of `fac[x]` for every positive gap length $x$.

**Modular division**

The modulus $10^9+7$ is prime. For nonzero `fac[x]` modulo the prime, Fermat's little theorem gives

$$
(\texttt{fac}[x])^{-1}
\equiv
(\texttt{fac}[x])^{\texttt{mod}-2}
\pmod{\texttt{mod}}.
$$

`pow(fac[x], mod - 2, mod)` computes this inverse by fast modular exponentiation.

Factorials through $10^5$ are precomputed once at module load. Since $S\le n\le10^5$, every required factorial is available.

**Combine both layers**

The multinomial factor chooses where infections from each gap appear in the global sequence. Multiplying by $2^{x-1}$ for each internal gap chooses that gap's own valid order. These decisions are independent, so multiplication counts every global infection sequence exactly once.

Exterior gaps are excluded from the powers-of-two loop because they have only one frontier and one order.

For $n=5$ and `sick=[0,4]`, gaps are $0,3,0$. The multinomial factor is one and the internal factor is $2^{2}=4$, matching the four valid orders.

## Complexity detail

Module initialization computes `fac[0..100000]` in $O(100000)$ time and space once, independent of an individual call.

For one call with $G=|\texttt{sick}|+1$ gaps, list construction and summation are $O(G)$. The exact source performs modular exponentiation for each nonzero gap and internal gap, costing $O(G\log\texttt{mod})$ bit-steps. With the fixed modulus treated as a constant, this is conventionally summarized as $O(n)$ time.

Gap storage is $O(G)$, while the global factorial table is $O(100000)$ shared space, which is $O(n_{\max})$ under the constraints.

## Alternatives and edge cases

- **Simulate infection choices:** Enumerating sequences is exponential and repeats equivalent substructure.
- **Dynamic programming over infected sets:** State space is exponential in $n$.
- **Leading gap:** Only infection from right to left is legal; do not multiply it by a power of two.
- **Trailing gap:** Only left-to-right infection is legal.
- **Empty gap:** Its factorial is $0!=1$ and it contributes no internal order factor.
- **Internal gap of one:** It has one order, corresponding to $2^0$.
- **Adjacent sick people:** Their internal gap length is zero and requires no special branch beyond the existing checks.
- **All but one initially sick:** $S=1$, and exactly one infection sequence exists.
- **Sorted sick input:** Gap construction relies on the promised increasing order.
- **Factorial bound:** The fixed table size is safe only because $n\le100000$.
- **Modulo inverses:** Ordinary integer division after modular reduction would be invalid; Fermat inverses are required.
- **Why interleavings remain legal:** Taking the next scheduled infection from any gap preserves that gap's frontier order, so the chosen person is still adjacent to an already infected boundary or predecessor.
