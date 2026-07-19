## General
**Represent two tuple positions as an unordered pair**

Generate every index pair $i<j$ once and compute `product = nums[i] * nums[j]`. A valid tuple exists precisely when two different unordered pairs have the same product. Because all values are distinct and positive, two different equal-product pairs cannot share exactly one value: if `{x,y}` and `{x,z}` had the same product, then $xy=xz$ would imply $y=z$. Equal-product pair collisions therefore already contain four distinct elements.

**Count the arrangements created by one collision**

Choose two unordered pairs with a common product. Either pair may occupy `(a,b)` rather than `(c,d)`, giving two choices. Each pair may also be written in either internal order, giving another $2\cdot2$ choices. Thus every unordered choice of two pairs produces

$$
2\cdot2\cdot2=8
$$

valid ordered tuples.

**Accumulate collisions as pairs arrive**

Store how many earlier pairs produced each product. If the current pair's product has already appeared $c$ times, pairing the current pair with each earlier one creates $c$ new pair-pair choices and therefore `8 * c` new ordered tuples. Add that amount before incrementing the product frequency. Every two-pair choice is counted exactly when its later pair is processed, so none is omitted or counted twice.

## Complexity detail
There are $\binom{n}{2}=O(n^2)$ unordered index pairs. Computing a product, looking up its frequency, and updating the answer take expected $O(1)$ time per pair, for $O(n^2)$ total time. In the worst case all pair products are different, so the hash table stores $O(n^2)$ keys and uses $O(n^2)$ space.

## Alternatives and edge cases
- **Count first, combine afterward:** Build all product frequencies, then add $8\binom{c}{2}$ for every frequency $c$. This has the same asymptotic bounds and is mathematically equivalent to the incremental collision count.
- **Enumerate ordered triples:** Choose `(a,b,c)` and derive `d = a * b / c`, then test membership and distinctness. This is correct with careful divisibility checks but takes $O(n^3)$ time.
- **Enumerate four positions:** Directly testing every ordered quadruple takes $O(n^4)$ time and repeats the same pair-product structure many times.
- **Fewer than four values:** No valid tuple can be formed, and no product frequency can reach two disjoint pairs.
- **No repeated pair product:** Every stored frequency remains one, so the answer stays zero.
- **Several pairs with one product:** A frequency of $c$ contributes $8\binom{c}{2}$ tuples, not merely eight.
- **Maximum values:** A pair product can reach $10^8$; the product itself is the hash key, and multiplication must use a sufficiently wide integer type.
