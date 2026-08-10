## General

**Turn every subarray sum into a difference of two prefix sums**

The requested object is a contiguous, nonempty subarray. That contiguity makes
prefix sums useful. Define `s[k]` as the sum of the first $k$ elements of
`nums`, with `s[0] = 0`. For example, if `nums = [2, 3, 1]`, then
`s = [0, 2, 5, 6]`. The extra initial zero is important: it lets a subarray
starting at index 0 use exactly the same formula as every other subarray.

Using half-open boundaries, the sum of `nums[i:j]` is

$$
\texttt{s[j]} - \texttt{s[i]}.
$$

Therefore `nums[i:j]` reaches the target precisely when

$$
\texttt{s[j]} \ge \texttt{s[i]} + \texttt{target}.
$$

For a fixed starting boundary `i`, the shortest qualifying subarray is the one
with the smallest ending boundary `j` satisfying that inequality. The exact
solution builds `s` with `accumulate(nums, initial=0)`, then finds that smallest
`j` using `bisect_left`.

**Why binary search is legal here**

Every value in `nums` is positive, not merely nonnegative. Consequently, each
new prefix sum is strictly larger than the previous one:

$$
\texttt{s[k+1]} = \texttt{s[k]} + \texttt{nums[k]} > \texttt{s[k]}.
$$

That strict increase is the key structural fact. It puts `s` in sorted order,
so `bisect_left(s, x + target)` returns the first index whose prefix sum is at
least `x + target`. In the loop, `x` is `s[i]`, making the searched value
exactly the threshold derived above.

The call searches the whole prefix array rather than explicitly restricting
the search to positions after `i`. This remains safe. Because `target` is
positive, `x + target` is strictly greater than `x = s[i]`. Every position at
or before `i` contains a value no greater than `s[i]`, so none can satisfy the
search. Any returned position necessarily has `j > i`, which also guarantees a
nonempty subarray.

**How the loop evaluates every possible start**

The prefix array contains $n+1$ boundaries for an input of length $n$.
`enumerate(s)` visits each boundary as a possible starting position `i` and
also supplies its prefix value `x`. For that start, binary search has two
possible outcomes:

- If a qualifying prefix exists, `j` is its earliest index. Then `j - i` is
  the number of array elements in `nums[i:j]`, and the solution compares this
  candidate with the best length seen so far.
- If no prefix reaches the threshold, `bisect_left` returns `len(s)`, which is
  $n+1$. The condition `j <= n` rejects this insertion position because it is
  not an actual prefix boundary in the array.

The best length starts as `n + 1`. No real nonempty subarray can be longer than
$n$, so this is an unambiguous sentinel meaning “no qualifying subarray has
been found.” Whenever a real `j` exists, `ans = min(ans, j - i)` preserves the
smallest length among all starts examined so far. At the end, `ans <= n` means
at least one valid candidate was recorded; otherwise the method returns the
required `0`.

**Detailed trace for the first example**

For `target = 7` and `nums = [2, 3, 1, 2, 4, 3]`, the prefix array is
`[0, 2, 5, 6, 8, 12, 15]`.

- At `i = 0`, the threshold is `0 + 7 = 7`. The first prefix at least 7 is
  `s[4] = 8`, giving the subarray `nums[0:4] = [2, 3, 1, 2]` of length 4.
- At `i = 1`, the threshold is 9. The first adequate prefix is `s[5] = 12`,
  so `[3, 1, 2, 4]` also has length 4.
- At `i = 2`, the threshold is 12. Binary search returns `j = 5` exactly,
  giving `[1, 2, 4]` of length 3.
- At `i = 3`, the threshold is 13. The first adequate prefix is `s[6] = 15`,
  giving `[2, 4, 3]` of length 3.
- At `i = 4`, the threshold is 15. Binary search returns `j = 6`, giving
  `[4, 3]` of length 2. This becomes the final minimum.
- Later starts have too little remaining sum, so their searches return the
  out-of-range insertion position 7.

Notice that binary search chooses the earliest successful end for each fixed
start. Choosing any later end could only increase `j - i`, so it could not
produce a better candidate for that same `i`.

