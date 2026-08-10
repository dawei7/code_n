## General

**Think of each operation as painting one horizontal layer**

Starting from zeros, one operation adds one across a contiguous interval. Imagine the target values as column heights. An operation paints one horizontal layer across consecutive columns.

The first column needs `target[0]` layers to begin. Moving from column `i-1` to `i`:

- If the new height is no larger, layers already started on the left can continue far enough to cover it. No new operation must begin here.
- If the new height is larger by `target[i] - target[i-1]`, that many additional layers must start at this position.

Therefore, the minimum is the first height plus every positive adjacent increase.

The exact source expresses this as

`target[0] + sum(max(0, b - a) for a, b in pairwise(target))`.

`pairwise` yields every adjacent `a, b` once, and the generator contributes only upward changes.

**A constructive schedule**

The formula is not merely a lower bound. Build the array layer by layer. At index zero, start `target[0]` interval operations. When moving right:

- End any layers no longer needed when the target decreases.
- Continue the remaining layers through the next column.
- Start exactly the positive height difference in new layers when the target rises.

Each started layer corresponds to one contiguous interval, ending wherever its height is no longer needed. This constructs the target using exactly the counted number of operations.

For `[1,2,3,2,1]`, one layer starts at index zero, another at index one, and another at index two. Their intervals can end at four, three, and two respectively, producing the target in three operations.

**Why every increase creates an unavoidable cost**

Consider boundary between indices `i-1` and `i`. Any operation covering both sides contributes equally to both values and cannot explain a higher target on the right. If `target[i]` exceeds `target[i-1]` by `d`, at least `d` operations must start at or after crossing that boundary while still covering index `i`.

At index zero, every unit of its target requires an operation beginning there because no earlier column exists.

Summing these independent required starts gives a lower bound:

$$
target[0]
+
\sum_{i=1}^{n-1}\max(0,target[i]-target[i-1]).
$$

The constructive schedule achieves the same number, proving optimality.

**Difference-array interpretation**

Define difference values with first entry `target[0]` and later entry `target[i]-target[i-1]`. Incrementing a subarray adds one at its left boundary in the difference array and subtracts one just after its right boundary.

Every positive difference unit requires an operation start. Negative differences can be supplied by endings of earlier operations and do not require new operations. The formula sums exactly the positive difference entries.

**Why decreases add nothing**

A decrease does not mean values need decrement operations; only increments are allowed. It means some intervals that built earlier columns simply stop before the lower column. Ending an interval is part of choosing its original range and costs no separate operation.

**Exact source behavior**

The input is guaranteed nonempty, so `target[0]` is safe. The method reads but does not mutate the target list. It assumes `pairwise` is available from `itertools` and Python 3.10 or newer.

**Tracing a mixed profile**

For `target = [3, 1, 5, 4, 2]`, the initial height contributes three. The drop from three to one contributes nothing because two existing layers simply stop. The rise from one to five contributes four new starts. Later drops again contribute nothing. The formula returns seven.

An explicit schedule can use one long layer across all five positions, two additional layers only at the first position, and four layers beginning at the third position with suitable ending points. Every operation corresponds to one counted start. This illustrates why a large rise after a valley cannot reuse layers that were forced to end before the low column.

## Complexity detail

Let $N$ be target length. `pairwise` and the generator are lazy, visiting each adjacent pair once. The sum performs constant work per pair, so time is $O(N)$.

Only generator state and scalar arithmetic are used, giving $O(1)$ auxiliary space, matching the manifest. No explicit difference array is allocated.

The result is guaranteed to fit a 32-bit integer, while Python would support larger exact values anyway.

## Alternatives and edge cases

- **Explicit difference array:** Build all adjacent differences and sum positive entries. It is correct but wastes $O(N)$ space.
- **Monotonic stack:** Layer starts and endings can be modeled with a stack, but the adjacent-rise formula is simpler.
- **Simulate every increment:** Applying operations one unit at a time to array values can be far too slow.
- **One element:** Exactly `target[0]` operations on that singleton are necessary.
- **Strictly increasing target:** Every positive difference contributes, and the total telescopes to the final height.
- **Strictly decreasing target:** Only the first height contributes; nested intervals can end successively.
- **Flat target:** One set of full-range layers builds every column together.
- **Valley then rise:** The rise after the valley starts new layers because earlier high layers had to end before the lower value.
- **No input mutation:** The generator only reads adjacent values.
- **Required import:** `pairwise` must be available from `itertools`.
