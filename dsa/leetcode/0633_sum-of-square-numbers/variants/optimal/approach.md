## General

**Restrict the search to nonnegative square roots.** The problem allows integers `a` and `b`, but signs do not affect squares: `(-a)^2 = a^2`. If any integer solution exists, a solution with both values nonnegative also exists. Each value is at most $\lfloor\sqrt c\rfloor$, because a larger square would already exceed `c`.

The exact solution searches this bounded square grid with two pointers:

- `a = 0` starts at the smallest possible first value;
- `b = int(sqrt(c))` starts at the largest possible second value.

It only considers states with `a <= b` because the equation is symmetric. A pair `(a,b)` and `(b,a)` contributes the same sum, so searching both orders would be redundant.

**Use monotonic movement instead of testing every pair.** At each step, compute

`s = a**2 + b**2`.

There are three cases.

1. If `s == c`, the current integers are a valid representation and the method returns `True`.
2. If `s < c`, the sum is too small. Decreasing `b` would make it even smaller, so no pair using the current `a` and any remaining smaller `b` can work. The only useful move is `a += 1`.
3. If `s > c`, the sum is too large. Increasing `a` would make it even larger, so no pair using the current `b` and any remaining larger `a` can work. The only useful move is `b -= 1`.

This is the same monotone reasoning used when searching a sorted matrix. For fixed `a`, the sum increases with `b`; for fixed `b`, it increases with `a`.

**Why pointer movement cannot skip a solution.** Suppose `s < c` at `(a,b)`. Every not-yet-checked pair `(a,b')` with `b' < b` has a smaller sum, so discarding the entire current-`a` row up to `b` is safe. Suppose instead `s > c`. Every pair `(a',b)` with `a' > a` has a larger sum, so discarding that current-`b` column is safe. Each step removes only combinations that are provably on the wrong side of `c`.

If the pointers cross, every unordered nonnegative pair in the allowed range has either been tested or ruled out by one of those monotone arguments. Returning `False` is then correct.

**Trace `c = 5`.** Start with `a = 0` and `b = floor(sqrt(5)) = 2`.

- `0^2 + 2^2 = 4`, which is too small, so increase `a`.
- `1^2 + 2^2 = 5`, so return `True`.

For `c = 3`, start at `(0,1)`. The sum 1 is too small, so `a` becomes 1. The sum at `(1,1)` is 2, still too small, so the pointers cross and the method returns `False`.

**Why the initial upper pointer is correct.** `sqrt(c)` may not be integral. Converting it with `int` truncates toward zero, which equals floor because `c` is nonnegative. Any integer `b` greater than that floor has `b^2 > c` and cannot participate in a nonnegative sum equal to `c`.

Within the stated 32-bit bound, standard floating square root has enough precision for these values in ordinary Python execution. For a more generally robust integer implementation, `math.isqrt(c)` computes the exact floor without floating-point concerns.

**The algorithm proves existence without constructing extra storage.** It returns as soon as one pair is found. The actual pair is not requested, so no path or candidate list is retained.

## Complexity detail

Let $m=\lfloor\sqrt c\rfloor$. Pointer `a` can increase at most $m+1$ times, and `b` can decrease at most $m+1$ times. Every loop iteration moves at least one pointer, so there are $O(m)=O(\sqrt c)$ iterations.

Each iteration uses a constant number of integer multiplications, additions, comparisons, and one pointer update under the fixed-width input model. Total time is $O(\sqrt c)$.

Only `a`, `b`, and `s` are stored, so auxiliary space is $O(1)$. These bounds match the manifest. Computing the initial square root is dominated by the scan in the challenge model.

## Alternatives and edge cases

- **Loop one value and test with `isqrt`:** For every `a`, compute `c - a*a` and check whether its exact integer square root squares back. This is also $O(\sqrt c)$ and straightforward.
- **Hash set of squares:** Store every square up to `c` and test complements. It uses $O(\sqrt c)$ extra space without improving the time bound.
- **Fermat's two-square theorem:** Factor `c` and ensure every prime congruent to 3 modulo 4 has an even exponent. It is elegant but relies on deeper number theory.
- **`c = 0`:** Both pointers start at 0, and `0^2 + 0^2 = 0` returns true.
- **Perfect square:** A representation with the other value 0 is found, such as `0^2 + 3^2 = 9`.
- **Equal values:** The condition `a <= b` includes pairs such as `1^2 + 1^2 = 2`.
- **Negative integers:** They need not be searched because changing signs leaves squares unchanged.
- **Pointer crossing:** It means every unordered candidate has been tested or eliminated; it is the correct failure condition.
- **Floating square root:** It is safe for the stated range, but `isqrt` is preferable for exactness on arbitrarily large integers.
- **Large upper bound:** The scan still uses constant memory even when it performs about $\sqrt c$ iterations.
