## General

**Arbitrary deletion removes the contiguity obstacle**

Choose any desired indices in their original order and delete every other element, including elements between consecutive choices. The retained choices then form a subarray of the resulting array. The task is therefore equivalent to selecting a non-empty subsequence of pairwise distinct values with maximum sum.

**Every distinct positive value belongs in the optimum**

A positive value increases the sum, and retaining one copy never conflicts with any different value. Thus an optimal selection contains exactly one occurrence of every distinct positive value. Additional copies would violate uniqueness, while zero and negative values cannot improve a sum that is already positive.

Scan the array once. A Boolean table indexed from 1 through 100 records which positive values have appeared. On the first occurrence of a positive value, add it to the running sum; ignore later copies. Simultaneously track the maximum array element.

If the positive sum is nonzero, it is the optimum by the preceding argument. Otherwise every element is non-positive. The selected result must still be non-empty, so choosing the single maximum element is optimal; this correctly prefers zero when zero is present and otherwise chooses the least negative value.

## Complexity detail

Let $n$ be the array length. The scan takes $O(n)$ time. The marker table always has 101 entries because the contract fixes the value range to $[-100,100]$, so the auxiliary space is $O(1)$.

Reading all $n$ input values is necessary to distinguish an unseen positive value or a larger non-positive fallback, giving a matching $\Omega(n)$ lower bound.

## Alternatives and edge cases

- **Hash set of positive values:** is equally direct and takes $O(n)$ expected time, but its usual bound is written $O(u)$ space for $u$ distinct positives; the fixed Boolean table makes the bounded-space guarantee explicit.
- **Sort and deduplicate:** obtains the same values in $O(n\log n)$ time and may mutate or copy the input unnecessarily.
- **Sliding window:** addresses uniqueness in the original contiguous array, but arbitrary deletions make original contiguity irrelevant here.
- **Duplicate positives:** contribute exactly once regardless of how many copies appear.
- **Zero without positives:** must be selected instead of any negative value, producing zero.
- **All negative values:** the non-empty requirement makes the maximum single element the answer.
- **Opposite signs:** values such as `-8` and `8` are distinct, but only the positive one can improve a positive result.
