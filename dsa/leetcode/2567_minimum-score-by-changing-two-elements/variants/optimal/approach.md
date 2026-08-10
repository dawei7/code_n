## General

**The low score can always be made zero**

The low score is the minimum absolute difference between any pair. After changing two elements, set at least one changed value equal to another value in the final array. Then two elements are equal and their absolute difference is zero. Since absolute differences cannot be negative, the low score is exactly zero.

With $n\ge3$, there is always an unchanged value available. The two changed elements can both be assigned a value already present among the survivors, creating duplicates without enlarging the remaining range.

Therefore, the optimization reduces to minimizing the high score, which is the maximum absolute difference. For any set of numbers, that maximum is simply

$$
\max(\texttt{nums})-\min(\texttt{nums}).
$$

**Only extreme values can control the high score**

Changing an element strictly inside the current minimum and maximum cannot shrink the range: both old extremes would remain. To reduce the high score, the two permitted changes must neutralize two occurrences among the low and high extremes.

After sorting, write the values as

$$
a_0\le a_1\le\cdots\le a_{n-1}.
$$

There are only three ways to distribute two changes between the ends:

- change the two smallest values;
- change one smallest and one largest value;
- change the two largest values.

Changing any less-extreme combination cannot produce a smaller surviving interval, because an unchanged value farther outside would still determine the range.

**Case one: neutralize the two smallest**

If `nums[0]` and `nums[1]` are changed into values inside the interval of the remaining elements, the smallest unchanged value becomes `nums[2]` and the largest remains `nums[-1]`. The smallest possible high score for this case is

`nums[-1] - nums[2]`.

The changed values can, for example, both be assigned `nums[2]`. This keeps them inside the new range and also makes the low score zero.

**Case two: neutralize one value at each end**

If `nums[0]` and `nums[-1]` are changed into the surviving interval, the new extremes are `nums[1]` and `nums[-2]`. The resulting high score is

`nums[-2] - nums[1]`.

Both changed values may be assigned any surviving value, such as `nums[1]`, so the bound is achievable and the low score remains zero.

**Case three: neutralize the two largest**

If `nums[-2]` and `nums[-1]` are changed, the largest unchanged value becomes `nums[-3]` while the minimum remains `nums[0]`. The high score is

`nums[-3] - nums[0]`.

Again, assigning both changed entries to an in-range survivor realizes this range and creates equal values.

The function returns the minimum of exactly these three expressions.

**Why no fourth case is needed**

Suppose a proposed solution changes two elements but leaves at least three of the four outer candidates `nums[0]`, `nums[1]`, `nums[-2]`, and `nums[-1]` in their original roles. Its surviving range contains one of the three intervals listed above and therefore cannot be narrower.

More directly, remove the two changed original positions temporarily. The minimum and maximum of the remaining $n-2$ values determine a range that changed values can be placed inside. To minimize this range, the removed positions must be some number from the left end and the rest from the right end. Removing two positions gives splits $2+0$, $1+1$, or $0+2$, precisely the three cases.

This argument is about occurrences, not distinct values. If several extremes are equal, the formulas still work: changing two copies may leave another equal copy as the extreme, and the corresponding difference reflects that.

**Walk through the first example**

Sorting `[1,4,7,8,5]` gives `[1,4,5,7,8]`. The candidates are:

- change the two smallest: $8-5=3$;
- change one at each end: $7-4=3$;
- change the two largest: $5-1=4$.

The minimum is $3$. In the first case, changing $1$ and $4$ to $6$ keeps all values between $5$ and $8$ and creates a duplicate, so high score is $3$ and low score is zero.

For any three-element array, changing two elements to equal the third makes all values equal. Each formula also becomes zero because its selected surviving minimum and maximum are the same occurrence value.

**Following the exact implementation**

The code calls `nums.sort()` and then reads the necessary indexed extremes. It does not use a linear-time selection routine to find only the three smallest and three largest values. Sorting mutates the caller's array but makes the three cases compact and transparent.

The manifest summary and complexity describe a possible linear extrema-tracking implementation. The algorithmic three-case insight is the same, but the checked-in source has sorting's actual runtime.

## Complexity detail

Let $n$ be the array length. Sorting `nums` takes $O(n\log n)$ time. Evaluating three differences and their minimum takes $O(1)$ time. The exact implementation is therefore $O(n\log n)$, not the manifest's stated $O(n)$.

Python's in-place Timsort may use $O(n)$ temporary memory in the worst case, even though no separate sorted list is created. After sorting, the arithmetic uses $O(1)$ additional space. A purpose-built scan retaining only three minima and three maxima could achieve $O(n)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Track six extremes:** Maintain the three smallest and three largest values in one pass, then evaluate the same formulas in $O(n)$ time and $O(1)$ space.
- **Try all changed pairs:** Choosing two indices gives $O(n^2)$ possibilities and is unnecessary because only extreme removals can shrink the range.
- **Change interior elements:** Unless an extreme is also changed, the old minimum or maximum survives and prevents the high score from shrinking.
- **Exactly three elements:** Two can be changed to the third, so the answer is always zero.
- **All values equal:** Both low and high scores are already zero; changing values to themselves or the same value preserves zero.
- **Duplicate extremes:** The sorted formulas correctly account for remaining copies of a minimum or maximum.
- **Low score:** It need not be optimized separately once a changed element is assigned equal to a surviving value; zero is the absolute lower bound.
- **Large values:** Only subtraction is used, and Python integers avoid overflow.
- **Input mutation:** `nums.sort()` changes the original order. Sorting a copy would preserve caller state at $O(n)$ explicit storage.
- **Manifest distinction:** The three-case method is optimal in insight, but this exact implementation uses full sorting rather than constant-space extrema selection.
