## Examples

**Example 1**

```text
      7
     / \
    3   15
       /  \
      9    20

In-order: 3 -> 7 -> 9 -> 15 -> 20
```

- Input: `operations = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"], arguments = [[[7,3,15,null,null,9,20]],[],[],[],[],[],[],[],[],[]]`
- Output: `[null, 3, 7, true, 9, true, 15, true, 20, false]`
- Explanation:
  1. Construct the iterator for `[7, 3, 15, null, null, 9, 20]`.
  2. The first two `next()` calls return `3` and `7`.
  3. `hasNext()` returns `true`; `next()` then returns `9`.
  4. `hasNext()` returns `true`; `next()` then returns `15`.
  5. `hasNext()` returns `true`; `next()` then returns `20`.
  6. `hasNext()` finally returns `false` because the traversal is exhausted.
