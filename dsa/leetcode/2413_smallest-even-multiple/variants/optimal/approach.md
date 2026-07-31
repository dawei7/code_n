## General

Every positive common multiple must be a multiple of `n`. If `n` is even, its smallest positive multiple, `n`, is already divisible by 2 and is immediately optimal.

If `n` is odd, `n` itself is not divisible by 2. Multiplying it by 2 produces an even number, and there is no positive multiple of `n` strictly between `n` and `2 * n`. Therefore `2 * n` is the smallest common multiple in the odd case.

## Complexity detail

One parity test and at most one multiplication take $O(1)$ time. The computation stores no input-sized data, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Least-common-multiple formula:** Computing $\operatorname{lcm}(n,2)=2n/\gcd(n,2)$ is correct, but the parity split is the same reasoning in simpler form.
- **Enumerate multiples:** Testing `n`, `2 * n`, and later multiples eventually works but performs unnecessary search.
- **Smallest input:** For `n = 1`, the first even multiple is 2.
- **Even input:** A number counts as its own multiple, so an even `n` is returned unchanged.
- **Largest input:** `n = 150` is even and remains within the legal result range.
