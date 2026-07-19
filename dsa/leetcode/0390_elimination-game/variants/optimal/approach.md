## General
**Represent the survivors as an arithmetic progression**

At every round, the remaining values have a first element `head`, a fixed gap `step`, and a count `remaining`. Initially these are `1`, `1`, and `n`. Eliminating alternating positions preserves an arithmetic progression, doubles its gap, and halves its count.

**Decide when the first survivor disappears**

A left-to-right pass always removes the current head, so advance `head` by `step`. On a right-to-left pass, the head is removed only when the number of remaining elements is odd: an odd-length sequence deletes both ends, whereas an even-length sequence keeps its left end.

**Update the compressed state after each round**

After applying the possible head shift, replace `remaining` with `floor(remaining / 2)`, double `step`, and reverse the direction. Once one value remains, the arithmetic progression's head is that value.

**Why no survivor values need to be stored**

The progression state exactly describes every live value as `head + k * step`. The head-shift rule selects the correct first survivor for either direction, and doubling the step describes taking every second element. Inductively, the compressed state matches the explicit sequence after every round, including the final singleton.

## Complexity detail
Each round halves `remaining`, so there are $O(\log n)$ rounds with constant work apiece. Four scalar state variables use $O(1)$ space.

## Alternatives and edge cases
- **Recursive recurrence:** can derive the survivor from the reversed smaller game in $O(\log n)$ time, using $O(\log n)$ call-stack space.
- **Explicit list simulation:** directly filters survivors but takes $O(n)$ total work and $O(n)$ storage.
- **Linked-list deletion:** avoids array shifts but still constructs all `n` nodes and performs linear total deletions.
- With $n = 1$, no round runs and the answer remains one.
- Left-to-right rounds always advance the head.
- Right-to-left rounds advance the head only for an odd survivor count.
- Integer division correctly discards the eliminated half after each round.
