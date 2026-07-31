## General

**Discard streams already covered by smaller denominations.** A denomination $c$ contributes the positive multiples of $c$. If a previously kept denomination $d$ divides $c$, every multiple of $c$ is already a multiple of $d$, so retaining $c$ cannot change the union. Sort the denominations and keep only those not divisible by an earlier kept value. Let $m$ be the number that remain.

**Turn the requested rank into a monotone counting question.** Let $a$ be the smallest retained denomination and define $U=ak$. The $k$ positive multiples $a,2a,\ldots,ka$ are all obtainable, so the answer is at most $U$. For any candidate limit $x$, count how many distinct obtainable amounts are at most $x$. This prefix count never decreases as $x$ grows, making it possible to find the first limit whose count reaches $k$.

**Count the union with inclusion-exclusion.** For every nonempty subset $S$ of the retained denominations, a number belongs to all streams in $S$ exactly when it is divisible by $\operatorname{lcm}(S)$. There are

$$
\left\lfloor \frac{x}{\operatorname{lcm}(S)} \right\rfloor
$$

such positive numbers through $x$. Add this quantity for odd-sized subsets and subtract it for even-sized subsets. Different subsets can have the same least common multiple, so combine their signed coefficients once. A least common multiple greater than $U$ never contributes anywhere in the search interval and may be omitted.

Binary-search the integer interval from $1$ through $U$. If the prefix count at `middle` is at least $k$, the answer lies at or to its left; otherwise it lies strictly to the right. When the bounds meet, every smaller value has count below $k$ while the final value has count at least $k$. Therefore that value is precisely the $k$-th distinct obtainable amount.

## Complexity detail

Let $m$ be the number of denominations left after redundant streams are removed, and let $U=k\min(\texttt{coins})$. Enumerating every nonempty subset and building its least common multiple takes $O(m2^m)$ time and stores at most $O(2^m)$ aggregated terms. Each of the $O(\log U)$ binary-search iterations evaluates at most $2^m$ terms. The total time is $O(2^m(m+\log U))$, and the auxiliary space is $O(2^m+m)$, including the retained denominations and coefficient table.

## Alternatives and edge cases

- **Heap merge of multiple streams:** Repeatedly extract the next value from the denomination streams and suppress duplicates. This uses $O(m)$ space but takes $O(k\log m)$ time, which is infeasible when $k$ approaches $2\cdot10^9$.
- **Scan every positive amount:** Test each integer for divisibility by any denomination until $k$ matches have appeared. This can take $O(Um)$ time and ignores the monotone count available to binary search.
- **Keep every original denomination:** Inclusion-exclusion remains correct, but divisible denominations introduce unnecessary subsets and repeated least common multiples.
- **No mixed-denomination sums:** An amount such as $a+b$ is irrelevant unless it is independently a multiple of some single denomination; this is not the ordinary unbounded coin-change problem.
- **Overlapping streams:** A common multiple of several denominations occurs only once in the ordered sequence; inclusion-exclusion is what removes the duplicate counts.
- **Denomination one:** Its stream contains every positive integer, so all other denominations are redundant and the answer is exactly $k$.
- **Large answers:** With `coins = [25]` and $k=2\cdot10^9$, the answer is $5\cdot10^{10}$, so implementations need an integer type wider than signed 32 bits.
- **Least common multiple growth:** In fixed-width languages, stop or cap an LCM calculation once it exceeds $U$ to avoid overflow; such a term contributes zero throughout the search interval.
