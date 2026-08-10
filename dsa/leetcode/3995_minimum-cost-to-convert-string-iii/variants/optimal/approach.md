## General

**Disjoint rule ranges turn the transformation into a left-to-right partition.**  At first glance, repeatedly rewriting a string suggests a large search over many intermediate strings. The restriction on reused positions removes that difficulty. Once a rule uses an interval, no later rule may touch any position in that interval. Therefore:

- a position is either left unchanged, which is possible only when its source and target characters already agree; or
- it belongs to exactly one interval handled by exactly one rule.

The chosen rule intervals are pairwise disjoint. If they are sorted by their left endpoints, they divide the string into finalized rule intervals and unchanged gaps. There is no need to decide the chronological order in which the rules were applied, because operations on disjoint positions do not affect one another.

This observation also explains why a rule is matched against the original `source` rather than against a separately maintained current string. When a rule is applied to an interval, none of those positions can have been used earlier. Their characters are still the original source characters. After the replacement, those positions can never be changed again, so the replacement must already equal the corresponding target substring.

**Define a prefix state.**  Let `dp[i]` be the minimum cost needed to finalize positions `0` through `i - 1` so that this entire prefix equals `target[:i]`. Positions from `i` onward have not been used and still contain their original source characters.

The base case is

`dp[0] = 0`,

because the empty prefix needs no operations. Every other entry begins at a large sentinel value called `infinity`, meaning that the prefix has not yet been shown reachable.

The loop considers positions from left to right. If `dp[index]` is still infinite, there is no valid finalized prefix ending there, so no transition from that position can participate in a complete solution. The source skips it immediately.

At a reachable `index`, the next unresolved position has exactly two possible roles.

**Option one: leave one character unchanged.**  If

`source[index] == target[index]`,

the character already has its required final value. The algorithm may finalize it without paying anything:

`dp[index + 1] = min(dp[index + 1], dp[index])`.

If the two characters differ, this transition is forbidden. Merely moving past a mismatching character would make it impossible for the finalized prefix to equal the target.

**Option two: begin a rule at this position.**  For every prepared rule, let `pattern` and `replacement` have a common length, and set

`end = index + len(pattern)`.

The rule can create a transition from `index` to `end` only when all of the following hold:

- `end <= n`, so the rule's interval stays inside the string;
- `target.startswith(replacement, index)`, so the rule writes exactly the required final substring;
- at every offset, the pattern character is either `"*"` or equals `source[index + offset]`.

If all checks pass, this entire interval becomes final in one operation:

`dp[end] = min(dp[end], dp[index] + total_cost)`.

The use of `min` matters because several different partitions or rules may reach the same prefix length. Only the cheapest prefix needs to be retained; future intervals depend on the endpoint and untouched suffix, not on how that prefix was produced.

**Prepare each true application cost once.**  A rule's charge is its supplied base cost plus the number of wildcard characters in its pattern. That number does not depend on which characters the wildcards happen to match. The source therefore constructs `prepared` entries containing

`(pattern, replacement, cost + pattern.count("*"))`

before running the dynamic program. This avoids recounting the same wildcards at every possible starting index.

**Why these transitions describe every legal solution.**  Take any successful transformation and sort its disjoint rule intervals from left to right. Look at the first not-yet-finalized position.

- If no interval covers it, the position remains unchanged, so its source character must equal its target character. The zero-cost one-character transition represents it.
- If an interval covers it, that interval must begin at this position; otherwise an earlier uncovered position would have been skipped. Because the interval was unused before the rule, its pattern matches the original source segment. Because it cannot be changed afterward, its replacement equals the target segment. The corresponding rule transition represents it.

Repeating this argument converts every successful transformation into a path from `dp[0]` to `dp[n]` with the same cost.

Conversely, every dynamic-programming transition is legal. A character transition preserves an already-correct character. A rule transition matches an untouched source interval, writes the required target interval, and starts exactly after the previously finalized prefix, so its positions do not overlap earlier rule ranges. A path reaching `n` therefore gives a complete valid transformation with exactly the accumulated cost.

