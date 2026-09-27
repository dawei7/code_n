# Guided Example: Maximum Number of Non-overlapping Palindrome Substrings

## 1. Selecting intervals, not palindromes

Every admissible choice is an interval of the string. A substring `s[i..j]` may
be selected only if it is a palindrome and its length is at least $k$. Write the
family of admissible intervals as

$$
\mathcal{F} = \{\, [i, j] : \texttt{s}[i..j] \text{ is a palindrome},\; j - i + 1 \ge k \,\}.
$$

Two intervals in a selection must be **disjoint**, and the objective is the
**cardinality** of the selection. The task is therefore a maximum-cardinality
interval-selection problem whose candidate set $\mathcal{F}$ happens to be
defined by a palindrome predicate. This reframing matters: it separates the
string work (which intervals belong to $\mathcal{F}$) from the combinatorial
work (which disjoint subfamily is largest), and it exposes the two classic tools
for the second half — a suffix dynamic program and an earliest-finish greedy.

For the official instance `s = "abaccdbbd"` with $k = 3$, the palindrome
shortlist is short, and the two admissible intervals are already separated by
the gap `cc`:

| Interval $[i,j]$ | Text | Length | Palindrome? | Length $\ge k = 3$? | In $\mathcal{F}$? |
|---|---|---|---|---|---|
| `[0,2]` | `"aba"` | 3 | yes | yes | **yes** |
| `[3,4]` | `"cc"` | 2 | yes | no | no |
| `[5,8]` | `"dbbd"` | 4 | yes | yes | **yes** |
| `[6,7]` | `"bb"` | 2 | yes | no | no |
| `[4,8]` | `"cdbbd"` | 5 | no ($c \ne d$) | — | no |
| `[1,5]` | `"baccd"` | 5 | no ($b \ne d$) | — | no |

Because `[0,2]` and `[5,8]` are disjoint, the answer is $2$. The interesting
work is not this instance but the machinery that can decide *any* instance,
including ones where a tempting early interval must be refused.

## 2. Growing a palindrome from its interior

A substring is a palindrome exactly when its two ends match and the interior
between them is itself a palindrome. Let $P(i,j)$ be the predicate "`s[i..j]` is a
palindrome". Then for $i < j$

$$
P(i,j) \;=\; \bigl(\texttt{s}[i] = \texttt{s}[j]\bigr) \;\wedge\; P(i+1, j-1),
$$

and $P(i,i)$ is true for every single character. The recurrence bottoms out at
an **empty** interior: when $j = i+1$ the window `s[i+1..i]` is empty and is
declared a palindrome by convention. That convention is exactly what makes
two-character palindromes work, and it is the base case that a careless
initialization destroys.

Evaluating the recurrence for the official instance, from the shortest windows
outward:

| Window $[i,j]$ | `s[i]`, `s[j]` | Interior `s[i+1..j-1]` | Interior is a palindrome? | $P(i,j)$ |
|---|---|---|---|---|
| `[3,4]` | `c`, `c` | `""` (empty) | yes, by convention | yes |
| `[6,7]` | `b`, `b` | `""` (empty) | yes, by convention | yes |
| `[5,8]` | `d`, `d` | `"bb"` = `[6,7]` | yes | yes |
| `[0,2]` | `a`, `a` | `"b"` = `[1,1]` | yes, single character | yes |
| `[2,4]` | `a`, `c` | `"c"` = `[3,3]` | yes, but ends differ | no |
| `[1,4]` | `b`, `c` | `"ac"` = `[2,3]` | no | no |
| `[1,5]` | `b`, `d` | `"acc"` = `[2,4]` | no | no |
| `[4,8]` | `c`, `d` | `"dbb"` = `[5,7]` | no | no |
| `[0,4]` | `a`, `c` | `"bac"` = `[1,3]` | no | no |

The dependency structure is a diagonal sweep: $P(i,j)$ reads $P(i+1,j-1)$, one
step inward, so windows must be processed in order of increasing length. Every
window of the instance is decided this way, in $O(n^2)$ predicates for $n$
characters, after which membership in $\mathcal{F}$ is a table lookup.

## 3. The suffix state and its skip-or-take recurrence

