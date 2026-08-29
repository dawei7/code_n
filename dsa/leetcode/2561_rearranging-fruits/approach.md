## General

**Only multiplicities matter**

The baskets are considered equal after sorting, so original positions have no importance. For each fruit cost $x$, both baskets must end with the same number of copies of $x$.

The counter `cnt` stores

$$
\texttt{cnt[x]}=
\text{count of }x\text{ in basket1}
-
\text{count of }x\text{ in basket2}.
$$

The code builds this difference by adding one for each first-basket value and subtracting one for the paired second-basket value. Using `zip` does not claim the values at matching positions must correspond; it is simply a convenient way to visit one item from each equally sized array per iteration. The final counter is an aggregate frequency difference.

A positive difference means basket1 has surplus copies that must move to basket2. A negative difference means basket2 has the surplus.

**Detect when equalization is impossible**

Across both baskets, the total number of copies of every cost must be split equally between the final baskets. If the combined count of a value is odd, such a split is impossible.

The parity of the combined count and the parity of `cnt[x]` are the same, because

$$
(c_1+c_2)-(c_1-c_2)=2c_2.
$$

Their difference is even. Therefore, `v % 2` being nonzero proves that the total count is odd, and the function immediately returns $-1$.

If the difference is even, `abs(v) // 2` is the number of copies of cost $x$ that are on the wrong side. For example, if basket1 has four more copies than basket2, two copies must cross from basket1, reducing the difference by four: basket1 loses two and basket2 gains two.

The list `nums` stores every misplaced copy from both sides with exactly this required multiplicity. Its length is even. Half of its entries belong to surpluses from basket1 and half to surpluses from basket2, because the baskets have equal sizes.

**Pair small misplaced values with large ones**

Every correcting exchange pairs one surplus item from one basket with one surplus item from the other. A direct swap of costs $x$ and $y$ costs $\min(x,y)$. To minimize the sum of these minima, small misplaced values should serve as the cheaper side of exchanges with large misplaced values.

After sorting `nums`, let `m = len(nums) // 2`. The first half contains exactly the $m$ globally smallest misplaced values. These are the only values that need to be priced as the smaller member of a pairing; the second-half values can be paired with them from the large end.

An exchange argument explains this. If two pairs have their cheaper members $a\le b$ and their larger partners are arranged so that a smaller partner is wasted with $a$ while a larger partner is paired with $b$, swapping the partners cannot increase either minimum. Pairing extremes ensures every globally small value pays once, while globally large values do not become unnecessarily expensive minima.

The implementation does not need to construct the actual pairs or track which basket contributed each entry. The balanced surplus counts guarantee compatible cross-basket partners, and the minimum-cost total depends on the $m$ smaller representatives.

**Sometimes two swaps through the global minimum are cheaper**

Let `mi` be the smallest fruit cost present anywhere. The expression `min(cnt)` returns the smallest key in the counter, which is the global minimum cost, not the smallest frequency difference.

For a direct exchange whose smaller misplaced value is $x$, the cost is $x$. There is another route: use a fruit of cost `mi` as an intermediary. Swap one misplaced fruit with the global-minimum fruit, then use that minimum fruit in the corresponding exchange on the other side. Each of the two swaps costs `mi`, for a total of $2\cdot\texttt{mi}$.

The intermediary may move between baskets during this process, but after the paired operations it can be placed consistently while the two misplaced values have crossed to their needed sides. Thus the cheapest price associated with smaller representative $x$ is

$$
\min(x,2\cdot\texttt{mi}).
$$

This matters when both directly swapped fruits are expensive. Even if $x$ is much smaller than its partner, two swaps involving a very cheap global minimum can cost less than $x$.

**Why summing the first half is sufficient**

Each necessary exchange corrects two entries of `nums`, one surplus from each basket. There are therefore `m` exchanges. Sorting and pairing the first-half values with second-half values makes each first-half value the direct-swap minimum. For every pair, the algorithm independently chooses the cheaper of the direct route and the two-minimum route.

These exchanges achieve equality because every listed surplus copy crosses once, and they have the lowest possible cost because any swap must pay at least either its smaller participating surplus or the cheapest possible two-step intermediary price. The sum

`sum(min(x, mi * 2) for x in nums[:m])`

therefore gives the global minimum.

For `basket1 = [4,2,2,2]` and `basket2 = [1,4,1,2]`, cost $2$ has difference $+2$ and cost $1$ has difference $-2$. The mismatch list is `[2,1]`, its first half is `[1]` after sorting, and `mi=1`. The cost is $\min(1,2)=1$.

## Complexity detail

Let $n$ be the size of each basket. Building the counter takes $O(n)$ time. The mismatch list contains at most $2n$ entries but in fact remains $O(n)$. Sorting it dominates with $O(n\log n)$ time, and the final sum is linear.

The counter and mismatch list use $O(n)$ auxiliary space. Sorting the Python list may also use $O(n)$ temporary memory. The baskets themselves are not modified.

## Alternatives and edge cases

- **Simulate arbitrary swaps:** Local choices can be suboptimal because an expensive direct swap may be cheaper through the global minimum. Frequency balancing exposes the real structure.
- **Use two frequency maps:** Separate basket counters are conceptually clear, but one signed counter stores the same information more compactly.
- **Already equal baskets:** Every difference is zero, `nums` is empty, `m=0`, and the sum correctly returns zero.
- **Odd total frequency:** An odd `cnt` difference means an odd combined multiplicity, so no sequence of swaps can split that value equally.
- **Duplicate costs:** Multiplicity is the entire point of the counter; every required surplus copy is repeated in `nums`.
- **Global minimum already balanced:** It can still be used as an intermediary. A physical minimum fruit exists in a basket even when it is not itself in the mismatch list.
- **Direct route cheaper:** When $x\le2\cdot\texttt{mi}$, one direct swap costs no more than using two intermediary swaps.
- **Indirect route cheaper:** When $x>2\cdot\texttt{mi}$, routing through the minimum saves cost.
- **Meaning of `min(cnt)`:** Python iterates the counter's keys for `min`, so this produces the smallest fruit value. It does not inspect signed counts.
- **Large answer:** Python integers avoid overflow; fixed-width languages should accumulate the total in a 64-bit type.
