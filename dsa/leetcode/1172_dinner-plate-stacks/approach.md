## General

**Two different choices must stay efficient**

`push` must find the leftmost stack with free capacity. `pop` must find the rightmost nonempty stack. `popAtStack` can create a hole in the middle that a later push should fill before using stacks farther right.

A plain list of stacks gives direct indexed access, but scanning from the left for every push can be slow when many early stacks are full. The solution combines:

- `self.stacks`, a list of the actual stack lists;
- `self.not_full`, a sorted set of indices whose existing stacks have room.

The sorted set's first element is always the smallest available index, exactly what `push` needs.

**Maintain no useless empty stacks at the right edge**

Internal empty stacks must remain addressable because their indices cannot shift. However, empty stacks at the end of `self.stacks` can be removed safely: no later stack exists whose index would change.

The implementation maintains the invariant that `self.stacks` has no trailing empty stack after a successful pop. Consequently, the last list entry, when any exists, is the rightmost nonempty stack. This makes `pop` a call to `popAtStack(len(self.stacks) - 1)`.

**Push into the leftmost available stack**

If `self.not_full` is nonempty, `self.not_full[0]` gives its minimum index. The value is appended there.

If that stack reaches `capacity`, its index is discarded from `not_full` because it can accept no more values. If it remains below capacity, it stays in the set for another push.

If `not_full` is empty, every existing stack is full. The leftmost nonfull position is therefore the next new index, so the code appends `[val]` to `self.stacks`. When capacity is greater than one, the new stack still has room and its index is added to the set. For capacity one, the new stack is already full and is not added.

**Pop from a requested index**

`popAtStack` first rejects negative indices, indices beyond the current list, and empty internal stacks. All return `-1` without changing the structure.

For a valid nonempty stack, `pop()` on the inner list removes and returns its top value.

If the affected stack is not a newly empty trailing stack, it now has free capacity, so its index is added to `not_full`. This includes an internal stack that becomes empty and a last stack that remains nonempty after losing one value.

**Trim a newly empty right edge**

If the pop empties the current last stack, the method enters a cleanup loop. It removes that stack and any other empty stacks immediately preceding it.

Before each list removal, its index is discarded from `not_full` because the stack will no longer exist. `discard` is safe whether the index was present or not.

The cleanup may expose a nonempty earlier stack, at which point it stops. That stack's index and every internal hole remain unchanged.

**Why `pop` is correct**

If no stacks exist, `len(self.stacks) - 1` is negative and `popAtStack` returns `-1`.

Otherwise, the no-trailing-empty invariant means the last existing stack is the rightmost nonempty stack. Delegating to `popAtStack` removes its top value and then restores the invariant by trimming if necessary.

**Trace the hole-filling behavior**

With capacity two, pushing one through five creates stacks `[1, 2]`, `[3, 4]`, and `[5]`. The nonfull set contains only index two.

Popping at index zero removes two and adds index zero to `not_full`. The next push chooses index zero rather than index two because zero is the minimum, restoring `[1, 20]`.

Later, popping the only value from the rightmost stack removes that stack from the list. Subsequent ordinary pops continue from the new rightmost nonempty stack.

**Why the invariants prove correctness**

After every operation, `not_full` contains exactly the indices of existing stacks whose sizes are below capacity, except that no removed trailing index remains. Push therefore selects the leftmost legal destination or appends the first new destination when none exists.

The stack list preserves all internal indices, and trailing cleanup preserves every still-addressable stack index. Its final entry is nonempty, so ordinary pop selects the required rightmost source. Each inner list uses append and pop at the end, preserving last-in-first-out behavior.

Thus all three operations meet their selection and stack-order rules.

## Complexity detail

Let `s` be the number of existing stack slots, `v` the number of stored values, and `m` the number of operations.

Sorted-set indexing, insertion, and deletion take `O(log s)` time. Inner-list append and pop are amortized `O(1)`. A cleanup loop can remove several trailing empty stacks in one call, but each stack slot is appended once and removed once, so cleanup is amortized across operations.

The total time over `m` operations is `O(m log s)`, matching the manifest. An individual call that trims many historical holes can exceed logarithmic time, but those removals cannot repeat.

The stack lists store `v` values and metadata for `s` stack slots. The sorted set stores at most `s` indices. Total space is `O(v + s)`.

## Alternatives and edge cases

- **Scan from index zero on every push:** This can take `O(s)` per push when many early stacks are full.
- **Use a min-heap of nonfull indices:** A heap can find the leftmost hole, but duplicate and stale entries require lazy cleanup. `SortedSet` maintains unique live indices directly.
- **Use a max-heap for nonempty indices as well:** That can support rightmost pop, but the no-trailing-empty invariant makes a second ordered structure unnecessary.
- **Capacity one:** Every push creates a full stack, and `not_full` remains empty until internal pops create holes.
- **Pop from an internal stack:** Its index is added to `not_full` so the next appropriate push can fill the hole.
- **Pop from an empty or missing index:** Return `-1` and leave all invariants unchanged.
- **Several trailing empty holes:** Empty internal stacks can become trailing after a later stack is removed; the cleanup loop removes all of them.
- **All stacks empty:** Cleanup makes `self.stacks` empty, and ordinary pop delegates with index negative and returns `-1`.
- **Duplicate values:** Stack selection depends on positions and capacity, not value uniqueness.
- **Amortized cleanup:** A single pop can trim many slots, but every trimmed slot was created earlier and is removed only once.