For each position $i$ define

$$
B(i) = \text{the maximum number of pairwise disjoint intervals of } \mathcal{F}
\text{ wholly contained in } \texttt{s}[i..n-1],
$$

with $B(n) = 0$ past the end of the string. The first interval of an optimal
selection either avoids position $i$ entirely or starts exactly at $i$ — if it
started later, it would avoid $i$ as well. Splitting on that choice gives

$$
B(i) = \max\Bigl(\; B(i+1),\;\; \max_{\substack{j \ge i+k-1 \\ P(i,j)}} \bigl(1 + B(j+1)\bigr) \;\Bigr).
$$

The first branch is the **skip** transition: position $i$ is left unused. The
second is the **take** transition: an admissible interval $[i,j]$ is consumed,
and the remaining selection lives in the suffix that starts at $j+1$. The answer
is $B(0)$.

The skip branch is not a formality. It is the difference between a correct
algorithm and a plausible but wrong one. Consider `s = "abxbaaa"` with $k = 3$:
the only intervals of $\mathcal{F}$ are `[0,4]` (`"abxba"`), `[1,3]` (`"bxb"`)
and `[4,6]` (`"aaa"`). Position $0$ *does* have an admissible interval, yet
$B(0) = B(1) = 2$ by skipping it and instead taking `[1,3]` together with
`[4,6]`. Taking `[0,4]` instead reaches only $1 + B(5) = 1$. A scanner that
commits to the first interval it finds at the earliest possible start returns
$1$ and is wrong; the recursion, which compares skip against take, returns $2$.

## 4. Worked trace of the official instance `s = "abaccdbbd"`, `k = 3`

Let $n = 9$. Candidate intervals are `[0,2]` and `[5,8]` from Section 1, so the
only positions with a non-empty take branch are $i = 0$ (end $j = 2$) and
$i = 5$ (end $j = 8$). Fill the suffix table from the right end leftward.

| $i$ | `s[i]` | Take ends $j$ with $P(i,j)$ and $j \ge i+2$ | Take branch $1 + B(j+1)$ | Skip branch $B(i+1)$ | $B(i)$ | Decision |
|---|---|---|---|---|---|---|
| 9 | — | none (past the end) | — | — | 0 | base case $B(9) = 0$ |
| 8 | `d` | none | — | 0 | 0 | skip |
| 7 | `b` | none | — | 0 | 0 | skip |
| 6 | `b` | none | — | 0 | 0 | skip |
| 5 | `d` | 8, via `"dbbd"` | $1 + B(9) = 1$ | $B(6) = 0$ | **1** | take `[5,8]` |
| 4 | `c` | none | — | $B(5) = 1$ | 1 | skip to reach `[5,8]` |
| 3 | `c` | none | — | $B(4) = 1$ | 1 | skip |
| 2 | `a` | none | — | $B(3) = 1$ | 1 | skip |
| 1 | `b` | none | — | $B(2) = 1$ | 1 | skip |
| 0 | `a` | 2, via `"aba"` | $1 + B(3) = 2$ | $B(1) = 1$ | **2** | take `[0,2]` |

Reading the table top to bottom shows the mechanism: the single interval
`[5,8]` establishes a *floor* of $1$ for every suffix that reaches it, so
$B(1) = 1$ even though positions $1$ through $4$ contribute nothing. At position
$0$ the take branch adds the disjoint interval `[0,2]` on top of that floor and
wins with $2$. The final answer $B(0) = 2$ selects exactly `"aba"` and
`"dbbd"`, matching the official explanation.

## 5. Why the reasoning is correct

**Invariant of the palindrome table.** After the diagonal sweep, the entry for
$[i,j]$ holds the truth value of "`s[i..j]` is a palindrome". The sweep is sound
because each entry is computed from already-finalized shorter windows, and it is
complete because the recurrence holds for every window with $i < j$ and the
bases $j = i$ (single character) and $j = i - 1$ (empty) are handled.

