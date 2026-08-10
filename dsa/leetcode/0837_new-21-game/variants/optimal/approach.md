## General

**Define the probability from a current score**

Let `dfs(i)` be the probability that Alice eventually stops with at most `n` points, given that she currently has exactly `i` points.

This state is sufficient because future draws are independent and uniformly distributed. How Alice reached `i` does not affect what can happen next.

The requested answer is `dfs(0)` because Alice begins with zero points.

**Terminal scores**

Alice stops drawing as soon as `i >= k`. At that point:

- if `i <= n`, the game is successful and `dfs(i) = 1`;
- if `i > n`, it is unsuccessful and `dfs(i) = 0`.

The code combines these through `return int(i <= n)`. The Boolean converts to one or zero.

The constraint `k <= n` means reaching the stopping threshold is not automatically a failure. Only overshooting `n` is.

**The direct recurrence**

When `i < k`, Alice draws one of `1,2,\ldots,maxPts` with equal probability. Writing `W = maxPts`, total probability gives:

$$
\operatorname{dfs}(i)
=\frac{1}{W}\sum_{x=1}^{W}\operatorname{dfs}(i+x).
$$

A straightforward memoized implementation would sum `W` terms for each of up to `k` drawing states, taking `O(kW)` time. The exact source derives a sliding-window recurrence that calculates each state in constant time.

**Base drawing state `k-1`**

At score `k-1`, one more draw always stops the game because even the smallest draw reaches `k`. Final scores range uniformly from `k` through `k+W-1`.

Successful draws end no higher than `n`. The number of successful outcomes is:

$$
\min(n-k+1,W).
$$

The term `n-k+1` counts integers from `k` through `n` inclusively, while the minimum prevents counting more than the `W` possible draws.

Therefore:

$$
\operatorname{dfs}(k-1)
=\frac{\min(n-k+1,W)}{W}.
$$

The special case in the code supplies this exact starting probability for the backward recurrence.

**Derive the constant-time neighboring-state formula**

For `i < k-1`, write the direct windows for two adjacent states:

$$
\operatorname{dfs}(i)
=\frac{\operatorname{dfs}(i+1)+\operatorname{dfs}(i+2)+\cdots+\operatorname{dfs}(i+W)}{W},
$$

$$
\operatorname{dfs}(i+1)
=\frac{\operatorname{dfs}(i+2)+\cdots+\operatorname{dfs}(i+W)+\operatorname{dfs}(i+W+1)}{W}.
$$

The windows share all middle terms. Subtracting the second equation from the first leaves only the value entering on the left and the value leaving on the right:

$$
\operatorname{dfs}(i)-\operatorname{dfs}(i+1)
=\frac{\operatorname{dfs}(i+1)-\operatorname{dfs}(i+W+1)}{W}.
$$

Rearranging:

$$
\operatorname{dfs}(i)
=\operatorname{dfs}(i+1)
+\frac{\operatorname{dfs}(i+1)-\operatorname{dfs}(i+W+1)}{W}.
$$

This is exactly:

`dfs(i + 1) + (dfs(i + 1) - dfs(i + maxPts + 1)) / maxPts`.

It replaces a sum of `W` probabilities with two cached probability lookups and constant arithmetic.

**Why recursion evaluates states in a usable order**

To compute `dfs(i)`, the expression first asks for `dfs(i+1)`. Repeatedly following that dependency reaches `dfs(k-1)`, whose direct formula is known.

As recursion unwinds toward zero, adjacent values become cached. The farther state `dfs(i+W+1)` is either terminal because it is at least `k`, or is a later drawing state that the preceding recursion has already computed or can compute without cycling.

`@cache` ensures each integer state is evaluated once even if referenced from multiple formulas.

**Example with one draw**

For `n=6`, `k=1`, and `W=10`, the initial score zero equals `k-1`. Successful final scores are 1 through 6, six of the ten equally likely draws. The base drawing formula returns

$$
\frac{\min(6-1+1,10)}{10}=\frac6{10}=0.6.
$$

For `n=10` with the same `k` and `W`, all ten outcomes are within the bound, so the result is 1.

**The `k=0` case**

When `k=0`, Alice begins with a score already at least `k` and draws nothing. Because the constraints also give `n >= 0`, `dfs(0)` enters the terminal branch and returns one. The `k-1` branch is never reached.

**Why the probability is correct**

Terminal states return the exact success indicator. The `k-1` formula explicitly counts its equally likely terminal outcomes. For every earlier state, the sliding formula is an algebraic rearrangement of the direct law-of-total-probability recurrence, not an approximation.

Caching changes only evaluation cost. Therefore, induction backward from `k-1` establishes that every computed drawing-state probability, especially `dfs(0)`, is exact up to floating-point representation.

## Complexity detail

There are `O(k)` nonterminal score states from 0 through `k-1`. Each is computed once and performs constant work after cached calls. The recurrence may also request terminal states beyond `k`, but at most a constant number per drawing state, so total computed states are `O(k)`.

Because `k <= n`, time is `O(k)` and therefore within the manifest's `O(n)` bound.

The cache stores `O(k)` probabilities. Recursive depth can be `O(k)` because the first dependency follows `i+1` to `k-1`. Thus, auxiliary space is `O(k)`, also within `O(n)`.

Floating-point arithmetic is appropriate for probabilities, and the accepted tolerance is `10^{-5}`.

## Alternatives and edge cases

- **Direct memoized average:** Sum all `maxPts` next states for every `i`. It is correct but costs `O(k\cdot maxPts)` time.

- **Bottom-up sliding window:** Store probabilities in an array and maintain the window sum iteratively. It achieves the same linear time without recursion and can make evaluation order easier to see.

- **Immediate-certain shortcut:** If `n >= k-1+maxPts`, every possible stopping score is at most `n`, so the answer is one. The recurrence also obtains that result without a separate branch.

- **`k=0`:** Alice draws nothing and succeeds with probability one.

- **`k=1`:** One draw ends the game, so the special `k-1` formula answers directly.

- **`n=k`:** Only stopping exactly at `k` succeeds; larger terminal scores fail.

- **`maxPts=1`:** Draws are deterministic. The recurrence still works and produces probability zero or one.

- **Terminal score above `n`:** The base branch returns zero even though the score has validly stopped the game.

- **Independent uniform draws:** The averaging recurrence relies on all `W` outcomes having probability `1/W`.

- **Cache necessity:** Without it, neighboring formulas could recompute the same future states many times.

- **Recursion depth:** A large `k` can approach Python's recursion limit; an iterative sliding-window DP avoids that runtime concern while preserving the same mathematics.
