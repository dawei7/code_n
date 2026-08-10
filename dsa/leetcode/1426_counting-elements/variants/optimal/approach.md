## General

**Presence decides qualification, frequency decides contribution**

For a value $x$, the condition is simply whether $x+1$ appears anywhere in the array. If it does, every occurrence of $x$ must be counted separately.

For example, in `[1,1,2]`, the value 2 appears once, but both copies of 1 qualify. The answer contribution from value 1 is two, not one and not limited by the frequency of 2.

This suggests grouping equal values first. The algorithm needs:

- A fast presence test for $x+1$.
- The number of copies of $x$ to add when the test succeeds.

A `Counter` supplies both.

**Build the frequency map**

`cnt = Counter(arr)` maps each distinct input value to its occurrence count. For:

```text
[1, 1, 2, 4]
```

the relevant mapping is:

```text
1 -> 2
2 -> 1
4 -> 1
```

Building this map retains duplicate information that a plain set would discard. At the same time, its keys provide expected constant-time membership-like lookups.

Python's Counter has another useful behavior: reading a missing key returns zero instead of raising `KeyError`. Therefore, `cnt[x + 1]` is positive exactly when the successor is present and zero when absent.

**Process one distinct value at a time**

The return expression is:

```python
sum(v for x, v in cnt.items() if cnt[x + 1])
```

`cnt.items()` yields each distinct value `x` once together with its frequency `v`. The condition tests whether the successor has nonzero frequency.

If the successor exists, the generator yields `v`, thereby counting every copy of `x`. If it does not, the generator yields nothing for this key.

Summing these contributions gives the total number of qualifying array positions.

**Why successor frequency is not added**

The task is not to form one-to-one pairs. If `arr = [1,1,1,2]`, one copy of 2 is enough to make all three copies of 1 qualify. The contribution is `cnt[1] = 3`.

Conversely, in `[1,2,2,2]`, value 1 contributes one because it occurs once. The three successor copies do not multiply that contribution. Value 2 contributes only if 3 exists.

The generator correctly uses `v` from the current key and uses `cnt[x+1]` only as a truth value.

**A complete grouped trace**

Consider `arr = [1,1,2,2,3,5]`:

| `x` | Frequency `v` | Is `x+1` present? | Contribution |
|---:|---:|---|---:|
| 1 | 2 | yes, 2 exists | 2 |
| 2 | 2 | yes, 3 exists | 2 |
| 3 | 1 | no 4 | 0 |
| 5 | 1 | no 6 | 0 |

The sum is four. This is the same result as examining every original position, but equal values share one successor lookup.

**Why iterating the Counter does not lose duplicates**

A common incorrect set solution iterates distinct values and adds one for each qualifying key. That would undercount duplicates. This implementation also iterates distinct keys, but it deliberately yields their full frequencies. The compression changes how work is organized without changing how many original elements contribute.

**Why the algorithm is correct**

Partition the input positions by their value $x$. All positions in one group have the same qualification result because the existence of $x+1$ is global. If the successor exists, exactly `cnt[x]` positions in that group qualify; otherwise, none do.

The generator computes precisely that group contribution for every distinct $x$. The groups are disjoint and cover the whole input, so their sum is exactly the requested count.

## Complexity detail

Let $n$ be the array length and $U$ the number of distinct values. Building the Counter takes expected $O(n)$ time. Iterating its $U$ entries and performing expected constant-time successor lookups costs $O(U)$. Since $U \le n$, total expected time is $O(n)$.

The Counter stores $U$ keys and frequencies, requiring $O(U)$ space, which is $O(n)$ in the worst case. The generator is lazy and does not materialize a list of contributions, so it adds only constant working state.

Hash-table bounds are expected or amortized under ordinary hashing behavior. With the constrained integer range, a fixed frequency array would also provide deterministic linear time.

## Alternatives and edge cases

- **Set plus original-array scan:** Build `set(arr)`, then add one for each original `x` whose successor is in the set. It has the same expected $O(n)$ time and naturally counts duplicates.
- **Incorrect set-key scan:** Iterating only unique values and adding one undercounts repeated `x` values.
- **Direct list membership:** Testing `x + 1 in arr` for every element uses linear search and can take $O(n^2)$ time.
- **Sort and count runs:** After sorting, compare adjacent distinct runs and add the earlier run length when values differ by one. This takes $O(n\log n)$ time.
- **Fixed frequency array:** Values lie between 0 and 1000, so an array of counts can replace the hash map with constant bounded storage.
- **Duplicate current values:** Every copy contributes when one successor exists; using frequency `v` handles them together.
- **Duplicate successor values:** More than one successor copy does not increase the contribution of `x`.
- **Largest value:** If its successor is absent, its frequency contributes zero.
- **Gaps larger than one:** Only exact successor $x+1$ matters; a later value $x+2$ does not qualify `x`.
- **Counter missing-key behavior:** `cnt[x+1]` returns zero without inserting a meaningful positive count, making it safe as a Boolean test.
