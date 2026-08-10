## General

The selected competitive solution uses iterative cascading. For distinct values, the standard idea is simple: begin with the empty subset, and for each new value, copy every subset already known and append that value to the copy. Every old subset represents the choice “do not use this value,” while every new copy represents “use it.” Duplicates require one precise restriction so the same value multiset is not generated from interchangeable array positions.

The method first sorts `nums`, making equal values consecutive. It initializes `result = [[]]` because the empty subset exists before any input element is processed. At each index `i`, it saves `size = len(result)`. The inner `range(size)` is a snapshot of how many subsets existed before the current element; subsets appended during this iteration are not visited again during the same iteration.

**What `previous_size` means**

Immediately before processing index `i`, `previous_size` equals the number of subsets that existed before index `i - 1` was processed. Therefore the interval

$$
[\texttt{previous\_size},\texttt{size})
$$

contains exactly the subsets newly created by the preceding input occurrence.

When `nums[i]` is a new value, the condition in the inner loop accepts every `j` from `0` through `size - 1`. Appending the value to every existing subset is necessary because it creates the version with that value for every distinct prior choice.

When `nums[i] == nums[i - 1]`, the condition accepts only indices `j >= previous_size`. In other words, this occurrence is appended only to subsets created by the previous equal occurrence. Those are precisely the subsets that already gained one additional copy of this value in the preceding step.

**Why restricting a duplicate prevents repetition**

Consider sorted `[1, 2, 2]`.

- Initially, `result` is `[[]]`.
- Processing `1` extends all old subsets, giving `[[], [1]]`.
- Processing the first `2` also extends all old subsets, adding `[2]` and `[1, 2]`.
- Processing the second `2` extends only `[2]` and `[1, 2]`, the entries created in the previous step. It adds `[2, 2]` and `[1, 2, 2]`.

If the second `2` also extended `[]`, it would create `[2]` again. If it extended `[1]`, it would recreate `[1, 2]`. Restricting the source interval removes exactly those duplicate routes while retaining the routes that increase the multiplicity from one `2` to two.

For a run of $c$ equal values, the first occurrence creates all subsets containing one copy from every prior base subset. The second occurrence extends only that new block, creating the corresponding two-copy subsets. The third extends only the two-copy block, and so on. Each original base subset therefore appears once with zero, one, through $c$ copies of the repeated value.

**Why the algorithm is complete**

Assume that before a group with value $x$ is processed, `result` contains every distinct subset that can be made from earlier groups, exactly once. Let one such subset be $S$, and suppose $x$ occurs $c$ times. The retained old entry represents $S$ with zero copies of $x$. The first occurrence creates `S + [x]`; each later occurrence extends the block from the preceding one and creates $S$ with one additional copy. After all $c$ occurrences, the result contains exactly the $c+1$ legal multiplicities for $x$ paired with every earlier subset.

No other multiplicities are legal, and none has two construction paths. This establishes the same invariant for the next group. Starting from the sole subset of no values, `[]`, induction over all sorted groups proves both completeness and uniqueness.

**Why each subset is copied**

The code performs `result.append(list(result[j]))` and only then appends `nums[i]` to `result[-1]`. It must not append directly to `result[j]`: doing so would destroy the already-valid subset representing exclusion of the current occurrence. A new list preserves both choices as independent output entries.

Setting `previous_size = size` after the inner loop records the boundary between the subsets that predated this iteration and those just appended. Notice that it stores the old size, not the new `len(result)`. That old size is exactly the starting index of the newly generated block that the next duplicate is allowed to extend.

The source also includes `Solution2` and `Solution3`, which generate position choices and remove duplicates afterward. They are separate alternatives; the selected `Solution` avoids generating duplicate subsets in the first place.

## Complexity detail

Let $n$ be the input length and $U$ the number of distinct returned subsets. For value frequencies $c_1,c_2,\ldots,c_k$,

$$
U=\prod_{r=1}^{k}(c_r+1).
$$

Every result entry other than the initial empty subset is created once. Copying its source list takes time proportional to that source subset's length, at most $n$, and appending the new value is amortized constant time. Across $U$ outputs, generation therefore costs $O(nU)$. Sorting adds $O(n\log n)$, which is covered by the stated output-sensitive $O(n\cdot U)$ bound for the nonempty input domain. If all values are distinct, $U=2^n$ and the familiar worst-case bound is $O(n2^n)$.

The manifest lists $O(n)$ auxiliary space. The algorithm is iterative, so there is no recursion stack. Its loop counters and boundary integers are constant space, while Python's sorting implementation may require up to $O(n)$ temporary storage. Each copied subset is immediately retained as part of the output rather than held in a separate working collection. Excluding output, $O(n)$ is therefore a safe bound. Including the returned nested lists, memory is $O(nU)$ in the worst case.

The source comment says $O(1)$ space, reflecting a convention that excludes both output and language-dependent sorting workspace. The package manifest's $O(n)$ claim is the more conservative Python-specific statement.

## Alternatives and edge cases

- **Backtracking with run skipping:** Sort, recursively include the current occurrence, and make the exclusion branch jump over all equal following occurrences. It has the same $O(nU)$ time and $O(n)$ auxiliary bound and may be easier to prove as multiplicity choices.
- **Grouped-frequency generation:** Count each distinct value and expand answers by choosing zero through its frequency. This makes duplicate handling explicit and can avoid repeated equality checks.
- **Bitmask and membership filtering:** Enumerate all position masks and add a subset only if it is not already in the answer or a set. It performs redundant work; list membership can make it much slower than $O(n2^n)$.
- **Snapshot the old size:** The inner loop must use the saved `size`. Iterating over the growing `result` directly could keep processing newly appended subsets and would corrupt both termination and multiplicities.
- **Update the boundary after generation:** `previous_size` must become the pre-iteration `size`. Assigning the final length would make the next duplicate's allowed interval empty.
- **Sorting is essential:** Without adjacent duplicates, comparison with `nums[i - 1]` cannot recognize a value's run, and equal subsets can be generated through separated occurrences.
- **Input mutation:** `nums.sort()` reorders the caller's list. Use `sorted(nums)` when preservation matters outside the challenge contract.
- **All values equal:** Each iteration extends only the one newly created multiplicity chain, so exactly $n+1$ subsets are returned instead of exploring $2^n$ position choices.
- **All values distinct:** Every iteration extends all existing subsets, doubling their count and producing the ordinary power set.
- **Negative values and zero:** The method relies only on sorting and equality; it handles the full stated value range without special cases.
