## General

**Turn an inclusive interval into two prefix counts**

Counting each integer from `num1` through `num2` is impossible when an endpoint can have 23 decimal digits. The standard interval identity is:

$$
\operatorname{answer}=F(\texttt{num2})-F(\texttt{num1}-1),
$$

where $F(B)$ counts valid nonnegative integers at most $B$. The implementation computes these two counts as `a` and `b` and returns their difference modulo $10^9+7$.

This reduces the task to one reusable digit dynamic program for an upper bound stored in the closure variable `num`.

**Build a number from left to right**

The state `dfs(pos, s, limit)` represents the number of ways to fill decimal positions from `pos` onward when:

- positions before `pos` have already been chosen;
- those chosen digits sum to `s`;
- `limit` says whether the chosen prefix is exactly equal to the corresponding prefix of `num`.

If `limit` is true, the digit at `pos` cannot exceed `int(num[pos])`. If it did, the completed number would exceed the bound. If `limit` is false, the chosen prefix is already smaller than the bound, so any digit from zero through nine is legal.

The code stores this maximum allowed digit in `up`.

**Update the tight-bound flag correctly**

After choosing digit `i`, the next state is tight only when the current state was tight and `i` equals the upper digit:

`limit and i == up`.

When the current state is not tight, `up` is nine. The left side of the conjunction is already false, so the next state stays false regardless of `i`. When the state is tight, choosing a smaller digit makes the constructed prefix permanently smaller, while choosing exactly the bound digit preserves tightness.

This single Boolean prevents the DP from generating values greater than `num`.

**Leading zeros let every value use the same length**

The recursion always processes exactly `len(num)` positions. Shorter numbers are represented with leading zeros. For example, under bound `"120"`, integer seven is represented as `"007"`.

Leading zeros add nothing to the digit sum and do not change the numeric value. Therefore the representation counts every integer from zero through the bound exactly once without needing a separate “started” flag.

**The base case applies the digit-sum condition**

When `pos >= len(num)`, all digits are fixed. The function returns one precisely when:

$$
\texttt{min_sum}\le s\le\texttt{max_sum},
$$

and zero otherwise. Summing the recursive results therefore counts all bounded digit strings whose digit sums lie in the required interval.

Every level reduces the remaining positions by one, so the recursion terminates.

**Why memoization changes the problem from exponential to manageable**

Without caching, many different digit prefixes lead to the same triple `(pos, s, limit)` and would recompute identical suffix choices. The `@cache` decorator stores each state once.

For instance, numerous two-digit prefixes can have the same sum and already be below the bound. Once they reach the same position, sum, and false tightness flag, their possible suffixes are identical. Reusing that result is the core dynamic-programming saving.

**Why the cache must be cleared between endpoints**

The nested function reads `num` from its surrounding scope, but `num` is not part of the cache key. The first call sets `num = num2`. Before counting `num1 - 1`, the code calls `dfs.cache_clear()` and then changes `num`.

Without clearing, a state cached for the digits of `num2` could be incorrectly reused for the different lower endpoint. Clearing is therefore a correctness requirement, not merely a memory optimization.

**Trace a small bound**

For `num = "12"`, `min_sum = 1`, and `max_sum = 8`, the first position may choose zero or one.

Choosing zero makes the prefix smaller, so the second digit may be zero through nine. Among values `00` through `09`, digit sums one through eight accept `01` through `08`.

Choosing one keeps the prefix tight. At the second position, only zero through two are permitted, producing `10`, `11`, and `12` with sums one, two, and three. These are also accepted. The count is eleven.

**Modulo subtraction**

Each state's sum is reduced modulo `mod`. The final expression `(a - b) % mod` returns the nonnegative modular interval count in Python, even if the stored residues satisfy `a < b`.

The problem guarantees `num1 >= 1`, so `int(num1) - 1` is nonnegative and converting it back to a decimal string is safe. Converting through Python's arbitrary-precision integer also supports the stated endpoint size.

**Why the returned interval is exact**

The DP enumerates every integer from zero to a bound exactly once through its fixed-length digit representation, excludes precisely the representations exceeding the bound through `limit`, and accepts exactly the allowed final sums. Thus $F(B)$ is correct. Values below `num1` appear in both prefix counts and cancel, while values from `num1` through `num2` appear only in the first, yielding the requested inclusive interval.

## Complexity detail

Let $L$ be the number of digits in the larger endpoint, and let $S=9L$ be the maximum reachable digit sum for an $L$-digit representation. There are $O(LS)$ pairs of position and sum and two values of `limit`. Each state tries at most ten digits, a constant for decimal notation. One endpoint count therefore takes $O(LS)$ time and $O(LS)$ memo space; running it twice changes only the constant factor.

Equivalently, because $S=9L$, the safe bound is $O(L^2)$ time and $O(L^2)$ cache space. The recursion stack has depth $O(L)$ and is dominated by the cache.

The exact implementation does not prune states once `s > max_sum`. Such states can never become valid because digits are nonnegative, but they are still explored up to the natural maximum $9L$. Therefore defining $S$ as `max_sum` would understate this particular code when `max_sum < 9L`. The manifest's $O(L*S)$ is accurate when $S$ denotes the reachable digit-sum range, not necessarily the input parameter `max_sum`.

## Alternatives and edge cases

- **Prune sums above `max_sum`:** Returning zero immediately can reduce practical states and supports a bound using $\min(9L,\texttt{max_sum})$.
- **Bottom-up digit DP:** Avoids recursion but requires carefully carrying tight and sum dimensions for each position.
- **Enumerate the numeric interval:** Infeasible because a 23-digit interval can contain astronomically many integers.
- **Count exact sums separately:** Valid but repeats work; one DP can test the entire allowed range at its base case.
- **Leading zeros:** They are intentional and ensure shorter integers are counted once without affecting digit sums.
- **Lower endpoint one:** `num1 - 1` becomes zero; since `min_sum >= 1`, zero contributes nothing.
- **Maximum digit sum unreachable:** If `min_sum > 9L`, every base case fails and the result is zero.
- **Wide sum range:** If the allowed range contains every reachable sum, the DP counts every number in the numeric interval.
- **Cache closure:** Clearing between the two values of `num` is mandatory because the bound is not in the memo key.
- **Modulo difference:** Python's modulo operation normalizes a negative residue into the required nonnegative range.
