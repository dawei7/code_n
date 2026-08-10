## General

The exact solution counts divider choices with memoized recursion. It scans from left to right and tracks how many seats have already entered the currently open section.

**Define the state**

`dfs(i, k)` is the number of valid ways to finish processing the suffix beginning at index `i` when the current section already contains `k` seats. Only values zero, one, and two can be valid:

- `k = 0` means the section has no seat yet;
- `k = 1` means it needs one more seat;
- `k = 2` means the section is complete and a divider may now be placed before a later section begins.

The existing left boundary is represented by the initial call `dfs(0, 0)`.

**Handle the fixed right boundary**

If `i >= len(corridor)`, the scan has reached the divider already installed at the corridor’s right end. The final open section is valid exactly when it contains two seats. Therefore the base case returns `int(k == 2)`.

This one line rejects corridors with an incomplete final section and accepts one completed final section without requiring an additional divider after the last character.

**Consume the current character**

The statement `k += int(corridor[i] == "S")` adds one only for a seat. Plants do not change the section’s seat count.

If `k > 2`, the current section already contains too many seats. A divider should have been installed earlier, and no future decision can remove the extra seat. The state returns zero immediately.

**Consider not placing a divider**

The line `ans = dfs(i + 1, k)` always represents continuing the current section past the current character. This is valid provisionally for zero, one, or two seats. If a third seat is later reached without dividing, that descendant state returns zero.

Keeping the no-divider branch when `k == 2` is important because plants may follow the second seat. A divider may be placed after any of those plants, or no additional divider may be needed if this is the final section.

**Consider placing a divider**

Only when `k == 2` does the code add

`dfs(i + 1, 0)`.

This places a divider immediately after index `i` and begins a fresh section at the next position with zero seats. Installing a divider when `k` is zero or one would permanently close a section with too few seats, so no such branch exists.

The two branches are different valid layouts because they disagree about whether a divider occupies that boundary. Their counts are added and reduced modulo `10**9 + 7`.

If `i` is the final character and `k == 2`, the apparent divider branch reaches `dfs(n,0)` and contributes zero, while the no-divider branch reaches `dfs(n,2)` and contributes one. Thus the code does not double-count the fixed right boundary.

**Cache overlapping states**

Different earlier divider decisions can reach the same pair `(i,k)`. The `@cache` decorator evaluates each such state once and reuses its answer. There are only about $3(n+1)$ possible valid pairs, turning the branching recurrence from exponential into linear work.

After `dfs(0,0)` returns, the source calls `dfs.cache_clear()`. This releases cached entries before the method returns, preventing the nested function from retaining them longer than necessary. It does not change peak memory during computation.

**Why every division is counted once**

At each boundary after a processed character, the recursion either places no divider or, if the current section has exactly two seats, places one. A complete path therefore specifies a unique set of divider positions.

Every path accepted by the base case has closed earlier sections only at two seats and leaves the final section with exactly two, so it is valid. Conversely, any valid divider layout makes one matching branch choice at every scanned boundary and never triggers `k > 2`. It reaches the base case with `k == 2` and contributes one. Hence the count is exact.

For a gap of plants between the second seat of one section and the first seat of the next, the recursion may place the divider after the second seat or after any plant in the gap. These independent choices are what the more compact combinatorial solution multiplies; the memoized DP counts them directly.

## Complexity detail

Let $n$ be the corridor length. There are $O(n)$ indexes and only three relevant seat counts. Each cached state performs constant work and makes at most two cached calls, so total time is $O(n)$.

The cache stores $O(n)$ results. The recursive no-divider path can advance one character per call before unwinding, producing $O(n)$ call-stack depth. Peak auxiliary space is therefore $O(n)$, not the manifest’s $O(1)$.

The exact recursive implementation may exceed Python’s default recursion limit for a legal corridor of length $10^5$ unless the execution environment raises that limit. An iterative combinatorial scan avoids this practical issue.

## Alternatives and edge cases

- **Constant-space combinatorics:** Pair seats from left to right and multiply the number of boundaries between the second seat of one pair and the first seat of the next. This achieves $O(n)$ time and $O(1)$ space and matches the manifest, but it is not the exact source.
- **Three-state iterative DP:** Maintain counts for open sections containing zero, one, or two seats while scanning. This avoids recursion but requires careful transition interpretation.
- **Enumerate divider subsets:** There are exponentially many boundaries, so direct subset testing is infeasible.
- **No seats:** The final state has `k = 0` and returns zero; a section must contain exactly two seats.
- **Odd number of seats:** Some final or intermediate section cannot be paired, so no recursive path reaches a valid final state.
- **Exactly two seats:** There is one valid way: add no internal divider, regardless of how many plants surround or separate the seats.
- **Four adjacent seats:** The divider position between the second and third seats is forced, so there is one way.
- **Plants between seat pairs:** Every boundary after the previous pair’s second seat and before the next pair’s first seat is a distinct divider choice.
- **Leading plants:** They lie inside the first section and create no divider choice before the first seat because the left divider is fixed.
- **Trailing plants:** They lie inside the final section and do not create alternative required right boundaries; the right divider is fixed.
- **Third seat without divider:** The `k > 2` check rejects that branch immediately.
- **Modulo:** Counts are reduced whenever two branches are added, preserving the requested result.
- **Final-position divider branch:** It contributes zero for a reset section with no seats, so the existing fixed right boundary is not counted as optional.
- **Cache cleanup:** `cache_clear` reduces retained memory after computation but does not make peak auxiliary space constant.
- **Recursion depth:** Long plant runs or long no-divider paths can create a stack proportional to corridor length.
