## General
**Count magical numbers at or below a candidate**

For a positive integer $x$, the numbers no greater than $x$ that are divisible by `a` or `b` can be counted by inclusion-exclusion:

$$
C(x)=\left\lfloor\frac{x}{a}\right\rfloor
+\left\lfloor\frac{x}{b}\right\rfloor
-\left\lfloor\frac{x}{L}\right\rfloor.
$$

The final term removes the duplicate count for multiples of both divisors. As $x$ increases, $C(x)$ never decreases, so the predicate $C(x)\geq n$ is monotone.

**Find the first value whose count reaches the target**

The answer is at least `1` and at most `n * min(a, b)`, because the first $n$ multiples of the smaller divisor are all magical. Binary-search that closed value range. If `C(mid) >= n`, retain `mid` as a possible answer by moving the upper bound to it; otherwise, discard `mid` and everything below it.

When the bounds meet, their common value is the smallest $x$ with at least $n$ magical numbers at or below it. Minimality means $x$ itself is magical and occupies position $n$. Apply the modulus only after finding this actual value so it does not disturb ordering or the count comparisons.

## Complexity detail
The search interval ends at $n\min(a,b)$ and is halved on each iteration. Computing $C(x)$ uses a constant number of arithmetic operations, so time is $O(\log(n\min(a,b)))$. Only fixed scalar state is stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Merge the multiples:** Advancing the next multiple of `a` and `b` generates the sequence correctly but takes $O(n)$ time.
- **Enumerate one least-common-multiple period:** The pattern repeats every $L$, permitting a block calculation, but enumerating and storing a period can be much larger and more intricate than binary search.
- **Test every positive integer:** Divisibility checks require time proportional to the answer and are too slow for the upper bounds.
- **Equal divisors:** When `a == b`, every magical number is a multiple of that shared value and inclusion-exclusion still counts it once.
- **One divisor divides the other:** The least-common-multiple subtraction collapses the count to the multiples of the smaller divisor.
- **Common multiples:** A value divisible by both `a` and `b` occupies only one position in the sequence.
- **Modulo timing:** Reduce only the final answer; applying the modulus during binary search would destroy the monotone numeric order.
- **Wide arithmetic:** Fixed-width implementations need a type capable of representing `n * min(a, b)` and the intermediate least common multiple.
