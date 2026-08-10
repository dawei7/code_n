## General

The iterator must expose the integers of a list of lists as one row-major sequence without copying them into a separate flat array. A position in the original structure needs two coordinates:

- `i` is the current row index;
- `j` is the current index inside that row.

The constructor sets both to zero and retains a reference to `vec`. It deliberately performs no traversal. This makes initialization constant time and avoids doing work the caller may never need if it consumes only the first few values.

The central complication is that rows can be empty. Even a nonempty row eventually becomes exhausted after all of its elements have been returned. The helper `forward()` repairs the cursor whenever it does not point to a current value.

**The normalized cursor state**

After `forward()` finishes, exactly one of two conditions holds:

1. `i < len(vec)` and `j < len(vec[i])`, so `(i, j)` identifies the next integer to return; or
2. `i == len(vec)`, so every row has been exhausted and no next integer exists.

The helper loops while `i` is a valid row and `j >= len(vec[i])`. An empty row has length zero, so `j = 0` already satisfies the exhaustion condition. A consumed nonempty row also satisfies it after `next()` increments `j` past the last valid position. In either case, the helper advances to the following row and resets `j = 0`.

The condition uses `>=` rather than equality. Under normal valid operations, `j` reaches exactly the row length, but `>=` expresses the broader truth that any position at or beyond the end is invalid and makes the helper robust to that state.

**How `next()` consumes one value**

`next()` first calls `forward()`. This ensures that any empty or exhausted rows have been skipped before indexing. It then reads `vec[i][j]`, increments `j`, and returns the saved value.

Incrementing `j` after reading is important: the current coordinate always means “the next value not yet returned,” not “the value returned most recently.” After the final value in a row, `j` becomes equal to that row's length. The method does not immediately seek the next row; the next operation performs that work lazily through `forward()`.

The contract guarantees every call to `next()` is valid. Therefore, after normalization inside `next()`, the exhausted state cannot occur. If a caller violated that precondition, indexing `vec[len(vec)]` would raise an error; the class is not required to manufacture a sentinel result.

**How `hasNext()` inspects without consuming**

`hasNext()` also begins with `forward()`, then returns whether `i < len(vec)`. If a valid row remains, normalization guarantees a valid element exists there. If `i` has reached the number of rows, no remaining row or element exists.

Calling `hasNext()` may move across empty or exhausted rows, but it never advances past a real integer. Once `(i, j)` points to a value, repeated calls to `hasNext()` cause the loop condition to fail immediately and leave the cursor unchanged. This idempotence is crucial for iterator behavior: clients often call `hasNext()` several times before calling `next()`, and those checks must not skip data.

**Trace with empty rows**

Consider

```text
[[], [1, 2], [], [], [3], []]
```

- Construction leaves `(i, j) = (0, 0)` without scanning.
- The first `hasNext()` calls `forward()`. Row `0` is empty, so `i` becomes `1`; row `1` has an element at `j = 0`, so movement stops. `hasNext()` returns `True`.
- Another `hasNext()` sees the same valid coordinate and returns `True` without changing it.
- `next()` normalizes without movement, reads `1`, advances `j` to `1`, and returns `1`.
- The next `next()` reads `2` and leaves `j = 2`, exactly the length of row `1`.
- On the following operation, `forward()` advances across the exhausted row and both empty rows, stopping at `(4, 0)`. `next()` returns `3`.
- A final `hasNext()` skips the exhausted row `4` and empty row `5`, reaches `i = 6`, and returns `False`.

The observed flattened order is `[1, 2, 3]`, and no empty row appears as data.

**Why the iterator cannot skip or repeat a value**

The only statement that moves within a nonempty row is `self.j += 1`, executed exactly once after that coordinate's value is returned. `forward()` changes rows only when the current row has no valid element at `j`, and it resets `j` to the first coordinate of the next row. It never moves away from a valid element. Thus each real coordinate is returned once before the cursor passes it, and rows are visited in increasing order. When `i` reaches the end, every earlier row has been proven exhausted, so no value remains.

The class stores `self.vec = vec`, a reference rather than a flattened copy. This is what enables constant auxiliary space. It also means the intended model is that the input structure remains stable while being iterated; arbitrary external mutation could change row lengths or values and is not part of the stated interface.

## Complexity detail

Let $V$ be the number of inner rows, $N$ the total number of integers, and $C$ the number of public method calls. The constructor performs three assignments and takes $O(1)$ time.

One individual call to `forward()`, and therefore one `next()` or `hasNext()`, can take $O(V)$ worst-case time if it encounters a long consecutive run of empty rows. It is inaccurate to claim a strict worst-case $O(1)$ bound for every operation.

Across the lifetime of the iterator, however, `i` only increases and each row is skipped at most once. The total work spent advancing rows is $O(V)$. Every public call adds one constant-time normalization check, and every successful `next()` adds constant work to read a value and advance `j`. Thus a sequence of calls costs $O(C+V)$ total, or $O(1+V/C)$ amortized per call. If the iterator is fully consumed with $N$ valid `next()` calls, traversal work is $O(N+V)$ overall.

The manifest's $O(1)$ time is best understood as the normal cursor operation or an amortized claim when row-skipping cost is distributed appropriately; it is not a per-call worst-case guarantee in the presence of arbitrarily many empty rows.

The object stores two indices and one reference to the existing input. `forward()` uses no recursion or auxiliary collection, so auxiliary space is $O(1)$. The input's own $O(N+V)$ storage is not copied and is not charged to the iterator.

## Alternatives and edge cases

- **Flatten in the constructor:** Copy every integer into one list and iterate with one index. Then each public operation is strict $O(1)$, but construction costs $O(N+V)$ time and storage costs $O(N)$, defeating the lazy iterator design.
- **Store row iterators:** Keep an iterator over rows and a current inner iterator, advancing until one has data. This matches the follow-up style in iterator-oriented languages and retains lazy $O(1)$ auxiliary state when the underlying iterators are references.
- **Leading empty rows:** The first operation skips them; the constructor remains $O(1)$.
- **Empty rows between values:** `forward()` may cross any number of them and stops at the next actual integer.
- **Trailing empty rows:** After the last value, normalization consumes all remaining empty rows and sets `i` to `len(vec)`.
- **Completely empty outer vector:** `i` starts equal to `len(vec)`, so `hasNext()` returns `False` immediately.
- **Only empty inner vectors:** One `hasNext()` may scan all rows and returns `False`; subsequent calls are constant time because the exhausted cursor is stable.
- **Repeated `hasNext()` calls:** Once normalized at a valid element or at exhaustion, further checks do not advance anything and return the same answer until `next()` consumes a value.
- **`next()` without a preceding `hasNext()`:** It is supported because `next()` performs its own normalization.
- **Invalid `next()` after exhaustion:** The contract guarantees this does not happen. The source would raise an indexing error rather than return a sentinel.
- **Rows with negative values or duplicates:** Values are returned unchanged. Cursor logic depends only on structure and lengths, not on integer contents.
- **External mutation:** Because `vec` is stored by reference, changing it during iteration can alter the observed sequence. Standard iterator use assumes the backing collection is not structurally modified unless explicitly supported.