**Invariant of the suffix table.** When $B(i)$ is written, every entry
$B(i')$ with $i' > i$ already holds the true optimum for its suffix. The
recurrence then partitions all selections inside `s[i..n-1]` by whether they use
position $i$, so $B(i)$ is an upper bound on both branches and the maximum of the
two.

**Soundness.** Every value counted by the recursion corresponds to a real,
constructible selection: the take branch commits to one admissible interval and
then recurses strictly to its right, so the chosen intervals are pairwise
disjoint by construction, and the skip branch chooses nothing and keeps all
options.

**Completeness by induction on $n - i$.** Let $S^{*}$ be an optimal selection
inside `s[i..n-1]` with $|S^{*}| = B^{*}$. If $S^{*}$ contains no interval
starting at $i$, then $S^{*}$ is a valid selection inside `s[i+1..n-1]`, so
$|S^{*}| \le B(i+1) \le B(i)$ by the inductive hypothesis. Otherwise $S^{*}$
contains some interval $[i,j] \in \mathcal{F}$; the remaining intervals of
$S^{*}$ are disjoint from it and therefore lie in `s[j+1..n-1]`, so $|S^{*}| \le
1 + B(j+1) \le B(i)$, where the last step is the take branch of the recurrence
at that same $j$. Hence $B(i) \ge B^{*}$, and since soundness gives $B(i) \le
B^{*}$, the table value is exactly optimal.

**Shortest-end dominance.** For a fixed start $i$, only the **smallest**
admissible end $j^{*}(i)$ can ever be needed, because $B$ is non-increasing in
its index (a longer suffix has at least as many options) and therefore
$B(j+1) \ge B(j'+1)$ whenever $j \le j'$. Replacing any chosen interval $[i,j']$
by $[i,j^{*}]$ keeps it admissible, keeps all other chosen intervals disjoint,
and cannot lower the count. This is the exchange argument behind the greedy
method in Section 7; the canonical recursion enumerates every $j$ and so does not
depend on the argument, but the argument explains why the greedy is safe.

## 6. Boundary analysis and the traps the instances expose

| Instance | Input | Answer | Which mechanism decides it |
|---|---|---|---|
| Threshold $k = 1$ | `s = "a"`, `k = 1` | 1 | every single character is a palindrome, so $B$ takes every position |
| Repeated characters, $k = 2$ | `s = "aaaaa"`, `k = 2` | 2 | five characters hold two disjoint length-2 intervals with one leftover |
| Only a length $k{+}1$ window qualifies | `s = "ababa"`, `k = 4` | 1 | `"abab"` fails, `"ababa"` succeeds; a shortest-window check of exactly $k$ would find nothing |
| Nested palindromes overlap | `s = "aabbaa"`, `k = 3` | 1 | `[1,4]` = `"abba"` is nested inside `[0,5]` = `"aabbaa"`; they overlap so at most one is selectable |
| Two separated long palindromes | `s = "abcbaefggfe"`, `k = 4` | 2 | `[0,4]` and `[6,9]` are disjoint, so the long tail palindrome is not required |
| No qualifying interval | `s = "adbcda"`, `k = 2` | 0 | the string has no palindrome of length $\ge 2$ at all |
| Threshold equals the length | `s = "racecar"`, `k = 7` | 1 | only the whole string qualifies, and it is a palindrome |
| Nothing at the maximum threshold | `s = "abcdef"`, `k = 6` | 0 | the only candidate window `[0,5]` fails at $a \ne f$ |
| Earliest start is a trap | `s = "abxbaaa"`, `k = 3` | 2 | taking `[0,4]` blocks `[1,3]` and `[4,6]`; skipping position $0$ is strictly better |

Three traps deserve explicit statement. First, **`k` is a lower bound, not an
exact length**: `"aabbaa"` and `"ababa"` show that the decisive interval can be
much longer than $k$, so testing only windows of length exactly $k$ misses
answers. Second, **nesting counts as overlapping** even when one
interval strictly contains the other, which is why `"aabbaa"` returns $1$ rather
than $2$. Third, **the earliest admissible interval is not always the best
first move**: in `"abxbaaa"` the interval with the smallest start is the wrong
choice, whereas the interval with the smallest **end** (`[1,3]`) is right. Only
the end position, not the start, controls how much room remains.

## 7. Alternatives compared

| Method | Selection rule | Verified result on `"abaccdbbd"`, $k=3$ | Verified result on `"abxbaaa"`, $k=3$ | Time | Space |
|---|---|---|---|---|---|
| Suffix DP with skip-or-take (traced above) | maximize $B(i) = \max(B(i{+}1),\, 1+B(j{+}1))$ | 2 | 2 | $O(n^2)$ | $O(n^2)$ for the palindrome table |
| Earliest-finish greedy | sort all intervals of $\mathcal{F}$ by right end, accept each one whose start is past the last accepted end | 2 | 2 | $O(n^2)$ to enumerate, $O(n^2 \log n)$ to sort | $O(n^2)$ for the interval list |
| Left-to-right first-found scan | walk positions in order and take the first admissible interval found at each position | 2 | **1 (wrong)** | $O(n^2)$ | $O(n^2)$ |
| Brute force over subsets | test every subfamily of $\mathcal{F}$ for disjointness | 2 | 2 | exponential | exponential |
| Manacher plus greedy | compute all maximal palindromic radii in linear time, then run the earliest-finish greedy on derived intervals | 2 | 2 | $O(n)$ | $O(n)$ |

The earliest-finish greedy is optimal because every interval has unit weight:
the classic exchange argument replaces the first interval of an optimal
solution by the one with the smallest end and never loses a later choice. The
first-found scan looks similar but is not the same rule — it fixes the start
before the end — and the last row of Section 6 is its counterexample. The DP is
the safest of the correct methods because it never commits to a rule about
which interval to prefer: it merely compares skipping against taking and lets
the table decide.

## 8. Verification against the authored cases

| Case | `s` | `k` | Computed answer | Authored expectation |
|---|---|---|---|---|
| `sample-1` | `"abaccdbbd"` | 3 | 2 | 2 |
| `sample-2` | `"adbcda"` | 2 | 0 | 0 |
| `trial-single-character` | `"a"` | 1 | 1 | 1 |
| `trial-repeated-characters` | `"aaaaa"` | 2 | 2 | 2 |
| `trial-length-k-plus-one` | `"ababa"` | 4 | 1 | 1 |
| `trial-separated-long-palindromes` | `"abcbaefggfe"` | 4 | 2 | 2 |
| `trial-overlap-forbidden` | `"aabbaa"` | 3 | 1 | 1 |
| `trial-threshold-is-whole-string` | `"racecar"` | 7 | 1 | 1 |
| `trial-no-match-at-max-threshold` | `"abcdef"` | 6 | 0 | 0 |

## 9. Derived time and auxiliary-space complexity

Let $n = \texttt{s.length}$, and let $m = \lvert \mathcal{F} \rvert$ be the number
of admissible intervals. For a string of length $n$ there are
$\frac{n(n+1)}{2}$ substrings, so $m = O(n^2)$.

$$
T(n) = O(n^2), \qquad S_{\text{aux}}(n) = O(n^2)
$$

**Time.** The palindrome sweep fills $\frac{n(n-1)}{2}$ entries, each by a single
character comparison and one table read, so it is $O(n^2)$. The suffix recursion
has $n+1$ states; each state scans at most $n - i - k + 2$ right ends, so the
take branches total

$$
\sum_{i=0}^{n-1} \max(0,\, n - i - k + 1) \;\le\; \sum_{i=0}^{n-1}(n-i) = \frac{n(n+1)}{2} = O(n^2).
$$

Both phases are quadratic, so the total is $O(n^2)$; with $n \le 2000$ this is
about $2 \times 10^6$ palindrome predicates plus at most $2 \times 10^6$ take
branches. The alternative of testing every subfamily of $\mathcal{F}$ would be
exponential and is not viable at this size.

**Auxiliary space.** The dominant allocation is the palindrome predicate table
with one entry per window, $O(n^2)$; the memoized suffix values add $O(n)$ and
the recursion stack is $O(n)$ deep, both dominated. Hence auxiliary space is
$O(n^2)$, roughly $4 \times 10^6$ boolean entries at $n = 2000$. A Manacher-style
radius array would reduce the string analysis to $O(n)$, but the suffix DP still
needs its own state, and the greedy variant needs the interval list, so the
interval-selection structure — not the palindrome detection — sets the floor for
the methods compared in Section 7.
