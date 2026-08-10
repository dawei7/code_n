## General

A base `k` is good when writing the given number in that base produces only digit `1`. If the representation contains `m + 1` ones, its value in ordinary decimal arithmetic is

$$
N = 1 + k + k^2 + \cdots + k^m.
$$

The input arrives as a string because `N` can be as large as $10^{18}$, but Python can represent it exactly after `num = int(n)`. The problem is therefore transformed from manipulating base digits into finding integers `k >= 2` and `m >= 1` that satisfy a geometric-sum equation.

**Why the solution tries the number of powers first.** For a fixed exponent `m`, define

$$
F_m(k) = 1 + k + k^2 + \cdots + k^m.
$$

For integer bases `k >= 2`, every positive-power term increases when `k` increases, so `F_m(k)` is strictly increasing. That monotonicity means there can be at most one base for a chosen `m`, and binary search can find it without trying every base.

The outer loop tries `m` from `63` down to `2`. Here `m` counts the highest power, so the representation has `m + 1` digits. The fixed upper value `63` is safely above what the input limit can require: even the smallest base `2` grows exponentially, while `N <= 10^{18}`. Trying a few impossible lengths is harmless because their geometric sums simply exceed `N`.

Descending `m` is what produces the smallest base. For the same target `N`, a representation with more ones must use a smaller base than a representation with fewer ones. Intuitively, adding higher positive powers makes the sum grow, so the base must be reduced to keep the total fixed. More formally, if `m_1 > m_2` and the two sums used bases `k_1 >= k_2`, then the first sum would contain every term of the second at values at least as large plus additional positive terms, making it greater than `N`. Therefore `k_1 < k_2`. The first equality found while lengths descend consequently has the smallest possible base.

**Evaluate one candidate exactly.** The helper `cal(k, m)` computes the geometric sum without floating-point arithmetic. It starts with `p = s = 1`, representing `k^0` and the initial sum. Each of `m` iterations multiplies `p` by `k` to obtain the next power and adds it to `s`. After iteration `i`, the newly added value is `k^(i + 1)`. When the loop finishes, `s` is exactly `F_m(k)`.

Exact integer evaluation matters. A formula involving logarithms or floating-point roots could estimate the base, but numbers near $10^{18}$ can be rounded, and a one-unit error changes whether the representation consists entirely of ones. This implementation uses comparisons and equality on exact Python integers, so no tolerance or corrective guess is needed.

**Binary-search the unique possible base.** For one `m`, the search interval is `[2, num - 1]`. Base `1` is forbidden. A good base never needs to equal or exceed `num`, because even the shortest legal all-ones representation is `11`, whose value is `k + 1`.

At every search step, `mid = (l + r) >> 1` is the floor of the midpoint. If `cal(mid, m) >= num`, then `mid` and all larger bases produce sums at least as large, so the smallest possible matching base remains in `[l, mid]` and the code sets `r = mid`. Otherwise, `mid` is too small and every base at or below it is also too small, so `l = mid + 1` is safe. The loop terminates at the first base whose sum is at least `num`. A separate exact test, `cal(l, m) == num`, distinguishes an actual solution from the first value that merely overshoots.

If equality holds, the returned string `str(l)` is a valid good base, and the descending-length argument proves it is globally smallest. If not, the outer loop proceeds to a representation with one fewer digit.

**Why `num - 1` is the guaranteed fallback.** The outer loop stops before `m = 1`. That missing case represents exactly two ones:

$$
N = 1 + k.
$$

It always has the solution `k = N - 1`, which is at least `2` because `N >= 3`. Thus every input has at least one good base. Returning `str(num - 1)` after all longer representations fail is not an approximation; it is the exact two-digit representation `11` in base `N - 1`.

For `N = 13`, trying a three-digit representation means `1 + k + k^2 = 13`, which holds at `k = 3`, so the result is `3` instead of the fallback `12`. For a target with no longer all-ones form, the search eventually reaches the guaranteed two-one construction.

## Complexity detail

Let $L = \log N$, ignoring the constant choice of logarithm base. There are $O(L)$ meaningful values of `m`. For each one, binary search performs $O(L)$ iterations over a numeric interval bounded by `N`. One call to `cal` performs `m` multiplications and additions, which is $O(L)$ under the usual unit-cost integer-arithmetic model. Multiplying these factors gives the manifest's $O(\log^3 N)$ time bound.

The final equality check adds one more geometric-sum evaluation per `m` and does not change the bound. The implementation keeps only the search bounds, midpoint, current power, and running sum, so auxiliary space is $O(1)$. Python integers grow with `N`; under a bit-complexity model, arithmetic costs depend on the number of bits, but the stated complexity follows the repository's ordinary arithmetic-operation convention.

## Alternatives and edge cases

- **Try every base:** Checking bases from `2` upward would eventually find the smallest answer, but `N` can be near $10^{18}$, making a linear numeric scan infeasible. Monotonic search by representation length avoids that range.
- **Use a floating-point `m`th root:** Estimating `k` from `N^(1/m)` can narrow the search, but rounding near large exact integers is dangerous. Every candidate still needs exact geometric-sum verification.
- **Use the closed geometric-series fraction:** `(k^(m+1) - 1) / (k - 1)` is mathematically equivalent. The iterative helper avoids division and keeps every intermediate operation visibly integral.
- **Smallest allowed input:** For `N = 3`, no representation with at least three ones exists, and the fallback gives base `2` because `3` is `11` in base `2`.
- **Very long candidate representation:** Impossible lengths cause `cal` to exceed `N`, and monotonic binary search rejects them safely. Starting at `63` is a conservative constant for the input range.
- **No solution for a tested `m`:** Binary search finds the first non-smaller sum, but only exact equality is accepted. Overshooting does not create a false good base.
- **String return type:** The input and required base are represented as strings, so the numeric base is converted back with `str` only when returned.
- **Guaranteed two-digit form:** The `m = 1` case must not be forgotten. `N = 1 + (N - 1)` proves `N - 1` is always a legal final answer.
