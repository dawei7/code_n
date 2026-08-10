## General

**Represent two copies through two subset sums**

Each topping type may be used zero, one, or two times. Directly choosing among three counts for every one of $m$ toppings gives $3^m$ combinations.

The exact solution uses a different representation. It first generates every subset sum where each topping is used zero or one time. Then it adds two independently chosen subset sums.

For any topping:

- If it appears in neither subset, its total count is zero.
- If it appears in exactly one subset, its total count is one.
- If it appears in both subsets, its total count is two.

Thus the sum of two 0/1 subset sums represents every legal 0/1/2 topping choice. Conversely, no topping can appear more than twice because each of the two subsets contains it at most once.

**Generate all one-copy subset sums**

Nested helper `dfs(i, t)` processes topping index `i` with current sum `t`. It has two branches:

- Skip the topping and keep `t`.
- Include one copy and add `toppingCosts[i]`.

At the end of the topping list, it appends `t` to `arr`. Starting from zero includes the empty subset.

The list contains exactly $2^m$ entries, counting different subsets separately even when they have equal sums. Duplicate numeric sums do not hurt correctness; they only repeat equivalent work later.

After generation, `arr.sort()` prepares the sums for binary search.

**Fix a base and the first topping subset**

The outer loops choose exactly one base cost `x` and one subset sum `y`. This already specifies the base plus one of the two allowed topping-copy layers.

The ideal second subset sum would make:

$$
x+y+z=\texttt{target}.
$$

So the desired `z` is `target - x - y`.

The algorithm iterates every base and every possible `y`, ensuring that all choices for these components are considered.

**Find the nearest second subset sum**

`bisect_left(arr, target - x - y)` returns the first sorted index whose sum is at least the desired complement.

The closest available value must be either:

- `arr[i]`, the first value on or above the target, or
- `arr[i - 1]`, the final value below it.

All earlier values are no closer than `arr[i - 1]`, and all later values are no closer than `arr[i]`. The source checks both indices when they are in bounds.

This reduces the second-subset search from scanning $2^m$ sums for every `y` to logarithmic lookup.

**Apply both optimization rules**

For a complete candidate cost `x + y + arr[j]`, the absolute distance is stored in `t`. The source replaces the best when:

- `d > t`, meaning the candidate is strictly closer, or
- `d == t and ans > candidate`, meaning distance ties and the candidate cost is lower.

`d` and `ans` begin at positive infinity, so the first valid candidate is accepted.

This exactly implements the primary objective of minimum absolute difference and the secondary objective of smaller cost.

**Trace how two copies are represented**

Suppose one topping costs five. The one-copy subset-sum list contains zero and five.

Choosing `y = 5` and second sum `z = 5` produces total topping contribution ten, representing two copies. Choosing five and zero represents one copy, and zero plus zero represents none.

With several toppings, membership decisions are independent in the two recursive subset layers, so every vector of counts in `{0,1,2}^m` is representable.

**Why exactly one base is enforced**

`x` comes from one iteration over `baseCosts`. No other base value is included in `y` or `arr[j]`, because those arrays are generated only from toppings.

Therefore every candidate includes one and only one base. Each base receives its own complete search over topping combinations.

**Why the returned cost is correct**

Every candidate examined is a legal dessert: one base plus two 0/1 topping subsets yields zero through two copies of each topping.

Every legal dessert can split each topping's copies across two subset layers and therefore appears as some `x + y + z`. For each fixed `x, y`, binary search checks the best possible `z` by distance, including the lower tie neighbor. Global tracking applies the exact distance and lower-cost tie rules.

Consequently the final `ans` is the closest legal dessert cost, with the lower cost chosen on equal distance.

## Complexity detail

Let $P=2^m$. Subset generation takes $O(P)$ recursive leaves and calls, and sorting `arr` takes $O(P\log P)=O(m2^m)$ time.

There are $nP$ base-and-first-subset pairs. Each performs one $O(\log P)=O(m)$ binary search and constant neighbor checks. Exact total time is $O(nm2^m+m2^m)$, usually written $O(nm2^m)$.

This differs from the manifest's $O(n3^m)$ time, which corresponds to direct ternary topping enumeration. The exact two-subset plus binary-search implementation has the bound above.

`arr` stores exactly $2^m$ subset sums, and recursion depth is $O(m)$. Peak auxiliary space is $O(2^m)$, not the manifest's looser $O(3^m)$ claim.

## Alternatives and edge cases

- **Direct ternary DFS:** Choose zero, one, or two copies per topping in $O(3^m)$ combinations. It is simpler conceptually but asymptotically larger.
- **Backtracking with pruning:** Track current best and stop some branches above target, but lower-cost tie handling and positive topping costs must be handled carefully.
- **Set of topping sums:** Deduplicating sums can reduce work, though sorting and completeness remain necessary.
- **Dynamic programming by reachable cost:** Cost bounds can support a Boolean reachable array, but the exact subset method avoids target-dependent sizing.
- **No toppings selected:** Both subset sums may be zero, so every base alone is considered.
- **One copy:** Include a topping in exactly one subset.
- **Two copies:** Include it in both subsets.
- **Exact target:** Distance becomes zero and cannot be improved, though the source continues searching.
- **Equal-distance candidates:** The explicit second condition retains the lower total cost.
- **Complement below all sums:** `i == 0` and only the first candidate is checked.
- **Complement above all sums:** `i == len(arr)` and only the last lower candidate is checked.
- **Duplicate subset sums:** They repeat candidates but cannot change the optimum.
- **One base at a time:** The outer loop enforces exactly one base.
- **Positive costs:** They keep all generated totals nonnegative, though binary search logic would also work with sorted signed sums.
- **Input preservation:** Arrays are read to generate sums and are not modified.
