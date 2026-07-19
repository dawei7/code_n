# Operations on Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1993 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Tree, Depth-First Search, Breadth-First Search, Design |
| Official Link | [LeetCode](https://leetcode.com/problems/operations-on-tree/) |

## Problem Description

### Goal

A rooted tree has $N$ nodes numbered from $0$ through $N-1$. It is described by `parent`, where `parent[0] = -1` identifies node $0$ as the root and every other entry gives that node's parent. Design a `LockingTree` that remembers which user, if any, currently owns the lock on each node.

The structure supports three operations. `lock` may claim only an unlocked node, and `unlock` may release a node only for the user who owns its lock. `upgrade` is more restrictive: its target must be unlocked, at least one of its descendants must be locked, and none of its ancestors may be locked. A successful upgrade removes every descendant lock, regardless of its owner, and then locks the target for the requesting user.

### Function Contract

**Inputs**

- `LockingTree(parent)` initializes the structure from a valid rooted tree with $2 \le N \le 2000$.
- `lock(num, user)` attempts to lock node `num` for the positive identifier `user`.
- `unlock(num, user)` attempts to remove `user`'s lock from node `num`.
- `upgrade(num, user)` attempts the ancestor-and-descendant checked upgrade at node `num`.
- Across one instance, at most $2000$ operation calls are made.

**Return value**

Each operation returns `true` exactly when it succeeds and changes the stored locks; otherwise, it returns `false` without changing them.

### Examples

**Example 1**

- Input: `operations = ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]`, `arguments = [[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]`
- Output: `[null, true, false, true, true, true, false]`
- Explanation: User $2$ first locks and then correctly unlocks node $2$; user $3$ cannot release that lock. After node $4$ is locked, upgrading the root clears node $4$ and locks node $0$, so the final lock attempt fails.

**Example 2**

- Input: `operations = ["LockingTree", "upgrade", "lock", "upgrade"]`, `arguments = [[[-1, 0, 0]], [0, 1], [1, 7], [0, 1]]`
- Output: `[null, false, true, true]`
- Explanation: The first upgrade has no locked descendant. Locking node $1$ supplies one, so the second upgrade succeeds.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Represent both directions of the tree.** The input already gives the upward link from every node to its parent. Build a children list once so an upgrade can also traverse downward. Alongside it, keep `locked_by`, where zero means unlocked and every positive value is the user who owns that node.

**Handle direct state changes locally.** A lock succeeds precisely when `locked_by[num]` is zero. An unlock succeeds precisely when it equals `user`. These checks update one array entry and do not impose ancestor or descendant restrictions that the contract reserves for `upgrade`.

**Validate an upgrade before committing it.** First reject a locked target. Then follow parent links from `parent[num]` to the root; encountering any locked node rejects the request without modifying state. If the ancestor path is clear, traverse every proper descendant using the children lists. Clear each lock encountered while recording whether at least one existed. If none existed, no state was changed and the upgrade fails. Otherwise, assigning `user` to the target completes the operation. Every required descendant lock is removed because the traversal visits the target's entire subtree except the target itself, and the target is locked only after all three conditions have been established.

#### Complexity detail

Constructing the children lists and lock array takes $O(N)$ time and $O(N)$ space. `lock` and `unlock` each take $O(1)$ time. An `upgrade` examines at most one ancestor path and one subtree, so its worst-case time is $O(N)$. The iterative traversal stack can hold $O(N)$ nodes, and all persistent structures also occupy $O(N)$ space.

#### Alternatives and edge cases

- **Scan the parent array for every descendant:** This avoids storing children, but determining whether every node belongs to the target's subtree can require following many parent chains, raising one upgrade to $O(N^2)$ time.
- **Maintain locked-descendant counters:** Counters can reject upgrades without locked descendants quickly, but a successful upgrade must still find and clear every locked descendant and carefully update all affected ancestors.
- A normal `lock` is allowed even when an ancestor or descendant is locked; those relationships constrain only `upgrade`.
- A locked node outside the target's subtree does not satisfy the locked-descendant condition.
- A failed upgrade must preserve every existing lock, including when a locked ancestor is found before the descendants are inspected.
- A successful upgrade clears descendant locks owned by any users, not just by the requesting user.

</details>
