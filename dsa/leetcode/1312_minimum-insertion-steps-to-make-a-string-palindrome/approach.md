## General

The exact Optimal solution defines a subproblem directly on a substring. `dfs(i, j)` means: the minimum number of insertions needed to make `s[i : j + 1]` a palindrome.

This state is sufficient because the decision at the two ends determines which smaller inner substring remains. The method never needs to construct the final palindrome; it only needs the minimum insertion count.

**Base case: zero or one character**

If `i >= j`, the substring contains at most one character. An empty string and a one-character string are already palindromes, so the method returns zero.

The `i > j` form occurs naturally after matching the two characters of a two-character substring and recursing inward. Treating both `i == j` and `i > j` with one condition keeps the recurrence simple.

**When the endpoint characters match**

If `s[i] == s[j]`, those two characters can serve as the matching outer pair of the final palindrome. They already satisfy each other, so no insertion is needed for them. The remaining work is exactly the inner substring:

`dfs(i + 1, j - 1)`.

Could inserting something around matching endpoints ever produce fewer insertions? No. Keeping the existing equal pair costs zero and leaves the smallest possible interior. Any solution that inserts an extra outer character spends at least one operation without removing the need to make the original interior palindromic.

For an already palindromic string such as `"zzazz"`, matching endpoints repeatedly move inward until a base case is reached, and every call returns zero.

**When the endpoint characters differ**

If `s[i] != s[j]`, the final palindrome must somehow give each endpoint a matching partner.

One choice is to preserve `s[i]` as the left outer character and insert another copy of it just after the current right boundary. That new character matches `s[i]`. The original `s[j]` remains inside, so the unresolved original interval becomes `[i + 1, j]`. This costs

`1 + dfs(i + 1, j)`.

The symmetric choice is to preserve `s[j]` as the right outer character and insert another copy just before the current left boundary. The remaining interval is `[i, j - 1]`, costing

`1 + dfs(i, j - 1)`.

The code combines these choices as

`1 + min(dfs(i + 1, j), dfs(i, j - 1))`.

Why are these two choices complete? In any palindrome containing all original characters in their original order, the unmatched left endpoint must eventually be paired with an inserted equal character on the right, or the unmatched right endpoint must be paired with an inserted equal character on the left. Inserting an unrelated character cannot resolve either mismatch and cannot improve the optimum. Taking the smaller recursive result therefore considers every useful first insertion.

**Following a mismatch**

Consider `s = "mbadm"`. The outer `m` characters match, so the problem reduces to `"bad"`. Its endpoints `b` and `d` differ.

The recurrence compares:

- insert `b` to match the left endpoint and solve `"ad"`, or
- insert `d` to match the right endpoint and solve `"ba"`.

Each of those two-character mismatches needs one more insertion. The inner `"bad"` therefore needs two insertions, and the matching outer `m` characters add none. The final answer is two.

The method returns only that number. Strings such as `"mbdadbm"` or `"mdbabdm"` demonstrate possible constructions, but recording the construction is unnecessary for the requested output.

**Why memoization matters**

Without caching, mismatching endpoints branch into two recursive calls, and many intervals are reached through several paths. For example, `dfs(i + 1, j - 1)` can arise after shrinking the left endpoint in one branch and the right endpoint in another.

`@cache` stores the result associated with each argument pair `(i, j)`. The first call solves the interval; every later call with the same indices returns the stored integer immediately. This converts an exponential recursion tree into a dynamic program over a quadratic number of intervals.

The cache is safe because `s` never changes. A pair `(i, j)` always refers to the same substring and therefore always has the same answer.

**Why the returned count is minimum**

For a base interval, zero is plainly optimal. Assume recursive answers for smaller intervals are optimal.

If endpoints match, using them together adds zero and leaves the optimal inner problem. If endpoints differ, every valid palindrome must make one of the two endpoint-matching insertions described above; the recurrence evaluates both and chooses the cheaper optimal remainder. By induction on interval length, every `dfs(i, j)` is optimal.

The outer call `dfs(0, len(s) - 1)` covers the complete string, so its value is the minimum number of insertions required.

## Complexity detail

Let $n$ be the string length. A cache state is an interval endpoint pair with $0 \leq i \leq j < n$, plus a small number of crossed base pairs. There are $O(n^2)$ possible states.

Each uncached state performs constant character comparisons, arithmetic, and at most two cached recursive calls. Total time is $O(n^2)$.

The memoization cache can store $O(n^2)$ integer results. The recursion stack can reach $O(n)$ depth because each call shrinks at least one boundary. Therefore, the exact source uses $O(n^2)$ auxiliary space overall, dominated by the cache.

This does not match the manifest's $O(n)$ space. A bottom-up longest-common-subsequence or interval DP can be row-compressed to $O(n)$ space, but the exact `@cache` implementation retains the quadratic state table. With $n \leq 500$, recursion depth is also bounded enough for typical Python limits, though recursion overhead remains real.

## Alternatives and edge cases

- **Longest palindromic subsequence:** The answer equals $n-\operatorname{LPS}(s)$ because characters outside a longest palindromic subsequence each need matching insertions. Computing LPS through LCS with the reversed string gives $O(n^2)$ time.
- **Row-compressed LCS:** Keeping only current and previous DP rows achieves $O(n^2)$ time and $O(n)$ space, matching the manifest rather than the exact source.
- **Bottom-up interval DP:** Fill substring lengths from one upward using the same endpoint recurrence. It avoids recursion but normally stores an $O(n^2)$ table.
- **Greedy endpoint choice:** Arbitrarily matching the left or right endpoint on a mismatch can miss the optimum. Both recursive possibilities must be compared.
- **Length one:** The initial call immediately returns zero.
- **Already a palindrome:** Every matching pair recurses inward without adding insertions, so the result is zero.
- **Two unequal characters:** Either character can be inserted beside the other, and the answer is one.
- **Repeated characters:** Equality is based on the current endpoints; internal repetitions are handled by their own subproblems.
- **Insertions only:** The recurrence never deletes or reorders an original character. Its conceptual inserted matches preserve original subsequence order.
- **No construction returned:** The cache stores counts, not decisions. Reconstructing one palindrome would require remembering which branch won.
- **Cache lifetime:** The nested cached function and its entries live for this method invocation and close over the immutable input string.
