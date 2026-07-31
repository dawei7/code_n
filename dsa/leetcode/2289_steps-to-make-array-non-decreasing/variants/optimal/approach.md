## General

**Track when an element disappears**

Process values from left to right. Store stack entries
`(value, deletion_round)`. A deletion round of zero means that the element
survives indefinitely under the prefix processed so far. The stack retains
the only earlier values that can still influence later elements.

**Remove predecessors that cannot defeat the current value**

For a current value $x$, pop every stack value less than or equal to $x$.
None of those values can directly remove $x$. They may, however, delay when a
larger value farther left becomes adjacent to $x$, so retain the maximum
deletion round among the popped entries.

If the stack is empty afterward, no greater value survives to the left and
$x$ has deletion round zero. Otherwise the new top is strictly greater than
$x$. The intermediate popped elements must disappear first, and then $x$
disappears in the following simultaneous round. Its round is therefore one
plus the maximum popped round. With no popped entries, this correctly gives
round one.

Each pop discards an element that can no longer affect any future value except
through the accumulated delay just transferred to $x$. Thus the stack
recurrence records the exact first round in which every removable element
meets its surviving greater predecessor. The maximum recorded round is the
last deletion round, which is exactly when the array becomes non-decreasing.

## Complexity detail

Each of the $n$ values is pushed once and popped at most once. The amortized
running time is therefore $O(n)$, even though one iteration may pop several
entries. At most $n$ value-round pairs occupy the stack, using $O(n)$ space.

## Alternatives and edge cases

- **Round-by-round simulation:** Rebuilding the array after every simultaneous deletion is direct and correct, but one removal per round can force $O(n^2)$ time.
- **Linked-list event simulation:** Neighbor links avoid rebuilding arrays, but scheduling simultaneous rounds correctly is more complicated and still needs explicit event state.
- **Already non-decreasing:** No element has a greater left neighbor, so every recorded round and the answer are zero.
- **Strictly decreasing:** Every element except the first is removed in the first simultaneous round, so the answer is one rather than $n-1$.
- **Delayed cascade:** An array such as `[6, 1, 2, 3, 4, 5]` removes only one new element per round and needs five steps.
- **Equal values:** Equality is non-decreasing; an equal predecessor does not remove the current value and must be popped by the stack recurrence.
- **Single element:** It is already non-decreasing and requires zero steps.
- **Simultaneous comparison:** Eligibility in a round uses neighbors before any deletion from that round; sequential deletion would produce a different result.
