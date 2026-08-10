## General

A valid pair `(i,j)` must satisfy

$$
i<j
\qquad\text{and}\qquad
j-i\ge k.
$$

For a fixed right endpoint `j`, the distance condition can be rearranged:

$$
i\le j-k.
$$

Therefore every valid left endpoint for this `j` lies in the prefix

$$
0,1,\ldots,j-k.
$$

To maximize `nums[i]+nums[j]` while `j` is fixed, only the largest value in that eligible prefix matters. The source maintains that one value as it moves `j` from left to right.

**Why the right endpoint starts at `k`**

When `j<k`, even the smallest possible left index zero has distance `j<k`, so no valid pair ends there.

At `j=k`, index zero becomes the first eligible left endpoint. That is why the loop begins with:

```python
for j in range(k, len(nums)):
```

The constraints guarantee `1\le k\le n-1`, so at least one iteration and at least one valid pair exist.

**Maintaining the best eligible left value**

The variable `x` stores the largest value among all left indices currently permitted.

Before evaluating right endpoint `j`, exactly one new left index becomes eligible: `j-k`. Every smaller index was already eligible for the previous right endpoint. The update:

```python
x = max(x, nums[j - k])
```

incorporates the new boundary value without rescanning the entire prefix.

After this update, the invariant is:

$$
x=\max_{0\le i\le j-k}\texttt{nums}[i].
$$

It holds initially at `j=k` because `nums[0]` is incorporated. If it holds for one `j`, then the next iteration adds exactly `nums[j+1-k]`, extending the eligible prefix by one position. Taking the maximum preserves the invariant.

**Best pair ending at the current position**

The source stores `nums[j]` in `y`. Since `x` is the largest value at any valid left index, the greatest pair sum with right endpoint `j` is:

$$
x+y.
$$

The update

```python
ans = max(ans, x + y)
```

compares this candidate with the best pair from all earlier right endpoints.

After the final iteration, every possible `j` with at least one valid left endpoint has been processed, and every valid pair belongs to exactly one such right endpoint. Hence `ans` is the global maximum.

**Why remembering the index of `x` is unnecessary**

The function returns only a sum, not the pair's indices. Every value included in `x` came from a position no greater than `j-k` at the moment it is used, so some valid left index is guaranteed to exist. Ties between equal maximum values do not affect the sum.

If reconstruction were required, the source would also store the index whenever `x` changes.

**A full trace**

For `nums=[1,3,5,2,8]` and `k=2`:

- `j=2`: index zero becomes eligible, so `x=1`; candidate is `1+5=6`.
- `j=3`: index one becomes eligible, so `x=3`; candidate is `3+2=5`.
- `j=4`: index two becomes eligible, so `x=5`; candidate is `5+8=13`.

The maximum is thirteen, produced by indices two and four whose distance is exactly two.

Notice that a left value remains eligible for every later right endpoint after it first enters. The running maximum captures this monotonic growth of the valid prefix.

**Why zero initialization is safe here**

The source begins with:

```python
ans = x = 0
```

Every input value is positive. As soon as the first iteration incorporates `nums[0]`, `x` becomes positive, and every candidate sum is positive. Zero can therefore never incorrectly beat a real candidate.

If negative values were allowed, these initial values could create a nonexistent better pair, and negative infinity would be needed instead. The current initialization relies on the explicit positive-input contract.

## Complexity detail

Let `n` be the array length. The loop runs for right endpoints `k` through `n-1`, at most `n-k\le n` iterations. Each iteration performs constant-time indexing, maximum comparisons, and addition. Total time complexity is `O(n)`.

The variables `ans`, `x`, `j`, and `y` are scalar. No prefix array, heap, or map is allocated, so auxiliary space complexity is `O(1)`.

The input list is only read and is not modified.

The linear bound is optimal in the worst case because an element near the end may be the right endpoint of the best pair, and each newly eligible left value may become the new maximum.

## Alternatives and edge cases

- **Enumerate every pair:** Testing all `O(n^2)` index pairs and filtering by distance is correct but unnecessary. The fixed-right-endpoint maximum reduces the search to one scan.

- **Recompute the eligible-prefix maximum:** Calling `max(nums[:j-k+1])` for every `j` repeats work and can produce `O(n^2)` time.

- **Prefix-maximum array:** Precomputing `prefixMax[t]` gives each right endpoint's best left value in constant time, but uses `O(n)` space. The source maintains only the current prefix maximum.

- **Heap of earlier values:** A heap is unnecessary because eligibility only expands; no old left index ever expires. A single maximum is enough.

- **Sliding-window maximum:** This is not a fixed-width window. All indices at least `k` behind `j` remain valid forever, so there are no removals.

- **`k=1`:** Every ordered pair with `i<j` is valid. The algorithm becomes the standard scan that pairs each element with the maximum earlier value.

- **`k=n-1`:** Only pair `(0,n-1)` is valid. The loop runs once and returns its sum.

- **Distance exactly `k`:** Index `j-k` is inserted before evaluating `j`, so boundary-valid pairs are included.

- **Large distance:** Any earlier index below `j-k` remains represented in `x` and can pair with `j`.

- **Equal values:** The maximum value is sufficient; which equal index supplies it does not affect the returned sum.

- **Positive-value guarantee:** It makes zero initialization safe. Extending the function to arbitrary integers would require `-inf` initialization.

- **No index reconstruction:** The source intentionally discards the maximizing left index because only the sum is requested.

- **Input order:** Values are never sorted because validity depends on original index distance. Reordering would destroy the condition.
