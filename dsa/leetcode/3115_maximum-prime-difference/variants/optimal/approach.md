## General

**The farthest prime indices must be the first and last ones.** Let the indices containing prime values be:

$$
p_1<p_2<\cdots<p_r.
$$

For any two prime positions $p_a$ and $p_b$, their distance is at most $p_r-p_1$. Therefore, the maximum is obtained by the leftmost prime and the rightmost prime. If there is only one prime, both chosen indices may be that same position and the distance is zero.

The source implements exactly this observation with an outer scan from the left and, only after finding the first prime, an inner scan from the right.

**Testing primality by trial division.** Helper `is_prime(x)` first rejects every `x < 2`. Values zero and one are not prime.

For `x >= 2`, it tests divisors from 2 through `int(sqrt(x))`. The expression:

`all(x % i for i in range(2, int(sqrt(x)) + 1))`

uses each remainder as a truth value. A zero remainder is false and makes `all` return false immediately, proving that `x` is composite. If no tested divisor divides `x`, every remainder is nonzero and the helper returns true.

It is sufficient to test through $\sqrt{x}$. If composite `x=ab` had both factors greater than $\sqrt{x}$, then $ab>x$, a contradiction. At least one nontrivial factor must lie within the tested range.

For `x=2` or `x=3`, the divisor range is empty. Python's `all` of an empty iterable is true, correctly classifying both primes after the `x < 2` rejection.

**Find the leftmost prime.** `enumerate(nums)` examines indices in ascending order. The first `x` passing `is_prime` is therefore at position $p_1$. No earlier prime exists because every earlier value was explicitly rejected.

The source does not continue the outer loop after this point. It immediately starts scanning from the array's final index down to `i`.

**Find the rightmost prime.** The inner range:

`range(len(nums) - 1, i - 1, -1)`

checks positions from the end down through the leftmost prime position. The first prime it encounters is $p_r$. Returning `j - i` gives $p_r-p_1$, the proven maximum distance.

Including `i` in the reverse scan handles the one-prime case. If no later prime exists, `nums[i]` is tested again, succeeds, and returns zero.

**Why the nested-looking loops are not quadratic.** The inner reverse scan is executed only once, after the outer scan finds the first prime, and the method returns from inside it. The outer prefix and inner suffix may overlap at `i`, but together they perform at most about $2n$ primality tests, not $n$ reverse scans.

**A trace for `[4,2,9,5,3]`.** Index zero contains composite four. Index one contains prime two, fixing the left endpoint. The reverse scan begins at index four, where three is prime, so it returns `4 - 1 = 3` immediately.

For `[4,8,2,8]`, the outer scan reaches prime two at index two. The reverse scan rejects index three's eight and then accepts index two itself, returning zero.

**Why the function is guaranteed to return.** The contract promises at least one prime-valued element. Therefore, the outer loop must find a prime. Once it does, the inner range includes that same index, so it must also find a prime and execute the return. The absence of an explicit fallback is justified by this guarantee.

**Prime values, not prime indices.** The helper is applied to `nums[i]`. An index such as 2 does not count unless the stored array value is prime, and a prime value may occur at a composite-numbered index. The returned quantity is the difference between positions after classification by values.

## Complexity detail

Let $V=\max(\texttt{nums})$. One primality test uses at most $O(\sqrt V)$ trial divisions. The two directional scans perform $O(n)$ tests in total, giving $O(n\sqrt V)$ time.

Here $V\le100$, so $\sqrt V\le10$ is a fixed constant. Under the actual contract, the exact implementation is therefore $O(n)$ time, matching the manifest.

The helper uses a lazy `range` and `all` plus scalar loop state. No prime table or index list is stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Prime lookup set:** Precompute the 25 primes at most 100 and test membership in constant time. This makes the fixed-domain nature explicit.
- **Sieve of Eratosthenes:** Useful for a much larger bounded value domain, but excessive for 100.
- **Collect every prime index:** Then subtract first from last; correct but uses $O(n)$ space unnecessarily.
- **One prime occurrence:** The reverse scan reaches the same index and returns zero.
- **Prime at both ends:** The method returns `n - 1`, the largest possible distance.
- **Values zero or one:** Rejected before trial division.
- **Values two and three:** Empty divisor ranges correctly produce true.
- **Perfect square composite:** The inclusive upper bound tests its square-root divisor.
- **Repeated prime values:** Each occurrence is a separate eligible index.
- **Nested loop appearance:** Only one reverse scan occurs because it is inside the first successful outer iteration and returns.
- **Guaranteed prime:** Ensures both scans terminate with a return.
- **Index versus value:** Primality belongs to `nums[index]`, while distance belongs to indices.
- **Floating square root:** Values are at most 100, so `int(sqrt(x))` is exact for the needed small integers.
- **No input mutation:** The array is only read.
- **Generalized bound:** Without the value cap, trial division exposes the $O(\sqrt V)$ factor hidden by the manifest's constant domain.
