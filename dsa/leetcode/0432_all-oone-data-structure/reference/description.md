## Description

Design a data structure that associates string keys with positive integer counts and can return a key at either
count extreme.

Implement the `AllOne` class with these operations:

- `AllOne()` creates an empty structure.
- `inc(key)` adds one to `key`'s count. A missing key is inserted with count $1$.
- `dec(key)` subtracts one from an existing key's count. Remove the key if its count becomes $0$; the input
  guarantees that the key exists before this call.
- `getMaxKey()` returns any key whose count is maximal, or `""` when the structure is empty.
- `getMinKey()` returns any key whose count is minimal, or `""` when the structure is empty.

When several keys share an extreme count, returning any one of them is valid.
