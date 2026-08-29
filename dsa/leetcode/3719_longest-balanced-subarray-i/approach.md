## General

**Count distinct values, not elements**

A subarray is balanced when its number of distinct even values equals its number of distinct odd values. Repeated occurrences of the same number do not increase either side. For example, `[2, 2, 2, 3]` contains one distinct even value, two, and one distinct odd value, three, so it is balanced despite having three even elements and only one odd element.

This distinction determines the data the algorithm must maintain. For each candidate subarray, it needs to know whether a value has appeared before and how many first-time values belong to each parity group. It does not need the full occurrence frequency of every value.

**Fix a left boundary and extend the right boundary**

Every subarray is identified by a left endpoint `i` and a right endpoint `j`. The outer loop chooses each possible `i`. For that fixed left endpoint, the inner loop advances `j` from `i` through the end of the array, so the current candidate grows as

`nums[i:j + 1]`.

The solution creates two pieces of state for each new `i`:

- `vis` is the set of values already present in the current candidate.
- `cnt[0]` is the number of distinct even values, while `cnt[1]` is the number of distinct odd values.

Both start empty or zero because no value has been included before the first inner-loop iteration.

When `nums[j]` is appended, the code first checks `if nums[j] not in vis`. If the value is new to this particular subarray, it must increase exactly one of the two distinct counters. The expression `nums[j] & 1` evaluates to zero for an even integer and one for an odd integer, so

`cnt[nums[j] & 1] += 1`

updates the proper group. The value is then added to `vis` so later copies will not be counted again.

If the value is already in `vis`, neither distinct count changes. The candidate's length still increases because a new array position was included, but the set of distinct values is unchanged. This is why a later duplicate can make a longer balanced subarray even though it does not affect the balance equation.

**Detect balance after each extension**

After processing the newly included value, the condition

`cnt[0] == cnt[1]`

is exactly the problem's definition. The left side is the number of distinct even values in `nums[i:j + 1]`, and the right side is the number of distinct odd values in the same subarray. When they are equal, the candidate is balanced and its length is `j - i + 1`.

The code updates

`ans = max(ans, j - i + 1)`

so `ans` always holds the longest balanced candidate encountered so far. It does not stop after finding one balanced ending for a fixed `i`. Extending farther may introduce matched new even and odd values or only duplicates, creating an even longer balanced subarray.

Consider the fixed-left scan of `[3, 2, 2, 5, 4]`:

| Current candidate | New distinct value? | Distinct evens | Distinct odds | Balanced? |
| --- | --- | ---: | ---: | --- |
| `[3]` | 3, yes | 0 | 1 | No |
| `[3, 2]` | 2, yes | 1 | 1 | Yes |
| `[3, 2, 2]` | 2, no | 1 | 1 | Yes |
| `[3, 2, 2, 5]` | 5, yes | 1 | 2 | No |
| `[3, 2, 2, 5, 4]` | 4, yes | 2 | 2 | Yes |

The duplicate two leaves both counters unchanged, but the length grows from two to three while the candidate remains balanced. The final new even value restores equality and makes the whole length-five array balanced.

**Why resetting state for every left endpoint is necessary**

The set `vis` describes values inside a particular `nums[i:j + 1]`. When `i` advances, the old leftmost value leaves the candidate, and whether another copy remains would need additional frequency bookkeeping. This smaller version of the problem avoids that complexity by starting a fresh set and counters for the next `i`.

The reset is inexpensive enough under `n <= 1500`. It lets every inner scan have a simple invariant: `vis` is exactly the set of values from the fixed `i` through the current `j`, and `cnt` classifies exactly those values by parity.

**Why the answer is complete**

Take any nonempty subarray `nums[L:R + 1]`. The outer loop eventually chooses `i = L`. During that outer iteration, the inner loop eventually reaches `j = R`. At that moment, every value in the chosen subarray has been inserted into `vis` on its first occurrence, no outside value has been inserted, and `cnt` contains its exact numbers of distinct even and odd values.

If the subarray is balanced, the equality succeeds and its length is compared with `ans`. Conversely, the equality can succeed only when the two exact distinct counts match, so every recorded candidate is valid. Since every endpoint pair is visited and `ans` retains the largest valid length, the returned value is the longest balanced subarray.

The initialization `ans = 0` handles arrays with no balanced nonempty subarray. Although the two counters are both zero before an inner scan begins, the code never tests the empty interval. It performs the comparison only after adding `nums[j]`, so it does not incorrectly treat an empty subarray as a positive-length answer.

## Complexity detail

Let `n` be the number of elements. For left endpoint zero, the inner loop runs `n` times; for left endpoint one, it runs `n - 1` times; and so on. The total number of candidate extensions is

$$
n+(n-1)+\cdots+1
=\frac{n(n+1)}{2}
=O(n^2).
$$

Each extension performs one expected $O(1)$ set membership test, at most one expected $O(1)$ insertion, a parity calculation, and constant-time counter and maximum operations. The expected total time complexity is $O(n^2)$.

For one fixed left endpoint, `vis` can hold at most `n` distinct values. `cnt` has exactly two entries and the remaining variables use constant space. The set is discarded and recreated between outer iterations rather than retained for all left endpoints, so peak auxiliary space is $O(n)$, not $O(n^2)$. Hash-set behavior supplies the expected-time qualification.

## Alternatives and edge cases

- **Rebuild sets for every endpoint pair:** Constructing the distinct even and odd sets from scratch for each subarray adds up to $O(n)$ work per pair and $O(n^3)$ total time. Extending the right boundary reuses everything learned for the shorter candidate.
- **Store two sets instead of `vis` and `cnt`:** Separate even and odd sets also work, and their sizes directly express the balance condition. The exact source uses one set plus two integer counts, which avoids choosing a set twice and stores each value only once.
- **Maintain occurrence counts while sliding the left boundary:** A more advanced method can update distinct counts as both boundaries move, but finding the globally longest equality is not a standard monotonic sliding-window problem. The larger version requires a more sophisticated segment-tree treatment; simple shrinking decisions can miss answers.
- **Compare counts of even and odd elements:** This solves a different problem. Duplicates must contribute only once, so an array such as `[2, 2, 2, 3]` demonstrates why raw parity totals are wrong.
- **All values have the same parity:** Every nonempty subarray has at least one distinct value of that parity and zero of the other, so no balance occurs. `ans` correctly remains zero.
- **One even and one odd value with duplicates:** Any subarray containing both distinct values and no additional unmatched distinct value is balanced regardless of their occurrence counts.
- **A duplicate at the right endpoint:** The distinct counters do not change, but the new longer length must still be tested. The code performs the equality check on every iteration, not only when a new value appears.
- **The same numeric value cannot belong to both groups:** Integer parity is fixed. A single `vis` set is sufficient because every first appearance maps unambiguously to `cnt[0]` or `cnt[1]`.
- **Single-element array:** Its one distinct value is either even or odd, so the counts are one and zero. The method returns zero, matching the absence of a balanced nonempty subarray.
- **Negative or zero values:** The stated input contains positive integers. Python's low bit still classifies other integers, but the approach relies only on parity and would conceptually extend; no extra handling is needed for the actual contract.
- **Large numeric values:** Set operations depend on how many values are stored, not on the maximum value `10^5`. No value-indexed array of that size is required.
- **Overlapping optimal candidates:** Every left boundary receives an independent scan, so overlapping, nested, and duplicate-containing subarrays are all evaluated without conflict.
