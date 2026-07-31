## General

**Two operation counts give a universal upper bound.** Suppose a sequence uses $a$ increments and $b$ duplications. It finishes with $b+1$ elements, and no element can exceed $a+1$: every value descends from the initial `1`, and at most all $a$ increments can contribute to one lineage. Its final sum is therefore at most

$$
(a+1)(b+1).
$$

This bound is attainable. Perform all $a$ increments on the original element first, making its value $a+1$, and then duplicate that element $b$ times. Every element then has value $a+1$, so the product is the exact final sum. Consequently, the original process is equivalent to choosing positive integers $p=a+1$ and $q=b+1$ with $pq \geq k$ while minimizing $p+q-2$.

**The best factors are as balanced as the integers allow.** For a fixed sum, a product is largest when its factors are closest. Let $r=\lfloor\sqrt{k}\rfloor$. Choosing

$$
p=r
\qquad\text{and}\qquad
q=\left\lceil\frac{k}{r}\right\rceil
$$

meets the product threshold. Moving the smaller factor below $r$ forces the other factor high enough that the sum cannot improve; moving both factors above $r$ also cannot lower their sum. Thus this pair attains the minimum.

Integer square root obtains $r$ exactly, and ceiling division computes `q = (k + r - 1) // r`. The required operation count is then `r + q - 2`.

## Complexity detail

Under the standard fixed-width integer model for the stated constraint, integer square root, ceiling division, and the remaining arithmetic each take constant time. The algorithm therefore uses $O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every increment count:** Trying all values from `1` through `k` and calculating the required duplicates is correct but takes $O(k)$ time.
- **Enumerate only through the square root:** This reduces the search to $O(\sqrt{k})$ time but still repeats comparisons that the balanced-factor argument resolves directly.
- **Use floating-point square root:** It is unnecessary and can introduce rounding uncertainty; integer square root preserves the exact boundary.
- **Duplicate before finishing increments:** Such a sequence may still work, but moving useful increments before duplications never worsens the result and exposes the maximal product construction.
- When $k=1$, both factors are $1$, giving zero operations.
- Perfect squares use equal factors.
- For a non-square, ceiling division is essential because a product below $k$ is not sufficient.
