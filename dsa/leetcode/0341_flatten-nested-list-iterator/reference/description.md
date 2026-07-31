## Description

You are given a nested list of integers called `nestedList`. Each top-level element is either an integer or another list, and any list may recursively contain further integers or lists. Implement an iterator that exposes the integers as one flattened sequence.

Implement the `NestedIterator` class with this interface:

- `NestedIterator(List<NestedInteger> nestedList)` initializes an iterator over `nestedList`.
- `int next()` returns the next integer in the flattened order.
- `boolean hasNext()` returns `true` while at least one integer remains and `false` after all integers have been consumed.

The judge exercises the class with logic equivalent to:

```text
initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to res
return res
```

The implementation is correct when `res` equals the expected flattened list.
