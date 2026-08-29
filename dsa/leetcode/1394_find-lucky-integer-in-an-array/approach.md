## General

**Count first, then test the definition**

A value $x$ is lucky when it occurs exactly $x$ times. The array's order is irrelevant; only the frequency of each distinct value matters.

`Counter(arr)` builds a mapping `cnt` from each distinct array value to its occurrence count. For `[1,2,2,3,3,3]`, the mapping is equivalent to `{1: 1, 2: 2, 3: 3}`. Each key equals its mapped count, so all three values are lucky.

Counting in one pass avoids repeatedly scanning the whole array for every candidate. Each occurrence performs one expected constant-time hash-table update.

**Filter exactly the lucky entries**

`cnt.items()` produces pairs `(x, v)`, where `x` is the array value and `v` is its frequency. The generator expression

`(x for x, v in cnt.items() if x == v)`

yields a value only when it equals its count. It does not yield the count separately because the two numbers are identical for a lucky entry.

This distinction is important. A value 2 appearing three times has pair `(2,3)` and is rejected, even though both numbers are positive and small. A value 3 appearing twice is also rejected. Equality, not a greater-than or at-least relationship, defines luckiness.

**Select the largest and handle no candidate**

There may be several lucky integers, so `max(...)` selects the largest yielded value. Dictionary iteration order is irrelevant because `max` examines all candidates.

If the generator yields nothing, ordinary `max` would raise an exception. Passing `default=-1` makes it return the required sentinel instead. Because valid array values are at least one, $-1$ cannot be confused with a real lucky integer.

For `[2,2,3,4]`, pairs include `(2,2)`, `(3,1)`, and `(4,1)`. Only 2 is yielded and returned. For `[2,2,2,3,3]`, the pairs are `(2,3)` and `(3,2)`; neither passes, so the default produces $-1$.

**Why it is enough to inspect distinct values**

Every occurrence of the same integer has the same global frequency. Testing $x$ once through the counter entry gives the same conclusion as testing every occurrence, without duplicate work. The output is a value, not an index or occurrence, so no positional information is lost.

The maximum possible lucky value is also limited by array length: a value larger than $n$ cannot occur that many times in an $n$-element array. The code does not need this observation for pruning because the frequency comparison rejects such values automatically.

**Why the algorithm is correct**

Counter construction records the exact number of occurrences for every distinct input value. The generator yields precisely those keys whose recorded frequency equals the key, so its yielded set is exactly the set of lucky integers. `max` returns the largest member when that set is nonempty, and the default returns $-1$ exactly when it is empty. Therefore the result satisfies both parts of the contract.

**Why a generator is appropriate**

The generator feeds candidates to `max` one at a time. It does not allocate a separate list of lucky values. The counter is still necessary, but candidate filtering uses only constant extra iteration state.

The method also leaves `arr` unchanged. Unlike a sorting solution, it does not reorder the caller's input.

## Complexity detail

Let $n$ be the array length and $u$ the number of distinct values. Building `Counter` takes expected $O(n)$ time. Scanning its $u$ entries takes $O(u)$, and $u\le n$, so total expected time is $O(n)$.

The counter stores $u$ key-count pairs, giving $O(u)$ auxiliary space. The generator is lazy and uses $O(1)$ additional state. These bounds match the manifest.

Hash-table complexity is expected rather than an absolute worst-case guarantee, but it is the standard model for Python `Counter`.

## Alternatives and edge cases

- **Fixed frequency array:** Values lie between one and 500, so an array of 501 counts gives $O(n+500)$ time and constant domain-bounded space.
- **Sort and scan runs:** Sorting groups equal values, then run lengths can be compared with values. It costs $O(n\log n)$ time and may mutate the input.
- **Repeated `arr.count`:** Count every candidate by rescanning the array. It is simple but can cost $O(n^2)$.
- **Scan possible values downward:** With a frequency array, check 500 down to one and return the first equality. This makes largest selection explicit.
- **Several lucky integers:** `max` returns the largest, not the first counter entry.
- **No lucky integer:** `default=-1` avoids an exception and returns the required sentinel.
- **Value one:** It is lucky exactly when it occurs once.
- **Value larger than array length:** It cannot be lucky and is rejected automatically.
- **Duplicate occurrences:** They are summarized into one counter entry and do not cause duplicate candidates.
- **Positive-value constraint:** It ensures $-1$ is an unambiguous failure value and zero need not be considered.
- **Input order:** It has no effect on frequencies or the maximum.
- **Input mutation:** `Counter` only reads `arr`.
- **Required import:** `Counter` must be available, normally from `collections`.
