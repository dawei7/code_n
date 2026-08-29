## General

**Reframe the task as stable compaction**

Moving every zero to the end while preserving nonzero order is equivalent to compacting all nonzero values into the earliest array positions. Once every nonzero has been placed in front, all remaining positions must be zeros because the operation only rearranges existing elements.

The exact solution performs this compaction with two conceptual pointers:

- `i`, supplied by `enumerate`, scans every original position from left to right;
- `k` is the next position where an encountered nonzero value belongs.

The scan pointer discovers values, while the write pointer marks the boundary between the compacted nonzero prefix and the zeros waiting behind it.

**Maintain three regions during the scan**

Immediately before processing index `i`, the array has this logical structure:

```text
[ stable nonzero prefix | zeros | unprocessed suffix ]
  indices [0, k)       [k, i)       [i, n)
```

More precisely:

1. indices before `k` contain exactly the nonzero values encountered so far, in their original relative order;
2. indices from `k` through `i - 1` contain zeros; and
3. indices from `i` onward have not yet been processed by the scan.

This invariant explains why an adjacent-looking swap between `k` and `i` is safe even when those indices are far apart.

**When the current value is zero, leave it in the zero region**

The source stores the current enumerated value in `x` and checks `if x`. For integer inputs, Python treats zero as false and every positive or negative nonzero integer as true.

If `x` is zero, no compaction write is needed. The scan advances to the next index while `k` stays fixed. The zero at `i` simply enlarges the middle zero region by one position.

Skipping writes for zeros is useful: a two-pass overwrite solution might later rewrite many positions with zero even when they already contain zero. This swap-based method lets zeros move into their final suffix positions as a consequence of relocating nonzero values.

**When the current value is nonzero, place it at `k`**

If `x` is nonzero, it is the next nonzero encountered in left-to-right order, so its final compacted position must be exactly `k`. The source swaps `nums[k]` and `nums[i]`, then increments `k`.

There are two cases.

If `k < i`, the invariant says `nums[k]` is zero. The swap moves the current nonzero left into its required compacted slot and moves that zero to index `i`. After `k` increments, the stable nonzero prefix has grown by one and the positions between the new `k` and the next scan index are still all zero.

If `k == i`, there is no zero gap: every value encountered so far is nonzero. The tuple assignment swaps the element with itself, leaving the array unchanged, and incrementing `k` extends the compacted prefix. The operation is logically harmless, though an optional `if k != i` check could avoid the physical self-assignment.

**Why relative order is preserved**

Nonzero values are encountered from left to right, and each one is written to consecutive positions `0, 1, 2, ...`. Therefore, the first encountered nonzero occupies index 0, the second occupies index 1, and so on. A later value can never be placed before an earlier value.

The value swapped rightward is always zero when `k < i`, not an earlier nonzero. Thus no previously compacted nonzero is displaced or reordered. This is a stable compaction, not merely a partition by value.

**Why all remaining positions are zeros at the end**

After the final scan index, the unprocessed suffix is empty. The invariant becomes

```text
[ all original nonzero values in order | only zeros ]
  indices [0, k)                    [k, n)
```

Every nonzero encountered increased `k` exactly once, so `k` equals the total number of nonzero elements. The array length is unchanged, meaning the remaining `n - k` positions equal the original number of zeros. Because the invariant says those positions contain zeros, both output requirements are satisfied.

**Trace the first example**

For `nums = [0,1,0,3,12]`:

| `i` | `x` | `k` before | Action | Array afterward | `k` after |
|---:|---:|---:|---|---|---:|
| 0 | 0 | 0 | skip | `[0,1,0,3,12]` | 0 |
| 1 | 1 | 0 | swap indices 0 and 1 | `[1,0,0,3,12]` | 1 |
| 2 | 0 | 1 | skip | `[1,0,0,3,12]` | 1 |
| 3 | 3 | 1 | swap indices 1 and 3 | `[1,3,0,0,12]` | 2 |
| 4 | 12 | 2 | swap indices 2 and 4 | `[1,3,12,0,0]` | 3 |

The encountered nonzeros `1`, `3`, and `12` occupy the prefix in exactly that order, and each swap pushes a zero into the position vacated on the right.

For `[0]`, the sole value is false in the condition, so no swap occurs and the array already has the required form.

## Complexity detail

Let $n$ be the array length. `enumerate` visits each position exactly once. Each iteration performs a constant-time truth test and, for a nonzero, one constant-time tuple swap. Total time is $O(n)$.

Linear time is asymptotically optimal because every element may affect whether and where compaction occurs; an algorithm cannot safely ignore an arbitrary unseen position.

The source stores `k`, `i`, `x`, and temporary values used by tuple assignment. It allocates no collection proportional to the input, so auxiliary space is $O(1)$. The list is modified in place and the method returns `None`.

If there are $z$ nonzero elements, the source executes exactly $z$ tuple swaps. In Python, each tuple swap assigns both indexed positions, including when `k == i`; consequently, an already compacted all-nonzero array still performs self-swaps. Adding a guard for `k != i` could reduce writes in that case without changing asymptotic bounds or correctness.

## Alternatives and edge cases

- **Overwrite then fill zeros:** Copy nonzeros forward with a write pointer, then assign zero to every remaining suffix position. This is also stable, $O(n)$ time, and $O(1)$ space, but it always performs a second filling phase.
- **Extra result array:** Append all nonzeros and then enough zeros to a new list. It is simple but violates the in-place $O(1)$-space requirement.
- **Unstable two-ended partition:** Swapping zeros with arbitrary nonzeros from the right can group zeros at the end but reverses or otherwise changes nonzero relative order.
- **No zeros:** `k == i` at every iteration, so the exact source self-swaps every value and leaves the list unchanged.
- **All zeros:** The condition is never true, `k` remains zero, and no writes occur.
- **Leading zeros:** Early nonzeros swap into the prefix, pushing those zeros rightward one at a time.
- **Trailing zeros:** Nonzeros already occupy their stable prefix positions; trailing zeros are skipped and remain in place.
- **Consecutive zeros:** They simply widen the middle zero region. The next nonzero jumps over the entire region with one swap.
- **Negative values:** Any negative integer is truthy in Python and is correctly treated as nonzero.
- **Duplicate nonzero values:** Stability concerns occurrences, not distinct values. Encounter order is preserved even when values compare equal.
- **Length one:** Either the single zero is skipped or the single nonzero is self-swapped; both outcomes are valid.
- **Cached loop value `x`:** `enumerate` supplies the current value before the swap. The decision is therefore based on the element originally encountered at index `i`, while subsequent iterations read the array's then-current contents. The invariant ensures swaps only place zero into an already processed index `i`, never corrupting the unprocessed suffix.
- **Input mutation:** In-place modification is required. Callers that need the original arrangement must make their own copy before invoking the method.
