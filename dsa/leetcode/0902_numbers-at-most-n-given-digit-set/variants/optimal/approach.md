## General

The exact solution uses digit dynamic programming. It constructs a decimal number one position at a time while ensuring that the represented value never exceeds `n`. Leading zero placeholders allow shorter positive integers to fit into the same fixed number of positions as `n`.

Let `s = str(n)`. The state `dfs(i, lead, limit)` counts valid completions from position `i`:

- `i` is the current decimal position.
- `lead` is 1 when no nonzero digit has been chosen yet, so all positions so far are leading placeholders.
- `limit` is true when the chosen prefix exactly equals `n`'s prefix. In that case, the current digit may not exceed `s[i]`.

If `limit` is false, the constructed prefix is already smaller than `n`, so any decimal digit up to 9 is numerically safe.

**Choose the upper digit.** The code sets `up = int(s[i])` when limited, otherwise 9, then loops through `j = 0..up`.

Digits in the supplied set are 1 through 9; zero is not an allowed written digit. Zero has one special role: while `lead` is true, choosing zero means “this shorter number has not started yet.” The transition stays in leading mode and advances to the next position.

Once a real allowed digit is chosen, `lead` becomes zero. From then onward, zero cannot be selected because it is not in `nums`, matching the rule that every written digit must come from the supplied set.

**Maintain the upper-bound flag.** The next state remains limited only when the current state was limited and chosen digit `j` equals the allowed upper digit. When currently limited, `up` is exactly `n`'s digit, so equality keeps prefixes tied. Choosing less makes the constructed number permanently smaller. When already unlimited, the conjunction begins false and remains false.

**Terminal condition excludes the number zero.** At `i == len(s)`, all positions have been processed. The expression `lead ^ 1` returns one if `lead` is zero and returns zero if `lead` is one. Thus a number that selected at least one real digit is counted, while the all-leading-zero path representing zero is excluded because the task asks for positive integers.

**How shorter lengths are counted.** Suppose `n` has three digits and the algorithm wants to represent one-digit number 7. It chooses leading zero placeholders for the first two positions and allowed digit 7 at the last position. Those zeros are not part of the written number. Each shorter positive integer has exactly one such padded representation, so there is no duplicate counting.
Every recursive path maintains a prefix no greater than `n` because limited positions never exceed the corresponding bound digit, and an earlier smaller choice releases the limit safely. Every nonleading digit belongs to `nums`. Thus every terminal path counted as one represents a valid positive integer at most `n`.

Conversely, take any valid positive integer at most `n`. Pad it on the left with zeros to `len(s)` positions. The recursion can follow those leading placeholders, then each of its allowed digits. Because the number is no greater than `n`, its padded digits never violate the active limit. It reaches a nonleading terminal state and is counted exactly once.

Memoization shares the count for repeated states. Many different conceptual prefixes have identical future behavior once only position, leading status, and limit status are retained.

For digits `["1","3","5","7"]` and `n=100`, all one-digit choices contribute four, all two-digit choices contribute $4^2=16$, and no valid three-digit choice is at most 100. The DP returns 20.

## Complexity detail

Let $d$ be the number of decimal digits in `n` and $k$ the number of allowed digits. There are at most $4d$ states from two boolean flags. The exact loop considers at most ten candidate decimal digits per state and uses expected constant-time set membership.

- **Time complexity:** $O(d)$ with the fixed decimal alphabet, or $O(dk)$ for a formulation iterating only allowed digits plus the leading choice.
- **Space complexity:** $O(d+k)$ for cached states, recursion stack, the decimal string, and allowed-digit set.

The manifest's $O(d\log k)$ time can describe binary-search counting among sorted allowed digits in a mathematical formulation, but the exact code scans digit values 0 through `up` and caches $O(d)$ states. Its literal space is not $O(1)$.

## Alternatives and edge cases

- **Combinatorial prefix counting:** Sum $k^\ell$ for all shorter lengths, then scan `n` left to right and count allowed digits smaller than each bound digit. This avoids recursion and can use constant scalar state.
- **Enumerate generated numbers:** Branching by allowed digits grows exponentially with length and repeats bound work.
- **Allow zero after the number starts:** Incorrect because the input digit set contains only 1 through 9; zero is only a leading placeholder.
- **Count the all-zero path:** That would include zero, which is not a positive integer.
- **One allowed digit:** The DP counts repeated uses of that digit whenever the resulting number is within the bound.
- **`n` smaller than every allowed digit:** No nonleading path fits, so the result is zero.
- **Number exactly equal to `n`:** It is counted only if every digit of `n` belongs to the allowed set.
- **Shorter numbers:** Leading placeholders count every valid shorter length exactly once.
- **Limit becomes false:** Once a chosen digit is smaller than `n`'s corresponding digit, later allowed digits may be chosen freely.
- **Unique sorted input digits:** The set discards ordering because this DP tests membership. Uniqueness prevents any conceptual duplicate choices.
- **Maximum `n`:** Its string has at most ten positions under the constraint, so state count remains tiny.
- **Cache key booleans:** `lead` is stored as integer 0 or 1 and `limit` as a boolean; both are hashable and fully describe future restrictions.
- **Manifest distinction:** Complexity should reflect this digit-state recursion rather than a separate binary-search counting formula.
