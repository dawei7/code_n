## General
**Count complete gifts with triangular numbers.** The first $G$ scheduled gifts use $G(G+1)/2$ candies. Compute the largest feasible $G$ with integer square root, avoiding floating-point rounding near the $10^9$ boundary. The remaining amount is

$$
R = C - \frac{G(G+1)}{2}.
$$

**Sum each person's arithmetic progression.** Person $i$ receives complete gifts numbered $i+1$, $i+1+P$, $i+1+2P$, and so on through $G$. The number of such gifts is

$$
q_i = \max\left(0, \left\lfloor\frac{G-1-i}{P}\right\rfloor + 1\right).
$$

Their complete-gift total is the arithmetic-series sum

$$
\frac{q_i\bigl(2(i+1)+(q_i-1)P\bigr)}{2}.
$$

**Place the final partial gift.** If $R>0$, the next scheduled gift is number $G+1$ and belongs to index `G % P`. Add all $R$ remaining candies there.

The triangular-number boundary accounts for every complete gift and no incomplete one. Grouping gift indices by their remainder modulo $P$ assigns each complete gift to exactly its intended person, and the arithmetic progression formula preserves their sum. The sole remainder then goes to the next cyclic recipient, matching the stopping rule.

## Complexity detail
Computing $G$ and $R$ takes constant time. One arithmetic-series calculation is performed for each of the $P$ people, so time is $O(P)$. The returned distribution contains $P$ integers and uses $O(P)$ space.

## Alternatives and edge cases
- **Gift-by-gift simulation:** It is simple and correct but performs $O(G)=O(\sqrt C)$ iterations instead of depending only on the output length.
- **Round-by-round formulas:** Sum complete rounds first, then distribute one partial round; this is also $O(P)$ but requires careful round-boundary arithmetic.
- **Exact triangular total:** When $R=0$, no partial gift is added.
- **One person:** Every complete and partial gift accumulates at index 0, producing `[candies]`.
- **Supply smaller than the first round:** Later people may receive zero candies.
- **Integer precision:** Use integer square root or equivalent exact adjustment rather than trusting a floating approximation.
