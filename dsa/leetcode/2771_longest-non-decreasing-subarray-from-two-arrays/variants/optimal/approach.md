## General

Only the value chosen at the immediately previous index matters when deciding whether a non-decreasing subarray can extend to the current index. However, that previous value could have come from either input array, so retain one state for each possibility.

**Two ending states**

At index $i$, let the first state be the greatest length of a valid subarray ending with `nums1[i]`, and let the second state be the corresponding length ending with `nums2[i]`. Each new state starts at $1$, because a subarray may begin at the current index.

To compute the new first state, compare `nums1[i]` with both values available at index $i-1$. Whenever the current value is at least a previous value, extend the matching previous state by one. Compute the new second state through the analogous two comparisons for `nums2[i]`.

**Why no earlier information is needed**

A contiguous subarray ending at $i$ must include index $i-1$. Its final choice there is either `nums1[i-1]` or `nums2[i-1]`, exactly the two stored possibilities. The associated state already represents the longest compatible prefix ending with that value, so testing both transitions considers every valid way to extend and taking their maximum is exact.

Record the largest state seen at any index, since the requested subarray may end before the arrays do. Once the next pair is computed, older states can be discarded.

## Complexity detail

Let $n$ be the common array length. The scan performs four constant-time comparisons per index, giving $O(n)$ time. It retains only two previous states, two current states, and the global maximum, so the auxiliary space complexity is $O(1)$.

## Alternatives and edge cases

- **Restart from every left endpoint:** Running the two-state transition separately for every possible start is correct but costs $O(n^2)$ time.
- **Full DP arrays:** Storing both states for every index also takes $O(n)$ time but uses $O(n)$ space even though only the previous pair is needed.
- **Enumerate all constructed arrays:** Trying both choices at every position produces $2^n$ arrays and is infeasible.
- A one-element input always returns $1$, because the required subarray is non-empty.
- Each state must restart at $1$ when neither previous choice can extend to its current value.
- Equality is valid because the condition is non-decreasing, not strictly increasing.
- The best subarray may begin after index $0$ or end before index $n-1$.
