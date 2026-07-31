## General

**Characterize the only possible range**

Let $x$ be the smallest array value and $n$ the array length. The definition fixes the required set as the $n$ integers from $x$ through $x+n-1$. Consequently, its largest possible member must be $x+n-1$, or equivalently the observed span must satisfy $\max(\texttt{nums})-x=n-1$.

The span condition alone is insufficient: duplicates can coexist with missing interior values. For example, `[1, 2, 2, 4]` has the correct endpoint span for length four but omits `3`.

**Combine span and distinctness**

Insert all values into a set. The array is consecutive exactly when the set still has $n$ elements and the maximum-minus-minimum span is $n-1$.

If both conditions hold, there are $n$ distinct integers inside an inclusive integer range that itself contains exactly $n$ values, so none can be missing. Conversely, every consecutive array has distinct members and the required endpoint span, so it passes both checks.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Building the hash set and finding both endpoints each take expected $O(n)$ time, giving $O(n)$ expected total time.

The set can store all $n$ values, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Sort then compare neighbors:** Sorting followed by adjacent-difference checks is correct but takes $O(n\log n)$ time.
- **Mark a fixed value domain:** A boolean array supports linear time but spends space according to the global value bound rather than the input length.
- **Endpoint span only:** This misses an interior gap when another value is duplicated.
- **Set size only:** Distinct values need not be consecutive; `[1, 3]` has no duplicate but has a gap.
- **Single element:** Any one-element array is consecutive because its required range contains only that value.
- **Arbitrary order:** Permuting a consecutive array does not change the result.
- **Duplicate:** Any repeated value forces some required range member to be absent.
