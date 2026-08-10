## General

**What is actually being counted**

The word “combination” in the title can be misleading. Here, order matters. For example, if `nums = [1, 2, 3]`, the sequences `(1, 3)` and `(3, 1)` are two different answers even though they contain the same values and have the same sum. A clearer mental model is therefore: count every ordered sequence whose elements come from `nums` and whose sum is exactly `target`. Each value may be used any number of times.

Trying to list every valid sequence would do far more work than the question requires. The number of sequences can grow very quickly, and many different partial choices lead to the same remaining sum. Dynamic programming avoids constructing the sequences themselves. It stores only how many sequences reach each possible subtotal.

**The state and why it is enough**

Let `f[i]` be the number of ordered sequences whose sum is exactly `i`. The final answer is then `f[target]`.

This state does not remember which values were used earlier. That information is unnecessary because every number in `nums` remains available after every choice. Once a sequence has reached subtotal `i - x`, appending `x` is always legal and creates a sequence with subtotal `i`. Consequently, the number of ways to finish at `i` depends only on counts for smaller subtotals, not on the detailed histories that produced them.

The solution creates `f = [1] + [0] * target`. Thus, `f[0] = 1`, while all positive subtotals initially have zero known sequences.

The value `f[0] = 1` represents the one empty sequence. It is not claiming that there is a nonempty way to choose numbers whose sum is zero. Rather, it provides the correct starting point for a one-element sequence. If `x` itself is an allowed value, then while computing `f[x]` the transition adds `f[x - x] = f[0] = 1`. That contribution is precisely the sequence `(x)`. If `f[0]` were zero, no sequence could ever begin, so every later count would incorrectly remain zero.

**Deriving the transition by choosing the final value**

Consider every valid sequence that sums to a positive subtotal `i`. It must have some final value `x` taken from `nums`. Removing that final value leaves an ordered sequence whose sum is `i - x`. Such a sequence is possible only when `i >= x`; otherwise the remaining sum would be negative.

For one fixed value `x`, there are exactly `f[i - x]` valid prefixes. Appending `x` to each prefix produces `f[i - x]` distinct sequences ending in `x`. The sets produced by different final values do not overlap, because a single sequence cannot have two different final elements. Therefore the counts may be added:

$$
f[i] = \sum_{x \in \texttt{nums},\ x \le i} f[i-x].
$$

That equation is implemented directly. The outer loop visits `i` from `1` through `target`. The inner loop examines every `x` in `nums`. When `i >= x`, it performs `f[i] += f[i - x]`.

The increasing order of `i` is essential. Every input number is positive, so `i - x < i`. Therefore, by the time the algorithm computes `f[i]`, every state it reads has already been completely calculated. There is no circular dependency and no need for recursion.

**Why the loop order counts ordered sequences**

The algorithm completes one destination subtotal before moving to the next. For a fixed `i`, it considers each possible final value. This means every arrangement of earlier values has already been included in `f[i - x]`, and appending `x` preserves that arrangement.

For `nums = [1, 2, 3]` and `target = 4`, the table develops as follows:

| Subtotal `i` | Contributions | `f[i]` |
|---:|---|---:|
| `0` | empty sequence | `1` |
| `1` | `f[0]` by appending `1` | `1` |
| `2` | `f[1]` by appending `1`, plus `f[0]` by appending `2` | `2` |
| `3` | `f[2]` by appending `1`, plus `f[1]` by appending `2`, plus `f[0]` by appending `3` | `4` |
| `4` | `f[3]` by appending `1`, plus `f[2]` by appending `2`, plus `f[1]` by appending `3` | `7` |

At subtotal `3`, for instance, appending `1` to the two sequences counted by `f[2]` gives `(1, 1, 1)` and `(2, 1)`. Appending `2` to the sequence counted by `f[1]` gives `(1, 2)`. Appending `3` to the empty sequence gives `(3)`. This demonstrates that the state remembers order through its already-counted prefixes even though it never stores those prefixes explicitly.

It is important that the subtotal loop is outside the `nums` loop. If the loops were reversed, all uses of one value would be processed together before the next value. That is the standard pattern for counting unordered coin selections, where `(1, 3)` and `(3, 1)` should collapse into one result. The exact solution instead asks, for each subtotal, “Which value comes last?” This is what keeps the two orders separate.

**Why every valid sequence is counted exactly once**

The claim follows by induction on the subtotal.

