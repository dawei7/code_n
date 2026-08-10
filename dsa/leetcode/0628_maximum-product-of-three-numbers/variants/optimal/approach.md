## General

**Negative numbers create a second winning shape.** If all numbers were nonnegative, the answer would obviously use the three largest values. With negatives, two very small values can have a large positive product because negative times negative is positive. That positive pair can then be multiplied by the largest positive value.

After sorting `nums` in ascending order, the only two products that can be optimal are:

1. `nums[-1] * nums[-2] * nums[-3]`, the three largest values;
2. `nums[-1] * nums[0] * nums[1]`, the largest value with the two smallest values.

The exact solution calls these `a` and `b` and returns `max(a, b)`.

**Why sorting exposes every needed extreme.** Ascending order places the most negative values at indices 0 and 1. If both are negative, their product is the largest positive product obtainable from a negative pair: increasing either one toward zero decreases the magnitude of that positive pair. The largest overall value is at index `-1`, so candidate `b` is the strongest product using two negatives.

The three greatest values are at indices `-3`, `-2`, and `-1`. Candidate `a` covers the ordinary all-positive case, a mix involving zero, and the all-negative case where no positive product is possible.

**Why there are no other sign patterns to examine.** A product of three real integers has these relevant forms:

- three nonnegative values, best served by the three largest values;
- one nonnegative value and two negative values, best served by the largest nonnegative value and the two most negative values;
- one negative value with two nonnegative values, producing a nonpositive result and never beating an available positive product;
- three negative values, producing a negative result.

If a positive product is possible, it must come from one of the first two candidates. If no positive product is possible, the input is effectively all negative apart from possible zeros. Among three negatives, the maximum is the value closest to zero, obtained by the three largest array values; if zero is available, candidate `a` or `b` includes it and returns zero rather than a negative product.

**An exchange view makes the extreme choice precise.** Suppose a candidate uses two negative numbers and a third value. Replacing either negative with a more negative value increases the positive product of that pair. Replacing the third value with the global maximum cannot decrease the complete product when the pair is nonnegative. Thus the best two-negative candidate is exactly `nums[0] * nums[1] * nums[-1]`.

For a candidate not relying on a negative pair, replacing any selected value with a larger unused value does not reduce the maximal relevant product. Repeating that exchange leads to the three largest elements, candidate `a`. Therefore, an optimal triplet must be represented by `a` or `b`.

**Trace representative cases.** For `[1,2,3,4]`, sorting leaves the same order. Candidate `a = 4 * 3 * 2 = 24`, while `b = 4 * 1 * 2 = 8`, so the answer is 24.

For `[-10,-10,1,2,3]`, `a = 3 * 2 * 1 = 6`. Candidate `b = 3 * (-10) * (-10) = 300`, revealing why checking only the three largest values is wrong.

For `[-3,-2,-1]`, `a = (-1) * (-2) * (-3) = -6`. Candidate `b` uses the same three values in another order and is also -6. That is the maximum because every possible triplet is the complete array.

**Duplicates and zeros require no branches.** Sorting keeps duplicate occurrences as distinct selectable elements, which is correct because selection is by array position. If zero can prevent a negative result, it naturally appears among one of the extreme triplets. Standard integer multiplication and `max` handle all ties.

**The exact source mutates the input.** Python's `nums.sort()` sorts the caller-provided list in place. The returned number is correct, but the order of `nums` is not preserved. The challenge does not require preserving it. In an API where mutation is undesirable, use `sorted(nums)` or the constant-state single scan.

## Complexity detail

Let $n$ be the length of `nums`. Python's in-place sort takes $O(n\log n)$ worst-case time. Reading six indexed values, computing two products, and taking their maximum are $O(1)$. The exact implementation's total time is therefore $O(n\log n)$.

The manifest lists $O(n)$ time and $O(1)$ space, which describes the editorial's single-scan method that tracks the two smallest and three largest values. It does not describe this literal sorting source. Python's Timsort can use $O(n)$ auxiliary merge storage in the worst case, even though it mutates the list in place. Thus the exact language-level auxiliary bound is $O(n)$, not the manifest's $O(1)$.

A five-extrema single scan would achieve the manifest bounds: update two minima and three maxima for each value, then evaluate the same two products. Product magnitude is at most $1000^3=10^9$, which fits a signed 32-bit integer; Python also provides arbitrary-precision safety.

## Alternatives and edge cases

- **Single scan over five extrema:** Track the two smallest and three largest values in $O(n)$ time and $O(1)$ space. This is the true optimal implementation and matches the manifest.
- **Heap selection:** Find three maxima and two minima with small heaps. It remains linear up to constant heap factors but is more complex than five scalar variables.
- **Brute-force triplets:** Checking every triple costs $O(n^3)$ and ignores the extreme-value structure.
- **All positive values:** The three-largest candidate wins.
- **Two large-magnitude negatives:** Their positive pair may make the two-smallest candidate win.
- **All negative values:** The three largest, meaning those closest to zero, produce the least negative and therefore maximum product.
- **Zeros present:** Zero correctly beats every negative product when no positive triplet exists.
- **Exactly three elements:** Both formulas use those same three positions in some order, so their product is returned.
- **Duplicate extrema:** Duplicates are separate array elements and may all be selected when present.
- **Input mutation:** `sort()` changes `nums`; use `sorted(nums)` to copy or a single scan to preserve order.
- **Manifest mismatch:** Do not claim $O(n)$/$O(1)$ for the literal Python source merely because a different algorithm can attain those bounds.
- **Integer range:** The constraint bounds the product by $10^9$ in absolute value, so fixed-width 32-bit signed arithmetic is safe.
