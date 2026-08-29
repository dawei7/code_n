## General

Only parity matters. Adjacent swaps can move even and odd elements, but swapping two elements of the same parity never improves the parity pattern. The source records positions of evens and odds, determines feasible starting parity, and matches one parity class to target positions `0,2,4,\ldots`.

**Feasibility**

An alternating length-`n` arrangement has parity counts differing by at most one.

If the input even/odd counts differ by more than one, no permutation can alternate, so the source returns `-1`.

If one parity has one extra element, it must occupy both ends and therefore must start at position zero. If counts are equal, either parity may start.

**Position lists**

`pos[0]` stores original indices of even values and `pos[1]` stores odd indices. Because the input is scanned left to right, each list is sorted.

`calc(k)` assumes parity `k` occupies even target indices:

`0,2,4,...`.

It pairs these targets with `pos[k]` in their existing order and sums absolute movements.

**Why order-preserving matching is optimal**

Elements of the same parity are interchangeable for validity. Under adjacent swaps, there is no benefit to making two same-parity elements cross: exchanging their assigned targets removes the crossing and cannot increase total distance.

Therefore the first current even should go to the first even target, the second to the second, and similarly for odds. This sorted matching minimizes total displacement.

The sum

$$
\sum_t |current_t-target_t|
$$

equals the minimum adjacent swaps. Each swap between opposite parities moves one tracked parity element one position toward its target. Same-parity swaps are unnecessary, and the order-preserving plan can realize all required movements.

Counting movement for only one parity does not miss a factor of two. One adjacent even-odd swap moves both elements, but it is one operation and advances exactly one tracked parity token by one position. Summing that class’s displacement counts each swap once.

**Choosing the start**

If evens are more numerous, only `calc(0)` is feasible. If odds are more numerous, only `calc(1)` is feasible.

When counts tie, both alternating patterns exist. The source computes both and returns their minimum.

**Example**

For parity pattern even, even, odd, odd, even, even positions are `[0,1,4]`. With even starting, targets are `[0,2,4]`, so movement is `0+1+0=1`. One adjacent swap creates alternation.

Actual integer magnitudes and distinctness do not affect this movement calculation; only positions and parity matter.

## Complexity detail

Building position lists takes `O(n)` time. Each `calc` call scans one parity list, and at most two calls are made, so total time is `O(n)`.

The exact source stores every even and odd index in `pos`, using `O(n)` auxiliary space. This contradicts the manifest’s `O(1)` claim. A streaming mismatch-count method may achieve constant extra space, but the protected implementation uses lists.

## Alternatives and edge cases

- **Simulate adjacent swaps:** Moving misplaced elements directly can also be linear with careful pointers, but position matching proves the count without mutating the array.
- **Try arbitrary permutations:** Values within a parity class are interchangeable; factorial enumeration is unnecessary.
- **Count mismatched positions only:** A misplaced element may need to travel several cells, so mismatch count alone does not equal adjacent-swap cost.
- **Count difference above one:** Alternation is impossible and returns `-1`.
- **Equal counts:** Both starting parities must be evaluated; costs can differ.
- **One extra even:** Even must occupy index zero and every even target.
- **One extra odd:** Odd must start.
- **Single element:** Count difference is one, its parity starts, and movement sum is zero.
- **Already alternating:** Current and target positions match, producing zero.
- **All same parity with n>1:** Count difference exceeds one and is impossible.
- **Negative integers:** Outside current positive constraints, `x&1` still classifies Python odd/even parity consistently.
- **Distinctness:** It is irrelevant to the parity-token proof but guaranteed by the statement.
- **No input mutation:** Position lists are derived while `nums` remains unchanged.
- **Why zip lengths match:** Feasibility and selected starting parity guarantee the tracked class count equals the number of even-index targets.
- **Manifest space mismatch:** Both position lists together always contain exactly `n` indices, so their storage cannot be called constant.
- **Crossing argument:** If two same-parity elements at positions `a<b` were assigned to targets `y<x`, swapping their assignments changes cost from `|a-x|+|b-y|` to `|a-y|+|b-x|` and never increases it. Repeating removes every crossing, proving sorted-to-sorted matching.
- **Why values are irrelevant:** Adjacent-swap validity observes only even versus odd. Distinct magnitudes do not change target slots or movement cost, so preserving numerical order within a parity class is unnecessary beyond the no-crossing position order.
- **Realizing the distance sum:** Move tracked parity elements toward their assigned slots from left to right. Each crossing with the opposite parity costs one adjacent swap and decreases remaining tracked displacement by one, constructing a sequence with exactly the calculated total.
