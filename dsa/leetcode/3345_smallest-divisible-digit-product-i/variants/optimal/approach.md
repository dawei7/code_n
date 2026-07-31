## General

Start at `n` and test candidates in increasing order. For each candidate, repeatedly take `value % 10` to obtain its final decimal digit, multiply that digit into the running product, and remove the digit with `value //= 10`. The candidate is valid exactly when the resulting product has remainder zero modulo `t`.

Returning the first valid candidate establishes minimality because every smaller permitted integer has already been tested and rejected. The loop also has a strict bound. Among any ten consecutive integers, one is a multiple of ten. Its last digit is zero, so its digit product is zero, and $0$ is divisible by every positive `t`. Consequently, a valid candidate always appears between `n` and `n + 9`.

## Complexity detail

Under the source constraints, at most ten candidates are checked and every one is at most `109`, so each has at most three digits. The total work is therefore $O(1)$ time and $O(1)$ auxiliary space.

The bounded-domain certificate replaces runtime scaling because the complete legal workload contains at most thirty digit extractions. If the upper bound on `n` were removed, the same method would take $O(\log n)$ time: the number of candidates remains at most ten, while extracting a candidate's decimal digits takes $O(\log n)$ operations.

## Alternatives and edge cases

- **Convert each candidate to a string:** Multiplying parsed characters is equally direct, but arithmetic extraction avoids allocating a temporary string.
- **Search without a ten-candidate bound:** An unbounded loop is still guaranteed to terminate, but expressing the proven bound makes the contract and worst-case work explicit.
- **Factor `t` first:** Tracking prime factors is useful in harder digit-product variants, but it adds machinery without reducing this bounded search.
- **Zero digit:** Any candidate containing zero has digit product zero and is valid for every permitted positive `t`.
- **Unit divisor:** When `t = 1`, `n` itself is always the answer.
- **Minimality:** A later valid number must not replace an earlier valid number; candidates must be examined in ascending order.
