## General

**Treat every valid answer as an increasing subset**

The available values are only 1 through 9, and each may be used at most once.
The order of numbers inside a combination does not create a different answer:
`[1, 2, 6]` and `[6, 1, 2]` describe the same chosen set. The exact solution
eliminates both repeated values and reordered duplicates by considering digits
in increasing order.

The recursive call `dfs(i, s)` means: digits smaller than `i` have already
received their final include-or-exclude decisions, `s` is the sum still needed,
and the shared list `t` contains the digits selected on the current path. The
only current candidate is `i`. Both recursive calls advance to `i + 1`, so a
chosen digit can never be chosen again, and every completed list in `t` is
strictly increasing.

Starting with `dfs(1, n)` means no digit has yet been decided, the complete
target sum remains, and `t` is empty.

**At each digit, explore the two exhaustive choices**

If the current state is still viable, the search first includes `i`:

1. Append `i` to `t`.
2. Call `dfs(i + 1, s - i)` because that amount has been paid toward the sum.
3. Pop `i` from `t` when the recursive branch returns.

The `pop` is the backtracking step. `t` is one mutable list shared by all
calls. Removing the included digit restores the list to exactly the state it
had before this choice, allowing the sibling branch to be evaluated correctly.
When a completed answer is stored, the source uses `t[:]` to copy the current
contents. Appending `t` itself would make every saved answer refer to the same
list and later pops would corrupt previously recorded results.

After restoring the path, the source explores the second choice with
`dfs(i + 1, s)`: exclude `i`, leave the remaining sum unchanged, and move to
the next digit. Include and exclude are the only possibilities for a value
that can be used at most once, so the two branches cover every subset.

**Recognize a solution as soon as the remaining sum reaches zero**

The first base case checks `s == 0`. If the current path also has exactly
`k` digits, it is copied into `ans`. Whether its length is correct or not, the
function then returns.

Returning immediately is safe because all available future digits are
positive. Once the remaining sum is zero, adding another digit would make the
chosen sum exceed `n`; exclusions would merely leave the same path and cannot
repair a wrong length. Thus a zero-sum path either is a complete answer now or
can never become one.

The order of this check before `len(t) >= k` is important for accepting a
solution that reaches both conditions at the same time. For example, after the
third digit of a required three-digit combination is included, the next call
has `s == 0` and `len(t) == k`; it must append the answer before the full-length
prune can reject further expansion.

**Three impossibility checks cut off a branch**

If the sum is not yet zero, the condition
`i > 9 or i > s or len(t) >= k` rejects the state for three separate reasons:

- `i > 9` means all legal digits have already been decided. A positive
  remaining sum cannot be formed without another candidate.
- `i > s` means the smallest still-available digit is already larger than the
  positive remaining sum. Every later digit is even larger, so including any
  of them would overshoot. Excluding them all would leave `s` positive.
- `len(t) >= k` means the required number of digits has already been selected,
  yet `s` is still positive. Any additional inclusion would violate the exact
  size requirement, and exclusions cannot reduce the remaining sum.

These tests do not discard a possible answer. They express conditions under
which no descendant can simultaneously reach sum zero and length `k`.

**Trace `k = 3` and `n = 9`**

The search begins at digit 1. Following include choices for 1 and 2 leaves
`t = [1, 2]` and remaining sum 6 at candidate 3. The DFS tries including 3,
then continues through decisions until that branch either exceeds the allowed
length or cannot reach the sum. Backtracking eventually excludes digits 3
through 5 and includes 6. The next call has `s = 0` and three selected digits,
so `[1, 2, 6]` is copied.

After returning, the shared path is restored and other choices are explored.
The same decision tree discovers `[1, 3, 5]` and `[2, 3, 4]`. It cannot produce
`[2, 1, 6]` because after deciding digit 1, every later call has `i >= 2`; the
search never moves backward. It also cannot reuse 3 because both the include
and exclude branches move from 3 to 4.

**Why every output is valid and unique**

An answer is appended only when its remaining sum is zero and its length is
exactly `k`. Subtracting a digit precisely when it is appended to `t` means
zero remainder is equivalent to the selected digits summing to `n`. Digits lie
between 1 and 9 because only those candidates can pass before the `i > 9`
prune. They are strictly increasing because `i` always advances, so no digit
is repeated.

Every subset of `{1,...,9}` corresponds to one unique sequence of nine binary
decisions: include each member and exclude each nonmember. The DFS contains
that path unless a prune proves it cannot become valid. Therefore every valid
size-`k`, sum-`n` subset reaches the success base case. Because two different
decision sequences cannot produce the same subset, no combination is emitted
twice.

The output order follows depth-first include-before-exclude traversal and is
not semantically important.

## Complexity detail

There are nine possible digits, each with an include or exclude choice, so a
simple upper bound is $2^9$ decision paths and $O(2^9)$ visited states. Copying
one completed combination costs $O(k)$. Using the manifest's output-aware
upper bound, time is $O(2^9k)$. The pruning conditions often visit far fewer
states, and the numeric universe is a fixed constant in this problem.

The active list `t` contains at most $k$ digits. The recursive stack can follow
candidate decisions through the digits 1 through 9, so its depth is at most 10;
under this fixed domain that is constant, while a generalized $D$-digit version
would use $O(D)$ stack space. Following the manifest's problem-bound notation,
working path space is $O(k)$, with a fixed additional recursion bound. The
returned collection can hold up to $\binom{9}{k}$ lists of length $k$, requiring
$O(k\binom{9}{k})$ output space, which is normally excluded from auxiliary
space.

## Alternatives and edge cases

- **Increasing-candidate loop backtracking:** At each depth, loop from a `start` digit through 9 and recurse after choosing one. It visits combinations directly instead of representing explicit exclusion branches and has the same uniqueness principle.
- **Enumerate all bitmasks:** Each mask from 0 through $2^9-1$ describes one subset. Check its bit count and sum, then emit matching masks. It is compact but less naturally pruned and still examines all 512 subsets.
- **Combination library:** Generate `combinations(range(1, 10), k)` and filter by sum. It is concise and examines exactly $\binom{9}{k}$ candidates, but hides the search reasoning an interview solution may be expected to demonstrate.
- **Minimum/maximum achievable-sum pruning:** With `r = k - len(t)` slots remaining, compare `s` against the sum of the next `r` smallest candidates and the `r` largest available digits. This can reject branches earlier but adds arithmetic not present in the exact source.
- **Target below the minimum possible sum:** For `k = 4, n = 1`, even `1+2+3+4` is too large. The exact `i > s` and length checks eventually reject all paths and return `[]`.
- **Target above 45:** The sum of all legal digits is 45, so no answer exists. The finite-candidate check eventually ends every path; an upfront bound could return earlier but is unnecessary.
- **`k = 9`:** The only possible selection is all digits, whose sum is 45. Thus only `n = 45` can produce an answer.
- **Reaching the target too early:** If `s == 0` with fewer than `k` digits, the branch returns rather than adding positive digits that would overshoot.
- **Filling all slots too early:** If `len(t) == k` while `s > 0`, the branch returns because adding another digit would violate the required size.
- **No duplicate-output set:** Strictly increasing construction makes permutations impossible, so `ans` can remain a list and needs no deduplication pass.
- **Input preservation:** `k` and `n` are integers and are never mutated. The changing state is confined to local parameters, `t`, and `ans`.
