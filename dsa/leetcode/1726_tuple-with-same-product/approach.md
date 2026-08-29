## General

**Group unordered pairs by their product**

The equation $a\cdot b=c\cdot d$ says that two pairs of input values have the same product. Instead of choosing four ordered values directly, the source first enumerates every unordered index pair and records how many pairs produce each product.

The nested loops use `i` from one through the end and `j` from zero through `i-1`. Thus every pair of distinct indices appears exactly once with `j < i`. A pair is never generated in both orders, and an element is never paired with itself.

For product `x = nums[i] * nums[j]`, `cnt[x] += 1` increments its frequency.

**Choose two pairs from one product group**

If product $P$ occurs for $v$ unordered pairs, any two different pairs in that group satisfy the required product equality. The number of ways to choose those two pairs without order is

$$
\binom v2=\frac{v(v-1)}2.
$$

The generator expression

`v * (v - 1) // 2 for v in cnt.values()`

computes this quantity for every distinct product, and `sum` adds them.

A product with frequency zero cannot exist in the dictionary, and frequency one contributes zero because there is no second pair.

**Why equal-product pairs automatically use four distinct values**

The contract says input values are distinct positive integers. Suppose two different unordered pairs with the same product shared a value $a$: they would be `{a,b}` and `{a,c}` with

$$
a b=a c.
$$

Because $a$ is positive and nonzero, cancellation gives $b=c$, making the pairs identical. That contradicts choosing two different pairs.

Therefore two different pairs in one product group cannot overlap. Their four elements are automatically distinct, so the source needs no explicit disjointness check.

Both positivity and distinctness support this shortcut. With zeros or repeated values, equal-product pair groups could contain overlapping index pairs and would require more careful counting.

**Turn one pair-of-pairs into eight ordered tuples**

Suppose the selected unordered pairs are `{a,b}` and `{c,d}`. There are three independent binary choices:

- Order `a,b` as `(a,b)` or `(b,a)`.
- Order `c,d` as `(c,d)` or `(d,c)`.
- Put the first pair on the left of the equality or the right.

That gives $2\cdot2\cdot2=8$ ordered tuples. All are different because the four values are distinct.

The source multiplies the total pair-of-pairs count by eight using `<< 3`. Left-shifting a nonnegative integer three bits is multiplication by $2^3=8$.

**Trace the first example**

For `nums = [2,3,4,6]`, the six unordered products are:

- `2*3=6`,
- `2*4=8`,
- `2*6=12`,
- `3*4=12`,
- `3*6=18`,
- `4*6=24`.

Only product 12 has frequency two. It contributes `2*1//2 = 1` pair-of-pairs, then the shift multiplies by eight. The answer is eight.

**Trace a product with more than two pairs**

If some product appears for four unordered pairs, there are `C(4,2)=6` ways to choose which two pairs supply the equality. Each creates eight ordered tuples, contributing 48.

It would be incorrect to use merely `v*8`, because the combinatorial object is a choice of two pairs among all $v$, not one pair independently.

**Why every valid tuple is counted once**

Take any valid ordered tuple `(a,b,c,d)`. Ignoring order within sides produces two distinct unordered input pairs with one common product. The nested loops inserted each of those pairs exactly once into that product group.

The combination count chooses their unordered pair-of-pairs exactly once. Among its eight expansions, exactly one restores the tuple's side order and within-pair order. Thus every valid tuple is included once.

Conversely, every counted product-group combination has equal products and four distinct elements, and each of its eight expansions satisfies the contract. No invalid tuple is introduced.

## Complexity detail

Let $n$ be the number of values. The nested loops generate

$$
\frac{n(n-1)}2=\Theta(n^2)
$$

pairs. Expected hash-map insertion is constant time, so pair enumeration takes expected $O(n^2)$ time. Summing frequencies visits at most one dictionary entry per pair product, also $O(n^2)$ in the worst case. Total expected time is $O(n^2)$.

If every pair product differs, `cnt` has $\Theta(n^2)$ entries, so auxiliary space is $O(n^2)$. These bounds match the manifest.

Python integers safely hold products up to $10^8$ and the final tuple count.

## Alternatives and edge cases

- **Four nested loops:** Test every ordered quadruple directly in $O(n^4)$ time, far beyond the constraints.
- **Store and sort all pair products:** Group equal adjacent products in $O(n^2\log n)$ time and $O(n^2)$ space.
- **Incremental tuple counting:** When a new pair product has appeared `v` times, add `8v` immediately. This avoids the final frequency pass with the same asymptotic bounds.
- **Fewer than four values:** No two disjoint pairs exist, and all product frequencies contribute zero combinations.
- **All products distinct:** Every frequency is one and the answer is zero.
- **Several equal-product pairs:** The combination formula counts every choice of two.
- **Distinct input values:** It guarantees two same-product pairs cannot overlap.
- **Positive values:** It permits cancellation in the disjointness proof and excludes zero-product overlap.
- **Pair order:** The nested loops record each unordered pair only once.
- **Tuple order:** The final factor eight restores all ordered arrangements.
- **Bit shift:** `<<3` is exact multiplication by eight for the nonnegative sum.
- **Input preservation:** The array is never sorted or modified.
