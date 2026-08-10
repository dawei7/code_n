## General

**Interpret removal as writing a valid prefix**

An array-backed Python list cannot physically discard arbitrary entries in constant time without shifting later elements. The custom judge does not require that. It asks for a count `k` and requires only `nums[:k]` to contain every original value not equal to `val`. Positions from `k` onward are unspecified.

The selected implementation therefore performs stable in-place compaction: scan every original value, copy each retained value into the next prefix position, and ignore each occurrence of `val`.

**Let `k` be both a count and a destination**

The source initializes `k = 0`. Before each scanned value `x`, the invariant is:

> `nums[:k]` contains exactly the already scanned values that are not equal to `val`, in their original relative order.

Because a prefix containing `k` values occupies indices zero through `k - 1`, index `k` is also the next free output position. This dual meaning avoids maintaining a separate write index and result count.

If `x == val`, the method performs no write and does not increment `k`. The retained prefix is unchanged, which is correct because this value must be excluded. If `x != val`, the source executes

```python
nums[k] = x
k += 1
```

The value is appended to the logical prefix and the next destination advances. This preserves the invariant.

**Why mutating during `for x in nums` is safe**

The loop reads source positions from left to right while writes move only to the left or remain at the current position. Before processing source index `i`, at most `i` earlier values have been retained, so `k <= i`. Therefore `nums[k] = x` never writes into an unvisited position after `i`.

The loop variable `x` receives the current value before the body writes anything. Overwriting an earlier array cell cannot change `x` or any future source value. This directionality is the key safety fact; a method that wrote beyond the current read position could destroy data before scanning it.

**The method preserves order even though it is not required**

Every retained value is encountered and written in original left-to-right order. Thus this variant returns a stable filtered prefix. The contract permits any order, but preserving it costs no additional asymptotic work in this scan-and-write design.

That property distinguishes it from the Competitive variant, which replaces unwanted values with elements taken from the end and may reorder the prefix.

**Trace the second example**

For `nums = [0,1,2,2,3,0,4,2]` and `val = 2`:

| Scanned `x` | Action | `k` | Meaningful prefix |
|---:|---|---:|---|
| `0` | write at 0 | 1 | `[0]` |
| `1` | write at 1 | 2 | `[0,1]` |
| `2` | skip | 2 | `[0,1]` |
| `2` | skip | 2 | `[0,1]` |
| `3` | write at 2 | 3 | `[0,1,3]` |
| `0` | write at 3 | 4 | `[0,1,3,0]` |
| `4` | write at 4 | 5 | `[0,1,3,0,4]` |
| `2` | skip | 5 | `[0,1,3,0,4]` |

The function returns five. This prefix differs in order from the illustrative output but contains the same retained multiset, and the judge explicitly sorts the prefix before comparison.

**Why every required value appears exactly once per occurrence**

Each original array position is scanned once. An occurrence equal to `val` takes the skip branch and never enters the answer prefix. Every other occurrence takes the write branch exactly once, even when several retained values are equal to each other. Consequently, the final prefix contains all and only the non-`val` occurrences, preserving multiplicity. The returned `k` equals the number of writes and therefore the required count.

**Do not confuse unspecified tail data with an error**

The source does not clear or resize the suffix. After compaction, it may contain old retained values, old occurrences of `val`, or values duplicated from the prefix. None belongs to the logical answer because the returned length excludes it. The underscores in examples are explanatory placeholders, not characters or values that the implementation should write.

## Complexity detail

Let $n$ be `len(nums)` and let $k$ be the number of retained occurrences.

- **Time complexity: $O(n)$.** Every input position is read once, and each iteration performs constant work. There are exactly $k$ assignments to the prefix.
- **Auxiliary space: $O(1)$.** Only the counter and current loop value are stored. The supplied array serves as output storage.

The worst case requires inspecting every position because an occurrence of `val` could appear at the end, so the linear bound is optimal.

## Alternatives and edge cases

- **Swap with the active tail:** On an unwanted value, replace it with the final unchecked value and shrink the active range. This can reduce writes when removals are rare but does not preserve order.
- **List comprehension or filtering:** It is concise but allocates $O(n)$ additional storage and does not implement the requested in-place prefix contract by itself.
- **Repeated deletion:** Removing individual Python-list elements shifts suffixes and can require $O(n^2)$ total time.
- **Empty input:** The loop performs no work and returns zero.
- **No occurrence of `val`:** Every value is written, possibly to its existing position, and `k = n`.
- **Every value equals `val`:** No write occurs; the returned logical prefix is empty.
- **Repeated retained values:** They are all kept because only equality with `val` causes removal.
- **`val` outside the array's value range:** No element matches, so the full array remains meaningful.
- **Order:** This exact source preserves relative order even though the judge does not require it.
- **Tail:** Never inspect positions at or beyond the returned `k` as part of the filtered result.
