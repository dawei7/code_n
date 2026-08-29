## General

**Store ownership and both tree directions**

`self.locked[node]` is -1 when a node is unlocked and otherwise stores the user ID that owns its lock. Storing the owner, rather than only a Boolean, is necessary because unlock succeeds only for the same user.

The input `parent` already supports walking upward. The constructor also builds `self.children` by appending each nonroot node to its parent's child list. This supports walking through all descendants during upgrade.

Together, these structures make direct lock checks constant-time and let upgrade inspect precisely the two relevant regions: the ancestor chain and descendant subtree.

**Lock checks only the node itself**

`lock(num, user)` succeeds when `self.locked[num] == -1`. It writes the user ID and returns true. Otherwise it makes no change and returns false.

The ordinary lock operation does not require ancestors or descendants to be unlocked. Consequently, locked nodes can coexist at different tree levels. This is why upgrade must inspect and clear the entire descendant subtree rather than stopping at the first locked node.

**Unlock checks exact ownership**

`unlock(num, user)` compares the stored owner with `user`. Equality proves both that the node is locked and that the caller owns it. The method then writes -1 and returns true.

An unlocked node stores -1, while valid user IDs begin at one, so an unlocked node cannot accidentally pass. A different user also fails without altering the lock.

**Check the upgrade node and all ancestors first**

Upgrade starts with `x = num` and follows `self.parent[x]` until -1. It rejects immediately if any visited node is locked.

Beginning at `num` itself enforces the first upgrade condition, that the target node is unlocked. Continuing through its parent, grandparent, and so forth enforces that no ancestor is locked.

This validation occurs before descendant traversal, so a failure cannot partially unlock descendants.

**Find and unlock every locked descendant**

Nested helper `dfs(x)` loops through children of `x`. For each child `y`, it clears its lock if present and sets `find = True`. It then recursively visits `y` regardless of whether `y` was locked.

Continuing below a locked child is necessary because ordinary locking allows deeper descendants to be locked too. Successful upgrade must unlock all descendants, not merely the highest locked ones.

The helper starts at `num` but examines only its children, so it never treats the target itself as a locked descendant. The earlier ancestor-chain check already proved the target unlocked.

**Require at least one locked descendant**

`find` begins false and becomes true only when DFS encounters a locked descendant. After traversal, false means the third prerequisite was absent. Upgrade returns false and leaves the target unlocked.

If true, all locked descendants have already been cleared. The method writes `self.locked[num] = user` and returns true.

Thus the mutations occur in a safe order: validate target and ancestors, clear descendants while proving at least one existed, then lock the target.

**Why upgrade is correct**

On a true return, the upward loop proves target and ancestors were unlocked. DFS proves at least one descendant was locked and clears every locked descendant. The final assignment locks the target for the requested user. All specified effects and preconditions hold.

On a false return from the ancestor scan, a required unlocked condition fails and nothing was changed. On a false return after DFS, there was no locked descendant; because no lock was encountered, DFS changed nothing. Therefore failed operations preserve valid state.

**Recursion depth in the exact Python source**

A valid tree may be a chain of 2000 nodes. Upgrading near its root recursively descends through nearly 2000 frames, which can exceed Python's usual recursion limit and raise `RecursionError`.

The algorithmic idea is correct, but an iterative stack would be safer for the full stated constraint. This is a runtime robustness issue in the exact implementation, not a change to its tree logic.

## Complexity detail

Construction takes $O(N)$ time and $O(N)$ space for owner, parent, and child lists. `lock` and `unlock` take $O(1)$ time.

An `upgrade` walks height $H$ upward and visits subtree size $D$ downward, for $O(H+D)$ time, at worst $O(N)$. Recursive DFS uses $O(H)$ call-stack space in the worst case. Persistent structures use $O(N)$ space.

## Alternatives and edge cases

- **Iterative descendant traversal:** Uses an explicit stack, preserves $O(N)$ worst-case work, and avoids Python recursion-limit failure.
- **Euler tour plus indexed locked nodes:** Can speed descendant discovery and range clearing but greatly complicates updates.
- **Ancestor lock counters:** Help check ancestors or descendants faster, but upgrade still must identify locks to clear unless additional structures are maintained.
- **Lock already locked node:** Returns false regardless of user.
- **Unlock by wrong user:** Returns false and preserves ownership.
- **Upgrade locked target:** Rejected by the inclusive upward scan.
- **Upgrade under a locked ancestor:** Rejected before descendant mutation.
- **Upgrade without locked descendants:** DFS finds none and returns false.
- **Several locked descendants by different users:** All are cleared, as required.
- **Locked descendant with locked child:** DFS continues below it and clears both.
- **Upgrade root:** It has no ancestors, but still must be unlocked and have a locked descendant.
- **Leaf upgrade:** Always fails the descendant condition.
- **Deep chain:** Exact recursion may exceed Python's stack limit near 2000 nodes.
- **Input parent array:** The object retains its reference and builds a separate children list.
