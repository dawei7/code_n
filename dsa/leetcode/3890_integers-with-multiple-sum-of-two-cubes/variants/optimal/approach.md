## General

**Bound every possible cube base**

Because the smaller base must be at least $1$, a possible larger base $b$ satisfies $1+b^3 \le n$. Build the cubes from $1^3$ through $B^3$, where $B$ is the largest base meeting that inequality. The constraint on `n` keeps $B$ below $1000$.

**Enumerate canonical pairs**

Choose the larger-position base first, then visit every earlier or equal base. This produces precisely the pairs $1 \le a \le b \le B$. If $a^3+b^3$ exceeds `n`, later values of $a$ only increase the sum, so the inner loop can stop.

Store how many canonical pairs produce each feasible total. The restriction $a \le b$ is essential: without it, $(a,b)$ and $(b,a)$ would falsely look like two distinct representations whenever $a \ne b$.

After enumeration, retain exactly the totals whose count is at least two and sort them. This final sort establishes the required ascending output order.

Every legal representation has positive bases, a larger base no greater than $B$, and one unique orientation with $a \le b$, so the enumeration includes it exactly once. Consequently a stored count is precisely the number of distinct pairs representing that total. Filtering counts of at least two selects exactly the good integers, and sorting supplies the required order.

## Complexity detail

There are $O(B^2)$ canonical pairs. Their expected hash-map updates take $O(B^2)$ time, and sorting the $G$ qualifying totals takes $O(G\log G)$ time. The total expected time is $O(B^2+G\log G)$, which is bounded by $O(B^2\log B)$. The cube list and representation map use $O(B^2)$ auxiliary space in the worst case.

The benchmark defines size as $B$, the number of possible larger cube bases. Pair counting grows quadratically in that size. A correct control that collects every feasible sum and then independently searches all possible base pairs for each distinct sum performs $\Theta(B^3)$ work.

## Alternatives and edge cases

- **Sort all pair sums:** Sorting the complete list and scanning equal runs avoids hashing but costs $O(B^2\log B)$ time and $O(B^2)$ space even when few totals qualify.
- **Merge sorted sum sequences:** A heap can generate pair sums in ascending order with less retained data, but it adds logarithmic work and more intricate duplicate-run handling.
- **Re-search every distinct sum:** A two-pointer cube search takes $O(B)$ time for one target, but repeating it for $O(B^2)$ feasible sums costs $O(B^3)$ overall.
- **Compare every pair of representations:** Directly comparing the $O(B^2)$ generated representations is even slower at $O(B^4)$.
- **Reversed bases:** Never count both $(a,b)$ and $(b,a)$; the contract's $a \le b$ condition gives one canonical orientation.
- **Equal bases:** A pair such as $(2,2)$ is legal, but one such pair alone cannot make its sum good.
- **Inclusive boundary:** A good integer equal to `n` belongs in the result.
- **No qualifying value:** Bounds below $1729$, the first possible good integer, return an empty array.
