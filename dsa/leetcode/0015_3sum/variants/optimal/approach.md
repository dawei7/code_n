## General

**Sorting turns each fixed first value into a two-pointer problem**

After `nums.sort()`, every returned triplet can be written in nondecreasing value order. Fix index `i` as the first value. The other two values must satisfy

$$
\texttt{nums[j]}+\texttt{nums[k]}=-\texttt{nums[i]},
$$

with `i < j < k`. Because the suffix is sorted, `j` can start immediately after `i` and `k` at the final index. Their sum moves predictably when either pointer moves.

Sorting changes the input order, but the contract asks for value triplets rather than original indices, so this mutation does not change the required result.

**Skip repeated pivot values**

The outer loop uses each possible pivot position through `n - 3`. If

```python
i and nums[i] == nums[i - 1]
```

is true, an identical pivot value was already processed with a suffix containing all value choices available now. Running the same search again could only reproduce triplets, so the duplicate pivot is skipped.

If `nums[i] > 0`, every later value is also positive. Three positive values cannot sum to zero, so `break` safely ends the entire search. Zero is not used for this break because `[0,0,0]` is valid.

**Move pointers according to the current sum**

For fixed `i`, calculate

```python
x = nums[i] + nums[j] + nums[k]
```

- If `x < 0`, the sum is too small. Decreasing `k` would choose an equal or smaller value and cannot help. Increasing `j` is the only move that can raise the sum.
- If `x > 0`, increasing `j` would keep or raise the sum. Decreasing `k` is the only move that can lower it.
- If `x == 0`, the sorted values form a valid triplet and are appended.

Each comparison also eliminates many pairs. When the sum is too small, every pair using the same `j` with a right endpoint no larger than `k` is too small. The symmetric fact holds for an excessive sum and fixed `k`.

**Advance both sides after a match and remove value duplicates**

After recording a triplet, keeping either selected pointer value can reproduce the same value combination. The method first moves both inward, then skips equal values:

```python
while j < k and nums[j] == nums[j - 1]:
    j += 1
while j < k and nums[k] == nums[k + 1]:
    k -= 1
```

The comparisons look backward for `j` and forward for `k` because those are the values just used before the move. The `j < k` guard preserves distinct indices and safe access.

Together with pivot deduplication, these loops ensure that each sorted value triplet is emitted once. Duplicate input occurrences remain usable when needed: `[-1,-1,2]` works because the pivot and left pointer occupy different indices before duplicates are skipped.

**Trace the standard example**

Sorting `[-1,0,1,2,-1,-4]` gives `[-4,-1,-1,0,1,2]`.

- Pivot `-4` has no suffix pair summing to `4`.
- Pivot `-1` starts with `j` at the second `-1` and `k` at `2`; their total is zero, producing `[-1,-1,2]`.
- Moving inward reaches `0` and `1`, producing `[-1,0,1]`.
- The next outer pivot is the repeated `-1`, so it is skipped.
- Once the pivot becomes positive, the loop stops.

**Why every distinct solution is found**

Take any sorted zero-sum triplet and consider its first value. The outer loop processes the first occurrence of that pivot. Within its suffix, two-pointer elimination discards only pairs proved too small or too large by sorted order. Therefore it cannot pass the solution pair without evaluating it. When evaluated, it is appended. Deduplication removes only equal values after that combination has been recorded, so it removes repeated output paths rather than a new value triplet.

## Complexity detail

Let $n$ be the array length.

- **Time complexity: $O(n^2)$.** Sorting costs $O(n\log n)$. For each of at most `n` pivots, `j` and `k` move inward a combined $O(n)$ times. The quadratic scan dominates sorting.
- **Space complexity: $O(n)$ under the manifest's conservative sorting bound.** Python's sorting implementation may use input-dependent temporary storage. Aside from sorting and the required output, the algorithm stores only indices and scalars, or $O(1)$ working state.

The number of returned triplets can itself be $O(n^2)$ and is not counted as auxiliary space.

## Alternatives and edge cases

- **Hash a Two Sum complement per pivot:** Also $O(n^2)$ time but needs $O(n)$ explicit hash storage and more careful output deduplication.
- **No-sort hashing:** Preserves input order but typically stores triplets in a set and has higher deduplication overhead.
- **Brute-force triples:** Tests $O(n^3)$ index combinations and is unnecessary after reducing the problem to sorted Two Sum.
- **All positive or all negative:** No zero-sum triplet exists; positive pivots trigger the early break.
- **Three zeros:** One `[0,0,0]` is emitted, then duplicate pointers/pivots are skipped.
- **Fewer than three elements:** The contract excludes this, but `range(n-2)` would perform no useful pivot iteration.
- **Distinct indices with equal values:** Pointer positions are distinct even when stored values match.
- **Output order:** Sorting produces nondecreasing values inside each triplet; the contract accepts any ordering.
- **Input mutation:** `nums.sort()` deliberately reorders the caller-provided list.
