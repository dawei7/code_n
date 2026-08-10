## General

**Compact distinct runs toward the front**

In a sorted array, duplicates are adjacent. Once one copy of a value has been placed in the answer prefix, every immediately following equal copy can be ignored until a different value begins the next run.

The competitive implementation uses `last` as the index of the last distinct value written to the prefix. A read index `i` scans the original array from left to right. The compacted answer always occupies `A[0:last + 1]`.

**Separate the empty case from index-based state**

The source begins with

```python
if not A:
    return 0
```

This is outside the Reference's non-empty constraint but makes the function robust. Without the guard, initializing `last = 0` would claim that index zero already contains a retained value when no such index exists. After the guard, `A[0]` is valid and serves as the first distinct value automatically.

**Maintain the compacted-prefix invariant**

Before each iteration with read index `i`:

- `A[0:last + 1]` contains one copy of every distinct value seen before `i`, in sorted order;
- `A[last]` is the most recently retained value; and
- every array position strictly after `last` is irrelevant unless it has not yet been scanned.

At `i = 0`, the comparison is `A[0] != A[0]`, which is false. No write occurs, and the initial one-element prefix remains correct. Starting the loop at zero therefore costs one harmless self-comparison and avoids a separate loop range.

**Advance the write boundary only for a new run**

The condition

```python
if A[last] != A[i]:
```

compares the current scanned value with the last retained distinct value. Equality means `A[i]` is another copy in the same sorted run, so the method skips it. A difference means a new run has begun.

For a new value, the order of these statements matters:

```python
last += 1
A[last] = A[i]
```

Incrementing first selects the next free prefix position. The assignment writes the new run's representative there. Incrementing afterward without adjusting the destination would overwrite the previous last distinct value.

The new value is greater than or equal to all earlier values because the input is non-decreasing, and it differs from the last one, so appending it preserves sorted order.

**In-place writes cannot destroy unread data**

For every read position `i`, `last <= i`. When a new value is found, incrementing `last` still gives `last <= i`, so the destination is the current position or an earlier one. The source never writes to an index greater than `i` and therefore never changes a value that a future loop iteration still needs to read.

When destination and source are the same index, the assignment is simply idempotent. When destination is earlier, the right-hand value `A[i]` is evaluated before the write.

**Convert the last index into the required count**

After the loop, `last` is an index, while the contract asks for a count. A prefix ending at index `last` has length `last + 1`, so the method returns

```python
return last + 1
```

Confusing the last index with the count is a common off-by-one error. For a one-element array, `last` is zero but the correct return is one.

**Trace `[1,1,2]`**

The self-comparison at `i = 0` does nothing. At `i = 1`, `A[last]` and `A[i]` are both `1`, so the duplicate is skipped. At `i = 2`, `2` differs from `A[0]`; `last` becomes one and `2` is written to `A[1]`.

The function returns `last + 1 = 2`, and the judged prefix is `[1,2]`. The old value at `A[2]` is outside that prefix and may be ignored.

**Why no distinct value is lost or duplicated**

Sortedness partitions the input into contiguous equal-value runs. The initial index represents the first run. Within a run, every comparison with `A[last]` is equal, so no extra copy is written. At the first element of the next run, the comparison differs, so exactly one representative is appended and `A[last]` changes to that run's value. Repeating this reasoning produces exactly one prefix entry per run. Runs occur in input order, so relative order is preserved.

## Complexity detail

Let $n$ be the array length.

- **Time complexity: $O(n)$.** The `for` loop performs one pass with constant work per element. The initial empty check is constant time.
- **Auxiliary space: $O(1)$.** The algorithm stores two integer indices and uses the input array as output storage. It does not allocate a collection that grows with $n$.

The method is asymptotically optimal because every element may need inspection to determine whether it starts a new run.

## Alternatives and edge cases

- **Count-style write pointer:** Store the number of retained values rather than the last retained index. This avoids the final `+ 1` but needs explicit handling before the first retained value.
- **Compare adjacent source elements:** Starting from index one, keep `A[i]` when it differs from `A[i - 1]`. Sortedness makes this equally correct.
- **Hash set:** It consumes extra space and does not inherently preserve sorted relative order in every language.
- **Repeated deletion:** Removing array elements shifts suffixes and can degrade to quadratic time.
- **Empty array:** The explicit guard returns zero, though this case is outside the stated lower length bound.
- **Single element:** The self-comparison does nothing and `last + 1` returns one.
- **All duplicates:** `last` stays zero, leaving one representative.
- **No duplicates:** `last` advances on every iteration after zero, and each assignment writes to its own index.
- **Long duplicate runs:** Run length does not affect memory or logic; all copies after the first are ignored.
- **Unspecified suffix:** The algorithm need not erase positions from `last + 1` onward, and the judge must not compare them.
- **Negative and boundary values:** The method uses no reserved sentinel, so all allowed integers are treated uniformly.
- **Sortedness requirement:** A value appearing again after a different value would be treated as a new run, so this exact solution is not a general unsorted deduplicator.
- **Input mutation:** The caller must inspect only the first returned-count positions for the logical result.
