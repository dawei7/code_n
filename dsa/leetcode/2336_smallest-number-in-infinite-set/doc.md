# Smallest Number in Infinite Set

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2336 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Design, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-number-in-infinite-set/) |

## Problem Description

### Goal

Maintain a set that initially contains every positive integer. Constructing
`SmallestInfiniteSet` restores this initial state. `popSmallest()` must find
the smallest number currently present, remove it, and return it.

The operation `addBack(num)` inserts the positive integer `num` only when it
is currently absent; adding a value that is already present has no effect.
Process the requested operation sequence in order and return each operation's
result, using `null` for construction and `addBack`.

### Function Contract

**Operations**

- `SmallestInfiniteSet()`: Initializes all positive integers as present.
- `popSmallest()`: Removes and returns the least currently present integer.
- `addBack(num)`: Restores `num` when absent, where $1 \le num \le 1000$.

At most 1000 calls to `popSmallest` and `addBack` occur in one trace.

**Return value**

For the app-local trace adapter, a list containing `null` for construction and
each `addBack`, and the returned integer for each `popSmallest`.

### Examples

**Example 1**

- Input: `operations = ["SmallestInfiniteSet","addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","popSmallest","popSmallest"]`,
  `arguments = [[],[2],[],[],[],[1],[],[],[]]`
- Output: `[null,null,1,2,3,null,1,4,5]`
- Explanation: Adding 2 initially changes nothing. After 1, 2, and 3 are
  removed, restoring 1 makes it the smallest again.

**Example 2**

- Input: `operations = ["SmallestInfiniteSet","popSmallest","addBack","popSmallest"]`,
  `arguments = [[],[],[1],[]]`
- Output: `[null,1,null,1]`
- Explanation: The removed value 1 becomes available again.

**Example 3**

- Input: `operations = ["SmallestInfiniteSet","addBack","popSmallest"]`,
  `arguments = [[],[1000],[]]`
- Output: `[null,null,1]`
- Explanation: Since 1000 was never removed, adding it back has no effect.
