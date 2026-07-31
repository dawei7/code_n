## General

**Locate the only formatting threshold**

An integer first needs a comma when it reaches four digits, so every value below `1000` contributes `0`. The constraint $n\le 10^5$ also matters: the largest possible representation is `"100,000"`, which still has exactly one comma. Therefore every value in the legal domain contributes either zero commas or one comma, and the contributing values are precisely the interval from `1000` through `n`.

**Count the interval instead of visiting it**

When $n\ge 1000$, the inclusive interval `[1000, n]` contains

$$
n-1000+1=n-999
$$

integers. Each contributes one comma, so this interval length is the answer. When $n<1000$, the interval is empty and the answer is `0`. Combining both cases gives `max(0, n - 999)`.

## Complexity detail

The calculation performs a fixed number of arithmetic and comparison operations, independent of `n`, so it takes $O(1)$ time and $O(1)$ auxiliary space.

The benchmark defines size as `n`, the inclusive upper endpoint, and uses legal tiers `6250`, `25000`, and `100000`. The accepted threshold formula and an independently expressed constant-time conditional should show flat relative growth. A correct enumeration that visits every value from `1` through `n` performs $O(n)$ work and should fail only the scaling verdict.

## Alternatives and edge cases

- **Piecewise conditional:** Return `0` below `1000` and `n - 999` otherwise; this is the same constant-time reasoning written without `max`.
- **General digit-block formula:** For an unrestricted upper bound, sum the sizes of ranges that contribute one, two, or more commas. That $O(\log n)$ method is unnecessary here because $10^5$ never reaches the two-comma threshold `1000000`.
- **Enumerate every integer:** Counting one contribution for each value at least `1000` is correct but takes $O(n)$ time instead of using the interval's size directly.
- **Endpoint below the threshold:** Every legal `n <= 999` must return `0`; subtracting `999` without clamping would produce a negative result.
- **First comma-bearing value:** At `n = 1000`, the interval contains exactly one value and the result is `1`.
- **Digit-length transitions:** Crossing from `9999` to `10000`, or from `99999` to `100000`, does not change the one-comma contribution of each new value.
