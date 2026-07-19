## General
**Generate only numbers that can qualify.** A positive stepping number cannot begin with zero, so place the one-digit values `1` through `9` into a breadth-first queue. If a dequeued number ends in digit `d`, any longer stepping number with that prefix must append either `d - 1` or `d + 1`. Append only the digits that remain within `0` through `9`, and do not enqueue a child larger than `high`.

**Keep the requested order without a final sort.** Breadth-first processing visits all one-digit numbers before all two-digit numbers, then all three-digit numbers, and so on. Within a fixed length, parent prefixes are processed in increasing order and each parent's smaller child is enqueued before its larger child. The generated positive values are consequently visited in increasing order. Add a visited value to the answer exactly when it is at least `low`; handle `0` separately because leading zero is not used as a generation seed.

**Why the generation is complete and exact.** Removing the last digit from any positive multi-digit stepping number leaves a shorter positive stepping number. Repeating that removal eventually reaches its nonzero first digit, which is one of the queue seeds. At each reconstruction step, the removed digit must differ from the current last digit by exactly $1$, so the breadth-first transitions recreate the number. Conversely, every transition appends precisely such a digit, so it cannot create a non-stepping number. Range checks then retain exactly the required values.

## Complexity detail
Each of the $S$ generated stepping numbers is enqueued and removed at most once, and each removal performs constant work. The time is $O(S)$. The answer and breadth-first queue together hold $O(S)$ values. The numeric digit length is bounded by the input constraint and does not add a larger term.

## Alternatives and edge cases
- **Scan every integer in the range:** Checking adjacent digits of every candidate is straightforward but takes time proportional to the width of the numeric interval rather than to the much smaller set of stepping numbers.
- **Depth-first generation plus sorting:** The same prefix transitions can be explored recursively, but arbitrary depth-first order requires an additional sort and uses recursion stack space.
- **Digit dynamic programming:** A digit-DP formulation is useful when only a count is requested over enormous string bounds, but it is unnecessary when this problem must enumerate the actual values under a 32-bit-scale bound.
- **Zero:** Include `0` exactly when `low` is `0`; never use it as a prefix for longer numbers.
- **Single-digit interval:** Every value from `0` through `9` is a stepping number.
- **Boundary digits:** A number ending in `0` has only a `1` child, while one ending in `9` has only an `8` child.
- **Inclusive endpoints:** Values equal to `low` or `high` must be returned when they satisfy the digit rule.
