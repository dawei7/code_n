## General

**Use the permutation property to identify exactly what must move**

Because `nums` is a permutation of `0` through `n - 1`, the sorted array is completely determined: value `i` belongs at index `i`. An entry is already correct when `nums[i] == i`. Such an entry does not have to participate in any swap.

Let `S` be the set of values currently at incorrect indices:

`S = { nums[i] : nums[i] != i }`.

If `S` is empty, the array is already sorted and the required return value is zero. Otherwise, every value in `S` must eventually move, because its present index is not its final index.

The surprising result is that the maximum feasible swap parameter is simply the bitwise AND of all values in `S`. The source computes that AND in one pass without explicitly storing the set.

**Why every feasible `k` is bounded by the misplaced values**

An allowed swap exchanges two current values `a` and `b` only when

`a AND b = k`.

Every bit that is set in `k` must therefore be set in both `a` and `b`. In particular, whenever a value participates in an allowed swap, it contains every set bit of `k`.

Each initially misplaced value must participate in at least one swap before the array can become sorted. Consequently, every set bit of a feasible `k` must appear in every value in `S`. The largest bit pattern with that property is

`K = AND of all values in S`.

Any feasible `k` can contain only bits present in `K`; in bitmask language, `k` must be a submask of `K`. Removing set bits never increases a non-negative integer, so no feasible parameter can be numerically larger than `K`. This establishes an upper bound, but an upper bound alone is not enough—we must also know that `K` really permits sorting.

**The value `K` itself is a universal swap pivot**

The permutation contains every integer from zero to `n - 1` exactly once. Since a bitwise AND cannot exceed any non-negative operand, `0 <= K <= x <= n - 1` for every `x` in `S`. Thus the value `K` exists somewhere in the permutation, even if it happens to be already at index `K`.

By definition of `K`, every misplaced value `x` contains all bits of `K`. ANDing `x` with the value `K` removes any extra bits of `x` and leaves exactly `K`:

`x AND K = K`.

Therefore, for the chosen parameter `k = K`, the item whose value is `K` may be swapped with every misplaced value. It acts as a universal pivot.

This remains useful even when `K` began in its correct position. Correct elements are not forbidden from moving temporarily; only the final arrangement matters. The pivot can leave its home, help rearrange other values, and return afterward.

**Why a universal pivot can realize every required rearrangement**

It is enough to show that two non-pivot misplaced values `a` and `b` can be exchanged while the pivot ends where it began. Perform these three value-based swaps:

1. Swap `K` with `a`.
2. Swap `K`, now at `a`’s former position, with `b`.
3. Swap `K` with `a` again.

Every one of those swaps is allowed because `K AND a = K` and `K AND b = K`. The combined effect exchanges `a` and `b` and restores `K` to its original location. Any permutation can be corrected using a sequence of ordinary pairwise exchanges, so replacing each required exchange by this three-swap pivot sequence proves that all misplaced values can be sorted using parameter `K`.

If the pivot value `K` is itself misplaced, the same connectivity argument is even more direct: it can swap with whichever misplaced value must occupy its current position, repeatedly resolving the permutation’s cycles. Either way, the star of allowed connections centered at value `K` is enough; misplaced values do not need to be directly swappable with one another.

We now have both directions. No feasible parameter can exceed `K`, and choosing `K` is sufficient. Hence `K` is exactly the maximum answer.

**How the source computes the intersection of bits**

The source initializes `ans = -1`. In Python’s bitwise model, `-1` behaves like an unbounded sequence of one bits, so

`-1 & x = x`

for every non-negative `x`. This makes `-1` a convenient identity value for an AND reduction. Whenever `i != x`, the statement `ans &= x` keeps only the bits shared by the previously seen misplaced values and `x`.

Correctly placed values are skipped. Including them would be wrong because they do not have to move and therefore do not constrain the allowed `k`. For example, the value zero may be correctly placed at index zero. ANDing it into the answer would force the result to zero even when all actual misplaced values share a larger bitmask.

