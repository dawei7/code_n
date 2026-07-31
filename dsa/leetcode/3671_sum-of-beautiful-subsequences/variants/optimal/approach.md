## General

Let $E(g)$ be the number of strictly increasing subsequences whose GCD is exactly $g$. Directly maintaining every evolving GCD is too expensive. Instead define $F(d)$ as the number of strictly increasing subsequences in which every selected value is divisible by $d$.

A subsequence contributes to $F(d)$ exactly when its GCD is a multiple of $d$, so

$$
F(d)=\sum_{d\mid g}E(g).
$$

By Möbius inversion,

$$
E(g)=\sum_{m\ge1}\mu(m)F(gm).
$$

Substitute this into the requested sum and group terms by $h=gm$:

$$
\begin{aligned}
\sum_{g\ge1}gE(g)
&=\sum_{h\ge1}F(h)\sum_{g\mid h}g\mu(h/g)\\
&=\sum_{h\ge1}\varphi(h)F(h).
\end{aligned}
$$

The final equality is the standard divisor identity for Euler's totient function. It replaces exact-GCD counting with divisibility counting.

**Count increasing subsequences for every divisor.** Fix $d$. Among values divisible by $d$, divide each value $x$ by $d$. This preserves strict numerical order. Process `nums` from left to right with a Fenwick tree indexed by quotient.

For current quotient $q=x/d$, query the total stored at indices below $q$. Each such prior subsequence may be extended by $x$, and the singleton `[x]` supplies one more way:

$$
\text{ways}=1+\operatorname{prefix}(q-1).
$$

Add `ways` at index $q$ and to $F(d)$. Querying only through $q-1$ prevents equal values from extending one another.

An input value $x$ belongs only to divisibility processes whose $d$ divides $x$. Enumerate the divisor pairs of $x$ through $\lfloor\sqrt{x}\rfloor$ and update only those Fenwick trees. Allocate a tree lazily with indices through $\lfloor V/d\rfloor$.

Finally compute Euler's totient values through $V$ with a sieve and return $\sum_d\varphi(d)F(d)$ modulo $10^9+7$. Every Fenwick count represents exactly an index-valid, value-increasing subsequence made entirely of multiples of its divisor, so the totient identity proves the final sum.

## Complexity detail

Let $V$ be the maximum value and

$$
T=\sum_{x\in\texttt{nums}}\tau(x),
$$

where $\tau(x)$ is the number of positive divisors of $x$. The totient sieve takes $O(V\log\log V)$ time. Trial divisor enumeration costs $O(n\sqrt V)$ in the worst case. Each of the $T$ divisor incidences performs one Fenwick query and update in $O(\log V)$ time. Total time is

$$
O(V\log\log V+n\sqrt V+T\log V).
$$

A divisor-$d$ tree has $O(V/d)$ entries. Across all lazily allocated divisors this is at most the harmonic sum $O(V\log V)$ space; the totient and total arrays add $O(V)$.

The benchmark defines its size as $n$ and uses strictly increasing arrays of lengths $3$, $6$, and $12$. The accepted divisor/Fenwick method remains polynomial. A calibrated correct alternative enumerates all nonempty subsequences and computes each increasing subsequence's GCD, producing exponential growth.

## Alternatives and edge cases

- **Enumerate every subsequence:** This is exact but takes $O(2^n n)$ time.
- **Track GCD states per ending value:** Many GCD/value combinations may accumulate and require more expensive ordered-prefix aggregation.
- **Equal values:** They cannot extend one another because the subsequence must be strictly increasing; separate occurrences still contribute separate singletons.
- **Decreasing array:** Only singleton subsequences contribute.
- **Repeated indices:** A subsequence may never reuse an index; left-to-right Fenwick processing enforces index order.
- **Divisor one:** Its tree counts every strictly increasing subsequence.
- **Large counts:** Reduce every Fenwick update, divisor total, and final weighted sum modulo $10^9+7$.
- **Perfect-square value:** Add its square-root divisor only once when enumerating a divisor pair.
