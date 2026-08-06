## Examples

**Example 1**

- **Input:** `operations = ["StringIterator","next","next","next","next","next","next","hasNext","next","hasNext"], arguments = [["L1e2t1C1o1d1e1"],[],[],[],[],[],[],[],[],[]]`

- **Output:** `[null,"L","e","e","t","C","o",true,"d",true]`

- **Explanation:** Constructing the iterator yields no value. The first six `next()` calls expand the runs as `"L"`, `"e"`, `"e"`, `"t"`, `"C"`, and `"o"`. Characters still remain, so `hasNext()` is `true`; the next character is `"d"`, and the final `hasNext()` is still `true` because the last encoded `"e"` has not yet been consumed.
