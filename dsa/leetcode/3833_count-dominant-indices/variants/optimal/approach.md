## General

**A right-to-left scan makes the needed suffix available**

For index `i`, dominance depends on every element to its right. Recomputing that suffix sum from scratch at each index would repeat work.

The source instead scans from right to left while maintaining `suf`. Before checking index `i`, the invariant is

$$
\texttt{suf}
=
\sum_{j=i+1}^{N-1}\texttt{nums}[j].
$$

The number of terms in this suffix is

$$
N-i-1.
$$

Therefore its average is exactly

$$
\frac{\texttt{suf}}{N-i-1}.
$$

The source compares `nums[i]` with that value and increments `ans` only for a strict greater-than result.

**Initialize with the rightmost suffix**

The scan begins at `i = N - 2`, the second-to-last index. Its right suffix contains only `nums[N - 1]`, so `suf = nums[-1]` is the correct initial sum.

After checking an index, the source performs

`suf += nums[i]`.

When the loop moves from `i` to `i - 1`, the needed suffix has gained exactly `nums[i]`. The update restores the invariant for the next iteration.

This ordering is essential. Adding `nums[i]` before the comparison would incorrectly include the candidate itself in its right-side average.

**The final element is excluded naturally**

The rightmost index has no elements after it, so its suffix average is undefined and the statement declares it non-dominant. The loop begins at `N - 2` and never checks `N - 1`.

For a one-element array, `range(n - 2, -1, -1)` is empty. The answer stays zero, correctly excluding the only, rightmost element.

**Trace the first example**

For `nums = [5,4,3]`, initialize `suf = 3`.

At index 1, the suffix count is $3-1-1=1$, and its average is $3/1=3$. Since $4>3$, index 1 is dominant. Add 4 to `suf`, making the suffix sum 7 for the next index.

At index 0, the suffix has two values and average $7/2=3.5$. Since $5>3.5$, index 0 is dominant. The rightmost index is never considered, so the final count is 2.

For `[4,1,2]`, index 1 compares 1 with 2 and fails. After adding 1, index 0 compares 4 with $3/2$ and succeeds, giving one.

**Why the running sum proves every decision**

Initially, `suf` is exactly the right suffix for the first checked index. If it is correct before checking `i`, the denominator counts precisely those terms, so the comparison matches the dominance definition.

After adding `nums[i]`, `suf` becomes the sum from index `i` through the end. That is exactly the right suffix for index `i - 1`. By induction, every eligible index is tested against the correct suffix average once.

The algorithm neither misses a dominant index nor counts a non-dominant one because `ans` changes only when this exact definition is true.

**Floating division in the exact source**

The source evaluates `suf / (n - i - 1)` as a Python floating-point value. Under the small constraints—at most 100 values, each at most 100—the numerator is at most 9900 and comparison gaps are far larger than floating precision, so this faithfully distinguishes the valid cases.

An exact integer comparison can avoid division altogether:

$$
\texttt{nums}[i](N-i-1)>\texttt{suf}.
$$

This follows by multiplying both sides by the positive suffix count. It is a preferable general formulation for much larger integers, but it is not the expression used by the exact source.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. The loop visits exactly $N-1$ eligible indices and performs constant arithmetic at each one. Total time is $O(N)$.

Only `n`, `ans`, `suf`, and the loop index are stored. No suffix array or copied slice is created, so auxiliary space is $O(1)$.

Reading all eligible values is necessary in the worst case because changing any unseen value can alter one or more suffix averages. The source achieves the optimal linear scan.

## Alternatives and edge cases

- **Exact cross multiplication:** Test `nums[i] * (n - i - 1) > suf`. It preserves strictness and avoids floating-point division while retaining $O(N)$ time.
- **Suffix-sum array:** Precompute every suffix sum and query each average in constant time. This is also $O(N)$ time but uses unnecessary $O(N)$ space.
- **Recompute every average:** Summing `nums[i + 1:]` for every index costs $O(N^2)$ time and creates repeated slice work in Python.
- **One element:** It is the rightmost element and is explicitly not dominant, so the answer is zero.
- **Two elements:** The first is dominant exactly when it is greater than the second.
- **Equality with the suffix average:** The requirement is strict, so equality does not increment the count.
- **Fractional average:** The source compares directly against the fraction; it does not round it up or down.
- **All equal values:** Every eligible value equals its suffix average, so none is dominant.
- **Strictly decreasing values:** Every value except the rightmost exceeds every value to its right and therefore exceeds their average.
- **Positive suffix count:** Every checked index has at least one right-side value, so the division denominator is never zero.
