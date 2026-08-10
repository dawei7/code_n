## General

For positive integers, the square function is strictly increasing:

$$
1^2<2^2<3^2<\cdots.
$$

That monotonic order allows binary search. The exact source uses Python's `bisect_left` with a `key` function rather than writing the search loop explicitly. It searches the integer candidates from `1` through `num` for the first candidate whose square is at least `num`, then checks whether that square is exactly equal.

**What sequence is searched.**

`range(1, num + 1)` represents the integers

$$
1,2,\ldots,\texttt{num}.
$$

The range object is lazy; it does not allocate a list containing all those integers. Its length and indexed elements can be obtained in constant time, which makes it suitable for binary search even when `num` is large.

The search interval is wider than mathematically necessary because a square root greater than one is much smaller than `num`. That does not change logarithmic complexity: repeatedly halving an interval of size `num` still takes $O(\log\texttt{num})$ comparisons.

**How `bisect_left` uses the key.**

The call supplies `key=lambda x: x * x`. During binary search, a candidate integer `x` is compared through its square. Conceptually, the searched ordered values are

$$
1^2,2^2,3^2,\ldots,\texttt{num}^2,
$$

but they are computed only at the midpoint indices inspected by binary search.

`bisect_left(..., num, key=...)` returns the first zero-based range index `p` whose transformed value is not less than `num`. Since the range element at index `p` is `p + 1`, the source adds one and stores

```text
l = p + 1.
```

Thus `l` is the smallest positive integer satisfying

$$
l^2\ge\texttt{num}.
$$

In mathematical language, `l` is the ceiling of the square root, but the implementation obtains it using only integer multiplication and binary search, never a square-root library function.

**Why the final equality decides the answer.**

If `num` is a perfect square, there is an integer $r$ with $r^2=\texttt{num}$. Every smaller positive integer has square below `num`, so the first candidate with square at least `num` is exactly `r`. The final test `l * l == num` returns true.

If `num` is not a perfect square, there are consecutive integers $r$ and $r+1$ such that

$$
r^2<\texttt{num}<(r+1)^2.
$$

The first candidate whose square reaches or exceeds `num` is `r + 1`, and its square is strictly greater. The equality test returns false.

The lower-bound search alone cannot distinguish equality from the first larger square; the final multiplication is therefore essential.

**A trace for `num = 16`.**

The searched candidates begin at one. Binary search discards halves according to whether the midpoint square is below 16. The first candidate whose square is at least 16 is `4`. `bisect_left` returns range index three, the added one converts it to candidate four, and `4 * 4 == 16` is true.

**A trace for `num = 14`.**

Candidate `3` has square nine, which is too small, while candidate `4` has square sixteen, which is the first square above the target. The lower bound is therefore `4`, but `4 * 4 == 14` is false. No integer can lie between `3` and `4`, so the number is not a perfect square.

**Why the search range always contains a lower bound.**

The input is positive. Candidate `num` belongs to the range, and

$$
\texttt{num}^2\ge\texttt{num}
$$

for every positive integer `num`. Therefore at least one candidate has a square not less than the target, and `bisect_left` never needs to return a position beyond the range's last element. After adding one, `l` is always a valid positive candidate.

**The smallest input.**

For `num = 1`, the range contains just candidate one. Its square equals the target, so `bisect_left` returns index zero, `l` becomes one, and the method returns true. No separate small-number branch is necessary.

**No floating-point approximation.**

Every operation is integer indexing, multiplication, or comparison. The result cannot suffer from a rounded square root near a large perfect square. Python integers also avoid multiplication overflow; a fixed-width language would need a wide enough type or a division-based comparison.

The source does use a standard-library binary-search helper, but the restriction specifically forbids square-root functions. `bisect_left` does not compute a square root; it performs the same monotone search an explicit loop would perform.

## Complexity detail

Let $N$ denote `num`. The virtual range contains $N$ candidates. Binary search inspects $O(\log N)$ midpoint candidates, and each key evaluation performs one constant-time integer multiplication under the usual bounded-word model. Total time is $O(\log N)$.

`range` stores only its start, stop, and step rather than $N$ elements. `bisect_left`, the lambda invocation, and local variables use $O(1)$ auxiliary space. This matches the manifest.

For strict bit-complexity analysis, multiplying arbitrary-precision integers is not truly constant time. Under the stated 32-bit input bound and standard interview model, the conventional $O(\log N)$ time and $O(1)$ space analysis is appropriate.

## Alternatives and edge cases

- **Explicit binary-search loop:** Maintain integer `left` and `right`, compare `mid * mid` with `num`, and move one boundary. It has the same asymptotic bounds and makes the mechanics visible without relying on `bisect_left`'s `key` parameter.

- **Newton's method:** Repeatedly replace a guess with `(guess + num // guess) // 2` until it no longer overshoots. It converges quickly but needs a careful integer stopping condition.

- **Subtract consecutive odd numbers:** The identity $1+3+5+\cdots+(2r-1)=r^2$ gives a simple test, but repeated subtraction takes $O(\sqrt N)$ time.

- **Built-in square root:** Converting `sqrt(num)` back to an integer would be concise but violates the explicit requirement and may introduce floating-point precision concerns.

- **`num = 1`:** The first candidate is an exact match and returns true.

- **`num = 2`:** Candidate one is too small and candidate two squares to four, so the final equality returns false.

- **Large 32-bit values:** Binary search remains logarithmic. Python multiplication is exact and cannot overflow.

- **Perfect square near the limit:** Lower-bound search finds its exact integer root; no approximate rounding is involved.

- **Non-square between adjacent squares:** The search returns the larger adjacent integer, and the equality check rejects it.

- **Positive-domain assumption:** The Reference excludes zero and negative inputs. If zero were allowed, this range beginning at one would need a special case because zero is itself a perfect square.
