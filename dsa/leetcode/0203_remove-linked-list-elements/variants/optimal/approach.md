## General
Deleting the head is awkward because there is no predecessor whose `next` pointer can be changed. Add a dummy node before the original head so every real node, including the first, has a predecessor.

Keep `current` at the final node of the already-filtered prefix and inspect `current.next`:

- If `current.next.val == val`, bypass that node by assigning `current.next = current.next.next`. Do **not** advance `current`; the replacement next node may also need deletion.
- Otherwise advance `current` to that retained node.

For `[1,2,6,6,3]` with `val = 6`, the pointer advances through `1` and `2`. It bypasses the first `6`, remains at `2`, then bypasses the second `6` as well. Advancing after a deletion would skip inspection of consecutive matches.

At every iteration, the chain from the dummy through `current` contains only retained nodes in their original order, and `current.next` begins the unprocessed suffix. Rewiring one pointer preserves all later nodes while removing exactly the matching node from reachability.

If the inspected node matches, bypassing it removes exactly that node and keeps the processed prefix unchanged. If it does not match, advancing incorporates it into the valid prefix. In both cases the prefix property is preserved and the unprocessed suffix shrinks by one node. When the suffix is empty, every original node has been inspected: all matching nodes are unreachable and every nonmatching node remains in original order. Returning `dummy.next` supplies the correct possibly changed head.

## Complexity detail
Every real node is inspected once, so time is $O(n)$. The dummy node and a constant number of pointers use $O(1)$ auxiliary space.

## Alternatives and edge cases
- Recursively filtering `head.next` and then deciding whether to keep `head` is concise but uses $O(n)$ call-stack space.
- Repeatedly special-casing matching head nodes works but complicates control flow and proof.
- Copying retained values into new nodes needlessly allocates another list and changes node identity.
- Empty lists, all-matching lists, and matching runs at either end are handled uniformly by the dummy predecessor.
