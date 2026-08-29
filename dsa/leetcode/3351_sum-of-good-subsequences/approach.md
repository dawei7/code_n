## General

**Summarize subsequences by their last value.** While scanning `nums` from left to right, every subsequence considered so far automatically respects index order. To decide whether the current value `x` can be appended, only the previous last value matters: the required absolute difference is one, so that endpoint must be either `x - 1` or `x + 1`.

The source maintains two dictionaries for each endpoint value $v$:

- `g[v]` is the number of good subsequences formed from processed positions that end at $v$.
- `f[v]` is the sum of the element sums of all those subsequences.

Both quantities are needed. The count says how many extensions are made, while the accumulated sum says how much existing content those extensions carry forward.

**Create the singleton ending at the current position.** A one-element subsequence is good by definition. The statements `f[x] += x` and `g[x] += 1` add the singleton containing this particular occurrence. Repeated equal values create different subsequences because they use different indices, so each occurrence must add its own singleton.

**Extend all subsequences ending at `x - 1`.** There are `g[x - 1]` such subsequences. Appending `x` creates the same number of new subsequences ending at `x`. Their old element sums total `f[x - 1]`. Each new subsequence also gains one copy of `x`, contributing another `g[x - 1] * x` across the group. Therefore the exact updates are

`f[x] += f[x - 1] + g[x - 1] * x`

and

`g[x] += g[x - 1]`.

**Extend all subsequences ending at `x + 1`.** The reasoning is symmetric. Those sequences also differ from `x` by exactly one at the new adjacent pair, so the source adds `f[x + 1] + g[x + 1] * x` to the total and `g[x + 1]` to the count.

The two predecessor groups are disjoint because no endpoint can simultaneously equal `x-1` and `x+1`. The singleton is disjoint from both because it has no earlier position. Thus these additions neither miss nor double-count a newly formed good subsequence.

**Why updating `f[x]` before reading the neighbors is safe.** The source performs the singleton update first, but then reads only keys `x-1` and `x+1`, never `x` itself. Consequently the current occurrence cannot accidentally extend itself, and existing subsequences ending at the same value are not extended because a difference of zero is invalid.

Earlier occurrences of `x` remain stored in `f[x]` and `g[x]`. The new contributions are accumulated alongside them so that a future value `x-1` or `x+1` can extend subsequences ending at any processed occurrence of `x`.

**Every good subsequence is counted exactly when its final index is processed.** Take any good subsequence. If it has one element, its final index creates it through the singleton update. Otherwise, remove its last element `x`. What remains is a previously processed good subsequence ending at either `x-1` or `x+1`, so exactly one neighbor transition reconstructs it. This also proves that every constructed subsequence is legal: the old part is good and the only new consecutive difference is exactly one.

At the end, endpoint groups partition all good subsequences by their last value. Summing every `f[v]` therefore produces the required sum of all elements across all good subsequences.

**Trace `nums = [1,2,1]`.** The first 1 creates count one and total one at endpoint 1. Processing 2 creates singleton `[2]` and extends `[1]` into `[1,2]`, so endpoint 2 has count two and total $2+3=5$. The final 1 creates its own singleton and extends both sequences ending at 2 into `[2,1]` and `[1,2,1]`. Together with the earlier endpoint-1 singleton, the endpoint totals ultimately sum to 14.

**The exact source delays modulo reduction, which materially changes its practical complexity.** The code defines `mod` but applies it only to `sum(f.values())` at the return. This is mathematically correct because reducing after exact addition gives the same final residue as reducing each update.

However, the number of good subsequences can be exponential. An alternating sequence such as 0, 1, 0, 1, and so on lets many existing subsequences extend at every step. Therefore `f` and `g` can contain integers with $\Theta(n)$ bits. Python preserves correctness with arbitrary-precision integers, but additions and multiplications are no longer constant-time and the stored values are no longer fixed-size words. The manifest's simple $O(n)$ time and $O(u)$ space bounds describe the standard implementation that reduces every update modulo $10^9+7$, not the full bit cost of this exact source.

## Complexity detail

Let $n$ be the array length and $u$ the number of distinct values, including the neighboring default-dictionary keys created by lookups. Under a unit-cost arithmetic model, each element performs a constant number of dictionary and arithmetic operations, so time is $O(n)$ and the dictionaries use $O(u)$ entries.

For the exact Python code, intermediate counts can reach $2^n$, requiring $O(n)$ bits per large value in the worst case. A conservative bit-complexity view allows up to $O(n^2)$ total bit work across the scan and $O(un)$ bits of dictionary payload. Applying `% mod` to every update would keep values below the modulus and restore the intended $O(n)$ fixed-word time and $O(u)$ fixed-word space.

## Alternatives and edge cases

- **Reduce every update modulo $10^9+7$:** This preserves the final residue and prevents the exact source's exponentially large intermediate integers.
- **Array-indexed states:** Because values are bounded, arrays can replace dictionaries, but allocate space proportional to the maximum value range rather than the values encountered.
- **Enumerate all subsequences:** There are $2^n-1$ nonempty subsequences, so direct generation is infeasible.
- **Single element:** It contributes its value once, including zero.
- **Zero singleton:** Its sum contribution is zero, but its count is essential because it can later extend to value one.
- **Duplicate values:** Different source indices define distinct subsequences even when their value sequences look identical.
- **Difference zero:** Existing states ending at `x` must not extend with another `x`.
- **Both neighbors present:** The `x-1` and `x+1` groups are both extended and are disjoint.
- **Negative dictionary key:** When `x=0`, reading `x-1` creates a harmless zero-valued `-1` entry in the `defaultdict`.
- **Upper-bound neighbor:** Looking up `x+1` beyond the input value bound is likewise harmless.
- **Order preservation:** Scanning left to right ensures every extension uses increasing indices without storing indices explicitly.
- **Final aggregation:** Summing endpoint totals is required; no single endpoint contains all good subsequences.
- **Modulo placement:** A final modulo is algebraically correct but computationally dangerous in Python for this recurrence.
- **Import requirement:** `defaultdict` and the `List` annotation must be available in the execution harness.
