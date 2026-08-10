## General

**Represent vowels by ordered indices**

Map the five vowels to indices:

`0 -> a`, `1 -> e`, `2 -> i`, `3 -> o`, and `4 -> u`.

A lexicographically sorted vowel string corresponds exactly to a non-decreasing sequence of these indices. Once index `j` is chosen, every later position may use `j` again or any larger index, but never a smaller one.

The cached function `dfs(i, j)` counts sorted completions when:

- `i` positions have already been filled, and
- `j` is the smallest vowel index allowed at the next position.

The initial call `dfs(0, 0)` has filled no positions and permits all five vowels.

**Generate the next vowel without building strings**

If `i < n`, the generator iterates `k` through `range(j, 5)`. Each `k` represents choosing that vowel at position `i`. The recursive call `dfs(i + 1, k)` moves to the next position and makes `k` the new minimum, allowing repetition while forbidding a lexicographically smaller later vowel.

The counts from all legal first choices are disjoint and exhaustive, so `sum` adds them.

For example, after choosing `i`, represented by index 2, the next call has `j=2`. It may choose index 2, 3, or 4, corresponding to `i`, `o`, or `u`. It cannot choose `a` or `e` because that would make the string decrease.

The source counts paths through the choice tree; it never creates the actual character strings. This avoids output-sized storage.

**Base case**

When `i >= n`, all required positions have been filled. The expression returns 1 because the completed sequence represents one valid string.

There is no failure base case for `j` because `j` always remains between 0 and 4. Even after choosing `u`, `range(4,5)` contains index 4, so the recursion can fill every remaining position with `u`.

For $n=1$, the initial state sums five base-case calls, one for each vowel, and returns 5.

**Why memoization changes the cost**

Many choice prefixes lead to the same state. For example, several prefixes can arrive at position `i` with minimum allowed vowel index 3. The number of completions depends only on `i` and `j`, not on the exact prefix.

`@cache` stores the result for each pair. The first call computes it; later calls reuse it. This collapses an exponentially branching enumeration into at most about $5(n+1)$ distinct states.

**A recurrence view**

The function implements

$$
F(i,j)=\sum_{k=j}^{4}F(i+1,k),
$$

with $F(n,j)=1$.

At each state, the possible strings are partitioned by their next vowel. Choosing different `k` values creates different characters at position `i`, so these groups cannot overlap.

**Why the count is correct**

Every recursion path selects exactly one vowel index for each of the $n$ positions. Because each next choice is at least the previous minimum `j`, the resulting sequence is non-decreasing and the corresponding string is lexicographically sorted.

Conversely, take any sorted vowel string. Its vowel indices are non-decreasing. At position `i`, its actual next index lies in `range(j,5)`, so the recursion contains that choice. Following the string's indices reaches one base-case return. The path is unique because the character at each position fixes `k`.

Therefore recursion paths and valid strings are in one-to-one correspondence, and summing cached subproblem counts returns the exact total.

**Connection to combinations with repetition**

A sorted string is completely determined by how many times each vowel appears. If the five counts are non-negative and sum to $n$, their characters have only one sorted arrangement. The number of such count vectors is

$$
\binom{n+4}{4}.
$$

The recursion computes this same quantity through ordered choices rather than evaluating the formula directly.

## Complexity detail

There are $n+1$ possible `i` values and at most five `j` values. Each uncached non-base state sums at most five recursive results. Since five is constant, time complexity is $O(n)$.

The cache stores $O(5n)=O(n)$ integer results. Recursion depth is $n$, so the call stack also uses $O(n)$ space. Total auxiliary space is $O(n)$.

These are the exact checked-in implementation bounds. The manifest's `O(1)` time and space describe the closed-form binomial formula, not this cached recursion. With $n\le50$, the linear state count and recursion depth are small.

Python integer values grow with the answer, but the constraints keep the result modest; standard complexity analysis treats each arithmetic addition as constant time here.

## Alternatives and edge cases

- **Closed-form combination:** Return $\binom{n+4}{4}$, or $(n+1)(n+2)(n+3)(n+4)/24$. This is $O(1)$ under fixed-size arithmetic and matches the manifest.
- **Five-counter dynamic programming:** Start with one string ending in each vowel and repeatedly take prefix sums. This uses $O(1)$ space and $O(n)$ time.
- **Uncached backtracking:** It enumerates every valid string and many internal prefixes, doing far more work than needed when only the count is requested.
- **Length one:** The five single-vowel strings are all valid.
- **Repeated vowels:** Passing `k` rather than `k+1` allows the same vowel at the next position.
- **No decreasing choice:** `range(j,5)` excludes all vowel indices below the previously selected minimum.
- **All `u` characters:** State `j=4` always has one continuation at each remaining position, so this string is counted.
- **No modulo required:** The problem requests the exact count, and the source returns it directly.
- **Manifest mismatch:** The variant label does not make this exact recursive source constant-time; it computes $O(n)$ cached states.
- **Recursion depth:** At most 50 under the contract, comfortably below ordinary Python recursion limits.
