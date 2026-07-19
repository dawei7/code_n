## General
**Count the union without enumerating it.** For a candidate bound $x$, ordinary division counts multiples of one divisor. Multiples shared by two divisors are counted twice and must be subtracted using least common multiples; numbers shared by all three are then added back. Define $L_{ab}=\operatorname{lcm}(a,b)$, $L_{ac}=\operatorname{lcm}(a,c)$, $L_{bc}=\operatorname{lcm}(b,c)$, and $L_{abc}=\operatorname{lcm}(a,b,c)$. Then

$$
C(x)=\left\lfloor\frac{x}{a}\right\rfloor+\left\lfloor\frac{x}{b}\right\rfloor+\left\lfloor\frac{x}{c}\right\rfloor-\left\lfloor\frac{x}{L_{ab}}\right\rfloor-\left\lfloor\frac{x}{L_{ac}}\right\rfloor-\left\lfloor\frac{x}{L_{bc}}\right\rfloor+\left\lfloor\frac{x}{L_{abc}}\right\rfloor.
$$

This is exactly the number of ugly numbers at most $x$.

**Binary-search the first sufficient bound.** The function $C(x)$ is monotone. Search the inclusive answer domain from 1 through $U$ for the smallest `x` satisfying $C(x)\ge n`. That first sufficient value must itself be ugly: otherwise its count would equal the preceding count, contradicting minimality. It is therefore exactly the $n$th ugly number.

**Compute least common multiples safely.** Use `left // gcd(left, right) * right`, dividing before multiplying. This reduces overflow risk in fixed-width languages while preserving the exact least common multiple needed by inclusion-exclusion.

## Complexity detail
The four least common multiples take a constant number of greatest-common-divisor operations on bounded machine integers. Binary search performs $O(\log U)$ iterations, and each evaluates seven constant-time integer divisions, giving $O(\log U)$ time. Only fixed scalar bounds and least common multiples are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Three-pointer sequence merge:** Advancing the next multiple of each divisor is correct and avoids duplicates, but takes $O(n)$ time and cannot handle $n$ up to $10^9$.
- **Test every integer:** Checking divisibility one value at a time may examine nearly the entire answer range.
- **Redundant divisors:** If one divisor is a multiple of another, inclusion-exclusion cancels the duplicate contribution correctly.
- **Equal divisors:** The union still contains each multiple once despite three identical input streams.
- **First position:** The answer is `min(a, b, c)`.
- **Shared multiples:** A number divisible by two or all three divisors occupies only one sequence position.
- **Large products:** Least common multiples and midpoint counts require sufficiently wide integer arithmetic in bounded-integer languages.
- **Lower-bound search:** Returning an arbitrary value with $C(x)\ge n$ is insufficient; the smallest such value is required.
