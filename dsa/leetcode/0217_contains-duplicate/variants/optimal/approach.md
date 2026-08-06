## General
Scan from left to right with a hash set containing values already encountered. Before inserting the current value, test membership. A hit proves that the same integer occurred at an earlier index, so the function can return immediately; otherwise add it and continue.

For `[1,2,3,1]`, the set before the final position is `{1,2,3}`. The last `1` is already present, which witnesses two distinct occurrences without needing their exact indices.

The algorithm stores values rather than counts because the question asks only whether multiplicity reaches two. Once a second occurrence is found, no later data can change the true result.

Before processing each position, the set contains exactly the distinct values in the earlier prefix. If the current value is present, that earlier prefix contains an equal occurrence at a different index, so returning true is correct. If it is absent, insertion restores the property for the extended prefix. If the scan finishes, every value was absent before insertion, so no two positions contain the same integer and returning false is correct.

## Complexity detail
Expected hash-set insertion and lookup are $O(1)$, giving expected $O(n)$ time. In the all-distinct case the set stores `n` values, using $O(n)$ space.

## Alternatives and edge cases
- **Sorting:** It places duplicates next to one another but costs $O(n \log n)$ time and may mutate the input.
- **Pairwise comparison:** Comparing every pair takes $O(n^2)$ time.
- **Whole-set length comparison:** Comparing `len(nums)` with `len(set(nums))` has the same expected bounds, but builds
  the full set even when a duplicate appears early.
- **Single value:** A one-element legal input contains no duplicate; negative values and zero are ordinary hash keys.
