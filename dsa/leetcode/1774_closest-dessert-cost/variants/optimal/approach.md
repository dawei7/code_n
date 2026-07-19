## General
**Turn portion limits into three-way choices**

Each of the $m$ topping types contributes either zero, one, or two copies of its price. Therefore every complete topping selection corresponds to one length-$m$ sequence over $\{0,1,2\}$, giving at most $3^m$ selections. Start with the only sum available before processing toppings, `0`. For a topping price `cost`, extend every previously reachable sum by both `cost` and `2 * cost`, while retaining the old sum for the zero-copy choice.

**Why the generated sums are exactly the legal sums**

After the first $i$ topping types have been processed, the set contains precisely the totals obtainable using zero, one, or two portions of each of those $i$ types. This is true initially for zero types. Extending every old total by the three legal contributions of the next topping preserves all prior choices and introduces no illegal multiplicity, so the statement remains true for the next type. After all toppings, no valid topping total is missing.

**Compare complete desserts with the tie-break built in**

Pair each reachable topping sum with every base cost, because exactly one base is required. Compare a candidate total by `(abs(total - target), total)`: the distance is considered first, and the total itself selects the cheaper dessert when distances match. Since every legal base-and-topping combination is examined, the smallest comparison key is the required answer.

## Complexity detail
There are at most $3^m$ reachable topping selections. Expanding the set and then combining its values with $n$ bases takes $O(n \cdot 3^m)$ time overall; the $O(3^m)$ generation term is absorbed because $n \ge 1$. The set of topping sums occupies $O(3^m)$ auxiliary space. Duplicate totals can make the actual set smaller, but the worst case still has exponentially many distinct sums.

## Alternatives and edge cases
- **Depth-first enumeration:** Recurse through the zero-, one-, and two-copy choices for every topping and update the best cost at each leaf. It has the same worst-case time and uses only $O(m)$ recursion depth, but it may revisit equal topping totals produced by different choices.
- **Meet-in-the-middle:** Split the toppings, enumerate both halves, sort one side, and binary-search around the remaining target. This reduces the exponential factor for larger $m$, although the given limit $m \le 10$ makes direct generation simpler.
- **Target-bounded dynamic programming:** Track reachable sums only up to a chosen bound around `target`. This can be effective for small prices, but the stopping bound and the smallest overshoot must be handled carefully.
- A dessert may use no toppings, but it must always use exactly one base.
- A base cost can already exceed `target`; it remains a legal candidate and may be the closest total.
- When one achievable total lies below `target` and another equally far above it, the lower total must be returned.
