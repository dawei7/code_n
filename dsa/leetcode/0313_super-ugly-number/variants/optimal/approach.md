## General

Every super ugly number is either 1 or a product of allowed primes. A direct generator can begin with 1 and repeatedly multiply previously generated values by primes. The challenge is avoiding duplicates: a number such as 14 could be produced as $2\cdot7$ from parent 7 or as $7\cdot2$ from parent 2.

The exact source uses a min-heap and a canonical-parent rule that prevents duplicates without a set. It pops the smallest pending value, pushes selected prime multiples of that value, and repeats exactly `n` times.

The local manifest describes merging monotone product streams in $O(nk)$ time and $O(n+k)$ space. That is a different pointer-DP method. This explanation follows the executable heap algorithm and analyzes its heap operations.

**Why the sequence begins with one**

The heap starts as `q = [1]`. The number 1 has no prime factors, so every one of its prime factors belongs to `primes` vacuously. It is always the first super ugly number.

On the first iteration, `heappop(q)` returns 1. Because no prime divides 1, the loop reaches every allowed prime and pushes each prime times 1. These are exactly the smallest nontrivial super ugly numbers.

The variable `x` records the most recently popped number. After exactly `n` pops, `x` is returned, so the one-based sequence position is handled directly. In particular, `n = 1` returns the initial 1.

**The canonical generation rule**

For a popped value $x$, the source scans the sorted primes from smallest to largest. For each prime $p$, it may push $p\cdot x$. Immediately after that, if $p$ divides $x$, it breaks the prime loop.

Therefore, if $s(x)$ denotes the smallest allowed prime factor of $x$, the source multiplies $x$ by every allowed prime $p\le s(x)$ and by no larger prime. For $x=1$, which has no prime factor, it multiplies by every prime.

This rule may initially seem backwards. Its purpose is to ensure that every new product is generated using its smallest prime factor as the multiplier.

Suppose the algorithm pushes

$$
y=p\cdot x.
$$

Because it reaches $p$ before breaking, either $x=1$ or every prime factor of $x$ is at least $p$. Hence, $p$ is the smallest prime factor of $y$.

**Why every super ugly number is generated**

Take any super ugly number $y>1$. Let $p$ be its smallest prime factor and define $x=y/p$.

The value $x$ is also a super ugly number because removing one allowed prime factor leaves only allowed prime factors. Every factor of $x$ is at least $p$; otherwise, $y$ would have a smaller factor than $p$.

When $x$ is eventually popped, its first dividing prime is therefore $p$ or a later prime. The scan reaches $p$, pushes $p\cdot x=y$, and only then may break. Thus, every valid $y$ has a generation step.

This argument builds numbers inductively from 1: the parent $x=y/p$ is smaller than $y$, so it appears earlier in the increasing process.

**Why no number is generated twice**

Any pushed product $y=p\cdot x$ uses $p$ as the smallest prime factor of $y$, as shown above. The smallest prime factor of a positive integer is unique. Once $p$ is fixed, its parent is uniquely $x=y/p$.

Therefore, $y$ has exactly one canonical pair `(parent, multiplier)` that satisfies the loop's rule. It cannot also be pushed from a different parent.

For 14 with primes `[2, 7, 13, 19]`, parent 7 multiplies by 2 and pushes 14. Parent 2 does not multiply by 7 because the prime loop for 2 pushes `2 * 2` and immediately breaks when it sees that 2 divides the parent. The duplicate route is never executed.

Because duplicates are prevented structurally, the source needs no `seen` set and never has to pop repeated heap values.

**Why heap order gives the correct rank**

Every pushed value is a valid super ugly number. Every valid number is eventually pushed exactly once. A min-heap always removes the smallest pending value.

Also, every generated child is strictly greater than its positive parent because each prime is at least 2. Thus, a not-yet-generated smaller value cannot be hidden behind a larger parent that must be popped later; its own smaller canonical parent appears first and generates it in time.

