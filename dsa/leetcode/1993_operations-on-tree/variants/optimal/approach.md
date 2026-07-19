## General
**Represent both directions of the tree.** The input already gives the upward link from every node to its parent. Build a children list once so an upgrade can also traverse downward. Alongside it, keep `locked_by`, where zero means unlocked and every positive value is the user who owns that node.

**Handle direct state changes locally.** A lock succeeds precisely when `locked_by[num]` is zero. An unlock succeeds precisely when it equals `user`. These checks update one array entry and do not impose ancestor or descendant restrictions that the contract reserves for `upgrade`.

**Validate an upgrade before committing it.** First reject a locked target. Then follow parent links from `parent[num]` to the root; encountering any locked node rejects the request without modifying state. If the ancestor path is clear, traverse every proper descendant using the children lists. Clear each lock encountered while recording whether at least one existed. If none existed, no state was changed and the upgrade fails. Otherwise, assigning `user` to the target completes the operation. Every required descendant lock is removed because the traversal visits the target's entire subtree except the target itself, and the target is locked only after all three conditions have been established.

## Complexity detail
Constructing the children lists and lock array takes $O(N)$ time and $O(N)$ space. `lock` and `unlock` each take $O(1)$ time. An `upgrade` examines at most one ancestor path and one subtree, so its worst-case time is $O(N)$. The iterative traversal stack can hold $O(N)$ nodes, and all persistent structures also occupy $O(N)$ space.

## Alternatives and edge cases
- **Scan the parent array for every descendant:** This avoids storing children, but determining whether every node belongs to the target's subtree can require following many parent chains, raising one upgrade to $O(N^2)$ time.
- **Maintain locked-descendant counters:** Counters can reject upgrades without locked descendants quickly, but a successful upgrade must still find and clear every locked descendant and carefully update all affected ancestors.
- A normal `lock` is allowed even when an ancestor or descendant is locked; those relationships constrain only `upgrade`.
- A locked node outside the target's subtree does not satisfy the locked-descendant condition.
- A failed upgrade must preserve every existing lock, including when a locked ancestor is found before the descendants are inspected.
- A successful upgrade clears descendant locks owned by any users, not just by the requesting user.
