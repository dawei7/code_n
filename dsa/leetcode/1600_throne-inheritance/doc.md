# Throne Inheritance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1600 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Design |
| Official Link | [LeetCode](https://leetcode.com/problems/throne-inheritance/) |

## Problem Description
### Goal
A royal family begins with one king and grows through births. The inheritance order starts with the king, then recursively visits each person's children from oldest to youngest before moving to the next younger sibling's branch. Thus each person precedes all of their descendants, and siblings retain their birth order.

Implement a stateful inheritance system. A birth appends a new child to the named living parent's children. A death only marks a known person as dead: it does not remove that person's position, descendants, or family relationships. An order query returns the current recursive succession order with dead people omitted while their living descendants remain in their normal positions.

### Function Contract
**Platform interface**

- `ThroneInheritance(kingName)` creates the family with the named king.
- `birth(parentName, childName)` records a distinct new child as the parent's youngest child and returns nothing; the parent is guaranteed alive.
- `death(name)` marks an existing person dead and returns nothing.
- `getInheritanceOrder()` returns all living people in current succession order.
- At most $10^5$ births and deaths and at most 10 order queries occur.

**Inputs**

- `kingName`: the initial king's name.
- `operations`: ordered `[name, arguments]` calls using `"birth"`, `"death"`, or `"getInheritanceOrder"`.

**Return value**

Return one output per operation: `null` for births and deaths, and the returned name list for an order query.

### Examples
**Example 1**

- Input: king `"king"`; births create children `andy`, `bob`, and `catherine`, then grandchildren `matthew`, `alex`, and `asha`.
- Output before any death: `["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]`.

**Example 2**

- Input: the same family after `death("bob")`.
- Output: `["king", "andy", "matthew", "alex", "asha", "catherine"]`; Bob is omitted but his children remain.

**Example 3**

- Input: a king with no births followed by `getInheritanceOrder()`.
- Output: `["king"]`.

### Required Complexity
- **Time:** $O(B+D+GP)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

Let $B$ be the number of births, $D$ the number of deaths, $G$ the number of order queries, and $P$ the number of people present when a query runs.

**Store the permanent family tree.** Map every parent name to a list of children appended in birth order. A birth is one list append. Maintain dead names in a hash set, so death is a membership-state update rather than a structural deletion. This distinction is essential because a dead person's descendants keep their inherited location.

**Generate succession as a preorder traversal.** Start at the king, visit the person, and then traverse each child subtree from oldest to youngest. Append a visited name only if it is not dead, but always traverse its children. An explicit stack avoids recursion-depth failure for a family chain approaching $10^5$ people. Push children in reverse order so the oldest is popped first.

The family adjacency lists contain every birth edge exactly once and preserve sibling age order. Preorder therefore implements the recursive successor rule: a person is followed by their oldest unvisited descendant branch before any younger sibling branch. Filtering a dead person's name without pruning that node leaves every descendant in precisely the position the unchanged family tree assigns. Hence each query returns all and only living people in the unique required order.

**Adapting the object trace locally.** The `solve` adapter constructs one object, dispatches calls sequentially, emits `None` for void mutations, and records each query result. This preserves state across the complete authored operation trace.

#### Complexity detail

Each birth appends once and each death inserts once, for $O(B+D)$ expected mutation time. Every query visits each of the $P$ people once, for $O(P)$ time per query and $O(B+D+GP)$ total. The child lists, dead set, and traversal stack store $O(P)$ names. The returned order itself is required output.

#### Alternatives and edge cases

- **Rebuild the full order after every birth:** This remains correct but repeats preorder work even when no query occurs, producing quadratic behavior over a long birth sequence.
- **Remove dead nodes from the tree:** This is incorrect because it can also disconnect or reorder their descendants; death is only a filter on query output.
- **Recursive DFS:** It expresses preorder directly but can exceed the language recursion limit on a deep lineage.
- Several children of one parent must remain in birth order, not alphabetical order.
- The king may die; an order query then begins with the first living person in the king's descendant preorder.
- A dead person may have living descendants, all of whom remain eligible.
- Repeated order queries without intervening mutations return equal lists.

</details>
