## General

**Build the permutation one position at a time**

The array positions and available values are both the integers from one through $N$. At position $i$, a value $j$ is legal exactly when $\gcd(i,j)=1$. Each value must be used once.

A brute-force permutation generator would explore all $N!$ orders and check many invalid arrangements only after constructing them. The exact solution instead uses subset dynamic programming: its state records which values have already been placed, and it extends only with values legal at the next position.

**Represent used values with a bit mask**

Bit $j$ of `mask` is one when value $j$ has been used. Bit zero is deliberately unused because values begin at one. The test:

`(mask >> j & 1) == 0`

means value $j$ is still available. Choosing it creates `mask | 1 << j`.

The number of one bits tells how many positions are already filled. Therefore:

`i = mask.bit_count() + 1`

is the next one-based position. The position does not need to be stored separately; it is completely determined by the subset size.

**Define the cached recurrence**

`dfs(mask)` returns the number of valid ways to fill positions `i` through $N$, given the used-value subset.

For every value `j` from one through $N$, the code checks two conditions:

1. its bit is not set;
2. `gcd(i, j) == 1`.

If both hold, all completions after placing `j` are counted by the recursive state with its bit set. These counts are added to `ans`.

When `i > n`, all $N$ positions are filled. The current construction is a complete valid permutation, so the base case returns one. It returns one rather than zero because this completed branch contributes one solution to its caller’s sum.

**Why memoization removes repeated work**

Different placement orders can lead to the same set of used values. Once the subset is fixed, the next position and remaining values are also fixed, and earlier order details cannot affect future legality. Therefore, all such paths have the same number of completions.

`@cache` stores one answer for each reached mask. Without it, the recursion would still revisit factorially many prefixes. With it, each of the at most $2^N$ subsets is solved once.

Although bit zero is unused and the integer masks can numerically reach beyond `(1 << n) - 1`, there are still only $2^N$ combinations of bits one through $N$.

**A trace for small $N$**

For $N=2$, state zero means position one. Both values one and two are coprime with position one, so two branches begin.

If value one is placed first, position two must receive two, but $\gcd(2,2)=2$, so that branch contributes zero. If value two is first, position two receives one and $\gcd(2,1)=1$, so the completed state contributes one. The answer is one.

For $N=3$, the same recurrence counts the three listed valid permutations without ever generating an invalid placement where a position/value gcd is greater than one.

**Why the recurrence counts exactly all valid permutations**

Every recursive path chooses one previously unused value for each position, so a completed path is a permutation. The gcd condition is checked at the moment of placement, so every completed path is self-divisible.

Conversely, take any self-divisible permutation. At position one, its value is unused and coprime, so the recurrence contains that branch. The same is true at every following position. The permutation therefore determines one complete recursion path. Different permutations differ at some position and take different branches, so none are counted twice.

This bijection proves the returned sum is exact.

**Why recursion is safe here**

The maximum depth is $N+1$, and $N\le12$. Unlike other recursive package solutions near Python’s recursion limit, this call stack is tiny and robust.

## Complexity detail

There are at most $2^N$ subset states. Each state loops over $N$ candidate values and performs a gcd test, giving $O(N2^N)$ time under the conventional small-integer gcd model. More precisely, Euclid’s algorithm adds a factor $O(\log N)$, but with $N\le12$ it is constant in practice and the manifest uses $O(N2^N)$.

The cache stores up to $2^N$ integer results. Recursion uses $O(N)$ stack depth. Total auxiliary space is $O(2^N)$.

## Alternatives and edge cases

- **Enumerate all permutations:** This takes $O(N!\cdot N)$ checking work and ignores early gcd pruning and shared subset states.
- **Bottom-up subset DP:** It can fill masks iteratively with the same $O(N2^N)$ time and $O(2^N)$ space, avoiding recursion.
- **Store position in the cache key:** It is redundant because `bit_count(mask)+1` uniquely determines it.
- **Use zero-based gcd positions:** The definition is one-indexed; using position zero would make every gcd equal to the chosen value and be wrong.
- **Bit zero:** It remains unused consistently. Candidate value `j` maps to bit `j`, not `j-1`.
- **Value one:** It is coprime with every position and can always be placed if unused.
- **`n = 1`:** The only placement has $\gcd(1,1)=1$, so the answer is one.
- **A state with no legal value:** Its loop adds nothing and correctly returns zero.
- **No modulo:** The problem requests the exact count, and Python integers hold it.
