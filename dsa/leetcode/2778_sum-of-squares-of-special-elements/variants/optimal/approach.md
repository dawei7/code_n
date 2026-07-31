## General

Divisors occur in complementary pairs. If $d$ divides $n$, then $n/d$ is also a divisor, and at least one member of the pair is no greater than $\sqrt{n}$. Therefore, inspect candidate divisors $d$ beginning at $1$ and stop after $d^2 > n$.

Whenever `n % d == 0`, add the square of `nums[d - 1]`, because the mathematical index is 1-based. Compute the paired divisor `n // d` and add `nums[n // d - 1]` as well. When $d^2 = n$, both expressions name the same middle divisor, so add it only once.

**Why every special element is counted exactly once**

Take any special index $i$. Its complementary divisor is $n/i$. One of $i$ and $n/i$ is at most $\sqrt{n}$, so the loop reaches that smaller member and discovers the pair. The algorithm then adds the values at both divisor indices. Different candidates below the square root generate different divisor pairs, and the equality guard handles the only pair whose two members can coincide. Thus every divisor index contributes once and only once, which makes the accumulated value exactly the requested sum of squares.

## Complexity detail

The loop tests $\lfloor\sqrt{n}\rfloor$ candidates, doing constant work for each, so the running time is $O(\sqrt{n})$. It stores only the total, current divisor, and paired divisor, giving $O(1)$ auxiliary space.

Because the source domain caps $n$ at $50$, legal inputs cannot support a reliable runtime-scaling verdict. The package therefore uses a bounded-domain certificate with structural proof and boundary cases instead of an out-of-contract benchmark.

## Alternatives and edge cases

- **Linear index scan:** Checking `n % i == 0` for every $1 \le i \le n$ is simple and correct, but costs $O(n)$ rather than using divisor pairs.
- **Precomputed divisor list:** Building a list before summing adds $O(\sqrt{n})$ storage without helping a single query.
- **1-based indexing:** A divisor $d$ selects `nums[d - 1]`; using `nums[d]` shifts every contribution and may access beyond the list.
- **Perfect-square length:** When `d == n // d`, square that array value once, not twice.
- **Length one:** The pair is $(1,1)$, so the only element is special and the equality guard counts it once.
- **Prime length:** Only indices $1$ and $n$ contribute.
- **Non-special large values:** Ignore them even if their magnitude exceeds every selected value; special status depends only on the index.