Together, these two directions show that `dp[n]` is the minimum possible total cost. If it remains infinite, no partition of the string into legal unchanged characters and rule intervals exists, and the source returns `-1`.

**Example of the prefix flow.**  For `source = "hello"` and `target = "world"`, the rule `"he" -> "wo"` can move `dp[0]` to `dp[2]` at cost `3`. From index `2`, the rule `"llo" -> "rld"` moves to `dp[5]` at an additional cost `4`. Thus `dp[5] = 7`. There is no need to materialize the intermediate string `"wollo"` because the two selected intervals, `[0, 2)` and `[2, 5)`, already describe the complete transformation.

For a wildcard pattern such as `"c*t"`, the matching loop checks the literal `c` and `t` against the source while accepting any character at the middle offset. The prepared cost adds one for that single wildcard.

## Complexity detail

Let:

- `n` be the common length of `source` and `target`;
- `R` be the number of rules;
- `L` be the maximum pattern length.

Preparing the rules counts wildcards in every pattern, taking `O(RL)` time in the worst case.

For each of up to `n` reachable prefix positions, the algorithm considers all `R` rules. Checking `startswith` can inspect up to `L` replacement characters, and checking the wildcard pattern can inspect up to `L` source characters. These are sequential checks, so their combined cost remains `O(L)` per rule rather than `O(L^2)`.

- Total time complexity is `O(nRL)`.
- Auxiliary space complexity is `O(n + R)`.

The `dp` array uses `n + 1` integers. The prepared list uses one tuple per rule and refers to the already-existing pattern and replacement strings rather than constructing expanded wildcard variants. The generator used by `all` holds only constant traversal state.

The sentinel `10**30` is safely larger than any legal answer. At most `n` positive-length rule applications can be disjoint. Each costs at most `1000 + 5`, so even a deliberately loose legal upper bound is only a few million when `n <= 5000`.

## Alternatives and edge cases

- **Search over complete intermediate strings:** Applying every matching rule in every order creates an enormous state graph. Disjointness means order is irrelevant, so prefix dynamic programming avoids that exponential search.
- **A used-position bitmask state:** Tracking which positions have been consumed is a faithful brute-force model, but it has up to `2^n` masks. Processing non-overlapping intervals from left to right makes the used prefix implicit in one index.
- **Shortest path interpretation:** Prefix lengths `0` through `n` form a directed acyclic graph. Unchanged characters and applicable rules are forward edges, and `dp` computes the shortest path in topological order. A general Dijkstra heap is unnecessary because every edge moves to a larger index.
- **Rule chaining on one interval:** Applying one rule and then another to the same characters is forbidden, even if the first replacement matches the second pattern. The source correctly offers only one rule transition for a finalized interval.
- **Overlapping rules:** Two individually matching rules cannot both be selected if their ranges overlap. Prefix transitions concatenate intervals, so overlap is impossible by construction.
- **Unchanged mismatching character:** A position may be unused, but it still must equal the target at the end. The zero-cost transition exists only when the source and target characters match.
- **Replacement matching:** Wildcards affect only the pattern. The replacement contains literal lowercase letters and must equal the target substring exactly.
- **Wildcard charge:** Each `"*"` adds one to the application cost regardless of which character it matches. Counting wildcards once per rule is sufficient.
- **Equal pattern and replacement lengths:** This guarantee keeps indices fixed. Without it, a one-dimensional prefix endpoint would not describe untouched suffix positions correctly.
- **Duplicate or competing rules:** Several rules may reach the same `end`. The `min` update automatically keeps the cheapest complete prefix.
- **Rules longer than the remaining suffix:** The `end > n` check rejects them before any character matching.
- **Impossible target:** If every possible path stops before `n`, `dp[n]` remains `infinity` and the method returns `-1`.
- **Already-equal strings:** The dynamic program can advance through every character at zero cost, so the result is `0` even if no rule is useful.
- **Short-circuit behavior:** `startswith` and `all` often stop at their first mismatch, improving practical speed, but the worst-case analysis must still allow all `L` characters to match.
