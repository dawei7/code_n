## General

**Combine pairwise compatibility into one mask.** In a nice window, no bit is
set by more than one element. The bitwise OR of the window therefore records
all bits currently in use. A new value can join exactly when its AND with this
aggregate mask is zero.

**Shrink only while a collision exists.** Maintain left and right boundaries
and the aggregate `used_bits`. If the next value shares a bit with the mask,
remove elements from the left until the collision disappears. Once the value
fits, OR it into the mask and update the best window length.

**Why XOR removes an outgoing value.** The current window is nice before the
new value is inserted, so every set bit belongs to exactly one resident
element. XOR with the outgoing value consequently clears precisely its bits
and cannot disturb bits owned by another element. This property would not be
safe for an arbitrary window containing duplicated set bits.

After shrinking, the maintained interval is nice and is the longest nice
interval ending at the current right index: any earlier left boundary retained
the conflicting bit. Every possible right endpoint is processed, so the
largest recorded length is globally optimal. Each element enters once and is
removed at most once.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The right boundary advances $n$ times and
the left boundary advances at most $n$ times in total, giving $O(n)$ time.
The boundaries, answer, and one integer bitmask use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate all intervals:** Incrementally OR-ing each interval still
  examines $O(n^2)$ candidates and is unnecessary.
- **Per-bit frequency array:** Maintain counts for the at most 30 relevant bit
  positions and shrink while any count exceeds one; this remains $O(n)$ time
  with a larger constant.
- **Recompute the window mask:** Rebuilding the OR after every left-boundary
  move can repeatedly scan the window and degrade to quadratic work.
- **Single element:** It is always nice, including when it has many set bits.
- **Duplicate values:** Two equal positive values share at least one bit and
  cannot coexist in a nice window.
- **Several simultaneous conflicts:** Removing one left element may not clear
  every bit shared with the incoming value, so shrinking uses a `while` loop.
- **Maximum nice length:** Positive values at most $10^9$ use only 30 possible
  bit positions, so a nice window cannot contain more than 30 elements, though
  the array itself may be much longer.
