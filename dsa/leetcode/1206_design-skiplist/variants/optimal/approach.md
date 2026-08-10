## General

A skiplist is a tower of sorted linked lists. Level zero contains every stored occurrence. Higher levels contain random subsets, creating express lanes that skip over many values. Search begins high, moves right while values are too small, then drops to lower levels near the target.

Each `Node` stores `val` and a `next` list whose length is that node’s height. `next[i]` points to the next node on level `i`. The head sentinel has value `-1` and all 32 possible levels, so every traversal has a stable starting node.

`self.level` records the number of currently active levels. It begins at zero and grows when an inserted node has a taller random height.

**Move to the predecessor on one level**

The helper `find_closest(curr, level, target)` advances while a next node exists and its value is strictly smaller than `target`. It stops at the rightmost node before the first value greater than or equal to the target.

Stopping before equality is important for duplicates. It makes search able to inspect an equal successor, insertion place a new duplicate before existing equals, and erase find an occurrence without passing over it.

**Search from the highest active level downward**

`search` starts at the head and visits levels from `self.level - 1` down to zero. On each, it advances to the predecessor. If the next node on that level equals the target, it returns true immediately.

When it drops a level, it keeps the current node rather than returning to the head. A node reached on level `i` necessarily has links on all lower levels, so it is a valid starting point. The higher-level scan has already skipped a large sorted prefix.

If no level exposes an equal successor, the target is absent. Level zero contains every stored occurrence, so a miss there is definitive.

**Choose an insertion height randomly**

`random_level` starts at one. While below 32 and a random draw is less than `p = 0.25`, it adds another level. Thus every node appears at level zero, about one quarter reach the next level, about one sixteenth reach the following level, and so on.

This geometric thinning is what gives expected logarithmic traversal length. The fixed cap prevents an unbounded node tower.

**Splice a new node into every level it owns**

`add` creates a node with the sampled height and raises `self.level` if needed. It traverses active levels from top to bottom. At each level, it finds the predecessor. If the new node owns that level, it points the node to the predecessor’s old successor and then points the predecessor to the node.

These two pointer assignments preserve sorted order and avoid losing the remainder of the list. At levels above the new node’s height, traversal still positions `curr` for an efficient descent but performs no splice.

Because predecessor search stops before equal values, duplicates are inserted before existing equal occurrences. They remain separate nodes, satisfying duplicate support.

**Erase one occurrence while repairing links**

`erase` performs the same top-down predecessor search. Whenever the next node equals `num`, it bypasses that link with

`curr.next[i] = curr.next[i].next[i]`.

`ok` records whether any equal link was found. At level zero, every occurrence exists, so a present value causes at least one removal and an absent value leaves `ok` false.

With duplicates of different heights, the equal link bypassed at one level need not always belong to the same physical node bypassed at a lower level. The ordered structure remains valid, and level zero loses exactly one occurrence, which defines the stored multiset. Upper express lanes may lose additional tower links but never create an incorrect value or order.

After removal, empty top levels are trimmed while keeping at least level one active once the structure has been used. This avoids future scans of head levels with no nodes.

**Why all operations preserve the abstract multiset**

Level zero is the authoritative sorted linked list. Add inserts one new node there in sorted position. Erase bypasses one equal node there when present. Search’s final level-zero check finds a target exactly when at least one occurrence remains.

Higher levels contain only forward links between nodes in the same sorted order. They accelerate navigation but do not change membership. Random heights affect performance, not logical correctness.

## Complexity detail

Let $n$ be the number of stored occurrences. With independent geometric heights and promotion probability one quarter, the expected number of nodes shrinks by a constant factor per level. Search, add, and erase therefore take expected $O(\log n)$ time.

The worst case is $O(n)$ for an unlucky random structure or because the fixed maximum level eventually caps growth. Expected complexity, rather than deterministic worst-case balance, is the skiplist guarantee.

The expected number of forward pointers per node is a convergent geometric sum, so total expected storage is $O(n)$. With maximum height 32, even worst-case pointer storage is at most $32n$, still $O(n)$ because 32 is fixed. The head uses 32 pointers.

Temporary variables use $O(1)$ space. Unlike some skiplist implementations, this code does not allocate a separate predecessor-update array during insertion.

## Alternatives and edge cases

- **Balanced binary search tree:** A red-black tree or AVL tree gives deterministic $O(\log n)$ operations but requires rotation and balance logic absent from this randomized structure.
- **Sorted Python list:** Search can use binary search, but insertion and erasure shift elements and cost $O(n)$.
- **Promotion probability:** A larger `p` creates more upper-level pointers; a smaller one creates fewer express lanes. One quarter is a standard space-conscious choice.
- **Empty skiplist:** `self.level` is zero before the first add, so search and erase loops do nothing and return false.
- **First insertion:** Its random height activates the needed levels, and the head supplies predecessors on all of them.
- **Duplicate values:** Each add creates a separate node. One erase removes one level-zero occurrence, and search remains true while any duplicate remains.
- **Erase absent value:** No equal successor is bypassed, `ok` stays false, and structure is unchanged.
- **Remove the tallest node:** The cleanup loop lowers active height until the top head link is nonempty or level one remains.
- **Maximum level cap:** It prevents arbitrarily tall towers but means asymptotic expected behavior eventually depends on a fixed 32-level ceiling.
- **Randomness:** Performance varies between runs, while sorted membership and return values do not.
- **Thread safety:** The class has no synchronization. Concurrent mutation would require external locking and is outside this interface.
- **Strict predecessor comparison:** Changing `< target` to `<= target` would move past duplicates and complicate search and erase semantics.
