## General

**Search candidate numbers in lexicographic order**

The exact solution uses backtracking rather than the linear greedy construction described by the manifest summary. It builds the answer from left to right, trying unused digits `1` through `9` in ascending order at every position. This traversal order is crucial: complete candidate strings are encountered in lexicographic order.

For equal-length strings made of digits, lexicographic order is determined by the first differing position. Trying the smallest possible first digit, then the smallest possible second digit under that prefix, and so on is precisely a depth-first enumeration from smallest to largest.

The first complete candidate satisfying the pattern is therefore the lexicographically smallest answer.

**Track the current prefix and used digits**

`t` is a list of digit characters forming the current prefix. A list supports efficient append and pop during recursion. When a complete answer is found, `''.join(t)` converts it to the required string.

`vis` is a Boolean array of length ten. Indices `1` through `9` represent whether each digit is already in `t`; index zero is unused. Before selecting digit `i`, the search checks `not vis[i]`. It marks the digit, appends it, explores, then unmarks and pops it. This restoration makes the same digit available in a different branch while still enforcing uniqueness within one candidate.

**Check only the newly created relation**

The recursion parameter `u` is the number of digits already placed, so it is also the index where the next digit will go. When `u > 0`, choosing `i` creates exactly one new adjacent pair between `t[-1]` and `i`. Earlier adjacent relations were already checked when those digits were appended.

If `pattern[u - 1] == 'I'`, the previous digit must be smaller. The branch is rejected when:

```python
int(t[-1]) >= i
```

If the symbol is `'D'`, the previous digit must be larger, so the branch is rejected when `int(t[-1]) <= i`.

Checking the constraint immediately prunes invalid prefixes. No extension can repair an already incorrect adjacent relation, so abandoning that branch is safe.

**Stop after the first full solution**

When `u == len(pattern) + 1`, the prefix has the required number of digits. Every adjacent relation has been validated, and uniqueness was enforced during selection. The function saves the joined string in nonlocal `ans`.

At the top of every recursive call, it checks:

```python
if ans:
    return
```

Once the first solution exists, later calls return without exploring larger candidates. Backtracking statements still restore `vis` and `t` while the successful recursion unwinds, but no new branches do substantive work.

The problem guarantees a solution because the pattern length is at most eight. There are at most nine required positions, and the distinct digits `1` through `9` can realize any sequence of increasing/decreasing comparisons, for example through the known run-reversal construction.

**Trace an all-decreasing pattern**

For `pattern = "DDD"`, trying first digit `1` fails immediately at the second position because no unused positive digit is smaller. The same happens for first digits `2` and `3` after exploring the limited descending prefixes they allow.

With first digit `4`, the ascending digit loop chooses the smallest legal continuation `3`, then `2`, then `1`. The complete candidate `"4321"` is valid. Any candidate beginning with `1`, `2`, or `3` has already been proven impossible, and every other valid candidate beginning with `4` is lexicographically no smaller than `4321`. Candidates beginning above `4` are larger at their first digit. Thus, stopping is correct.

**Why the first solution is globally smallest**

Depth-first search with ascending choices visits prefixes in lexicographic order. More formally, before exploring a prefix beginning with digit $d+1$, it completely explores every feasible prefix beginning with digit $d$. The same ordering holds recursively at every later position.

Pruning removes only prefixes that already violate uniqueness or their latest required comparison. Such a prefix cannot lead to a valid full number, so pruning never removes a legitimate answer.

Every valid answer corresponds to one path choosing its digits in order. Therefore, the first full path that survives all checks is the first valid string in lexicographic order. Saving it and halting returns exactly the requested minimum.

**Exact implementation versus the advertised greedy method**

The Optimal manifest describes emitting small digits and reversing runs of `D` in linear time. That is an asymptotically stronger equivalent construction. The shipped solution does not perform run reversal; it enumerates constrained digit permutations with early stopping. A faithful approach document must describe this backtracking behavior and its actual search complexity, while presenting the linear greedy form only as an alternative.

## Complexity detail

Let $L=\lvert\texttt{pattern}\rvert+1$, with $2\le L\le9$. At recursion depth $d$, an unconstrained search can have up to:

$$
P(9,d)=\frac{9!}{(9-d)!}
$$

distinct prefixes. An upper bound on visited search nodes is $\sum_{d=0}^{L}P(9,d)$. Thus, parameterized by the number of available digits, the exact backtracking algorithm has factorial/exponential worst-case search rather than $O(n)$ time. Pattern pruning and stopping at the first solution reduce actual work, and the fixed nine-digit domain makes the absolute search bounded.

Joining the successful length-$L$ prefix costs $O(L)$. The recursion stack and `t` use $O(L)$ space, while `vis` has fixed size ten. The exact auxiliary space is $O(L)$.

The manifest's $O(n)$ time and $O(n)$ space describe the run-reversal greedy alternative, not this exact implementation.

## Alternatives and edge cases

- **Reverse consecutive `D` runs:** Start with digits `1` through `n+1` and reverse the positions covered by each maximal decreasing run. This constructs the smallest answer in $O(n)$ time.
- **Stack-based greedy:** Push successive digits and flush the stack at each `I` or at the end. Popping reverses precisely the required decreasing segments.
- **Try all permutations then filter:** It is correct but misses the safe prefix pruning used by the exact DFS and performs much more work.
- **All `I` symbols:** The first path chooses `1, 2, ..., n+1` and succeeds without backtracking.
- **All `D` symbols:** Smaller starting digits fail until the smallest digit large enough to support the full descending run is tried.
- **Alternating symbols:** Constraint checks apply locally as each digit is appended; no special pattern form is needed.
- **Digit uniqueness:** `vis` prevents outputs such as `123414321` even if their adjacent comparisons appear suitable.
- **Maximum pattern length eight:** Exactly nine distinct digits are required, consuming the full allowed set.
- **First position:** With `u = 0` there is no prior digit or pattern relation, so every unused digit is structurally eligible.
- **Successful early exit:** `ans` stops all lexicographically larger branches after the first valid complete string is found.
