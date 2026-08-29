## General

**Always sell a currently most valuable ball**

The value of a ball is the number of balls of that color that remain immediately before the sale. If one color currently has 8 balls and another has 5, selling from the first color earns 8 now. Delaying that sale cannot make it worth more, while selling the lower-valued ball first earns only 5.

An exchange argument makes the greedy rule precise. Suppose a sale plan chooses a ball worth $y$ while another available ball is worth $x>y$. Swap the higher-valued ball into the earlier sale. The immediate profit increases by $x-y$. The later inventory levels can be rearranged so that no later sale becomes more valuable than what was gained. Therefore some optimal plan always takes one of the largest current inventory counts.

Selling one ball at a time would be too slow because `orders` can reach $10^9$. The source groups many equal-valued greedy sales into arithmetic-series layers.

**Sort colors into descending inventory levels**

`inventory.sort(reverse=True)` puts the largest count at index 0. The variable `i` grows until indices `0` through `i-1` form the current highest plateau. `cnt = i` is the number of colors on that plateau.

The inner loop advances while `inventory[i] >= inventory[0]`. Initially this finds all colors tied at the maximum. After a layer is removed, only `inventory[0]` is changed to the next height; earlier array entries may still store old larger numbers, so the `>=` comparison deliberately absorbs them into the conceptual plateau. `i` never moves backward.

`nxt` is the next lower inventory height, or zero when every color is already in the plateau. Lowering all `cnt` plateau colors from current height `inventory[0]` down to `nxt` sells

$$
\textit{tot}=\textit{cnt}\bigl(\textit{inventory}[0]-\textit{nxt}\bigr)
$$

balls.

**Sell a complete layer**

When `tot <= orders`, the customer can buy the entire layer. For each plateau color, sold values are

$$
\textit{inventory}[0],\ \textit{inventory}[0]-1,\ldots,\textit{nxt}+1.
$$

There are `x = inventory[0] - nxt` terms. The sum for one color is the arithmetic-series formula

$$
\frac{(\textit{nxt}+1+\textit{inventory}[0])x}{2}.
$$

Multiplying by `cnt` accounts for every plateau color. The source uses `a1 = nxt + 1` and `an = inventory[0]` to implement this formula.

Afterward, all those colors conceptually have `nxt` balls. Assigning `inventory[0] = nxt` records the new plateau height. The next outer iteration expands `i` across any colors already stored at that same level.

**Sell only part of a layer**

If `tot > orders`, there are not enough orders to reach `nxt`. Let

`decr = orders // cnt`.

This is the number of complete value levels that can be sold from every plateau color. Those full levels range from `inventory[0]` down through `inventory[0] - decr + 1`. Their arithmetic sum is multiplied by `cnt`.

After the full levels, `orders % cnt` balls remain to sell. Every plateau color now has the same current value `inventory[0] - decr`, so each remaining sale earns exactly that amount. The second addition handles this remainder.

No later iteration is needed after a partial layer because those calculations consume all originally remaining orders. The source subtracts the whole hypothetical `tot` rather than the actual remaining order count, making `orders` negative; the `while orders > 0` condition then exits. This unusual bookkeeping is safe because the profit for exactly the requested remainder was already added.

**A trace**

For `inventory = [2,5]` and `orders = 4`, sorting gives `[5,2]`. The first plateau has one color at height 5 and next height 2. Its complete layer would sell three balls worth 5, 4, and 3. Since three orders are available, the source earns 12 and lowers the top to 2.

Now both colors form a plateau of size two at value 2, with one order remaining. No full level across both colors fits, so `decr=0` and the remainder sale earns 2. Total profit is 14.

**Why layer processing preserves optimality**

Before each outer iteration, all colors in the prefix are the colors with greatest current inventory, at one common conceptual height. Greedy optimality says sales should come from this prefix until it reaches the next height. Every complete layer sale takes exactly those highest-valued balls.

If orders stop within a layer, all plateau colors offer equal value at each complete level, and all remainder choices offer the same next value. The arithmetic formulas therefore sum exactly the same multiset of values that an optimal one-by-one greedy process would select.

By induction over layers, `ans` is the maximum profit for every processed sale. The final modulo operation changes only the representation of that total, not which sales were chosen.

## Complexity detail

Let $n$ be the number of colors. Sorting costs $O(n\log n)$ time. The plateau index `i` advances from 0 to $n$ only once across all outer iterations, so all inner-loop work is $O(n)$. Each layer performs constant arithmetic, and there are at most $n$ distinct levels. Total time is $O(n\log n)$.

Python's in-place Timsort may use $O(n)$ temporary memory in the worst case. Beyond sorting workspace, the algorithm uses constant scalar state. Thus the implementation's auxiliary space is $O(n)$ under Python's sorting behavior, matching the manifest.

The input inventory list is mutated. Arithmetic-series evaluation avoids any dependence on `orders` in the loop count, which is essential when orders is as large as $10^9$.

Modulo $10^9+7$ is applied after each layer. Python integers prevent overflow before reduction, and modular addition permits these intermediate reductions.

## Alternatives and edge cases

- **Max-heap one sale at a time:** Pop the largest inventory, earn it, decrement, and push it back. It mirrors the greedy rule but costs $O(\textit{orders}\log n)$ and is too slow for $10^9$ orders.
- **Binary search a final inventory threshold:** Find the value down to which all larger inventories are sold, then calculate arithmetic sums and a remainder. It can achieve similar asymptotic time but requires careful threshold counting.
- **Counting buckets:** Inventory values reach $10^9$, so a bucket for every possible value is impractical.
- **One color:** The answer is the sum of the descending values for the requested number of balls.
- **All colors tied:** The first plateau contains every color, and partial-layer remainder handling chooses any equal-valued colors.
- **Orders end exactly at a layer boundary:** `tot == orders` takes the complete-layer branch, reduces orders to zero, and exits.
- **Orders end inside a level:** `orders % cnt` sells only the needed number of equal-valued balls.
- **Next level zero:** It represents exhausting all remaining colors; the arithmetic formula still applies.
- **Input mutation:** Descending sort and updates alter `inventory`. Copy it first if caller-visible preservation were required.
- **Partial branch subtracts too much:** This intentionally forces loop termination after exact profit for all remaining orders has already been computed.
