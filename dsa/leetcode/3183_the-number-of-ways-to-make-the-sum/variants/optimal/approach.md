## General

**Separate the limited coin from unlimited coins**

Coins 1, 2, and 6 are unlimited. Value 4 may be used only zero, one, or two times.

The source first computes `f[s]`: number of order-independent combinations making sum $s$ using only unlimited values 1, 2, and 6.

Then every valid complete combination belongs to exactly one case:

- zero 4-coins: `f[n]`;
- one 4-coin: `f[n-4]` when $n\ge4$;
- two 4-coins: `f[n-8]` when $n\ge8$.

Adding these disjoint cases enforces the limit exactly.

**Unbounded coin-change DP**

`f[0] = 1` represents the one way to make zero: choose no unlimited coins.

For each coin `x` in `[1,2,6]`, sums are processed upward from $x$ to $n$:

`f[j] += f[j-x]`.

Every combination counted in `f[j-x]` can receive one more $x$ to make $j$.

Processing coins in a fixed outer order ensures combinations rather than permutations. A multiset using 1 and 2 is created when processing 2, regardless of how those coins could be arranged.

Ascending sums allow the same coin to be reused indefinitely because `f[j-x]` may already include that coin from the current outer iteration.

**Example n = 4**

Unlimited DP counts:

- four 1s;
- two 1s and one 2;
- two 2s.

That is `f[4] = 3`. One 4-coin contributes `f[0]=1`. Two 4-coins are impossible. Total is 4.

For $n=12$, the three cases cover 0, 1, or 2 value-4 coins; no case with three is added, so invalid `[4,4,4]` is excluded.


Standard coin DP invariant says after processing first $p$ unlimited denominations, `f[s]` counts each multiset using those denominations exactly once. The upward transition partitions combinations by whether they use an additional current coin.

Every legal full combination has a unique number $c\in\{0,1,2\}$ of 4-coins. Removing them leaves an unlimited-coin combination summing to $n-4c$, counted by the corresponding `f` entry. Conversely, adding $c$ 4-coins to such a combination is legal. This bijection proves the final sum.

**Relation to the manifest**

The manifest describes a closed-form arithmetic progression for denominations 1, 2, and 6 and claims $O(1)$ resources. The exact source allocates an $n+1$ DP array and loops through it for three coins. Its actual complexity is linear.

**Modulo**

Every DP update and each final addition is reduced modulo $10^9+7$. Modular addition preserves the requested final residue and prevents large counts.

**Why the three 4-coin cases do not overlap**

A coin combination has a definite number of value-4 coins. It cannot belong to both the zero-4 and one-4 cases, for example. This makes ordinary addition correct; no inclusion-exclusion is needed.

The residual unlimited combination may itself contain coins summing to 4 or 8, but those are values 1, 2, and 6, not additional value-4 coins. Coin identity by denomination keeps the cases distinct.

**Detailed DP trace**

For target 6, after processing coin 1, every sum has exactly one representation. Processing coin 2 adds representations with one or more 2s: `f[2]` gains `f[0]`, `f[4]` gains current `f[2]`, and so forth. Processing coin 6 adds one new representation to `f[6]` from `f[0]`.

The current-iteration use of updated `f[j-x]` is intentional. At $j=4$ for coin 2, `f[2]` already includes a 2, allowing combination `[2,2]`. A descending loop would suppress this valid unlimited reuse.

**Why limited 4 is handled afterward**

Running ordinary ascending coin DP with denomination 4 would allow three, four, or arbitrarily many copies. Adding one and two fixed residual cases is simpler than introducing a bounded-count dimension and makes the maximum of two explicit.

**Order-independence proof**

Every unlimited combination has a largest denomination in the fixed processing order. It is first created when that denomination is processed, by extending a combination of the residual sum using only denominations no larger in the order. No later permutation of the same multiset creates another entry, so arrangements are not overcounted.

## Complexity detail

Each of three unlimited coins scans at most $n$ sums, so time is $O(n)$. The fixed factor three does not change the bound.

Array `f` has $n+1$ entries, giving $O(n)$ auxiliary space.

This contradicts the manifest's $O(1)$ time and space, which apply only to its described formula, not this code.

The output is one integer.

## Alternatives and edge cases

- **Closed-form counting:** Count solutions to $a+2b+6c=s$ arithmetically for the three residual targets, matching the manifest.
- **Bounded-coin DP including 4:** Add a dimension or process two individual 4-coins in descending sums; more general but unnecessary.
- **Process sums downward for unlimited coins:** Incorrect because it would allow each denomination only once.
- **Process coins inside sums:** It can count different orders as distinct, violating the statement.
- **n below 4:** Only `f[n]` contributes.
- **n from 4 through 7:** Zero- and one-4 cases contribute.
- **n at least 8:** All three allowed counts are considered.
- **Coin value 1:** Guarantees every target has at least one combination.
- **Zero residual:** `f[0]=1` correctly represents using only the selected 4-coins.
- **Three 4-coins:** Never represented.
- **Modulo timing:** Per-update reduction is algebraically safe.
- **Order independence:** Fixed outer denomination order is essential.
