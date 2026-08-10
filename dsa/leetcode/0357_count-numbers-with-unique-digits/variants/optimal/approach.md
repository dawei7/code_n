## General

The interval $0\le x<10^n$ contains every decimal number whose ordinary representation has at most $n$ digits. The exact solution counts these numbers with a memoized digit-by-digit search. Its state remembers how many digit positions remain, which digits have already been used, and whether the number is still in its leading-zero region.

This is a digit dynamic program, not the direct permutation-product method named by the manifest. There is no loop that computes the number of valid one-digit, two-digit, and longer numbers through multiplication. Instead, the source explores digit choices and caches equivalent remaining subproblems.

**Treat every number as an `n`-position representation.**

It is useful to imagine every number padded on the left to exactly $n$ positions. For $n=3$, the number `7` can be viewed as `007`, while `42` can be viewed as `042`. Those padding zeros are not part of the ordinary decimal representation, so they must not make the number invalid and must not reserve digit zero.

The Boolean `lead` captures this distinction. It is true while all positions chosen so far have been padding zeros. When `lead` is true and the next choice `j` is zero, the recursive call keeps the same digit mask and keeps `lead` true. Once a nonzero digit is chosen, `lead` becomes false. Any later zero is a real digit and is marked as used like every other digit.

Without this special handling, padding `7` as `007` would appear to repeat zero and be rejected, even though the actual representation `7` has one unique digit. Conversely, after starting the number, a value such as `101` must be rejected because its real digits repeat `1`; the mask enforces that.

**Meaning of the recursive state.**

`dfs(i, mask, lead)` returns the number of valid ways to fill positions `i` down through `0`, given the prefix already chosen.

- `i` is the index of the next position. The initial call uses `n - 1`, so there are $n$ positions to fill.
- Bit `j` of `mask` is `1` exactly when decimal digit `j` has already appeared as a real, non-padding digit in the prefix.
- `lead` is true exactly when no real digit has been chosen yet.

The state does not need to remember the complete prefix. Future legality depends only on which digits are unavailable and whether zero would still count as padding. Two different prefixes with the same three state values have exactly the same possible suffixes, which is why memoization is valid.

**The base case counts one completed number.**

When `i < 0`, every position has been decided. The function returns `1` because the choices along that recursion path form one valid integer.

The path that selects leading zero in every position reaches this base case with an empty mask and `lead` still true. It represents the integer zero and contributes exactly one. This directly explains the required result for `n = 0` as well: the initial call is `dfs(-1, 0, True)`, which returns one without entering the digit loop. The only integer in $[0,1)$ is zero.

**Trying the next digit.**

At an unfinished position, the loop considers every decimal digit `j` from `0` through `9`. The bit expression `mask >> j & 1` tests whether `j` has already been used. If it is set, choosing `j` would create a repeated real digit, so the loop skips it.

There is one subtlety: padding zero is never placed in the mask. Therefore, while `lead` is true, the used-digit test does not forbid another padding zero. This is correct because any number of left-padding zeros describe the same shorter representation.

If `lead` is true and `j == 0`, the algorithm fills one more padding position through `dfs(i - 1, mask, True)`. Otherwise, `j` is a real digit. The expression `mask | 1 << j` sets its bit, and the recursive call uses `lead = False`. All returned completion counts are summed in `ans`.

Operator precedence makes `1 << j` occur before bitwise OR, so the expression adds precisely digit `j` to the used set. Similarly, shifting the mask right by `j` and ANDing with one extracts that bit.

**A trace for two positions.**

For `n = 2`, the search represents numbers from `00` through `99`.

- The branch beginning with padding zero represents one-digit numbers. Its second position may be padding zero, producing the integer `0`, or any digit `1` through `9`, producing nine one-digit positive numbers. This branch contributes `10`.
- A first real digit can be any of `1` through `9`, giving nine choices. The second real digit can be any of the remaining nine digits, including zero but excluding the chosen first digit. These two-digit numbers contribute $9\cdot9=81$.

The total is $10+81=91$. Repeated-digit values `11`, `22`, and so on are skipped because the first digit's bit is already set when the second position is processed.

**Why every valid number is counted once.**

Every integer below $10^n$ has exactly one length-$n$ padded representation. The search follows exactly one branch for each digit of that representation. Padding zeros do not enter the mask, and every real digit does. If the ordinary representation repeats a digit, its later occurrence finds the bit already set and that branch is rejected. If all real digits are distinct, no choice is rejected and the path reaches the base case.

Therefore every valid number contributes one and every invalid number contributes zero. Different integers have different padded representations, so no two successful paths represent the same value.

**What caching removes.**

Many prefixes lead to the same remaining problem. For example, after using digits `1` and `2`, the future choices depend on the mask containing those two bits, not on whether the prefix order was `12` or `21`. `@cache` stores a result for each argument triple. When the same state is requested again, the saved count is returned instead of rebuilding its entire subtree.

## Complexity detail

Let $D=10$ be the number of decimal digits. There are at most $n$ unfinished position values, $2^D$ masks, and two values of `lead`. Each cached state tries $D$ candidate digits. A general upper bound for the exact digit DP is therefore

$$
O(nD2^D)
$$

time and $O(n2^D)$ cache space. The recursion stack uses another $O(n)$ space. With fixed decimal $D=10$, the time simplifies to $O(n)$ and the cache to $O(n)$ as functions of $n$, although the hidden factor includes up to `1024` masks and ten transitions per state.

The manifest's $O(n)$ time is compatible with treating the decimal alphabet as constant. Its $O(1)$ space, however, describes a direct running permutation product, not this memoized source. The source allocates cached states proportional to the number of processed position layers and uses recursion. Under the published constraint $n\le8$, all storage is absolutely bounded by a small constant domain, but the algorithmic implementation is still not constant-space in a parameterized analysis.

Many theoretical states are unreachable, so the actual cache is smaller than the full product. For example, a mask cannot contain more real digits than the number of positions already processed. The upper bound remains a clear description of the method.

## Alternatives and edge cases

- **Direct combinatorial product:** Count zero, then for each positive length choose the first digit in `9` ways and later digits from the remaining `9`, `8`, and so on. Accumulating these exact-length counts takes $O(n)$ time and $O(1)$ space and matches the manifest summary.

- **Plain backtracking without caching:** It follows the same validity rules but recomputes equivalent suffix states reached by different prefix orders, exploring a much larger recursion tree.

- **Bottom-up mask dynamic programming:** Store counts by used-digit mask and extend them one digit at a time. It avoids recursion but still uses subset-state storage.

- **`n = 0`:** The initial state is already complete and counts the single integer zero.

- **Leading zeros:** They are representation padding, not repeated decimal digits. They must neither set bit zero nor turn `lead` false.

- **A real zero:** Once a nonzero digit has started the number, choosing zero sets its bit. A second real zero is then correctly forbidden.

- **Numbers longer than ten digits:** No positive decimal integer can have more than ten distinct digits. Although the source constraints stop at eight, the count would stop increasing after length ten except for already-counted shorter numbers.

- **Inclusive zero and exclusive upper bound:** Exactly $n$ padded positions cover `0` through $10^n-1$, so the search includes zero and excludes $10^n$ automatically.

- **Cache lifetime:** The cached function is defined inside one method call, so its memoized states belong only to that invocation and cannot leak results across different values of `n`.
