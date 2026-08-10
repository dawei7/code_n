## General

**The global minimum must be a lower value**

Each original value $a$ creates $a-k$ and $a+k$, separated by $2k$. Since $k>0$, the smaller member of every pair is its lower value.

After sorting `nums`, `nums[0]` cannot be a higher value: its corresponding lower value would be even smaller and would also appear. Therefore, it must pair with some later `nums[i]` as

$$
\texttt{nums[i]}-\texttt{nums[0]}=2k.
$$

The source tries every possible partner index `i`.

**Reject impossible candidate gaps**

The gap `d` must be positive because $k$ is positive, and it must be even because `d = 2k`.

Candidates with `d == 0` or odd `d` are skipped.

For a valid gap, the recovered original value for a pair $(low,high)$ is their midpoint:

$$
\frac{low+high}{2}.
$$

The source uses a right shift by one, `>> 1`, which is exact because the gap and hence the sum parity are compatible.

**Greedily pair the smallest unused value**

For one candidate `d`, `vis` marks elements already used as higher partners. `nums[i]` is initially marked because it pairs with `nums[0]`, and their midpoint begins `ans`.

`l` identifies the smallest remaining value not already consumed as a higher element. This value must be the lower member of its pair. Pairing it with anything other than `nums[l] + d` cannot fit the fixed candidate $k$.

`r` advances until the difference from `nums[l]` is at least `d`:

- if the difference is smaller, that position cannot be the required higher partner, so move right;
- if the first adequate difference is greater than `d` or no position remains, this candidate gap is impossible;
- if it equals `d`, mark `r` used, append the midpoint, and continue.

Always taking the smallest unused lower value makes the validation deterministic.

**Why duplicates are handled**

`vis` tracks positions, not numeric values. If the multiset contains repeated lower or higher numbers, separate occurrences can be paired separately.

For `[1, 1, 3, 3]` with `d = 2`, the first 1 pairs with one 3 and the second 1 pairs with the other. Both midpoints are 2.

**Why the greedy validation is correct**

Fix a candidate gap `d`. The smallest unused number cannot be a higher member of a still-unformed pair, because its lower partner would be smaller and unused; that contradicts its minimality. It must therefore be a lower member.

Its only possible higher partner has value exactly `low + d`. Choosing one occurrence of that value is forced. Removing this pair leaves the same problem on the remaining multiset.

By induction, the greedy process succeeds if and only if the multiset can be partitioned into fixed-gap pairs.

When `len(ans) == n >> 1`, every required pair has been formed and the source returns their midpoints. The problem guarantees at least one candidate succeeds.

**Trace the ambiguous example**

For sorted `[2, 4, 6, 8, 10, 12]`, pairing global minimum 2 with 4 gives `d=2` and $k=1$. Greedy pairs 6 with 8 and 10 with 12, producing `[3, 7, 11]`.

Pairing 2 with 8 instead gives `d=6` and $k=3$. Greedy pairs 4 with 10 and 6 with 12, producing another valid answer `[5, 7, 9]`. Returning the first successful answer is allowed.

The source sorts `nums` in place, so it mutates the caller's array order.

**Why `r` never needs to move backward**

As `l` advances through sorted lower candidates, the required partner value `nums[l] + d` never decreases. Any position skipped by `r` for being too small for an earlier lower value is also too small for every later one.

This monotonicity makes one linear validation possible for each candidate gap. Used higher positions are skipped through `vis` when they are encountered as possible lower positions.

The success-length test is sufficient because each appended midpoint corresponds to two distinct consumed positions. Reaching half the input length means a complete partition has been constructed.

## Complexity detail

Let $M$ be the length of `nums`, equal to twice the recovered array length.

Sorting costs $O(M\log M)$. Up to $M-1$ candidate partners are tried, and each validation advances its pointers through at most $M$ positions, giving $O(M^2)$ worst-case time. This dominates sorting.

Each candidate allocates a Boolean list of length $M$ and an answer list of length at most $M/2$, so auxiliary space is $O(M)$.

## Alternatives and edge cases

- **Multiset counter validation:** Repeatedly remove the smallest value and its value-plus-gap partner from a frequency map. It expresses the same greedy proof.
- **Try arbitrary pairings:** Exponential backtracking is unnecessary because the smallest unused lower partner is forced for a fixed gap.
- **Zero gap:** It implies `k = 0` and must be rejected.
- **Odd gap:** It cannot equal `2k` for integer `k`.
- **Duplicate values:** Position-based `vis` preserves multiplicity.
- **Multiple valid answers:** The first successful candidate may be returned.
- **Two input numbers:** Their positive even difference yields their midpoint.
- **Large numeric values:** Midpoint arithmetic remains within Python integer capacity.
- **First element role:** Sorted global minimum must be lower, which reduces possible `k` values to its partner choices.
- **Candidate failure:** A missing exact-gap partner invalidates that `d` immediately.
- **Input mutation:** `nums.sort()` changes the input order.
- **Existence guarantee:** The final empty return is a fallback outside the promised valid cases.
- **Monotonic partner pointer:** Sorted required partner values mean `r` never needs to retreat.
