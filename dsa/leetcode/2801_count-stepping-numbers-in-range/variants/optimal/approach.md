## General

**Count a prefix range, then subtract.** Directly iterating from `low` to `high` is impossible because each bound can contain up to one hundred decimal digits. The solution instead defines an implicit counting function $F(B)$: the number of positive stepping numbers no greater than the decimal bound $B$. The desired inclusive-range answer is

$$
F(\texttt{high})-F(\texttt{low}-1).
$$

The code evaluates the same cached depth-first digit dynamic program twice. It first sets the closed-over string `num` to `high` and stores the result in `a`. It then clears the cache, changes `num` to `str(int(low) - 1)`, computes `b`, and returns `(a - b) % mod`.

Subtracting `F(low - 1)` removes precisely the valid numbers strictly below `low` while retaining `low` itself when it is stepping. Python's arbitrary-precision integers make `int(low) - 1` safe even for a one-hundred-digit input. When `low` is `"1"`, the new bound is `"0"`, for which the digit DP correctly counts no positive number.

**Build all numbers up to a bound one digit at a time.** The recursive state is `dfs(pos, pre, lead, limit)`.

`pos` is the digit position currently being chosen. `pre` is the most recent significant digit, or `-1` before the number has started. `lead` says that every chosen position so far is still a skipped leading zero. `limit` says that the already chosen prefix is exactly equal to the bound's prefix, so the current digit may not exceed the corresponding bound digit.

These four pieces of information are sufficient. Whether the next digit is legal depends only on the previous significant digit. Whether it is allowed by the upper bound depends only on whether the prefix is still tight. The earlier full prefix does not otherwise affect any future choice, which is why many prefixes can share one cached state.

**Respect the upper bound.** If `limit` is true, `up` is the integer value of `num[pos]`. Otherwise, the current digit may be any value through nine. The loop tries every `i` from zero through `up`.

The recursive tight flag is written as `limit and i == up`. When the state is tight, `up` is the actual bound digit, so equality means the new prefix remains tight. When the state is already loose, the first operand is false, so the next state stays loose even if `i` happens to equal nine. This compact expression therefore implements the usual digit-DP transition correctly.

**Separate skipped padding from a real zero digit.** Shorter positive integers must also be represented inside a fixed-length traversal. The program models them with leading zeros that do not belong to the number. If `i == 0 and lead`, recursion advances while preserving `lead = True` and leaving `pre` unchanged.

That branch is different from choosing zero after the number has begun. Once a nonzero digit has started the number, a later zero is a real digit and is allowed only if its absolute difference from `pre` is one. For example, `10` is stepping, while `20` is not. Keeping `lead` separate prevents the skipped zeros before `10` from being compared with its first digit.

**Enforce the stepping rule.** In the non-leading branch, a digit is accepted when `pre == -1` or `abs(i - pre) == 1`. The first significant digit has no predecessor, so any choice from one through nine is allowed. Every later digit must differ from its immediate predecessor by exactly one. The recursive call records `i` as the new previous digit and sets `lead` to false.

At `pos >= len(num)`, all positions have been assigned. The return value is `int(not lead)`. It is one if at least one significant digit was chosen and zero if the path consisted entirely of leading zeros. This deliberately excludes the number zero, matching the positive bounds and preventing the padding-only representation from being counted as a stepping number.

**Why the DP counts every valid number exactly once.** Every positive integer no longer than the bound has a unique length-equal representation obtained by padding it with leading zeros. The recursion follows exactly one digit choice for that representation. The `limit` rule admits it if and only if it does not exceed the bound, and the `pre` rule admits it if and only if every pair of adjacent significant digits differs by one. Conversely, every accepted recursion path becomes one positive integer satisfying both conditions. This is a bijection, so `dfs(0, -1, True, True)` equals $F(B)$.

**The cache must be cleared between bounds.** The decorated function closes over `num` rather than receiving the bound as an argument. Cache keys contain only `pos`, `pre`, `lead`, and `limit`. Results computed for `high` would therefore be incorrectly reused for `low - 1` if `dfs.cache_clear()` were omitted. Clearing the cache after storing `a` is a correctness requirement, not merely a memory optimization.

Each state returns its count modulo $10^9+7$. Modular reduction can occur before higher states add the value because addition respects congruence. The final subtraction also uses Python's modulo operator, which returns a nonnegative residue, so a negative intermediate difference is normalized automatically.

## Complexity detail

Let $d$ be the number of digits in the current bound. There are $d$ possible positions, eleven meaningful previous-digit values from `-1` through nine, two values of `lead`, and two values of `limit`. That is at most $44d$ cached states. Each state tries at most ten digits, a constant. One call to $F$ therefore takes $O(d)$ time with a moderate constant factor.

The algorithm performs two such calls, for `high` and `low - 1`. Both bounds have at most $d$ digits, so total time remains $O(d)$. Converting a length-$d$ decimal string to a Python integer and back also costs at least linear work and does not change the asymptotic result.

The cache stores $O(d)$ states. Recursion can reach depth $d$, so the call stack also uses $O(d)$ space. The cache is cleared between the two runs, which prevents both tables from being retained simultaneously. Total auxiliary space is $O(d)$.

The manifest's $O(L \cdot 10)$ notation describes the same fact when $L$ is digit count: each of a linear number of states considers at most ten digits. Because ten is a fixed decimal-alphabet size, this simplifies to $O(L)$.

## Alternatives and edge cases

- **Enumerate stepping numbers with BFS:** Start from digits one through nine and append previous-digit minus one or plus one. This works well for machine-sized bounds, but one-hundred-digit ranges can contain exponentially many stepping numbers, so counting with digit DP is essential.
- **Bottom-up digit DP:** The same state transitions can be filled iteratively. It avoids recursion depth concerns but usually needs more bookkeeping for the tight and leading-zero dimensions.
- **Include zero:** Some definitions regard zero as stepping. This problem's positive range does not need it, and the base case intentionally returns zero for the all-leading-zero path.
- **Bound equal to zero:** The only full recursion path stays in leading zeros, so $F(0)=0$.
- **Single-digit values:** Every digit from one through nine is stepping because there is no adjacent pair to violate the rule.
- **Digits at the boundaries:** From zero, the only legal next significant digit is one. From nine, the only legal next digit is eight. The absolute-difference test handles both without special branches.
- **Leading zeros:** They are padding rather than part of the number and must not set `pre` to zero. The dedicated `lead` branch preserves that distinction.
- **Inclusive lower bound:** Subtracting $F(\texttt{low})$ would wrongly remove `low` itself. The conversion to `low - 1` is what makes the result inclusive.
- **Cache contamination:** Because `num` is external to the cache key, reusing cached states after changing `num` would produce invalid counts. The explicit clear is indispensable.
- **Modulo subtraction:** Returning `(a - b) % mod` ensures an answer in the required range even when the stored residues satisfy `a < b`.
- **Very long inputs:** Python can parse the one-hundred-digit lower bound, and the DP's state count grows only linearly with its length.
