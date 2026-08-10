## General

**View operations as multiplication blocks**

The screen begins with one `A`. A useful sequence always has the form “Copy All, followed by one or more Paste operations.” If the screen currently contains `x` characters and a block performs one copy plus `g - 1` pastes, then:

- the block costs `g` operations;
- each paste adds another `x` characters;
- the screen ends with `g * x` characters.

Thus a block of length `g` multiplies the current count by `g`.

If several blocks have multipliers `g1, g2, ..., gt`, the final character count is their product, while the operation count is their sum. Reaching exactly `n` becomes a factorization problem: express `n` as a product of integer multipliers and minimize their sum.

**The recursive state**

`dfs(x)` means the minimum number of operations needed to reach exactly `x` characters from the initial one character.

The base state is `dfs(1) = 0` because the screen already has one `A` and no operation is required.

For `x > 1`, the initial candidate `ans = x` represents one Copy All at the beginning followed by `x - 1` Paste operations. This multiplies one by `x` in a single block and is always legal. It is especially important when `x` is prime, because no nontrivial factor split exists.

**Use a divisor as the final multiplication block**

Suppose `i` divides `x`. We can first reach `x // i` characters optimally, then perform:

- one Copy All;
- `i - 1` Paste operations.

Those `i` new operations multiply `x // i` by `i`, reaching `x`. The candidate cost is therefore:

`dfs(x // i) + i`.

The loop tests every divisor `i` from two through the square root of `x` and takes the minimum against the one-block baseline.

For `x = 9`, the divisor three yields `dfs(3) + 3`. Reaching three costs three operations, then copying three `A` characters and pasting twice costs three more, for a total of six. The one-block baseline would cost nine.

For `x = 12`, divisor two gives `dfs(6) + 2`, while divisor three gives `dfs(4) + 3`. Recursive calls factor the quotient further, so the algorithm considers multi-block constructions without explicitly enumerating operation strings.

**Why checking divisors only through the square root is enough**

Every composite `x` has at least one factor no larger than its square root. A divisor above the square root is paired with a complementary divisor below it.

More deeply, a complete strategy corresponds to a multiset of block multipliers whose product is `x` and whose sum is the operation count. Multiplication and addition are both independent of the order of those factors. We may therefore reorder any factorization so that one of its smallest factors is the final block. If the factorization has more than one nontrivial factor, its smallest factor is no larger than the square root of `x`.

The loop can choose that small final factor `i`, and `dfs(x // i)` handles all remaining factors in any optimal order. There is no need also to try the complementary large factor as the final block to preserve the minimum.

**Why composite block multipliers should be split**

Suppose one block multiplier is composite, `g = p * q` with `p, q >= 2`. Leaving it as one block costs `p * q` operations. Splitting it into consecutive blocks with multipliers `p` and `q` costs `p + q` operations and produces the same multiplication.

For integers at least two, `p + q <= p * q`, with equality only for two and two. Splitting a composite factor is never worse. Repeating the split shows that an optimal cost is the sum of the prime factors of `n`, counted with multiplicity.

The exact recursive solution reaches that result through divisor transitions rather than directly running a prime-factorization loop. Memoization ensures that if the same quotient state is reached from different divisor choices, it is solved only once.

**Why the recursion terminates**

Every recursive call uses `x // i` with `i >= 2`, so its argument is strictly smaller than `x`. Repeated calls therefore descend toward one and cannot cycle. A prime state makes no recursive calls and returns its baseline.

The `@cache` decorator stores results by integer argument. This avoids redoing a subproblem such as `dfs(6)` if multiple higher states request it.

**Why the recurrence is correct**

Consider an optimal strategy for `x > 1`. If it consists of one multiplication block, its cost is `x`, which the baseline includes. Otherwise, factor multipliers can be reordered so that a smallest factor `i <= sqrt(x)` is last. Before that last block, the screen must contain exactly `x // i` characters.

The cheapest possible prefix reaching that amount costs `dfs(x // i)` by definition, and the last block costs `i`. The loop considers this divisor, so it includes a candidate no more expensive than the optimal strategy.

Conversely, every candidate constructed by the recurrence is a legal sequence: the recursive prefix reaches the quotient exactly, and the final copy-paste block multiplies it to `x` exactly. The algorithm therefore cannot return an impossible lower cost. Taking the minimum of all legal candidates produces exactly the optimum.

## Complexity detail

Let `N` be the requested final count and let `tau(N)` denote the number of positive divisors of `N`.

The mathematical prime-factorization solution can run in `O(sqrt(N))` time and `O(1)` space, which is the bound advertised by the manifest. The exact source, however, is a memoized recursive divisor search. For each visited divisor-state `x`, it tests every integer through `sqrt(x)`. All visited states divide the original `N`, so a conservative bound is `O(tau(N) * sqrt(N))` time. A more precise expression is the sum of `sqrt(x)` over visited divisor states. With `N <= 1000`, this remains small, but the literal implementation should not be described as a single factorization scan.

The cache stores one result per visited state, at most `O(tau(N))` states. Recursive depth is `O(log N)` because each call divides its argument by at least two. Thus literal auxiliary space is `O(tau(N) + log N)`, not strict `O(1)`. The iterative prime-factorization alternative achieves the manifest's constant-space bound.

## Alternatives and edge cases

- **Iterative prime factorization:** Repeatedly divide `n` by each smallest factor and add that factor to the answer. It directly implements the sum-of-prime-factors result in `O(sqrt(N))` time and `O(1)` space and matches the manifest more literally.

- **Bottom-up dynamic programming:** For every target up to `n`, try possible previous divisors. It is easy to formulate but typically costs `O(N^2)` time or `O(N sqrt N)` with divisor checks and uses `O(N)` space.

- **Breadth-first search over screen and clipboard states:** It can find a shortest operation sequence, but the state space and clipboard dimension are unnecessary once the multiplication structure is recognized.

- **Greedily paste until close to `n`:** Copy timing determines future multiplication, so local closeness does not guarantee a minimum operation count.

- **`n = 1`:** The base case returns zero. Copying the existing character would not change the screen and would waste an operation.

- **Prime `n`:** No divisor is found through the square root. The only factorization is the single factor `n`, so the baseline `n` is optimal.

- **Power of two:** Repeated factor two blocks are optimal. Each block copies and pastes once, doubling the count at a cost of two.

- **Repeated prime factors:** They are counted with multiplicity. For twelve, the factors `2, 2, 3` sum to seven operations.

- **Copy without a later paste:** It does not change the screen and cannot improve a minimum-length sequence. Useful blocks always include at least one paste.

- **Partial copy:** It is not allowed. The multiplication argument depends on Copy All placing the entire current screen in the clipboard.

- **Overshooting:** Every chosen multiplier divides the target state, so recurrence candidates reach exactly `n` and never need to remove characters.

- **Missing cache:** Correctness would remain, but repeated divisor subproblems could be recomputed many times. Memoization is part of the exact source's practical efficiency.

- **Variable shadowing:** The nested `dfs(n)` parameter shadows the outer method's `n`. Each invocation still uses its own target value correctly, but a name such as `x` would make the state distinction clearer.
