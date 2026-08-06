## Examples

**Example 1**

- **Input:** `root = [7,3,15,null,null,9,20], operations = ["BSTIterator","next","next","prev","next"]`
- **Output:** `[null, 3, 7, 3, 7]`
- **Explanation:** Initialized before 3. First `next()` moves to 3. Second `next()` moves to 7. `prev()` moves back to 3. Third `next()` moves to 7.

**Example 2**

- **Input:** `root = [1], operations = ["BSTIterator","hasNext","next","hasPrev","hasNext"]`
- **Output:** `[null, true, 1, false, false]`
- **Explanation:** Pointer starts before 1. `hasNext()` is `true`. `next()` returns 1. `hasPrev()` is `false` (cannot go before 1). `hasNext()` is `false`.

**Example 3**

- **Input:** `root = [2,1,3], operations = ["BSTIterator","next","next","next","prev","next"]`
- **Output:** `[null, 1, 2, 3, 2, 3]`
- **Explanation:** Traverses 1, 2, 3 in order, then steps back to 2 and forward to 3.
