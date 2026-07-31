## Description

`RandomizedCollection` stores a multiset of integers, so duplicate occurrences are permitted. Implement these operations:

- `RandomizedCollection()` initializes an empty collection.
- `insert(val)` always adds one occurrence and returns `true` exactly when `val` was absent before the call.
- `remove(val)` removes one occurrence when available and returns whether a removal occurred.
- `getRandom()` chooses uniformly among stored occurrences. Consequently, a value's probability is proportional to its multiplicity.

All operations must run in average $O(1)$ time.
