## General

**Count subarrays by their right endpoint**

Every subarray has one unique ending index. While scanning from left to right, the algorithm counts how many strictly increasing subarrays end at the current element and adds that number to the total.

Let `cnt` be the length of the longest strictly increasing suffix ending at the current position. If that suffix has length $L$, then exactly $L$ increasing subarrays end there: take the last one element, last two elements, and so on through all $L$ suffix elements.

No longer subarray ending there is increasing, because extending beyond the maximal suffix crosses a non-increasing adjacent pair.

**Initialize the first element**

The input is nonempty. At index zero, the one-element subarray `[nums[0]]` is strictly increasing vacuously because it contains no adjacent pair that violates the condition.

Therefore, the code initializes:

```python
ans = cnt = 1
```

`cnt = 1` is the current increasing suffix length, and `ans = 1` counts the first singleton.

**Update from each adjacent pair**

`pairwise(nums)` yields consecutive values `(nums[i-1], nums[i])`. For pair `(x, y)`:

- If `x < y`, the previous increasing suffix extends through `y`, so `cnt += 1`.
- Otherwise, strict increase breaks. The only increasing suffix guaranteed to end at `y` is the singleton `[y]`, so `cnt = 1`.

After updating, `ans += cnt` adds all newly completed increasing subarrays ending at `y`.

Equality belongs in the breaking case. “Strictly increasing” requires `x < y`; equal adjacent values cannot appear together in a valid length-two-or-more subarray.

**Trace the first example**

For `[1, 3, 5, 4, 4, 6]`, suffix lengths by position are:

```text
value:          1  3  5  4  4  6
suffix length:  1  2  3  1  1  2
```

The first run extends from one to three to five. The drop from five to four resets the count. Equality between the two fours resets it again. The final six extends only from the second four.

Summing suffix lengths gives `1 + 2 + 3 + 1 + 1 + 2 = 10`, which counts every increasing subarray exactly once by its ending position.

**Why suffix length equals the number of new subarrays**

Suppose the maximal increasing suffix ending at index `i` begins at index `p`. For every start index `q` between `p` and `i`, `nums[q..i]` is a suffix of an increasing sequence and is therefore increasing. There are `i - p + 1 = cnt` such starts.

Any start before `p` crosses the adjacent boundary where increasing order failed, so that subarray is not strictly increasing. Thus, there are exactly `cnt` valid subarrays ending at `i`.

Since subarrays ending at different indices are distinct and every subarray has one end, summing these exact counts neither misses nor duplicates anything.

**Equivalent run-length viewpoint**

An entire maximal increasing run of length $L$ contains:

$$
1+2+\cdots+L=\frac{L(L+1)}{2}
$$

increasing subarrays. The online method accumulates those terms as the run grows rather than waiting until the run ends. Resetting `cnt` begins the next triangular sum.

This avoids storing run boundaries or constructing any subarray.

**Why positivity is not required by the algorithm**

The statement gives positive values, but the method uses only adjacent comparisons. It would work unchanged for zero or negative integers. Positivity matters to the contract but not to this particular invariant.

**Recovering the valid start interval**

The suffix length also identifies the exact range of valid starts. At ending index `i`, a value `cnt = L` means starts `i - L + 1` through `i` work, while every smaller start fails. This interval is contiguous because removing elements from the left of an increasing subarray preserves strict increase. There cannot be a valid earlier start separated from the suffix by an invalid start: both would cross the same failing adjacent comparison. The algorithm does not store the boundary explicitly because its length contains the same information, but this start-interval view makes the “add `cnt`” step concrete.

## Complexity detail

Let $n$ be the array length. `pairwise` produces exactly $n-1$ adjacent pairs lazily. Each iteration performs one comparison and constant-time updates, so total time is $O(n)$.

Only `ans`, `cnt`, and the current pair are stored. `pairwise` maintains constant iterator state, so auxiliary space is $O(1)$.

The answer can reach $n(n+1)/2$ when the entire array is increasing. Python integers handle that value; a fixed-width implementation should use 64-bit arithmetic for $n=10^5$.

## Alternatives and edge cases

- **Split into maximal runs:** Measure each increasing run and add $L(L+1)/2$. This is equivalent and also $O(n)$ time, but the suffix method is naturally online.
- **Enumerate every subarray:** Checking all starts and ends takes at least $O(n^2)$ time and is unnecessary.
- **Dynamic-programming array:** Store the increasing suffix length for every position. It gives the same recurrence but wastes $O(n)$ space because only the previous length is needed.
- **One element:** Initialization counts its singleton and the pairwise loop is empty.
- **Fully increasing array:** Suffix lengths are `1` through `n`, yielding all $n(n+1)/2$ subarrays.
- **Strictly decreasing array:** Every pair resets, so only the $n$ singleton subarrays count.
- **Equal adjacent values:** Equality resets because the condition is strict.
- **Increase after a reset:** A new run begins and can grow independently from the broken prefix.
- **Large answer:** Use a wide integer type outside Python.
