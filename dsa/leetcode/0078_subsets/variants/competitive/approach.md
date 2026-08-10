## General

**Grow the power set one input value at a time**

Before processing any number, the only subset of the empty processed prefix is the empty subset, so `result` starts as `[[]]`. When a new value `x` is introduced, every subset of the enlarged prefix falls into exactly one of two categories:

- It does not contain `x`, in which case it is already present in `result`.
- It contains `x`, in which case removing `x` leaves one previously existing subset.

Therefore the new power set is the old power set plus one copy of every old subset with `x` appended. This is often called cascading because each stage grows directly from the complete preceding stage.

**Snapshot the old result size before appending**

At the start of an outer iteration, `size = len(result)` records how many subsets belong to the already processed values. The inner loop visits exactly indices `0` through `size - 1`.

This snapshot is essential because the loop appends new subsets to `result`. Iterating to the list's continuously changing length would also visit newly added subsets during the same stage, append the same `nums[i]` repeatedly, and destroy the one-copy construction. Restricting the loop to the old prefix ensures every old subset creates exactly one new subset.

**Copy before adding the new value**

`result.append(list(result[j]))` creates an independent copy of an existing subset. `result[-1].append(nums[i])` then changes only that new list.

If the source appended `result[j]` itself and then appended the value, the old no-new-value subset and its intended new counterpart would be aliases of one object. Adding the value to one would modify both, losing the exclusion category. The fresh list preserves both versions.

After the first value, the result contains `[]` and `[x]`. After a second value `y`, the two old subsets remain, while their copies become `[y]` and `[x, y]`. The result size doubles at every stage, matching the binary include/exclude choices of the power set.

**Why sorting is performed and what it changes**

The source calls `nums.sort()` before generation. Sorting is not required for correctness because the contract permits any output order and each input value is unique. It does make elements within every produced subset appear in ascending numeric order and gives a predictable stage order.

This call mutates the caller's input list. The problem requires the returned power set but does not request mutation of `nums`; therefore this is an observable side effect not needed by the algorithm. A non-mutating alternative would iterate over `sorted(nums)` or simply retain original order.

Sorting does not create or remove membership patterns. Because all values are unique, there is still a one-to-one correspondence between old subsets and new subsets containing the stage's value.

**An induction proof for each cascade stage**

Before processing `nums[i]`, suppose `result` contains every subset of `nums[:i]` exactly once. This is true at `i == 0` because the processed prefix is empty and `result` contains exactly `[]`.

The inner loop preserves every old subset and appends a distinct copy of it containing `nums[i]`. Old subsets are precisely those excluding the new value; appended subsets are precisely those including it. The two groups cannot overlap because only the second contains `nums[i]`. Within each group, uniqueness follows from uniqueness at the preceding stage and from copying each old subset once.

Their union is every subset of `nums[:i + 1]`. Induction through all sorted values proves that the final `result` is the complete duplicate-free power set.

**Trace `[1, 2, 3]`**

The stages are:

`[[]]`

then `[[], [1]]`,

then `[[], [1], [2], [1, 2]]`,

and finally those four old lists followed by `[3]`, `[1, 3]`, `[2, 3]`, and `[1, 2, 3]`.

The stage order differs from some example orderings but is allowed. More importantly, every newly appended subset at a stage contains the current value exactly once because the input has no duplicates and only one append is performed.

**Output storage is the dominant resource**

The algorithm is iterative and has no call stack. It does allocate each subset list required by the output. Those lists are not incidental waste: returning the materialized power set necessarily requires them. Still, complexity explanations must distinguish unavoidable result storage from extra working storage.

## Complexity detail

After all `n` stages there are $2^n$ subsets. Copying old subset lists and appending values writes $\Theta(n2^n)$ total element occurrences across the result. Sorting adds $O(n\log n)$ time, which is dominated by generation for the nontrivial power-set output. Total time is $O(n2^n)$, matching the manifest.

Excluding the result, the loop uses scalar indices and one at-most-`n`-element list while a new output subset is being copied. Python's in-place sort may also use up to $O(n)$ temporary storage, so an honest auxiliary bound is $O(n)$, matching the manifest. The returned power set itself occupies $\Theta(n2^n)$ space. The source comment's `O(1)` applies only to a very narrow exclusion of output objects and sort/copy temporaries.

## Alternatives and edge cases

- **Recursive include/exclude DFS:** It mirrors the binary membership decisions and uses $O(n)$ stack space.
- **Bitmask generation:** Enumerate all $2^n$ masks and include `nums[j]` when bit `j` is set. It has the same output-sensitive complexity.
- **Non-mutating iteration:** Use the original order or a separate `sorted(nums)` result to avoid changing the caller's list.
- **Snapshot omission:** Looping over the growing result would reuse subsets created in the current stage and could append the same value repeatedly.
- **Aliasing omission:** Appending an old subset without copying would mutate the exclusion version when the new value is added.
- **Empty subset:** It is seeded explicitly and remains in the result through every stage.
- **Full subset:** It is created by repeatedly copying the prior full-prefix subset and appending the new stage value.
- **One input value:** The single stage turns `[[]]` into `[[], [value]]`.
- **Negative values:** Sorting changes their position but not membership logic.
- **Unique input:** It guarantees the include and exclude construction cannot create duplicate value subsets.
- **Any output order:** Cascading order is valid without post-processing.
- **Input mutation:** `nums.sort()` is an unnecessary but real side effect of the selected source.
- **Maximum length ten:** The result has 1024 subsets, and memory is dominated by those required output lists.
