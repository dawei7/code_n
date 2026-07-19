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
