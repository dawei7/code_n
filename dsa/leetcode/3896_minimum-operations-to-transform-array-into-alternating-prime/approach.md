## General

Every array position can be changed independently: an operation increments one chosen element and has no effect on any other index. The target property is also position-local. Even indices need prime values; odd indices need non-prime values.

Therefore, the global minimum is the sum of the smallest legal increment for each element. The source prepares primality information once, then uses one rule for even indices and another for odd indices.

**The fixed global prime sieve**

Before the `Solution` class is created, the module allocates `is_prime` for every integer from 0 through `MX = 200000`. It initially assumes all entries are prime, then explicitly marks 0 and 1 as non-prime.

For every candidate divisor $i$ through $\lfloor\sqrt{\texttt{MX}}\rfloor$, if $i$ is still marked prime, the sieve marks

$$
i^2,\ i^2+i,\ i^2+2i,\ldots
$$

as composite.

Starting at $i^2$ is sufficient. A smaller composite multiple $i\cdot q$ has $q<i$ and was already marked when processing a smaller prime factor. After the sieve finishes, `is_prime[x]` gives the correct status of every value in the fixed range.

The module then builds the sorted list `primes` by collecting every index whose flag remains true.

**Why the ceiling 200000 is enough**

Input values are at most $10^5$. An even-indexed value may need to move upward to the next prime, so preprocessing only through $10^5$ would require an argument about what happens just beyond that boundary.

For every integer $x>1$, Bertrand's postulate guarantees a prime $p$ with

$$
x<p<2x.
$$

For $x\le10^5$, such a prime is below 200000. The special input $x=1$ reaches prime 2 directly. Thus the list contains a prime at or above every allowed input, and `bisect_left` always returns a valid list position.

**Even indices: move to the next prime**

At an even index, the element must become prime. Because decrements are forbidden, the only candidates are primes $p\ge x$. Each candidate costs $p-x$ increments, so the smallest feasible prime also has the smallest cost.

The source computes

```text
j = bisect_left(primes, x)
```

The returned index `j` identifies the first prime not smaller than `x`. The contribution is `primes[j] - x`.

If `x` is already prime, the left-biased search finds `x` itself and the contribution is zero. If `x` is composite, it finds the next larger prime and returns the exact distance to it.

**Odd indices: a prime needs at most two increments**

At an odd index, any non-prime value is already legal and costs zero. Work is needed only when `is_prime[x]` is true.

There are two prime cases:

- If $x=2$, then $x+1=3$ is also prime, but $x+2=4$ is composite. The minimum cost is two.
- Every prime greater than 2 is odd. Adding one produces an even integer greater than 2, and every such integer is composite. The minimum cost is one.

That is exactly the source branch

```text
ans += 2 if x == 2 else 1
```

No binary search is necessary for odd indices. The structure of prime numbers proves the nearest non-prime increment directly.

**Why per-index minima add to the global minimum**

Let $d_i$ be the minimum increments needed to make position $i$ satisfy its parity rule. Performing those increments at every index creates an alternating-prime array with total cost $\sum_i d_i$.

Any valid transformation must independently spend at least $d_i$ operations on position $i$, because operations on other positions cannot change its value. Therefore every valid total costs at least $\sum_i d_i$. The construction reaches that lower bound, so summing the source's per-index contributions is globally optimal.

For `nums = [1,2,3,4]`:

- index 0 moves from 1 to prime 2, costing one;
- index 1 moves from prime 2 through prime 3 to non-prime 4, costing two;
- index 2 already contains prime 3; and
- index 3 already contains non-prime 4.

The total is three.

## Complexity detail

The checked-in source has a global preprocessing phase and a method-call phase. Their costs should not be merged without identifying the bound each one uses.

Let $U=\texttt{MX}=200000$, let $P$ be the number of primes at most $U$, and let $N=\lvert\texttt{nums}\rvert$.

The sieve costs

$$
O(U\log\log U)
$$

time and $O(U)$ space. Building `primes` scans the flags in $O(U)$ time and stores $O(P)$ values, which remains $O(U)$ space.

During `minOperations`, the source scans $N$ elements. Every even index performs a binary search over `primes` in $O(\log P)$ time. Every odd index uses a constant-time table lookup and branch. The method-call time is

$$
O(N\log P),
$$

which can be written as $O(N\log U)$. The method itself uses $O(1)$ additional working space beyond the global tables.

Including module initialization, the exact source costs

$$
O(U\log\log U+N\log U)
$$

time and $O(U)$ persistent auxiliary space.

The manifest writes these bounds using $M=\max(\texttt{nums})$. That describes an input-sized sieve design, but this source always sieves to the fixed 200000 ceiling, even when all supplied values are tiny. For source-accurate analysis, $U$ must denote that fixed global ceiling. Under the frozen constraints, $U$ is a constant limit, but stating it explicitly explains the actual memory allocation and import-time work.

## Alternatives and edge cases

- **Input-sized sieve:** Sieve only through a proven bound above the current maximum input. This may reduce work for small arrays but requires computing a safe next-prime ceiling.
- **Next-prime lookup table:** A reverse pass can store the next prime for every value, reducing even-index queries from binary search to $O(1)$ at the cost of another $O(U)$ array.
- **Per-value trial division:** Testing successive numbers avoids global storage, but repeated primality tests can be much slower across $10^5$ elements.
- **Even index already prime:** `bisect_left` returns that same value, so its cost is zero.
- **Odd index already composite:** The source leaves it unchanged, which is optimal because zero operations are possible.
- **Odd index equal to 1:** One is non-prime by definition, so it needs no operation.
- **Odd index equal to 2:** One increment reaches 3, still prime; two increments reach 4, so this is the only prime odd-position value costing two.
- **Odd index holding an odd prime:** Adding one makes an even number greater than 2, hence a composite, so one operation is sufficient.
- **Largest allowed input:** The preprocessing ceiling contains a later prime for every $x\le10^5$; the binary-search index cannot run beyond `primes` under the contract.
- **Index parity is zero-based:** Positions 0, 2, 4, and so on require primes; reversing the parity would solve a different problem.
- **Fixed preprocessing mismatch:** The source's setup cost depends on 200000 rather than the observed input maximum, despite the manifest's $M$ notation.
- **Required library name:** Standalone execution needs `bisect_left` from Python's `bisect` module to be available.
