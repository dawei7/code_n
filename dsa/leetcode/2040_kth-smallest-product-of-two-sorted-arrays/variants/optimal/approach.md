## General
**Binary-search the product value**

For a candidate integer $x$, let $C(x)$ be the number of indexed pairs whose
product is at most $x$. This count is monotone: increasing $x$ cannot remove a
qualifying pair. The desired product is therefore the smallest $x$ for which
$C(x)\ge k$.

Every legal product lies in $[-R,R]$. Binary-search this inclusive value range,
retaining the lower half whenever the count reaches `k` and otherwise
discarding the candidate and everything below it.

**Count one sorted row according to its sign**

Iterate through the shorter array and use binary search in the longer sorted
array. For a fixed value $a$:

- If $a>0$, then $ab\le x$ is equivalent to
  $b\le\lfloor x/a\rfloor$. A right-bound binary search counts that prefix.
- If $a=0$, all $B$ products qualify exactly when $x\ge0$.
- If $a<0$, division reverses the relation:
  $b\ge\lceil x/a\rceil$. A left-bound binary search locates that suffix.

Integer floor and ceiling division must be mathematically correct for negative
operands. In Python, `x // a` supplies the floor, while
`-((-x) // a)` supplies $\lceil x/a\rceil$.

**Choose the first value reaching the requested rank**

For every candidate, the three sign cases partition all indexed pairs and
count each exactly once, so $C(x)$ is exact. If $x$ is below the `k`th product,
fewer than `k` pairs qualify; at the `k`th product and above, at least `k`
qualify. Lower-bound binary search therefore terminates at precisely that
product, including when many pairs share the same value.

## Complexity detail
The value search performs $O(\log R)$ iterations. Each iteration examines the
shorter array's $A$ values and performs an $O(\log B)$ binary search, giving
$O(A\log B\log R)$ time. Apart from counters and search bounds, the algorithm
uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Generate and sort every product:** Materializing all $MN$ products is
  correct but costs $O(MN\log(MN))$ time and $O(MN)$ space.
- **Sign-partitioned two pointers:** Negative, zero, and positive sections can
  support a linear counting pass per candidate, improving the logarithmic
  factor but requiring more intricate pointer directions.
- Duplicate array values create duplicate indexed products and must count
  separately toward `k`.
- Zero products lie after every negative product and before every positive
  product.
- For a negative fixed factor, qualifying values form a suffix rather than a
  prefix of the other array.
- The first and last ranks may return $-10^{10}$ and $10^{10}$ respectively.
- Searching only products that visibly occur is unnecessary; lower-bound
  search over the integer range still lands on an occurring product.
