## General

**Replace an average comparison with a sum comparison**

Every candidate subarray must contain exactly `k` elements. Its average is its sum divided by `k`. Because the denominator is the same positive number for every candidate, the subarray with the largest sum also has the largest average.

This lets the algorithm postpone division. It finds the maximum sum among all length-`k` windows and divides that one sum by `k` at the end. Besides being simpler, this performs only one floating-point division and keeps all window comparisons in exact integer arithmetic.

For example, if `k = 3`, comparing sums twelve and fifteen gives the same ordering as comparing averages four and five. There is no danger of a denominator changing the result because both candidates have exactly three elements.

**Compute the first complete window**

The first possible window is `nums[0:k]`. The solution sums it once and assigns that value to both `s` and `ans`:

- `s` is the sum of the window currently being examined;
- `ans` is the largest complete-window sum seen so far.

Initializing `ans` from a real window is important. Array values may all be negative. If `ans` began at zero, every actual sum could be smaller and the algorithm would incorrectly report an average that belongs to no subarray.

When `k` equals the array length, this first window is also the only window. The later loop has no iterations, and dividing `ans` by `k` returns the correct whole-array average.

**Slide by changing only two contributions**

After the first window, each next window starts one position later. Most elements are shared with the previous window. Exactly one old element leaves from the left, and exactly one new element enters from the right.

When the loop index is `i`, `nums[i]` is the entering element. The leaving element is `nums[i - k]` because it lies exactly `k` positions earlier. Therefore, the next sum is obtained with:

`s += nums[i] - nums[i - k]`.

This constant-time update avoids summing the same overlapping elements again.

Suppose `k = 3` and the current window is indices zero through two. When `i = 3`, the next window is indices one through three: add `nums[3]` and subtract `nums[0]`. On the next iteration, add `nums[4]` and subtract `nums[1]`. The formula continues in this way until the final length-`k` window.

After each update, `ans = max(ans, s)` records the larger of the best earlier sum and the new window's sum.

**The invariant behind the loop**

At the beginning of an iteration with index `i`, before the update, `s` is the sum of the length-`k` window ending at `i - 1`. Subtracting `nums[i - k]` removes that window's first element, and adding `nums[i]` appends the next element. Consequently, after the update, `s` is exactly the sum of the length-`k` window ending at `i`.

At the same point, `ans` contains the largest sum among all earlier complete windows. Comparing it with the newly computed `s` extends that statement to include the new window.

The initialization establishes both statements for the first window. The update preserves them for every later window. When the loop ends, every possible starting index from zero through `len(nums) - k` has been covered exactly once, so `ans` is the maximum length-`k` sum.

Dividing by the positive integer `k` converts that maximum sum to the maximum average. This final division is valid for negative sums as well; multiplication or division by a positive quantity preserves ordering.

**Why there is no need to remember the best window's indices**

The required output is only the average value, not the subarray itself. Therefore, storing the best sum is sufficient. If the problem also asked for indices, the algorithm could update a best-start variable whenever `s` exceeds `ans`, but that state would not improve the requested result.

**Why every possible candidate is examined**

An array of length `N` contains exactly `N - k + 1` contiguous subarrays of length `k`. The initialization handles the one starting at zero. The loop runs with `i` from `k` through `N - 1`; each such `i` creates the window starting at `i - k + 1`. Those starts are one through `N - k`. Together, initialization and loop cover all legal starts without duplication or omission.

## Complexity detail

Let `N` be the number of elements. Summing the first `k` values takes `O(k)` time. The loop then processes `N - k` entering elements, doing constant work for each. The total is `O(k + N - k) = O(N)` time.

The sliding-window state itself consists of two sums and one index, so the algorithmic technique needs `O(1)` auxiliary space.

There is a Python-specific detail in the exact solution: `nums[:k]` creates a new list containing the first `k` elements before `sum` processes it. That temporary list takes `O(k)` additional memory, so the literal implementation's peak auxiliary space is `O(k)` rather than strict `O(1)`. Summing the first window with an index loop, or with an iterator that does not materialize a slice, preserves the identical algorithm and restores the intended `O(1)` working-space bound.

Python integers avoid overflow while accumulating sums. In a fixed-width language, the maximum possible magnitude of a length-`k` sum should be checked and a sufficiently wide integer type used before converting the final result to floating point.

## Alternatives and edge cases

- **Recompute every window sum:** Summing each length-`k` subarray independently is easy to describe but costs `O(k)` per window and `O(Nk)` overall. It repeats work on the `k - 1` overlapping elements.

- **Prefix sums:** Build `prefix[i]` as the sum before index `i`, then obtain any window sum as `prefix[i + k] - prefix[i]`. This also takes `O(N)` time, but stores `O(N)` extra values when the rolling sum needs only constant state.

- **Divide every window sum:** Comparing averages on each iteration is correct, but unnecessary. All denominators equal `k`, so integer sums give the same ordering with fewer floating-point operations.

- **Initialize the maximum to zero:** This fails when every valid window has a negative sum. Initializing from the first actual window guarantees that `ans` always corresponds to a legal candidate.

- **All negative values:** The sliding update and maximum comparison work unchanged. The least negative window sum becomes `ans` and produces the largest, though still negative, average.

- **`k = 1`:** Every single element is a candidate window. The sliding update compares all values, and the answer is the maximum element divided by one.

- **`k = N`:** There is only one candidate. The loop is empty and the initialized whole-array sum is returned after division.

- **Repeated equal maxima:** The algorithm retains a maximum value but does not care which equal-sum window produced it, because only the average is requested.

- **Large values or large `k`:** Use a numeric type wide enough for the sum in languages with fixed-width integers. Converting each term to floating point early is not needed and can introduce rounding.

- **Contiguous versus noncontiguous selection:** A sliding window is valid because the requested subarray must be contiguous. Choosing the `k` individually largest values would solve a different problem.

- **Temporary slicing:** The slice in the exact Python source is concise but allocates. Avoiding the slice is necessary if the `O(1)` auxiliary-space claim must describe the literal implementation rather than the abstract sliding-window method.
