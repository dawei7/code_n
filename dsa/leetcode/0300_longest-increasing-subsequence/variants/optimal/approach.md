## General

A subsequence keeps the original left-to-right order but may skip any elements. It does not need to occupy one continuous range of the array. “Strictly increasing” means every chosen value must be greater than the previously chosen value; equality is not allowed.

The exact source uses dynamic programming over the ending index. For each position, it asks which earlier increasing subsequence can legally accept the current value as its new last element.

The local manifest describes the faster binary-search tails method, but that method is not present in `solution.py`. This explanation follows the executable nested-loop dynamic program and gives its actual quadratic time bound.

**Choosing a state with a precise ending**

Let `f[i]` mean:

> the length of the longest strictly increasing subsequence whose final chosen element is exactly `nums[i]`.

Requiring the subsequence to end at `i` turns an open-ended global question into a state that can be extended. If an earlier state ends at index `j`, then `nums[i]` can be appended precisely when both of these facts hold:

- $j<i$, which is guaranteed because the inner loop considers only earlier indices;
- `nums[j] < nums[i]`, which preserves strict increase.

When those conditions hold, an increasing subsequence of length `f[j]` ending at `j` becomes one of length `f[j] + 1` ending at `i`.

**Why every state starts at one**

Every single array element is a valid strictly increasing subsequence by itself. It contains no adjacent chosen pair that could violate the order. Therefore, before considering any predecessor, the best known length ending at each index is one.

The source creates `f = [1] * n`. This initialization also handles an element that has no smaller value before it: no transition improves its state, so its best subsequence remains the one-element sequence containing only itself.

**The recurrence**

For each `i` from 1 through $n-1$, the inner loop checks every `j` from 0 through $i-1$. When `nums[j] < nums[i]`, the candidate length is `f[j] + 1`, and the source applies

`f[i] = max(f[i], f[j] + 1)`.

Formally,

$$
f[i]=1+\max_{\substack{0\le j<i\\\texttt{nums}[j]<\texttt{nums}[i]}} f[j]
$$

when at least one valid predecessor exists. If none exists, $f[i]=1$ from initialization.

Taking the maximum is necessary because a value may extend several different subsequences. The closest earlier smaller value is not necessarily part of the longest one. A more distant index may carry a much larger `f[j]`, so every earlier legal predecessor must be considered by this implementation.

**Why the outer loop runs left to right**

When computing `f[i]`, every needed state `f[j]` has $j<i$. The left-to-right outer loop guarantees that all of them are already final. There is no circular dependency and no need to revisit an earlier state after processing later values.

This is the dynamic-programming ordering: solve all smaller-index ending states before using them to solve the current ending state.

**A complete state trace**

For `nums = [10,9,2,5,3,7,101,18]`, the states become:

| Index `i` | Value | Best valid predecessor idea | `f[i]` |
| --- | --- | --- | --- |
| 0 | 10 | none | 1 |
| 1 | 9 | no earlier value is smaller | 1 |
| 2 | 2 | no earlier value is smaller | 1 |
| 3 | 5 | extend the subsequence ending at 2 | 2 |
| 4 | 3 | extend the subsequence ending at 2 | 2 |
| 5 | 7 | extend a length-2 sequence ending at 5 or 3 | 3 |
| 6 | 101 | extend the length-3 sequence ending at 7 | 4 |
| 7 | 18 | extend the length-3 sequence ending at 7 | 4 |

The final state array is `[1, 1, 1, 2, 2, 3, 4, 4]`. One length-four subsequence is `[2, 3, 7, 18]`; another valid choice replaces 18 with 101.

The table also shows that a state stores only a length, not the actual chosen elements. The problem asks only for the maximum length, so predecessor pointers are unnecessary.

**Why the answer is the maximum state, not the last state**

The longest increasing subsequence may end anywhere. A small value near the end of the array might be unable to extend the best earlier sequence, even though that earlier sequence remains a valid answer.

