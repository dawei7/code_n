## General

**Minimize a bit mask from the most significant bit downward**

The numerical order of nonnegative integers is determined by their highest differing bit. If two possible OR values agree above bit `i`, the value with zero at bit `i` is smaller than the value with one there, no matter what happens in all lower bits. Therefore the algorithm should try to make the most significant bit zero first, then the next bit, and so on.

The choice from one row is independent of the choice from every other row. The selected values interact only through their final bitwise OR. This independence lets the source turn “does some complete selection work?” into a separate existence check for each row.

Let `B` be the bit length of the largest grid value. No input value has a set bit at position `B` or above, so the answer needs only bit positions `B-1` through zero. The source obtains `B` as `mx.bit_length()` and examines those bits in descending order.

**View a candidate number as a set of allowed bits**

For nonnegative integers `x` and `mask`,

`(x | mask) == mask`

exactly when every bit set in `x` is also set in `mask`. In set terminology, the set bits of `x` are a subset of the set bits allowed by `mask`. If one value satisfying this relation is selected from every row, the OR of all selected values also has no bit outside `mask`.

The variable `ans` stores higher bits that earlier tests proved unavoidable. At bit `i`, lower bits have not yet been optimized and must remain free to be either zero or one. The trial mask is

`mask = ans | ((1 << i) - 1)`.

The term `(1 << i) - 1` has ones in exactly the lower positions `0` through `i-1`. It has zero at the current position `i`. Thus the mask means:

- higher bits already proved necessary by `ans` are allowed;
- higher bits previously kept at zero remain forbidden;
- the current bit `i` is tentatively forbidden; and
- all lower, undecided bits are allowed.

This is the correct feasibility question for trying to set answer bit `i` to zero.

**Why checking each row separately is sufficient**

For every row, the nested loops search for at least one value `x` whose bits fit inside the trial mask. If every row has such a value, select one witness from each row. Their OR also fits inside the mask, because OR cannot introduce a bit absent from every selected operand. Therefore a complete selection exists with all settled higher-zero decisions respected and current bit `i` equal to zero.

Conversely, if one row has no compatible value, no complete selection can fit inside the mask: the required choice from that row alone introduces some forbidden bit. There is no column-matching constraint and no limit on how often a column index can be used across rows, so there is no hidden coupling between row witnesses. Rowwise existence is both necessary and sufficient.

When every row passes, the source leaves `ans` unchanged, permanently choosing zero at bit `i`. When a row fails, it executes `ans |= 1 << i`. This marks the current bit as unavoidable, restoring it to the allowed set for all lower-bit decisions.

**Feasibility invariant**

Before testing bit `i`, there exists a selection whose OR uses no bit outside

$$
\texttt{ans}\;\mathbin{\vert}\;(2^{i+1}-1).
$$

In words, all undecided bits through `i` are temporarily allowed, while every settled higher zero remains forbidden. Initially, allowing all `B` relevant bits admits every grid value, so the invariant holds.

The trial mask removes only bit `i` from this allowed set. If every row has a compatible value, those witnesses prove feasibility with that bit removed. If a row fails, the previous invariant still guarantees feasibility when bit `i` is restored; setting it in `ans` preserves the invariant for the next lower bit.

The failure also proves necessity. Because all settled higher decisions must remain fixed for any numerically competitive answer, and no selection respects those decisions while omitting bit `i`, every feasible answer with the same optimal higher prefix must contain bit `i`. Lower bits cannot compensate for setting this more significant bit.

After bit zero is decided, no undecided positions remain. The invariant says a selection exists whose OR is contained in `ans`. Every one-bit added to `ans` was proven necessary under the already-minimal higher prefix, so the attainable minimum OR cannot omit any of them. Hence the minimum OR equals `ans` exactly.

**Example of the bit decisions**

For `grid=[[1,5],[2,4]]`, the values in binary are `001`, `101`, `010`, and `100`. The largest value needs three bits.

At bit two, the trial mask allows only lower bits `011`. The first row can use `1` and the second can use `2`, so bit two stays zero. At bit one, the higher zero remains forbidden and the trial mask allows only bit zero. The second row has no value contained in `001`, so bit one is forced into `ans`. At bit zero, trying to forbid it leaves mask `010`; the first row has no compatible choice, so bit zero is also forced. The result is `011`, or three.

The method never has to commit to the same witness values across successive trial bits. A feasibility test asks only whether some selection exists under the current prefix. Rechoosing witnesses later is legitimate because the problem asks for the minimum value, not for the selected coordinates.

## Complexity detail

Let `T` be the total number of grid cells and `B` the bit length of the largest value. Computing the maximum visits all cells once in `O(T)` time. For each of `B` bits, the worst case scans every row and every cell before determining feasibility, costing `O(BT)` overall.

For a rectangular `M\times N` grid, `T=MN`, so this is the manifest's `O(BMN)` bound. Here values are at most `10^5`, making `B\le17`; under that fixed constraint the scan is effectively linear in the number of cells, though retaining `B` makes the bit dependency explicit.

The source stores only scalar masks, loop variables, and Boolean `found`. The `map(max, grid)` expression streams row maxima rather than building a second matrix. Auxiliary space is `O(1)`, matching the manifest. The input grid is read-only and the returned answer is one integer.

## Alternatives and edge cases

- **Enumerate one choice per row:** This requires `N^M` combinations for an `M\times N` grid and is infeasible. The allowed-mask test collapses a complete-choice search into independent row witnesses.
- **Dynamic programming over reachable OR values:** Maintain every OR obtainable after each row. With `B` bits there can be up to `2^B` states, which is avoidable because numeric mask feasibility supports a direct greedy decision.
- **Choose the smallest number from each row:** A row's numerically smallest value is not always best for the combined OR; a slightly larger value may reuse bits already forced by other rows instead of introducing a new high bit.
- **Clear bits from least significant to most significant:** This can sacrifice a high bit to save lower bits, producing a numerically worse answer. Decisions must follow significance from high to low.
- **Binary search the answer as an integer:** Feasibility is monotone under adding allowed bits by subset inclusion, not necessarily under ordinary numeric order. A smaller integer can forbid a useful lower-bit combination that a different smaller-or-larger mask allows.
- **Confuse OR containment with numeric comparison:** `x <= mask` does not imply that `x`'s set bits are contained in `mask`. The exact test is `(x | mask) == mask`, or equivalently `x & ~mask == 0`.
- **One row:** The result is simply that row's minimum value. The bit greedy reconstructs that minimum by testing which bit prefixes some row value can satisfy.
- **One column:** Every row choice is forced, so the answer is the OR of that column. Failed feasibility tests force exactly those bits.
- **Repeated values and duplicate columns:** They do not affect existence. The inner loop stops at the first compatible witness in each row.
- **A bit absent from every cell:** Every row passes when that bit is tentatively forbidden, so it remains zero.
- **Positive-value contract:** `mx` is at least one, so `bit_length` is positive. The same logic would also handle zeros if they were allowed, but an all-zero grid would need the empty bit loop, naturally returning zero.
- **Witnesses are not stored:** Feasibility at each prefix is enough to determine the minimum OR. If the actual chosen cells were required, an additional reconstruction pass or stored witnesses would be necessary.
- **Early row failure:** Once one row has no compatible value, the trial is impossible and the source may stop scanning that bit. This improves typical time but not the worst-case bound.
