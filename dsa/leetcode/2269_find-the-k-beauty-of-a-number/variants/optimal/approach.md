## General

**Treat the decimal representation as the window source**

Convert `num` to its decimal string so that every contiguous length-$k$
substring is directly available, including ones beginning with zero. There
are $d-k+1$ possible starting positions when the number has $d$ digits.

For each start, parse the corresponding slice as an integer. If that value is
nonzero and `num % divisor == 0`, increment the answer. The explicit nonzero
check must precede the remainder operation because division by zero is
undefined and zero is excluded by the contract.

**Why the scan gives the exact k-beauty**

Every length-$k$ substring is uniquely identified by its starting position,
and the loop visits precisely the starts from zero through $d-k$. Parsing
preserves the substring's numeric value while naturally ignoring leading
zeroes. The two tests are exactly the definition of a qualifying window:
nonzero and a divisor of the original number. Therefore each qualifying
occurrence contributes once and no other window contributes.

## Complexity detail

Let $d$ be the number of decimal digits in `num`. The scan visits $d-k+1$
windows, and slicing and parsing each window takes $O(k)$ time, for
$O(dk)$ total time. A temporary window contains $k$ characters, giving $O(k)$
auxiliary space.

The legal bound `num <= 10^9` gives $d\le10$, so at most 100 digit-character
inspections are possible. The package records this fixed legal workload with a
bounded-domain certificate instead of claiming a measured scaling verdict.

## Alternatives and edge cases

- **Arithmetic rolling window:** Powers of ten can extract or update each window numerically without string slicing, but the string form expresses leading-zero semantics more directly.
- **Precompute all divisors:** Enumerating divisors of `num` does extra work; only at most ten substring values need testing.
- **Zero window:** Skip it before taking a remainder because zero is not a divisor.
- **Leading zeroes:** `"04"` is interpreted as $4$ and may qualify.
- **Repeated substring value:** Count every qualifying position separately.
- **Whole-number window:** When $k=d$, the only window equals `num` and contributes one.
- **One-digit windows:** Test each decimal digit independently, excluding digit zero.
- **Maximum value:** `1000000000` has ten digits and remains within the fixed bound.
