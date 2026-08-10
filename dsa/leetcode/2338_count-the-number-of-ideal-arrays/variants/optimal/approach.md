## General

**Compress repeated values into a strict divisibility chain**

An ideal array is nondecreasing because each positive value divides the next, and a smaller positive number cannot be divisible by a larger one. Equal adjacent values are allowed.

Compress every maximal run of equal values into one value. For example,

`[1, 1, 2, 2, 2, 8]`

becomes the strict chain `[1, 2, 8]`. Each chain value strictly divides the next. Conversely, repeating the values of any strict divisibility chain in positive-length runs produces an ideal array.

The exact solution separately counts:

1. strict divisibility chains of each length and final value;
2. ways to expand a strict chain into `n` array positions.

**Precompute ways to place run boundaries**

A strict chain of length `j` must appear as `j` nonempty consecutive runs in the length-`n` array. There are `n - 1` gaps between adjacent positions. Choosing `j - 1` of those gaps as change points uniquely determines the run lengths.

The number of expansions is

`C(n - 1, j - 1)`.

The table `c` is Pascal's triangle. Its entry `c[i][j]` becomes `C(i, j)` through

`C(i,j) = C(i-1,j) + C(i-1,j-1)`.

Thus `c[-1][j - 1]`, the final row, is the needed `C(n - 1, j - 1)`.

Only columns zero through 15 are stored because a strict divisibility chain under `maxValue <= 10000` is very short. Each next distinct value is at least twice the previous one, so 16 columns safely cover all possible chain lengths.

**Count strict divisibility chains by their endpoint**

`f[value][j]` counts strict chains of length `j` ending at `value`.

Every single value forms one chain of length one, so `f[i][1] = 1` for all `i` from one through `maxValue`.

To extend a chain ending at `i`, choose multiplier `k >= 2`. The new endpoint `k * i` is a strictly larger multiple of `i` and remains allowed while it is at most `maxValue`. The update

`f[k * i][j + 1] += f[i][j]`

appends this endpoint to every chain counted by `f[i][j]`.

The loops perform this extension for chain lengths one through fourteen. Every strict chain has a unique previous endpoint and final multiplier, so the recurrence neither misses nor duplicates it.

**Combine chain identity with boundary placement**

For every final value `i` and chain length `j`, there are `f[i][j]` choices of strict chain and `C(n-1,j-1)` choices of positive run lengths. Their product counts all ideal arrays whose compressed chain is one of those chains.

The nested final loops add

`f[i][j] * c[-1][j - 1]`

for all endpoints and lengths.

Every ideal array has one unique compressed chain and one unique set of run boundaries, so it appears in exactly one product term. Conversely, every counted chain and boundary choice expands into a valid ideal array because equal repetitions preserve divisibility and every strict transition is to a multiple.

**Why this differs from prime-exponent distribution**

The editorial and manifest describe another combinatorial method that fixes a final value, factors it, and distributes prime exponents among positions. The exact solution never factors numbers. It enumerates strict multiplier chains and then chooses where their values change.

Both methods count the same objects, but the state meanings and preprocessing are different. The approach must follow `f` and Pascal placement to explain the provided code.

**Modulo is applied throughout**

Every Pascal sum, chain extension, and final contribution is reduced modulo `10^9 + 7`. Modular arithmetic preserves the requested remainder while keeping table entries bounded.

## Complexity detail

Let `M = maxValue`. Building the 16-column Pascal table takes `O(16n) = O(n)` time and space.

For each of 14 chain lengths, the multiplier loops perform roughly

`sum_{i=1}^{M} (floor(M/i) - 1) = O(M log M)`

updates. The constant 14 does not change the class, so total time is `O(n + M \log M)`. The final summation is `O(16M)`.

The `f` table contains `16(M+1)` entries and `c` contains `16n` entries, giving exact auxiliary space `O(M + n)`. The manifest's `O(M)` assumes comparable bounded parameters or a combination table represented more compactly.

No recursion or input mutation occurs. All arithmetic values are reduced modulo the fixed modulus.

## Alternatives and edge cases

- **Prime-exponent stars and bars:** Factor each possible final value and multiply `C(exponent+n-1, exponent)` across primes. This is elegant and often faster, but it is not the exact source's recurrence.
- **DP over every array position and value:** Transition from each divisor to its multiples for all `n` positions. This costs roughly `O(nM \log M)` and repeats work that run compression removes.
- **Enumerate arrays directly:** There are `M^n` raw arrays, which is infeasible.
- **Chain length one:** Every constant array is counted once, with `C(n-1,0)=1`.
- **`maxValue = 1`:** The only strict chain is `[1]`, so the only ideal array is all ones.
- **Repeated values:** They are represented by run lengths, not by repeated nodes in `f`.
- **Strict transition:** Multiplier starts at two. Multiplier one would duplicate equal runs inside the compressed chain.
- **Why chains stay short:** Every strict multiple at least doubles the value, limiting length logarithmically in `M`.
- **Final value endpoint:** Chains with different endpoints or different intermediate values remain distinct and occupy different `f` contributions.
- **Unique expansion:** Choosing boundary gaps determines positive run lengths summing to `n`.
- **Impossible long chains:** Their `f` entries stay zero even though table columns exist.
- **Modulo multiplication:** Both factor counts are already reduced, and their product is reduced when accumulated.
- **`n >= 2`:** The Pascal table has a valid last row and supports every possible chain length no greater than `n`; entries with `j-1 > n-1` remain zero.
- **Input values:** Only scalar parameters are read; all state is newly allocated.
