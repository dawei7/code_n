## General

**Treat mirrored positions as independent pairs**

Because `n` is even, the array contains exactly `n / 2` mirrored pairs:

`(nums[i], nums[n - 1 - i])`.

For the final array to be complementary, every pair must have one common target sum `S`. Since each value after replacement must lie from one through `limit`, every possible target lies in

$$
2 \le S \le 2\cdot\texttt{limit}.
$$

For a fixed target, different pairs can be changed independently. The total number of moves is the sum of each pair’s minimum cost. The challenge is to evaluate all target sums without examining every pair for every target.

**Understand one pair’s piecewise cost**

Take one pair and reorder its values so `x <= y`. Its current sum is `x + y`.

With zero moves, the pair can reach only `x + y`.

With one move, keep one value and replace the other:

- keeping `x` permits sums from `x + 1` through `x + limit`;
- keeping `y` permits sums from `y + 1` through `y + limit`.

Because `x <= y <= limit`, these ranges overlap or touch and their union is the continuous interval

$$
[x+1,\ y+\texttt{limit}].
$$

Therefore the minimum pair cost is:

- two moves for `2 <= S < x + 1`;
- one move for `x + 1 <= S < x + y`;
- zero moves at `S = x + y`;
- one move for `x + y < S <= y + limit`;
- two moves for larger valid `S`.

This step pattern changes only at a few known boundaries, which makes a difference array appropriate.

**Encode the step pattern with boundary changes**

The array `d` does not store costs directly. It stores how the cost changes when the target advances to an index. Prefix-accumulating `d` later reconstructs the actual total.

For each pair, the source performs these conceptual updates:

- `d[2] += 2` starts the pair at cost two for the smallest target;
- at `x + 1`, cost drops from two to one, a net change of `-1`;
- at `x + y`, cost drops from one to zero, another `-1`;
- at `x + y + 1`, cost rises from zero to one, a change of `+1`;
- at `y + limit + 1`, cost rises from one to two, another `+1`.

The source writes the first net `-1` as consecutive `-= 2` and `+= 1` operations. It writes the last net `+1` as `-= 1` followed by `+= 2`. Those pairs look redundant but algebraically encode exactly the boundary changes above.

All mirrored pairs update the same `d`. Difference arrays are additive, so at any target the reconstructed prefix sum equals the sum of all pair costs.

**Sweep all target sums at once**

`accumulate(d[2:])` produces successive prefix sums beginning at target two. The first yielded value includes every pair’s baseline `+2`. Each later value applies all boundary changes at the next target index.

Taking `min(...)` selects the target sum requiring the fewest total moves. The source’s slice also includes the sentinel index `2 * limit + 1`, one beyond the valid target range. At that boundary pair costs can only rise from one to two; no update decreases the cost after `2 * limit`. Consequently including this extra accumulated value cannot create a smaller answer than the valid range, although restricting the slice to valid targets would be clearer.

For `nums = [1, 2, 4, 3]` and `limit = 4`, the mirrored pairs are `(1, 3)` and `(2, 4)`. Target four already fits the first pair and needs one change in the second, producing total one, which the sweep finds.

**Why the minimum is correct**

For any fixed target `S`, the five-case derivation gives the exact minimum moves for each pair: zero if unchanged, one if changing either member can reach `S`, and otherwise two. The difference updates reconstruct precisely that function. Adding pair functions gives the exact total moves for `S` because a move affects only one element in one pair.

Every legally complementary array has some target in the enumerated range, and every target in that range can be evaluated by the sweep. Taking the smallest reconstructed total therefore returns the global minimum number of moves.

## Complexity detail

Let `n` be the array length and `L = limit`. Processing `n/2` mirrored pairs takes $O(n)$ time, with constant work per pair. The difference array has $2L + 2$ positions, and accumulating its slice takes $O(L)$ time. Total time is $O(n + L)$.

The difference array uses $O(L)$ space. `accumulate` is lazy, so `min` consumes values without constructing another full prefix-sum list. All other state is constant size.

The input array is read but not modified. Sorting within a pair is done through a constant-time swap of local variables.

## Alternatives and edge cases

- **Brute force every target and pair:** This follows the definition but costs $O(nL)$, repeating the same piecewise-cost reasoning for every target.
- **Binary-search counting:** Sort smaller and larger pair members and count zero-, one-, and two-move cases for every target with binary searches. It is correct but slower by logarithmic factors and uses more involved statistics.
- **Combine redundant updates:** The two operations at `x+1` can be written as `d[x+1] -= 1`, and those at `y+L+1` as `d[y+L+1] += 1`. The exact source leaves their derivational components separate.
- **Pair values already equal the chosen target:** The update at `x+y` makes that pair contribute zero.
- **Target at two:** Only `[1,1]` is unchanged; other pairs require one or two changes according to the same boundaries.
- **Target at `2L`:** Only `[L,L]` is unchanged, and the allocated sentinel safely records changes just beyond this valid endpoint.
- **`x == y`:** The one-change intervals still form `[x+1, x+L]`, and the zero-cost point `2x` lies within it.
- **Minimum array length two:** There is one pair, so the result is zero because choosing its current sum already makes all pairs agree.
- **Repeated mirrored pairs:** Their identical difference updates simply add, correctly multiplying their contribution.
- **Even-length guarantee:** Every element belongs to exactly one pair. An unpaired center in an odd-length array would need separate treatment.
- **Replacement bounds:** The interval endpoints `x+1` and `y+L` come directly from keeping one value and choosing the other in `[1,L]`; overlooking these bounds gives incorrect one-move ranges.
