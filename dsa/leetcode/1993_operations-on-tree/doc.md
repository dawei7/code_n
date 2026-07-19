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
