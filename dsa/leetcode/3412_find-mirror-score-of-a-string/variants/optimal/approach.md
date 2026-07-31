## General

For each letter, store the indices at which that letter has appeared but has not yet been marked. When the scan reaches index `i`, the only eligible partners are in the collection for the mirror of `s[i]`.

The process requires the closest eligible index on the left. Indices enter each letter's collection in increasing order, so the closest one is always the most recently stored index. A stack therefore implements the rule directly: pop from the mirror stack when it is non-empty, add the index distance, and do not store `i` because it is immediately marked. If the mirror stack is empty, push `i` onto the stack for its own letter so a future mirror may use it.

The mirror of zero-based alphabet position $c$ is $25-c$. Thus 26 stacks are enough for every lowercase letter. At every step, a stack contains exactly the earlier unmarked indices carrying that letter: unmatched indices are pushed once, and a matched index is removed exactly when it is marked. Its top is consequently the closest valid `j`, so every score increment matches the prescribed process.

## Complexity detail

Each index is pushed at most once and popped at most once. All other work per character is constant, giving $O(n)$ time. In the worst case no character finds a mirror, so the stacks retain all $n$ indices and use $O(n)$ space.

The benchmark defines `size` as the string length and uses legal all-`a` strings of lengths 64, 256, and 512, spanning 8x. The accepted stack simulation is linear. A correct direct simulation that scans backward at every index to locate the closest unmarked mirror performs $O(n^2)$ work on these no-match inputs and must fail only the scaling verdict.

## Alternatives and edge cases

- **Backward search from every index:** This follows the statement literally but takes $O(n^2)$ time when mirrors are absent or far away.
- **Queues instead of stacks:** A queue selects the earliest unmarked mirror, violating the closest-index requirement.
- **Single character:** It has no earlier index and contributes zero.
- **Marked indices:** A popped partner is removed permanently, and a current index that finds a partner must not be pushed.
- **Symmetric arrival order:** Either member of a mirror pair may appear first; the same stack lookup handles both directions.
- **Repeated letters:** Multiple unmatched copies accumulate in increasing order and are consumed from the most recent one backward.
- **No mirror pairs:** Every index remains stored and the final score is zero.
