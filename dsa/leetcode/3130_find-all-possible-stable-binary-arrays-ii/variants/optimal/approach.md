## General

**View stability as a bound on every equal-bit run**

The condition says that every subarray longer than `limit` must contain both bit values. This is equivalent to saying that no consecutive run of zeros or ones may have length greater than `limit`. A run of `limit + 1` equal bits is itself a forbidden subarray. If no such run exists, any longer subarray must cross a boundary between 0 and 1 and therefore contains both.

We must count arrays that use exactly `zero` zeros and `one` ones while respecting this run bound.

**Memoized state**

The exact Optimal solution uses the top-down function `dfs(i, j, k)`:

- $i$ is the exact number of zeros in the represented array;
- $j$ is the exact number of ones;
- $k$ is its last bit.

Consequently, `dfs(i,j,0)` and `dfs(i,j,1)` are disjoint categories. Their sum for the requested counts covers every possible nonempty final array.

The `@cache` decorator remembers each result. Many larger states ask for the same smaller counts, so caching changes the process from an exponential recursion tree into a dynamic program with a two-dimensional grid of states and two final-bit layers.

**Axis base cases**

When $i=0$, the array, if valid, consists entirely of $j$ ones. There is exactly one such array. It belongs to the ending-in-one category and is valid only when $j\le\texttt{limit}$. Therefore:

`int(k == 1 and j <= limit)`.

When $j=0$, the symmetric all-zero run is counted only for $k=0$ and $i\le\texttt{limit}$. These rules also prevent a state from pretending that an all-one array ends in zero or vice versa.

**Constant-time transition for an ending zero**

To construct an array counted by `dfs(i,j,0)`, remove its last zero. Its prefix has $i-1$ zeros and $j$ ones and may end in either bit. Ignoring the run limit for a moment gives

$$
\operatorname{dfs}(i-1,j,0)+\operatorname{dfs}(i-1,j,1).
$$

Appending zero fails only for prefixes whose trailing zero-run already has length exactly `limit`. There is a one immediately before that run because $j>0$. Delete those `limit` trailing zeros as well as the new zero being appended. What remains uses $i-\texttt{limit}-1$ zeros and $j$ ones and ends in 1. This is a one-to-one description of all forbidden extensions, so the recurrence subtracts

$$
\operatorname{dfs}(i-\texttt{limit}-1,j,1)
$$

whenever $i-\texttt{limit}-1\ge0$.

This subtraction is what removes a costly loop over every possible final run length. It is a sliding-window or inclusion-exclusion recurrence in disguise: add all one-step extensions, then remove exactly the extension that falls beyond the allowed window.

**Symmetric transition for an ending one**

Removing the final one gives either ending category at counts $(i,j-1)$. The extensions that create `limit + 1` trailing ones correspond exactly to states with $j-\texttt{limit}-1$ ones ending in zero. Hence:

$$
\operatorname{dfs}(i,j,1)
=\operatorname{dfs}(i,j-1,0)+\operatorname{dfs}(i,j-1,1)
-\operatorname{dfs}(i,j-\texttt{limit}-1,0),
$$

with no subtraction when the index would be negative.

Every accepted extension remains represented, and every newly overlong run is removed once. By induction on $i+j$, both state meanings are correct. Adding the two states at $(\texttt{zero},\texttt{one})$ therefore gives the complete count.

**Exact handling of the modulus**

The problem requests the result modulo $10^9+7$, but the exact function does not reduce cached states. It computes full Python integers and applies `% mod` only to the final sum. Exact integer arithmetic makes that mathematically correct:

$$
(a+b)\bmod M
$$

is the same whether intermediate additions and subtractions were reduced earlier or not. However, it is an important implementation distinction. Counts may have hundreds of digits at the ID 3130 limits, so retaining full values is less efficient than storing residues.

The final `dfs.cache_clear()` discards memo entries after the result has been obtained.

## Complexity detail

Let $z=\texttt{zero}$ and $o=\texttt{one}$. There are at most $2(z+1)(o+1)=O(zo)$ distinct states. Each state makes at most three cached subproblem accesses and a constant number of arithmetic operations. In the conventional unit-cost DP model, time is $O(zo)$.

The memo table contains $O(zo)$ integers. Recursion can follow one-unit decreases through a path of length $O(z+o)$, so the call stack uses another $O(z+o)$ space. The cache dominates, giving $O(zo)$ auxiliary space.

Two exact-code risks matter at the larger constraints $z,o\le1000$:

1. Standard Python commonly limits recursion to roughly one thousand nested calls. A dependency path can exceed that, and this source does not call `sys.setrecursionlimit`. It can therefore raise `RecursionError` for legal large inputs unless the judge environment raises the limit externally.
2. Arithmetic is performed on full exact counts. The cost of adding these integers grows with their bit length, so the strict bit-complexity can be greater than $O(zo)$ and memory can be much larger than a residue table.

The manifest's $O(zo)$ time and $O(zo)$ space are the intended DP bounds, but they assume constant-size modular values and a recursion environment capable of reaching all states. A bottom-up implementation with per-state modulo realizes those guarantees more robustly.

## Alternatives and edge cases

- **Bottom-up DP:** Fill `dp0` and `dp1` tables in increasing counts with the same recurrence. It removes the recursion-limit defect and naturally stores every value modulo $10^9+7$.
- **Rolling storage:** Dependencies jump back by `limit + 1` along one dimension, so careful rolling-window sums can reduce some storage, but the implementation becomes more subtle than the full table.
- **Explicit run-length state:** Record the final bit and current run length, then append only legal bits. This is easy to reason about but costs $O(zo\cdot\texttt{limit})$ states or transitions.
- **Alternating bounded compositions:** Count choices of positive zero-run and one-run lengths for every possible number of runs. It offers a combinatorial route but needs bounded-composition formulas and careful start/end cases.
- **`limit = 1`:** Only alternating arrays are stable. If the zero and one counts differ by more than one, the answer is zero; otherwise one or two starting-bit choices may work.
- **Very large `limit`:** If `limit` is at least both counts, every arrangement is stable because neither bit can form an excessive run.
- **Axis states:** When one bit count is zero, the only candidate is a single run, which is accepted only when its length is within the limit.
- **Negative recurrence index:** The code conditionally skips the subtraction instead of calling an invalid state. This represents the fact that too few equal bits exist to create an overlong suffix.
- **Modulo subtraction:** A bottom-up modular version must normalize negative residues. The exact Python version postpones modulo, so ordinary integer subtraction remains exact.
- **Recursion depth at 1000:** This is a material legal-input risk for the exact source, not merely a theoretical concern. Iteration is the dependable remedy.
- **I and II share the same source:** Although ID 3130 has much larger limits than ID 3129, the repository's exact Optimal solutions are identical. The algorithmic recurrence scales quadratically, while its practical recursion and big-integer issues become more serious here.
