## General

**Fix the leftmost unresolved bit**

Suppose the scan has reached index `i`, and all earlier bits are already
`1`. Every operation beginning before `i` has already been decided, while
an operation beginning after `i` cannot touch `nums[i]`. Therefore:

- if `nums[i]` is `1`, flipping the window at `i` would only make it wrong;
- if `nums[i]` is `0`, the window starting at `i` is the only remaining
  operation that can make it `1`, so that flip is forced.

Process each start index from `0` through `n - 3`. Whenever the current bit
is zero, flip that bit and the next two bits and increment the operation count.

**Why the greedy count is minimum**

The decision at every scanned index is unique, not merely locally attractive.
Any successful sequence must make exactly the same choice there, because no
later window can repair that position. Inductively, the greedy scan performs
every operation required by any solution and no optional operation, so its
count is minimum.

After the final possible window start is processed, the last two bits can no
longer be changed without disturbing an already fixed earlier bit. If both are
`1`, the forced sequence succeeds; otherwise the target is impossible and
the answer is `-1`.

## Complexity detail

The scan visits each of the $n$ positions at most once, and every chosen
operation flips exactly three values, so the running time is $O(n)$. The
implementation mutates the working input and uses only counters and indices,
for $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Track active flips without mutation:** A fixed-size parity window can
  derive each effective bit while leaving the input unchanged. It also runs in
  $O(n)$ time and uses $O(1)$ space because the window length is fixed at
  three, but it is less direct here.
- **Repeatedly search for the first zero:** Applying the same forced rule via
  `index(0)` is correct, yet rescanning the settled prefix makes it $O(n^2)$.
- **Breadth-first search over arrays:** Exploring all flip combinations can
  prove optimality on tiny inputs but has exponentially many states and is
  unnecessary because every decision is forced.
- An all-ones array needs zero operations.
- A zero among the final two positions after the scan proves impossibility.
- The minimum legal length is three; an all-zero length-three array is solved
  by exactly one flip.
- Overlapping chosen windows are expected, and earlier flips may determine
  whether the next window is forced.
