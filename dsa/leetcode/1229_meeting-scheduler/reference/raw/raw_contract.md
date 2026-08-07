## Function Contract

**Inputs**

- `slots1`: The first person's availability slots.
- `slots2`: The second person's availability slots.
- `duration`: The required meeting length.

Let $n = \lvert\texttt{slots1}\rvert$ and $m = \lvert\texttt{slots2}\rvert$. Every slot contains exactly two integer endpoints `[start, end]` with `start < end`. Slots belonging to the same person are pairwise nonintersecting, but neither input list is guaranteed to arrive in chronological order.

The source describes slot endpoints as inclusive. Meeting length follows elapsed-time semantics: a meeting that begins at `start` and lasts `duration` is returned as `[start, start + duration]`.

**Return value**

Return `[start, start + duration]` for the feasible meeting with the earliest `start`. Return `[]` if no pair of slots shares at least `duration` time units.
