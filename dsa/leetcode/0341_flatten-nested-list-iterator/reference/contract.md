## Function Contract

**Inputs**

- `nested_list`: The app-local representation of the recursively nested integers; LeetCode's native constructor receives the equivalent `nestedList` through its `NestedInteger` interface.

**Return value**

The app adapter returns all integers in iterator order. The native `NestedIterator` instead exposes them one at a time through `next()` while `hasNext()` reports availability.