The pop sequence is consequently the strictly increasing sequence of all super ugly numbers. Counting `n` pops returns the requested rank.

**Tracing the beginning of the example**

With primes `[2, 7, 13, 19]`:

- Pop 1; push 2, 7, 13, and 19.
- Pop 2; push 4 and break at prime 2.
- Pop 4; push 8 and break at prime 2.
- Pop 7; push 14, then push 49 and break at prime 7.
- Pop 8; push 16 and break at prime 2.
- Pop 13; push 26, 91, and 169 before breaking at prime 13.

The heap globally orders these candidates, so the popped sequence begins `1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32`. The twelfth popped value is 32.

**The 32-bit guard**

`mx = (1 << 31) - 1` is the largest signed 32-bit integer. Before multiplying by prime `k`, the source tests

`x <= mx // k`.

For positive integers, this is equivalent to $kx\le mx$, but it avoids performing a potentially overflowing multiplication in a fixed-width language. Python integers would not overflow, yet the guard keeps the heap limited to values inside the promised answer domain.

If a product for the current prime is too large, larger sorted primes also cannot produce an in-range product. The source still checks divisibility and may break at the canonical smallest divisor; no required in-range value is lost. The guarantee that the requested answer fits ensures enough valid values remain available for `n` pops.

## Complexity detail

Let $k$ be the number of allowed primes. Each of the $n$ iterations performs one heap pop and examines at most $k$ primes, performing at most $k$ heap pushes.

The heap can contain up to $O(nk)$ pending values under a conservative worst-case bound. Each push or pop costs $O(\log(nk))$. Therefore, a conservative exact-source time bound is

$$
O(nk\log(nk)),
$$

plus $O(nk)$ divisibility and bound checks.

The pending heap can use $O(nk)$ space in the same conservative worst case. It contains unique integers, so no separate deduplication set is allocated.

The manifest's $O(nk)$ time and $O(n+k)$ space apply to an array of the first $n$ values plus one pointer per prime, not to the min-heap operations in this source.

## Alternatives and edge cases

- **Pointer dynamic programming:** Store the first $n$ sequence values and one index per prime. At each step, select the smallest `prime * sequence[index]` candidate and advance every pointer producing that minimum. This gives $O(nk)$ time and $O(n+k)$ space and matches the manifest.
- **Heap plus a `seen` set:** Multiply every popped value by every prime and insert unseen products. It is easier to derive but stores a hash set and performs more duplicate attempts than the canonical-parent rule.
- **Heap without duplicate control:** The same number may be popped several times, corrupting the one-based rank unless duplicate pops are explicitly skipped.
- **Test every positive integer:** Factor each candidate using the allowed primes until `n` values are found. Large gaps make this much less efficient than generating only valid products.
- **Unsorted primes:** The break rule relies on ascending order so the first divisor is the smallest prime factor. The contract guarantees sorting; without it, the canonical proof would fail.
- **Duplicate primes:** Repeated multipliers could push duplicates even under the break rule. The contract guarantees unique primes.
- **`n = 1`:** The first heap pop is 1, which is returned without requiring any nontrivial factor.
- **One allowed prime:** The sequence is powers of that prime beginning with 1. Every popped nontrivial value pushes its next power and immediately breaks.
- **Products with several representations:** The smallest-prime canonical parent selects exactly one, as illustrated by 14.
- **Repeated prime factors:** Values such as 8 are handled normally; parent 4 multiplies by its smallest factor 2.
- **Overflow boundary:** A product equal to `mx` is allowed because the guard uses `<=`; a larger product is not inserted.
- **Large Python integers:** Python itself would support them, but the explicit cap intentionally limits generated candidates to the problem's signed-32-bit guarantee.
- **Positive factors only:** Every child exceeds its parent, supporting forward generation and heap ordering.
- **Return value after the loop:** `x` is assigned on every iteration, and $n\ge1$, so it always holds the nth popped number when returned.
