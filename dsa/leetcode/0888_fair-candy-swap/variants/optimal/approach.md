## General
**Derive the required difference between the two boxes**

Let $A$ and $B$ be Alice's and Bob's current candy totals. If Alice gives size $x$ and receives size $y$, equality after the swap requires

$$
A-x+y=B-y+x,
$$

so $x-y=(A-B)/2$. The existence guarantee implies that the total difference is even. For each candidate `x`, the only Bob box that can pair with it is therefore `y = x - difference`, where `difference` stores `(A - B) // 2`.

**Find the required Bob box in constant expected time**

Place all sizes from `bobSizes` in a hash set. Scan Alice's boxes and compute the corresponding `y`; as soon as `y` belongs to Bob's set, return `[x, y]`.

Membership proves that both selected box sizes actually exist. The derived equation then makes the post-swap totals equal. Conversely, every valid swap must satisfy the same equation, so scanning every Alice size and testing its unique required partner cannot miss all valid answers.

## Complexity detail
Summing both arrays, building Bob's set, and scanning Alice's boxes take $O(p+q)$ expected time. The set stores at most $q$ distinct sizes, giving $O(q)$ auxiliary space.

## Alternatives and edge cases
- **Try every pair of boxes:** Directly checking all exchanges is correct but costs $O(pq)$ time.
- **Sort and use two pointers:** Comparing pair differences after sorting works in $O(p\log p+q\log q)$ time and can avoid a hash set when in-place sorting is allowed.
- **Hash Alice's sizes instead:** Rearranging the same equation permits storing either person's values; storing the smaller side can reduce practical memory use.
- **Duplicate box sizes:** A set may collapse duplicates because the answer needs only one box of each required size.
- **Multiple valid exchanges:** Any pair satisfying the membership and equal-total conditions is acceptable.
- **Alice has the larger total:** Then `difference` is positive, so Alice must give a box larger than the one she receives by exactly that amount.
- **Bob has the larger total:** A negative `difference` correctly makes the required Bob box larger than Alice's candidate.
