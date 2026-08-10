## General

**Generate allowed numbers as a digit tree**

Starting from zero, appending digit `d` creates `x * 10 + d`. The source performs breadth-first search over this construction tree, using a deque initialized with zero.

Each popped number is tested before its children are appended. A qualifying value must be strictly greater than `k`, divisible by `k`, and within the signed 32-bit limit.

**Put the smaller digit branch first**

If `digit1 > digit2`, the method recursively calls itself with the digits swapped. After that normalization, children are enqueued in ascending digit order.

Breadth-first traversal processes shorter digit sequences before longer ones, and ascending child order gives lexicographic order within a fixed length. For canonical positive decimal strings, shorter length means smaller value and lexicographic order matches numeric order. Therefore the first qualifying canonical value is the smallest.

If the digits are equal, only one child is enqueued, avoiding two identical branches.

**How a zero digit affects the queue**

The search begins at numeric zero so it can build every allowed digit sequence uniformly. If the smaller digit is zero, appending it to zero produces zero again. More generally, leading-zero sequences generate duplicate numeric values.

These duplicates delay the search but do not invalidate the first-answer guarantee. The first canonical representation of every positive number appears at its natural length in ordinary breadth-first and lexicographic order. A later leading-zero representation only repeats a value whose canonical representation was already processed; it cannot introduce a new smaller answer after a larger canonical answer.

A visited set or special handling of leading zero could eliminate duplication, but the exact source uses neither.

**Test the strict and divisibility conditions**

`x > k` enforces "larger than," so `k` itself is never returned even though it is always divisible by itself. `x % k == 0` checks that the remainder is zero.

These tests occur after the limit check and before expansion. The value zero never qualifies because $k\ge1$ and zero is not greater than $k$.

For `k=2` and digits zero and two, values such as two fail the strict condition, while 20 is greater and divisible by two, so it is returned.

**Stop at the 32-bit boundary**

When a popped `x` exceeds $2^{31}-1$, the source returns -1. In canonical BFS order, every not-yet-seen new positive representation is no smaller than the first over-limit canonical value. Later smaller queue values caused by leading zeroes are duplicates of values already processed at shorter depths.

Thus no unseen valid in-range number remains, and -1 is correct.

The source may enqueue children larger than the limit, but it checks them when popped and never expands the first over-limit value.

**Handle two zero digits**

If both digits are zero, every generated integer is zero. No value can be greater than positive `k`, so the source immediately returns -1. This guard also prevents an endless zero-only queue.

**Why breadth-first order yields the minimum**

Every positive integer composed only of the allowed digits has a path from zero whose edge labels are its decimal digits, possibly with leading-zero duplicates. BFS reaches its canonical path by increasing digit length. Digit normalization and enqueue order visit canonical strings lexicographically within a length.

Numeric decimal order is length first, then lexicographic for equal length. Therefore the first new canonical number satisfying the conditions is the globally smallest legal integer.

**Search size**

With two distinct digits, depth $D$ has up to $2^D$ generated digit sequences. The 32-bit bound limits useful canonical decimal length to at most ten digits, but leading-zero duplicate paths still contribute to the breadth of each explored level.

This brute generation is acceptable under the fixed limit, though a remainder-state BFS could avoid storing full exponential candidate trees.

## Complexity detail

Let $D$ be the number of digit positions explored before a solution or the 32-bit cutoff. With two distinct digits, the source can generate $O(2^D)$ queue nodes and takes $O(2^D)$ time and space. With identical digits, branching drops to one per level.

The deque stores candidate Python integers. The recursive digit swap adds only one call and constant space.

## Alternatives and edge cases

- **BFS over remainders modulo `k`:** Tracks at most $k$ states and can reconstruct the smallest digit string, avoiding duplicate full-number generation; the strict-greater and 32-bit conditions need careful handling.
- **Enumerate multiples of `k`:** Test $2k,3k,\ldots$ until the limit, which can require roughly $2^{31}/k$ checks.
- **Depth-first generation:** Does not naturally visit values in numeric order and may find a larger answer first.
- **Both digits zero:** Immediate -1 because only zero can be formed.
- **Equal nonzero digits:** Only one branch is needed at each depth.
- **One digit zero:** Leading-zero paths create duplicates but not new numerical values.
- **Digits supplied in reverse order:** The recursive swap normalizes their generation order.
- **Candidate equals `k`:** Rejected by the strict `x > k` test.
- **No in-range solution:** The first unseen canonical value beyond the limit proves -1.
- **Boundary value $2^{31}-1$:** Allowed because rejection uses strictly greater than the limit.
- **Duplicate queue values:** They affect efficiency, not correctness.
- **Imported deque:** The exact source assumes `deque` is available in the execution environment.
