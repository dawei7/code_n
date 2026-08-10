## General

A split after index $i$ creates:

$$
\textit{left}=\texttt{nums}[0..i]
$$

and

$$
\textit{right}=\texttt{nums}[i+1..n-1].
$$

Both parts must be nonempty, so $i$ ranges only from zero through $n-2$.

The source precomputes three kinds of information:

- prefix sums, to evaluate the two part sums in constant time;
- whether every prefix `nums[0..i]` is strictly increasing;
- whether every suffix `nums[i..n-1]` is strictly decreasing.

It then tests every legal boundary once.

**Prefix sums**

The line:

`s = list(accumulate(nums))`

creates cumulative sums, so:

$$
s[i]=\sum_{j=0}^{i}\texttt{nums}[j].
$$

For a split after `i`, the left sum is directly `s[i]`. The total array sum is `s[n - 1]`, so the right sum is:

`s[n - 1] - s[i]`.

This avoids summing either subarray again for each boundary.

**Marking strictly increasing prefixes**

The boolean array `f` has this meaning:

`f[i]` is true exactly when `nums[0..i]` is strictly increasing.

A one-element prefix is vacuously strictly increasing, so `f[0]` begins true.

For every later position, the source first copies the previous prefix status:

`f[i] = f[i - 1]`

and then checks the new adjacent pair. If:

`nums[i] <= nums[i - 1]`

the required strict increase fails, so `f[i]` becomes false.

Both equality and a decrease invalidate the prefix. Once a prefix is invalid, extending it cannot remove the earlier bad pair, so copying `f[i-1]` correctly keeps every later prefix false.

Equivalently:

$$
f[i]=f[i-1]\land(\texttt{nums}[i-1]<\texttt{nums}[i]).
$$

**Marking strictly decreasing suffixes**

The array `g` is built in the opposite direction:

`g[i]` is true exactly when `nums[i..n-1]` is strictly decreasing.

The one-element suffix at $n-1$ is vacuously valid. Scanning backward, the suffix beginning at `i` remains valid only if the already-checked suffix beginning at `i+1` is valid and:

$$
\texttt{nums}[i]>\texttt{nums}[i+1].
$$

The source marks failure with:

`if nums[i] <= nums[i + 1]:`

`    g[i] = False`

Again, equality is not allowed because the order must be strict.

**Testing one split**

For boundary `i`:

- `f[i]` confirms that the complete left part is strictly increasing;
- `g[i + 1]` confirms that the complete right part is strictly decreasing.

Only when both booleans are true does the source compute:

`s1 = s[i]`

`s2 = s[n - 1] - s[i]`

and minimize:

`abs(s1 - s2)`.

Every valid split is evaluated, and no invalid split can influence `ans`.

For `nums = [1, 3, 2]`, both boundaries are valid. Their sum differences are four and two, so the minimum is two.

For `nums = [3, 1, 2]`:

- the split after zero has right part `[1,2]`, which is not decreasing;
- the split after one has left part `[3,1]`, which is not increasing.

No boundary passes both flags.

**Why local adjacent checks establish whole-part order**

A sequence is strictly increasing exactly when every adjacent pair increases. Therefore, if `f[i-1]` confirms all earlier adjacent pairs and `nums[i-1] < nums[i]` confirms the new pair, the entire prefix through `i` is increasing. The converse is immediate: one failed adjacent pair makes the complete prefix invalid.

The same argument applies backward to decreasing suffixes. This is why one boolean per endpoint is sufficient; no complete subarray comparison is needed during the boundary scan.

**Handling the absence of a valid split**

`ans` starts as infinity. Every valid split replaces it with a finite nonnegative difference, while invalid boundaries leave it unchanged.

The final expression returns `ans` if it is finite and $-1$ otherwise. Since all real absolute differences are finite and nonnegative, infinity cannot be confused with a legitimate result.

## Complexity detail

Let $n$ be `len(nums)`.

Creating the prefix-sum list takes $O(n)$ time. Building `f` and `g` requires one pass each, and checking all $n-1$ split positions requires one more pass. Total time is $O(n)$.

The exact source allocates three length-$n$ lists: `s`, `f`, and `g`. Its auxiliary space complexity is therefore $O(n)$.

This is a source/manifest mismatch. The manifest reports $O(1)$ space and describes maintaining a prefix sum while intersecting boundary ranges, but `solution.py` materializes all three arrays. A more compressed method is possible, yet it is not the exact implementation explained here.

The input array is not modified.

## Alternatives and edge cases

- **Try every split and rescan both parts:** Validating order and recomputing sums at each boundary can take $O(n^2)$ time.
- **Constant-space boundary analysis:** One can locate the farthest valid increasing prefix and earliest valid decreasing suffix, then scan sums with a running prefix total. This can achieve $O(1)$ auxiliary space and matches the manifest's intent.
- **Prefix and suffix sum arrays:** Two sum arrays work, but one prefix-sum array already derives the right sum from the total.
- **Two-element array:** Both parts contain one element and are vacuously ordered, so the sole split is valid.
- **Equal adjacent values:** Equality violates both strict increase and strict decrease where that pair belongs.
- **Singleton side:** A one-element left or right part is always valid; the initial true boundary flags model this.
- **Every split invalid:** Infinity remains untouched and the method returns $-1$.
- **Difference zero:** A perfectly balanced valid split returns zero, which is distinct from the no-split sentinel.
- **Positive values:** They make cumulative sums monotone, but the prefix-sum and order logic would also work with arbitrary integers.
- **Input size:** Storing three linear arrays is feasible for $n\le10^5$, though it does not meet the manifest's claimed constant-space bound.
