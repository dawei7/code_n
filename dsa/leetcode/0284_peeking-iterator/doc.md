# Peeking Iterator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 284 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Design, Iterator |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/peeking-iterator/) |

## Problem Description
### Goal
Wrap an existing integer iterator with the usual `next()` and `hasNext()` behavior plus a new `peek()` operation. `peek()` returns the value that the next `next()` call would return but must leave that value unconsumed.

Repeated peeks before an advance must return the same value, while `next()` consumes exactly one value and moves the wrapper forward. `hasNext()` reports whether either a cached peeked value or an underlying value remains. Preserve the original iteration order and state across an arbitrary valid operation sequence. The app supplies offline iterator data, while the native class wraps LeetCode's provided `Iterator` interface directly.

### Function Contract
**Inputs**

- `iterator_data`: offline values exposed by the underlying iterator
- `operations`: `peek`, `next`, and `hasNext` calls to execute

**Return value**

The app adapter returns one result per operation. The native `PeekingIterator` class directly implements those three methods over LeetCode's provided `Iterator`.

### Examples
**Example 1**

- Input: `iterator_data = [1,2,3], operations = ["next","peek","next","next","hasNext"]`
- Output: `[1,2,2,3,false]`

**Example 2**

- Input: `iterator_data = [1,2,3], operations = ["hasNext","peek","next","next","hasNext"]`
- Output: `[true,1,1,2,true]`

**Example 3**

- Input: `iterator_data = [1], operations = ["peek","peek","next","hasNext"]`
- Output: `[1,1,1,false]`
