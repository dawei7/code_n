# Flatten Nested List Iterator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 341 |
| Difficulty | Medium |
| Topics | Stack, Tree, Depth-First Search, Design, Queue, Iterator |
| Official Link | [LeetCode](https://leetcode.com/problems/flatten-nested-list-iterator/) |

## Problem Description
### Goal
Design an iterator over a recursively nested list containing integers and sublists. Flatten its logical contents in left-to-right depth-first order: when a sublist is encountered, all of its contents appear before continuing with later siblings.

`next()` returns and consumes the next integer, while `hasNext()` reports whether another integer remains without consuming it. Empty lists at any depth contribute no values and must be skipped. Preserve state across interleaved valid calls and avoid eagerly copying the entire flattened sequence. The app adapter collects all emitted integers; the native class operates on LeetCode's `NestedInteger` interface incrementally.

### Function Contract
**Inputs**

- `nested_list`: a list whose elements are integers or recursively nested lists. The app adapter uses ordinary Python lists; LeetCode supplies the native `NestedInteger` interface.

**Return value**

- For the app-local `solve` adapter, a list containing every integer in the order produced by the iterator. The native submission exposes the required `NestedIterator.next()` and `NestedIterator.hasNext()` methods directly.

### Examples
**Example 1**

- Input: `nested_list = [[1, 1], 2, [1, 1]]`
- Output: `[1, 1, 2, 1, 1]`

**Example 2**

- Input: `nested_list = [1, [4, [6]]]`
- Output: `[1, 4, 6]`

**Example 3**

- Input: `nested_list = [[], [[]]]`
- Output: `[]`