For example, in `[1, 2, 3, 0]`, the states are `[1, 2, 3, 1]`. Returning `f[-1]` would incorrectly give one. Returning `max(f)` gives three, the length of `[1, 2, 3]`.

The source therefore returns `max(f)`. The input is guaranteed nonempty, so this maximum is always defined.

**Why the recurrence finds every valid subsequence**

Consider an optimal increasing subsequence ending at index `i`. If it has length one, initialization already represents it. Otherwise, let `j` be the index of its second-to-last chosen element. Because it is a subsequence, $j<i$; because it is strictly increasing, `nums[j] < nums[i]`. The inner loop examines that exact `j`, and the best subsequence ending at `j` is at least as long as the prefix used by the chosen optimal subsequence. Thus, the transition can construct a candidate at least as long as any valid sequence ending at `i`.

Conversely, every transition appends `nums[i]` only to an earlier state with a smaller final value. It preserves index order and strict value order, so it never creates an invalid subsequence. Hence, after the inner loop, `f[i]` is exactly the best length ending at `i`. Taking the maximum over all possible final indices gives the global answer.

## Complexity detail

Let $n$ be the length of `nums`. For index `i`, the inner loop performs exactly $i$ predecessor checks. Across all indices, the number of checks is

$$
1+2+\cdots+(n-1)=\frac{n(n-1)}{2},
$$

which is $\Theta(n^2)$. Each successful check performs a constant-time addition and maximum operation, so the exact source's time complexity is $O(n^2)$.

The array `f` stores one integer for each input position, using $O(n)$ auxiliary space. The loop indices and temporary candidate values use $O(1)$ additional space. No recursion stack is used.

The local manifest's $O(n\log n)$ bound belongs to the binary-search replacement method described in the editorial, not to this nested-loop implementation. Accurately analyzing `solution.py` gives $O(n^2)$ time and $O(n)$ space.

## Alternatives and edge cases

- **Binary-search tails:** Maintain `tails[length - 1]` as the smallest attainable final value of an increasing subsequence of that length. Replace the first tail greater than or equal to each number using `bisect_left`. This achieves $O(n\log n)$ time and $O(n)$ space and matches the manifest summary, but it is not the exact source.
- **Top-down recursion with memoization:** Define the best length ending at or starting from an index and cache results. It can express the same $O(n^2)$ transitions but adds recursion overhead and stack usage.
- **Brute-force subsequence enumeration:** Include or exclude each element and test order. This explores up to $2^n$ choices and ignores the shared substructure captured by `f`.
- **Greedily keep the next larger value:** Taking the first available increase can leave an unnecessarily large tail and block useful later values. The dynamic program compares all legal predecessors rather than committing to one local choice.
- **Using `<=` in the transition:** That would compute a longest non-decreasing subsequence. The problem requires strict increase, so duplicates must not extend a state.
- **Returning `f[-1]`:** This considers only subsequences ending at the last input element. The correct answer is `max(f)` because the optimum may end earlier.
- **One element:** `f` is `[1]`, no loop transition is needed, and the answer is one.
- **All values equal:** No strict comparison succeeds. Every state remains one, so the result is one.
- **Strictly increasing input:** Every position extends the entire best prefix. The states become `1, 2, ..., n`, and the answer is $n$.
- **Strictly decreasing input:** No later value has a smaller predecessor. Every state remains one.
- **Negative values:** Comparisons, rather than magnitude assumptions or array indexing, drive the recurrence. Negative and positive integers work identically.
- **Repeated values separated by other elements:** Equal values may each start or participate in different candidate sequences, but one equal value cannot directly extend another because the comparison is strict.
- **Subsequence versus subarray:** Skipped indices are permitted. The transition from any earlier `j` to `i` deliberately allows gaps.
- **Length only:** If the actual subsequence were required, store a predecessor index whenever `f[i]` improves, then backtrack from the index of `max(f)`. The current contract does not require that extra state.
- **Maximum input length:** With $n=2500$, the quadratic method performs roughly three million pair checks, consistent with the given bound, even though the follow-up requests a faster asymptotic method.
