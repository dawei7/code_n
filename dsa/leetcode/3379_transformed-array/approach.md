## General

**Compute each destination directly.** Starting from index `i`, moving right by positive `x` or left by `abs(x)` is the same signed index arithmetic:

$$
\text{destination}=i+x.
$$

The only extra work is wrapping that integer into the valid circular range 0 through $n-1$.

**Use modulo for circular wrapping.** Indices that differ by a multiple of $n$ refer to the same circular position. The canonical destination is

$$
(i+x)\bmod n.
$$

The source writes this as

`(i + x % n + n) % n`.

First reducing `x` prevents unnecessarily large offsets. Adding `n` before the final modulo is a common language-independent way to protect against negative remainders. In Python, `x % n` is already nonnegative for positive `n`, so the addition is redundant but harmless.

**Positive values move right.** If `x=3`, adding three to `i` advances three array positions. Crossing index `n-1` wraps because the final modulo removes full cycles.

**Negative values move left.** If `x=-2`, adding it subtracts two from `i`. Python normalization maps a negative raw index to the equivalent index near the end of the circular array.

**Zero stays at the same index.** With `x=0`, the expression becomes `i`. The returned value is `nums[i]`, exactly matching the separate zero rule without needing a branch.

**Read every destination from the original array.** The list comprehension constructs a new list. It never writes into `nums` while other destinations are being computed. This independence matters: the movement rule uses original values, not earlier transformed outputs.

**Trace `[3,-2,1,1]`.** With $n=4$:

- at index zero, destination is $(0+3)\bmod4=3$, giving one;
- at index one, destination is $(1-2)\bmod4=3$, giving one;
- at index two, destination three gives one;
- at index three, destination zero gives three.

The result is `[1,1,1,3]`.

**Large movements simply contain full cycles.** Moving `x=n` steps returns to the starting index. Moving `n+1` is equivalent to moving one. Negative offsets behave symmetrically. Reducing by `x % n` captures this equivalence before combining with `i`.

**Separate displacement from the value eventually copied.** The current value `x = nums[i]` is used only to choose a destination index. Once that index is known, the output receives `nums[destination]`, not the normalized displacement and not the destination number itself. This distinction is easy to miss when reading the compact comprehension.

For example, if the destination index is two and `nums[2] = -7`, the result stores negative seven. It does not move seven more positions. Every output entry performs exactly one lookup.

**Why reducing `x` before adding `i` is equivalent.** Write `x = qn + r`, where `r = x % n`. Then

$$
i+x=i+qn+r.
$$

The term $qn$ represents complete circles and vanishes modulo $n$, leaving the same destination as `i+r`. The extra `+n` also vanishes under the final modulo. Therefore the exact expression is algebraically identical to `(i+x) % n` for every positive, zero, or negative input value.

**Each output calculation is independent even when destinations overlap.** Several starting positions may land on the same source index and copy the same value. No capacity is consumed and no source value is removed, so this many-to-one mapping is permitted.

**Why one formula covers every rule.** Signed addition captures direction, modulo captures repeated wrapping, and zero addition captures the stationary case. The comprehension applies that exact mapping once per original index, so every output position receives the specified source value.

**Why the output order is correct.** `enumerate(nums)` yields pairs in increasing index order. Each computed source value is appended to the list in that same order, so output position `i` corresponds to the action originating at input position `i`.

## Complexity detail

Let $n$ be the array length. The comprehension performs constant arithmetic and one lookup for every element, taking $O(n)$ time.

The returned list contains $n$ elements and uses $O(n)$ space. Aside from the required output, local variables use $O(1)$ auxiliary space. Python integer modulo cost is constant under these small bounded values.

## Alternatives and edge cases

- **Step-by-step movement:** Simulating every step can cost proportional to the magnitudes of values and repeats full cycles.
- **Branch on sign:** Separate positive, negative, and zero formulas work but are unnecessary.
- **In-place transformation:** It would corrupt later reads unless a full original copy were retained.
- **Single-element array:** Every movement wraps to index zero, so the result equals the input.
- **Value zero:** Destination is the current index.
- **Value equal to `n`:** One full circle returns to the current index.
- **Large positive value:** Modulo removes complete rightward cycles.
- **Large negative value:** Modulo normalizes complete leftward cycles.
- **Landing on a negative value:** The output stores that value; it does not trigger another movement.
- **Independent actions:** Movement chains are not followed recursively.
- **Python negative modulo:** It already returns a nonnegative residue, making `+n` defensive rather than necessary.
- **Nonempty constraint:** It guarantees modulo divisor `n` is positive.
- **Output identity possibility:** Different starting indices may read the same destination without conflict.
- **One lookup only:** Landing on another nonzero value does not trigger a second movement.
- **Copied value versus index:** The output stores `nums[destination]`, not `destination`.
- **Input preservation:** The list comprehension never mutates `nums`.
- **Type imports:** `List` must be available for annotations.
