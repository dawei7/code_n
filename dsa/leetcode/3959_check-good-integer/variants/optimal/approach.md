## General

For one decimal digit $d$, its contribution to `squareSum - digitSum` is

$$
d^2-d = d(d-1).
$$

Therefore the two sums never need to be stored separately. Repeatedly take `n % 10` to obtain the last digit, add `digit * digit - digit` to one running score, and remove that digit with integer division by ten. After every digit has been processed, compare the score with the inclusive threshold `50`.

This directly evaluates the definition because addition distributes over subtraction:

$$
\sum_d d^2 - \sum_d d = \sum_d (d^2-d).
$$

The loop visits each decimal position exactly once, and the final comparison is true exactly for good integers.

## Complexity detail

An integer `n` has $\lfloor \log_{10} n \rfloor + 1$ decimal digits. Processing each digit once takes $O(\log n)$ time and the running score, digit, and shrinking value require $O(1)$ auxiliary space.

## Alternatives and edge cases

- **String conversion:** Iterating over `str(n)` is also $O(\log n)$ time but creates a decimal string using $O(\log n)$ additional space.
- **Separate sums:** Maintaining `digitSum` and `squareSum` is correct, but their difference can be accumulated directly with one variable.
- **Inclusive threshold:** A score equal to `50` is good; using a strict comparison would reject that boundary.
- **Zero digits:** A zero contributes `0^2 - 0 = 0` and must not change the score.
- **Maximum value:** `10^9` has ten decimal positions but only one nonzero digit, so its score is zero.
