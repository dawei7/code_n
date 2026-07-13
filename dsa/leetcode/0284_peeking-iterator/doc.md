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

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Keep exactly one value ahead of the public cursor**

During construction, consume the underlying iterator's first value when one exists. `peek()` returns the cache. `next()` returns it and immediately refills from the underlying iterator.

When `has_next` is true, the cache contains exactly the next unconsumed underlying value. When false, both the wrapper and underlying iterator are exhausted.

**Peek observes the cache; next advances it**

`peek()` never touches the underlying iterator, so any number of peeks returns the same next value. `next()` returns that cached value and refills once, advancing the public sequence by exactly one element. When no refill is possible, both layers are exhausted, making `hasNext()` accurate.

#### Complexity detail

Every method makes at most one underlying iterator call and constant local work, using one cached value and one boolean.

#### Alternatives and edge cases

- **Copy all remaining values:** uses $O(n)$ space.
- **Delete the first list item repeatedly in an adapter:** can take $O(n^2)$ due to shifting.
- Repeated peeks are idempotent, and consuming the final value makes `hasNext()` false.

</details>
