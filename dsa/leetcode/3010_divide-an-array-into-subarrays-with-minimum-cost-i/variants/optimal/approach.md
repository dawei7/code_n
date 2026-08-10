## General

**A partition is determined by its start indices**

Dividing `nums` into three nonempty contiguous subarrays requires two cut starts after index zero. If the second subarray begins at $i$ and the third at $j$, then:

$$
1\le i<j<N.
$$

The three costs are `nums[0]`, `nums[i]`, and `nums[j]`. The contents after each start do not affect cost.

The first cost is therefore forced. Minimizing the total reduces to choosing two distinct values from `nums[1:]` with minimum possible sum.

**Why the two smallest later values always form valid starts**

Take the indices of the two smallest values after index zero and order those indices increasingly. The earlier can start the second subarray and the later can start the third. Both subarrays are nonempty, and the remaining suffix after the later index forms the third subarray.

Thus there is no compatibility constraint beyond choosing two distinct positions. Numeric order and index order need not agree; chosen indices can always be sorted into the required cut order without changing their values or total cost.

**Maintain the two smallest values in one scan**

`a = nums[0]` stores the forced first cost. `b` and `c` begin at infinity and represent the smallest and second-smallest later values seen.

For each `x`:

- if `x < b`, the previous smallest becomes second-smallest (`c = b`) and `b = x`;
- otherwise, if `x < c`, `x` becomes the second-smallest.

Using strict comparisons still handles duplicates correctly. If `x == b` and `c` is larger, the `elif x < c` branch stores the second copy in `c`. Distinct indices, not distinct numeric values, are required.

After at least two later elements—the array length is at least three—both `b` and `c` are finite. The answer is `a + b + c`.


Any valid three-way division chooses two later starts, so its extra cost is the sum of two elements from `nums[1:]`. No pair can have a sum smaller than the two smallest values of that multiset.

The scan invariant ensures `b` and `c` are exactly those two smallest values after every processed prefix. Their source indices can be ordered into valid second/third starts, so the lower bound is achievable. Adding forced `nums[0]` gives the global minimum.

**Scan invariant**

Initially, no later values have been processed and both sentinels are infinity. After processing a value:

- when it is below `b`, shifting old `b` to `c` preserves the two best values;
- when it lies between `b` and `c`, replacing only `c` is correct;
- when it is at least `c`, neither stored minimum changes.

Induction establishes the invariant through the whole suffix.

**An exact Python space subtlety**

The loop is written `for x in nums[1:]`. Python list slicing constructs a new list containing $N-1$ references. Therefore, although the minimum-tracking algorithm itself uses only three scalars, this exact implementation allocates $O(N)$ temporary auxiliary space.

The manifest claims $O(1)$ space, which would be accurate for `for i in range(1, len(nums))` or `itertools.islice(nums, 1, None)`, but not for the protected source as written. Time remains linear.

The slice does not mutate `nums`; it copies references to its integer elements.

**Why subarray endings require no optimization**

Once starts $0<i<j$ are selected, contiguity forces the three pieces to be `nums[0:i]`, `nums[i:j]`, and `nums[j:n]`. There is no separate choice of endings, and every element is covered exactly once.

The cost definition reads only positions zero, $i$, and $j$. Values inside the pieces can be arbitrarily large or small without affecting this particular division’s cost. This is why choosing the two cheapest later start values completely solves the partition problem rather than serving as a heuristic.

## Complexity detail

Let $N$ be the array length. Creating `nums[1:]` takes $O(N)$ time and space. The scan performs constant work for each of $N-1$ values, so total time is $O(N)$.

The three logical minimum variables are $O(1)$, but the exact slice makes auxiliary space $O(N)$. This is a real implementation/manifest mismatch rather than output space, since the method returns one integer.

## Alternatives and edge cases

- **Sort the suffix:** Taking its first two values works but costs $O(N\log N)$ time and usually allocates a slice.
- **Enumerate cut pairs:** Testing all $i<j$ costs $O(N^2)$ despite the absence of interaction between chosen values.
- **Use `nsmallest(2, nums[1:])`:** It expresses the goal but still creates the slice unless given an iterator.
- **Duplicate minimum values:** Two equal values at different positions may be both chosen; the strict-update branches retain both.
- **Exactly three elements:** Both later values are forced and the result is the sum of all three.
- **Smallest value at a later index order:** Numeric minima can always be ordered by their indices to define the two cuts.
- **Positive-value guarantee:** Infinity sentinels are safe; the logic would also work for negative values.
- **Manifest space mismatch:** Use $O(N)$ auxiliary space for this exact sliced loop.
- **Input preservation:** The source array is not sorted or modified.