The base state is correct: `f[0] = 1` counts exactly the empty sequence. Assume that for every subtotal smaller than `i`, the stored value counts every valid ordered sequence for that subtotal exactly once.

Take any valid sequence summing to `i`, and call its last value `x`. After removing `x`, its prefix sums to `i - x`. By the induction assumption, that prefix occurs exactly once among the `f[i - x]` possibilities. When the inner loop processes this particular `x`, the algorithm appends `x` conceptually and counts the original sequence. Thus, no valid sequence is missed.

Conversely, every contribution added from `f[i - x]` corresponds to a valid prefix summing to `i - x`. Appending the allowed positive value `x` makes its sum exactly `i`, so the algorithm never counts an invalid sequence. A sequence cannot be counted under two different inner-loop choices because its final value is fixed. Within the same choice of `x`, it cannot be duplicated because its prefix was counted once by the induction assumption. Therefore `f[i]` is exact. Applying the argument through `i = target` proves that the returned value is the required answer.

## Complexity detail

Let $n$ be the number of elements in `nums`, and let $T$ be `target`.

The outer loop runs once for every subtotal from `1` through $T$. For each subtotal, the inner loop checks all $n$ values. The comparison `i >= x`, the array access, and the addition each take constant time. The total running time is therefore $O(n \cdot T)$. This bound includes values larger than the current subtotal: they still cost a constant-time check even though they do not cause an addition.

The array has $T+1$ entries, covering indices `0` through `target`, so the auxiliary space is $O(T)$. The algorithm does not store actual sequences, and the nested loops use only a few scalar variables beyond that table. Because the implementation is iterative, it also avoids a recursive call stack.

The statement guarantees that the final answer fits in a 32-bit integer. In Python, integers expand automatically, so intermediate additions are safe as well. In a fixed-width language, the problem’s guarantee supplies the required bound for the returned count, although the implementation should still use the language’s appropriate integer type consistently.

## Alternatives and edge cases

- **Top-down dynamic programming:** Define a memoized function for the number of sequences that sum to a remaining value, try every `x <= remain`, and recurse on `remain - x`. It uses the same recurrence and has the same $O(n \cdot T)$ time and $O(T)$ asymptotic space. The bottom-up version is preferable here because it avoids recursive-call overhead and makes the dependency order explicit.

- **Plain backtracking:** Recursively trying every possible next value without memoization can enumerate an exponential number of choice paths. Many paths ask for the answer to the same remaining sum, so repeating those calculations is unnecessary when only the count is requested.

- **Reversing the two loops:** Iterating through `nums` first and subtotals second solves a different counting problem: it counts unordered multisets of values. It would merge sequences such as `(1, 3)` and `(3, 1)`, so it must not be used for this contract.

- **Sorting `nums`:** Sorting would permit the inner loop to stop as soon as `x > i`. This may reduce some checks, but sorting is not required for correctness and does not improve the worst-case $O(n \cdot T)$ bound. The exact solution remains correct for any input order.

- **A value larger than `target`:** Such a value never satisfies `i >= x` for any computed subtotal and contributes nothing. For example, `nums = [9]` and `target = 3` leaves every positive table entry at zero, so the answer is correctly `0`.

- **Only one usable value:** If `nums = [x]`, the answer is `1` when `target` is a multiple of `x` and `0` otherwise. The recurrence naturally walks through those reachable multiples; repeated use of a value is allowed.

- **Distinct input values:** The contract says the elements of `nums` are unique. If the same value appeared twice, the inner loop would add the same family of sequences twice and overcount. The algorithm relies on the stated uniqueness guarantee rather than deduplicating the array.

- **Positive values are essential:** Positivity guarantees that every dependency `i - x` is a smaller subtotal and that every sequence has finite length. If zero were allowed, appending zero could produce infinitely many distinct sequences without changing the sum. If negative values were allowed, positive and negative cycles could likewise generate infinitely many sequences, and the table would no longer have a simple increasing dependency order.

- **Negative-number follow-up:** To make a version with negative values well-defined, the problem needs an additional restriction that prevents unlimited cycles. A common choice is to impose a maximum sequence length. The dynamic-programming state would then need another dimension, such as both the current sum and the number of elements used; the one-dimensional subtotal table alone would no longer be sufficient.

- **The empty sequence:** The public constraints make `target` positive, so the empty sequence is never returned as the final answer. It still must be counted internally at subtotal zero because it is the unique prefix from which every one-element sequence begins.
