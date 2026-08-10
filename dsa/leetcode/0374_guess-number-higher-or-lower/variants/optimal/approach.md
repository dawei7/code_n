## General

The judge response changes monotonically as guesses move from `1` toward `n`. Guesses below the hidden number receive `1`, the hidden number receives `0`, and guesses above it receive `-1`. The exact source turns those responses into a sorted key sequence and lets Python's right-bisection routine find the boundary.

This is binary search, but it is expressed in one call rather than an explicit `low`, `high`, and `mid` loop.

**The platform API is part of the environment.**

`guess(x)` is already supplied. The solution should call it but should not implement it or try to access the hidden `pick` directly. The native method receives only `n`; the app adapter's extra `pick` input exists solely to emulate the platform API.

For any candidate `x`, the responses are:

$$
\operatorname{guess}(x)=
\begin{cases}
1,&x<\texttt{pick},\\
0,&x=\texttt{pick},\\
-1,&x>\texttt{pick}.
\end{cases}
$$

**Why the response is negated.**

The source uses `key=lambda x: -guess(x)`. Negating the three responses produces

$$
-\operatorname{guess}(x)=
\begin{cases}
-1,&x<\texttt{pick},\\
0,&x=\texttt{pick},\\
1,&x>\texttt{pick}.
\end{cases}
$$

As candidate numbers increase, this transformed key sequence is non-decreasing: a block of `-1` values, one `0`, and then a block of `1` values. That sorted-key property is exactly what bisection requires.

Without negation, the raw responses would go from `1` to `0` to `-1`, which is decreasing and would not match the ascending order assumed by `bisect`.

**What sequence is searched.**

`range(1, n + 1)` represents every legal guess from one through `n`. It is lazy and indexable, so Python can binary-search it without allocating an array of up to more than two billion integers.

At zero-based range index `p`, the candidate value is `p + 1`. The key function calls the judge only for midpoint candidates inspected by the bisection algorithm.

**`bisect.bisect` means right bisection.**

In Python's `bisect` module, `bisect` is an alias for `bisect_right`. With target key zero, it returns the insertion position after all transformed values less than or equal to zero.

The values less than or equal to zero correspond exactly to candidates satisfying

$$
x\le\texttt{pick}.
$$

There are exactly `pick` such candidates in the range `1, 2, ..., n`. Therefore the returned zero-based insertion position is numerically equal to the hidden value itself.

This explains the initially surprising absence of `+ 1`. A left-bisection position for the zero key would be `pick - 1`, the range index of the hidden number. Right bisection steps past that zero and returns `pick`, which is already the candidate value that must be returned.

**A trace for `n = 10`, `pick = 6`.**

The conceptual transformed key sequence is

```text
candidate: 1  2  3  4  5  6  7  8  9  10
key:      -1 -1 -1 -1 -1  0  1  1  1   1
```

Right bisection of target zero returns the boundary between the zero and the first one. That insertion position is six. The method returns `6`.

Binary search does not construct or inspect this full table; it learns enough through a logarithmic number of midpoint `guess` calls.

**Boundary case when the pick is one.**

The first candidate has key zero, and every later candidate has key one. Right bisection returns position one, which equals the hidden number. This works even though the zero occurs at range index zero.

**Boundary case when the pick is `n`.**

Every candidate below `n` has key `-1`, and candidate `n` has key zero. No key one exists. Right bisection returns the length of the range, which is `n`, again exactly the hidden value.

**Why binary search is valid.**

The hidden pick is fixed for the entire game, so repeated calls describe one consistent monotone boundary. Every candidate below it belongs to the `-1` key region, the pick is the final key no greater than zero, and every larger candidate belongs to the positive region. `bisect_right` is defined to locate exactly the first position after that nonpositive region.

Since the position equals the count of legal candidates no greater than the pick, and those candidates begin at one, it equals the pick. The one-line result is therefore not merely an insertion index; it is the requested hidden number.

## Complexity detail

The virtual range has length $n$. Bisection halves its remaining interval after each key comparison, so it makes $O(\log n)$ calls to `guess`. Range indexing, response negation, and comparisons use constant time. Total time is $O(\log n)$.

`range` stores only constant-size metadata, and the iterative library search uses a constant number of indices. Auxiliary space is $O(1)$, matching the manifest.

No multiplication or midpoint expression appears in the source, so fixed-width midpoint overflow is not a concern here. The library manages its indices, while the candidate range endpoint remains representable in Python.

## Alternatives and edge cases

- **Explicit binary search:** Keep inclusive `low` and `high`, call `guess(mid)`, and move left or right according to the response. It has the same bounds and is usually easier to port across languages.

- **Use `bisect_left`:** Searching for key zero with left bisection returns range index `pick - 1`; the implementation would then need to add one. The exact source instead uses right bisection and returns its position directly.

- **Linear guessing:** Try candidates from one upward until `guess` returns zero. It is simple but can require $O(n)$ API calls.

- **Ternary search:** Splitting into three regions uses two judge calls per iteration. Despite fewer levels, it generally performs more comparisons than binary search.

- **`n = 1`:** The only key is zero, right bisection returns one, and the method returns the sole legal pick.

- **Several API calls at the same candidate:** The pick never changes, so responses are consistent. The bisection implementation generally need not repeat candidates.

- **Response signs:** The API's `-1` means the guess is too high and `1` means too low. Reversing that interpretation would destroy the key monotonicity.

- **Lazy range:** Replacing `range` with `list(range(...))` would be impossible at the upper bound due to memory. Keeping the range virtual is essential.

- **No direct access to `pick`:** Correct native code must infer it only through `guess`; the adapter-specific hidden parameter is not part of the solution method.