**Why taking the minimum gives the global answer**

Every contiguous subarray has one unique pair of prefix boundaries `(i, j)`.
For each possible `i`, the algorithm finds the least `j` that reaches the
target, if one exists. That candidate is the shortest valid subarray starting
at `i`; all later ends for that start are dominated because they are longer.
The loop considers every start, so the globally shortest qualifying subarray
must appear among the candidates compared into `ans`. If no start produces a
candidate, no valid boundary pair exists, and returning `0` is correct.

This reasoning relies directly on positivity. With negative numbers, prefix
sums would not be sorted, a later end might reduce the sum, and `bisect_left`
would no longer answer the required question.

**The branch label and the exact source must not hide a complexity mismatch**

The exact file in this branch implements the prefix-sum plus binary-search
method described above. Its actual bounds are $O(n \log n)$ time and $O(n)$
space, even though the current variant manifest declares $O(n)$ time and
$O(1)$ space. The editorial's sliding-window method achieves those stronger
bounds, but it is not the code stored in this optimal solution file. An
approach document must describe the executable source faithfully, so the
complexity below reports the source's real costs rather than repeating the
inconsistent metadata.

The source also assumes `accumulate` from `itertools`, `bisect_left` from
`bisect`, and `List` for the annotation are already available in the execution
environment; they are referenced but not imported in this file.

## Complexity detail

Let $n$ be `len(nums)`. Constructing the $n+1$ prefix sums takes $O(n)$ time.
The loop runs $n+1$ times, and each `bisect_left` over an array of length $n+1$
takes $O(\log n)$ time. The total time is therefore $O(n \log n)$. The final
iteration beginning at prefix boundary $n$ cannot find a positive target in
the empty suffix, but it changes only a constant amount of work outside its
binary search and does not affect the bound.

The list `s` stores $n+1$ integers, so auxiliary space is $O(n)$. The remaining
variables—`n`, `ans`, `i`, `x`, and `j`—use $O(1)$ space. Python's binary search
is iterative and does not create an additional array.

## Alternatives and edge cases

- **Sliding window:** Because all values are positive, extend a right boundary to increase the sum and repeatedly advance the left boundary while the sum is at least `target`. Each boundary advances at most $n$ times, producing the true asymptotically optimal $O(n)$-time, $O(1)$-space solution described by the editorial; it differs from the exact source in this branch.
- **Brute-force starts and ends:** Enumerating every subarray and maintaining a running sum avoids extra prefix storage but takes $O(n^2)$ time in the worst case, which is too slow for $n$ up to $10^5$.
- **Prefix sums with a linear scan for every start:** Prefix sums make each sum lookup constant time, but checking every later end still considers quadratically many boundary pairs. Binary search is what reduces each start's search to logarithmic time.
- **A one-element answer:** If any `nums[i]` is at least `target`, searching from prefix boundary `i` can return `j = i + 1`, and `ans` becomes 1. No nonempty subarray can be shorter, although the exact loop harmlessly continues.
- **No qualifying subarray:** If even the sum of the whole array is below `target`, every search returns insertion position $n+1$; `ans` stays at its sentinel and the method returns `0`.
- **Exact equality:** `bisect_left` searches for the first value greater than or equal to the threshold, so a subarray whose sum equals `target` is accepted, as required. Using a strict-greater search would be wrong.
- **Repeated prefix values:** They cannot occur under the positive-integer contract. If zeros were allowed, the array would still be non-decreasing and `bisect_left` could still locate an earliest adequate boundary, but the proof that a whole-array search cannot return at or before `i` would need the positive target together with non-decrease rather than strict increase.
- **Negative values:** They would destroy sorted prefix sums and invalidate this binary search. A general integer-array version requires a different technique, commonly a monotonic deque over prefix sums.
- **Large sums:** The maximum possible total exceeds ordinary 32-bit signed range under some related constraints, so fixed-width implementations should use a wide integer type. Python integers grow automatically and do not overflow here.
- **Input preservation:** `accumulate` creates a new prefix list and never changes `nums`, so the caller's array remains intact.
