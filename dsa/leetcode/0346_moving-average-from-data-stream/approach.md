## General

**Store only the fixed number of values that can still affect an answer.**

After at least `size` calls, every new average depends only on the newest `size` stream values. Anything older can never reenter a future window, so retaining the entire stream would waste memory.

The exact source uses a fixed-length list as a circular buffer. It also keeps a running sum, allowing each new average to be calculated without summing the buffer again.

The three object fields are:

- `self.data`: an array of exactly `size` slots;
- `self.s`: the sum of the values currently in the live window;
- `self.cnt`: the total number of calls already completed.

The manifest summary mentions a deque, but the checked-in source uses modular indexing into an array. Both designs have similar asymptotic bounds, yet the overwrite behavior here is specifically circular-buffer behavior.

**Initialize empty slots with zero.**

The constructor creates `self.data = [0] * size`. Before the window fills, some buffer slots do not represent actual stream values. Zero is a convenient neutral placeholder because subtracting it does not alter the running sum.

The constructor also sets `self.s = 0` and `self.cnt = 0`, matching an empty stream. The contract guarantees `size >= 1`, so the buffer is never empty and modular indexing is always defined.

**Find the slot for the next value.**

At the start of a `next(val)` call, the source computes

$$
i=\text{cnt}\bmod\text{size}.
$$

For the first `size` calls, this yields indices `0, 1, ..., size - 1`, filling unused slots from left to right. After that, the remainder wraps back to zero and repeats cyclically.

When the buffer is full, slot `i` contains exactly the value that arrived `size` calls earlier—the oldest value in the current window. That is the value that must expire when `val` enters.

For a buffer of length three, write indices follow

$$
0,1,2,0,1,2,\ldots.
$$

On the fourth call, index zero holds the first stream value, which is exactly the one no longer among the newest three.

**Update the sum before overwriting the slot.**

The assignment

`self.s += val - self.data[i]`

adds the entering value and subtracts the value leaving from slot `i`. It must read `self.data[i]` before that slot is overwritten. Reversing these operations would lose the expired value and make it impossible to remove its contribution.

During the initial filling phase, `self.data[i]` is zero, so the update simply adds `val`. Once full, it performs the exact sliding-window transition

$$
\text{new sum}
=\text{old sum}+\text{new value}-\text{oldest value}.
$$

The source then stores `val` in `self.data[i]`. This makes the circular buffer ready to treat that value as the oldest one after another `size` calls.

**Increment the count and choose the correct denominator.**

After inserting the value, `self.cnt += 1` records that one more stream item has been seen. The number of actual values in the current window is

$$
\min(\text{cnt},\text{size}).
$$

Before the buffer fills, the average must divide by the number of calls so far, not by unused capacity. After it fills, every live window contains exactly `size` values.

Returning

`self.s / min(self.cnt, len(self.data))`

therefore uses the correct denominator in both phases. Python's `/` produces a floating-point result even when the division is exact.

**Walk through window size three.**

Start with `data = [0,0,0]`, sum zero, and count zero.

- `next(1)` writes index `0`. The sum becomes `0 + 1 - 0 = 1`, the count becomes one, and the average is $1/1=1.0$.
- `next(10)` writes index `1`. The sum becomes `11`, the count becomes two, and the average is $11/2=5.5$.
- `next(3)` writes index `2`. The sum becomes `14`, the count becomes three, and the average is $14/3$.
- `next(5)` wraps to index `0`, where old value `1` is stored. The sum becomes $14+5-1=18$, slot zero becomes `5`, and the average is $18/3=6.0$.

At that point, the logical live window is `[10,3,5]`, even though the physical buffer order is `[5,10,3]`. Circular storage does not need to arrange values chronologically because only the sum and next overwrite position matter.

**The state invariant.**

After `cnt` completed calls:

- `self.s` equals the sum of the newest `min(cnt, size)` values;
- each of those values appears in one circular-buffer slot;
- if fewer than `size` calls occurred, all remaining slots still contain their neutral initial zero;
- the next index `cnt % size` is unused during initial filling or contains the oldest live value after the buffer is full.

The constructor establishes this invariant for zero calls. A new call subtracts exactly the slot identified by the final point, adds and stores the new value, and advances the count. The invariant is therefore preserved. Dividing its exact sum by its exact live count proves every returned average is correct.

## Complexity detail

Let $w$ be the configured window size and $m$ the number of calls to `next`. Constructor allocation of the fixed array takes $O(w)$ time and $O(w)$ space.

Each `next` call performs a constant number of arithmetic operations, one array read, one array write, and no loop. Its worst-case time is $O(1)$, so $m$ calls take $O(m)$ total time.

The array never grows beyond $w$ slots, and the other fields are scalars. Persistent space is $O(w)$, matching the manifest's `O(size)` bound.

## Alternatives and edge cases

- **Deque plus running sum:** Append each new value, pop from the left when capacity is exceeded, and update the sum with both changes. It has the same $O(1)$ time per call and $O(w)$ space and matches the manifest wording, but needs a deque object rather than a fixed array.

- **Store the entire stream:** Append all values and sum the final window for every call. This can take $O(w)$ time per average and $O(m)$ storage, retaining values that will never matter again.

- **Recompute the circular-buffer sum:** Fixed storage alone controls space, but calling `sum(data)` each time would cost $O(w)$ per call. The running sum is what produces constant-time updates.

- **Window size one:** Every call overwrites the sole slot, subtracts the previous value, and returns the new value as a float.

- **Fewer calls than capacity:** Zero placeholders are subtracted, and the denominator uses `cnt`, so unused slots do not dilute the average.

- **Exactly full buffer:** On the `size`-th call, the last unused slot is filled and the denominator becomes `size`. Expiration begins only on the following call.

- **Negative stream values:** Running-sum addition and subtraction work normally; no positivity assumption is used.

- **Repeated values:** Each occurrence occupies its own arrival slot. Overwriting one old occurrence subtracts exactly one copy from the sum.

- **Physical versus chronological order:** The array's index order rotates after wrapping. Correctness depends on which slot expires next, not on printing the buffer in stream order.

- **Overflow in fixed-width languages:** The maximum live absolute sum can be proportional to `size * abs(val)`. Python integers grow automatically; other languages should choose a sufficiently wide accumulator.
