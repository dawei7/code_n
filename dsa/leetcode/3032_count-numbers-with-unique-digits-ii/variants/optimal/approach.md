## General

**Count a prefix range, then subtract.** Define $F(X)$ as the number of positive integers from 1 through $X$ whose decimal digits are all unique. The requested inclusive-range answer is

$$
F(b)-F(a-1).
$$

The exact source evaluates the same digit dynamic program twice: first with `num = str(a - 1)` and then with `num = str(b)`. Subtraction removes all valid numbers below $a$ while retaining both endpoints when they qualify.

**Build numbers from most significant digit to least.** Function `dfs(pos, mask, limit)` counts valid completions from decimal position `pos`.

`mask` is a ten-bit set of digits already used after the number has started. Bit $d$ is one exactly when digit $d$ already appears in the constructed number. This lets the loop reject a repeated digit with

`if mask >> i & 1: continue`.

`limit` means the chosen prefix is still equal to the bound's prefix. When it is true, the next digit cannot exceed the bound digit `int(num[pos])`. When false, any digit 0 through 9 is allowed.

**Handle leading zeros without treating them as digits.** Digit DP conceptually pads every shorter number to the bound's length with leading zeros. Those padding zeros must not participate in uniqueness. Otherwise a one-digit number represented as `0007` would appear to repeat zero.

The exact transition computes

`nxt = 0 if mask == 0 and i == 0 else mask | 1 << i`.

While no non-leading digit has been selected and the choice is zero, the mask remains zero. The number has not started. Once any nonzero digit is selected, its bit is recorded. A later actual zero then sets bit 0 like any other digit, and another zero is correctly rejected.

For example, the padded construction `0010` ignores the first two zeros, then records digit 1 and digit 0. Construction `0100` records 1 and the first actual 0, then rejects the repeated final 0.

**Update tightness correctly.** The next state is tight only if the current state was tight and the selected digit equals its upper bound:

`limit and i == up`.

When `limit` is false, `up` is 9, but the expression remains false even if digit 9 is chosen because of the first operand. Once a constructed prefix is below the bound, later positions stay unrestricted.

**Count only positive completed numbers.** When `pos` reaches `len(num)`, all positions have been chosen. The source returns one if `mask` is nonzero and zero otherwise. A nonzero mask means the number started and all chosen actual digits were unique, because repetitions were filtered during transitions. A zero mask represents the all-leading-zero construction—the number zero—which is excluded because the problem counts positive integers.

This base case also makes $F(0)=0$, which is necessary when $a=1$ and the first bound is `a - 1 = 0`.

**Why memoization is valid.** From a given `(pos, mask, limit)` state, the number of legal suffix completions depends only on those three values and the current bound string `num`. The decorator `@cache` stores that result so different prefixes that arrive at the same state do not repeat work.

The bound string is a captured outer variable rather than part of the cache key. Therefore the line `dfs.cache_clear()` between the two calls is essential. Without it, states computed for $a-1$ could be incorrectly reused for $b$. Clearing makes every cached result correspond to the currently assigned `num`.

**A small counting example.** To count through 20, the DP considers padded two-digit forms. Leading zero plus digits 1 through 9 represents one-digit numbers and contributes nine. Two-digit constructions from 10 through 20 are checked by mask: 11 is rejected because digit 1 is already set; all other numbers in that interval have distinct digits. The count is 19, agreeing with the example.

**The source differs from the manifest.** The local manifest describes scanning every integer in the range and checking a digit set. The protected Optimal source does not scan the range. It performs digit DP over a bounded set of positions and used-digit masks. This distinction changes the parameterized complexity and explains why the implementation remains efficient even if the numeric interval were widened.

## Complexity detail

Let $D$ be the number of digits in the bound. There are at most $D\cdot2^{10}\cdot2$ states: a position, one of 1024 masks, and a tightness flag. Each state tries at most ten next digits. One call therefore takes

$$
O(D\cdot2^{10}\cdot10)
$$

time and $O(D\cdot2^{10})$ cache space, plus an $O(D)$ recursion stack. Running it twice changes only the constant factor because the cache is cleared between bounds.

Since decimal digits form a fixed ten-symbol alphabet, this is commonly simplified to $O(D)$ time and $O(D)$ space with a large constant, although the explicit mask factor describes the actual table more honestly. Under the stated $b\le1000$, $D\le4$, so all of these quantities are tiny.

The manifest's $O(RD)$ bound, where $R=b-a+1$, applies to a brute-force range scan and does not describe this source.

## Alternatives and edge cases

- **Scan every number in $[a,b]$:** Convert each to a string and compare its length with a digit set. It is simple under $b\le1000$ but costs $O(RD)$ rather than counting the numeric prefix structurally.
- **Combinatorial counting by length:** One can count shorter unique-digit numbers with permutations and handle the bound's prefix manually. That can use constant space but is easier to make off-by-one errors in.
- **Bitmask without memoization:** The state representation remains correct, but repeated suffix subproblems cause unnecessary exponential branching.
- **$a=1$:** The lower prefix bound is zero. The all-zero construction is excluded, so $F(0)=0$ and subtraction works.
- **Number zero:** It is never counted because the terminal state requires a nonzero mask.
- **Leading zeros:** They keep `mask == 0` and may repeat freely as padding; they are not digits of the represented positive number.
- **Actual zero after the number starts:** It sets bit 0 and cannot appear again, exactly like every other decimal digit.
- **Repeated nonzero digit:** Its bit is already set, so that transition is skipped.
- **Inclusive upper bound:** Tight states allow selecting `up` itself, so a valid $b$ is counted.
- **Cache clearing:** It is mandatory because `num` is not included in the cached arguments and changes between the two prefix counts.
- **Manifest mismatch:** The explanation and complexity must follow digit DP, not the documented range scan, because digit DP is what the Optimal source actually executes.
