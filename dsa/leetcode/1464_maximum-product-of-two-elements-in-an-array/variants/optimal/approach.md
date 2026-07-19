## General
**Reducing the objective to the two largest values**

Every input value is at least `1`, so every adjusted factor `nums[i] - 1` is nonnegative. If one selected value is replaced by a larger unselected value at a different index, its adjusted factor cannot decrease, and multiplying it by the other nonnegative factor cannot make the product smaller. Repeating this exchange shows that some optimal pair consists of the largest and second-largest array entries, counting duplicate occurrences separately.

The subtraction does not change the ordering: whenever $a \ge b$, then $a-1 \ge b-1$. It is therefore sufficient to identify the two largest original values and apply the adjustment only once at the end.

**Maintaining two maxima in one pass**

Keep `largest` and `second_largest`, representing the greatest and second-greatest values among the elements processed so far. When a new value exceeds `largest`, the old largest becomes the second largest and the new value takes first place. Otherwise, if the new value exceeds `second_largest`, update only the second position.

The second comparison deliberately allows a value equal to `largest` to become `second_largest`. For example, after reading both `5` entries in `[1,5,4,5]`, the maintained pair must be `(5, 5)`, because those occurrences occupy different valid indices.

**Why the maintained pair is sufficient**

After processing one element, `largest` is correct and a second value is not yet available. Assume the two variables correctly describe the two greatest processed occurrences before the next element. If the new value is greater than `largest`, it becomes the greatest and the former greatest is necessarily next. If it is not greater than `largest` but is greater than `second_largest`, it belongs in second place. Otherwise both existing values remain at least as large, so the pair does not change.

Thus, after the entire array has been scanned, the variables hold exactly the two greatest occurrences. The exchange reasoning establishes that their adjusted product is at least the product of every other valid pair, so `(largest - 1) * (second_largest - 1)` is the required maximum.

## Complexity detail
The algorithm visits each of the $n$ elements once and performs only a constant number of comparisons and assignments per element, for $O(n)$ time. It stores two running values regardless of the input length, so its auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Sort the array:** Sorting and using the final two entries is concise and correct, but it costs $O(n \log n)$ time and may mutate the input unless a copy is made.
- **Maximum heap:** A heap can expose the two greatest elements in $O(n)$ construction time, but it requires $O(n)$ auxiliary storage and is unnecessary when only two values are needed.
- **Enumerate every pair:** Checking all $n(n-1)/2$ index pairs directly is correct but takes $O(n^2)$ time and repeats comparisons that the two-maxima invariant avoids.
- **Duplicate maximum:** Two equal maximum values are a valid pair when they come from separate positions. The update rules must preserve both occurrences.
- **Exactly two elements:** Both entries must be selected, and the same one-pass logic still produces their adjusted product.
- **Values equal to one:** An adjusted factor may be zero. Because all factors are nonnegative, selecting the two largest original values remains valid even when the maximum product is zero.
- **Distinct indices:** Never reuse one occurrence as both factors. Tracking two processed occurrences, rather than merely the maximum numeric value, enforces this requirement.