If at least one value is misplaced, the first such value changes `ans` from `-1` to that value, and all later operations keep `ans` non-negative. If no value is misplaced, `ans` remains `-1`. The final `max(ans, 0)` converts only that already-sorted sentinel case to the required answer zero.

**Trace the first two examples**

For `[0, 3, 2, 1]`, values zero and two are fixed. The misplaced values are three and one, so `K = 3 AND 1 = 1`. Those two values can be swapped directly because their AND is one, producing the sorted permutation.

For `[0, 1, 3, 2]`, only three and two are misplaced. Their AND is two, so `k = 2` is both feasible and maximal. A larger value would require a bit not shared by both values and therefore could not be the result of their necessary swap participation.

For the reverse permutation `[3, 2, 1, 0]`, every value is misplaced and their common AND is zero. The value zero is the universal pivot because `0 AND x = 0` for every value `x`. Parameter zero allows the necessary rearrangement, while no positive bit is shared by all values that must move.

## Complexity detail

Let `n` be the permutation length. The loop visits each index-value pair exactly once. Each comparison and bitwise AND operates on values bounded by `n - 1` and is treated as constant time under the usual machine-integer model. Total time is therefore `O(n)`.

The algorithm stores only the running answer plus the loop variables `i` and `x`. It never constructs `S`, a graph of allowed swaps, permutation cycles, or a copy of the array. Its auxiliary-space complexity is `O(1)`.

The proof uses a conceptual pivot-swap sequence, but the method does not have to perform those swaps because the task asks only for the maximum `k`, not for the sorted permutation or a list of operations. Constructing an explicit sequence could require `O(n)` swaps and output space, but that is outside the requested return value.

## Alternatives and edge cases

- **Build the misplaced set explicitly:** Collecting all `nums[i]` with `nums[i] != i` and reducing them afterward yields the same answer, but it spends `O(n)` extra space that the streaming AND does not need.
- **Binary search the numeric value of `k`:** Feasibility is not monotone in ordinary numeric order, because changing bits can create or destroy exact-AND edges unpredictably. The common-bit argument derives the unique maximum directly.
- **Build an allowed-swap graph:** For a candidate `k`, one could connect pairs whose AND equals `k` and analyze whether permutation cycles can be resolved. Considering all pairs is quadratic, and the value-`K` pivot proves connectivity without constructing the graph.
- **AND every array value:** Correctly placed values impose no necessary swap condition. Including them can erase bits and produce an answer smaller than the true maximum.
- **OR instead of AND:** OR records bits present in at least one misplaced value. A permitted `k` needs each of its bits in every value that must move, so intersection by AND is the required operation.
- **Already sorted permutation:** No value needs a swap. The running sentinel remains `-1`, and `max(ans, 0)` returns the explicitly required zero.
- **Exactly two misplaced values:** A permutation cannot have exactly one misplaced position. With two, their values must exchange, and the answer is their direct bitwise AND.
- **Answer zero:** Zero is always a valid pivot value because the permutation contains zero and `0 AND x = 0`. A zero answer does not mean sorting is impossible; it means the misplaced values share no positive bit.
- **Pivot initially fixed:** The value `K` may temporarily leave index `K`. Three pivot swaps can exchange two other values and restore it, so being initially correct does not make it unusable.
- **Duplicate values:** The proof relies on `nums` being a permutation. If duplicates or missing values were allowed, value `K` might not exist as a pivot, and the same formula would no longer be justified.
- **Why `K` stays in range:** A bitwise AND of non-negative operands cannot introduce a bit absent from an operand, so `K` is no larger than each misplaced value and is one of the permutation’s legal value-domain integers.
- **Python’s `-1` sentinel:** The identity `-1 & x = x` is language-specific bitwise behavior. In a fixed-width unsigned implementation, initialize with all bits set over the value domain or handle the first misplaced value separately.
- **Missing type import:** The stored source uses `List` without importing it. The judge may provide that typing symbol, while standalone Python would require `from typing import List`.
