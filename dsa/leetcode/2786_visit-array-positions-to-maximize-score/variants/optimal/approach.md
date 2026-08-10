## General

**A path is a subsequence that must begin at index zero**

Every move goes to a larger index, so visited values form a subsequence of `nums`. Position zero is mandatory and contributes `nums[0]` immediately. Later positions may be skipped freely.

The score for adding a visited value depends on only one fact about the previously visited position: whether its value is even or odd. The exact solution compresses all possible visited subsequences into two dynamic-programming states.

**Define the two states**

`f[0]` is the best score of any valid visited subsequence among processed indices whose last visited value is even. `f[1]` is the corresponding best score ending in an odd value.

Both begin at negative infinity, meaning unreachable. The parity of `nums[0]` is computed with `nums[0] & 1`, and that state is initialized to `nums[0]`. The opposite parity remains unreachable because a valid path cannot skip the required starting position and pretend it ended in another parity.

Negative infinity is useful because subtracting `x` and adding a finite value still leaves an impossible candidate at negative infinity.

**Process one optional new position**

For current value `v`, let `p = v & 1`. A best path ending at `v` can come from:

- a previous best path already ending in parity `p`, with no penalty;
- a previous best path ending in parity `p ^ 1`, paying penalty `x` for the parity change.

Before adding `v`, the better predecessor score is:

`max(f[p], f[p ^ 1] - x)`.

Visiting `v` then adds its positive value:

`f[p] = max(f[p], f[p ^ 1] - x) + v`.

The other parity state remains unchanged, representing the best subsequence that skips this position.

**Why the old same-parity state does not need a separate skip maximum**

The assignment always adds `v` to the selected same-parity destination state. At first this may appear to discard the option of skipping `v` and keeping old `f[p]`.

All input values are positive. If old `f[p]` is reachable, visiting `v` from it pays no parity penalty and produces `f[p] + v > f[p]`. Therefore the old state can never remain optimal for parity `p` after this positive same-parity value becomes available. The best path ending in parity `p` should always append `v`.

The state for the opposite parity is not updated and naturally preserves its skip option.

If values could be zero or negative, this simplification would require reconsideration. Positivity is a material part of the proof.

**Read the opposite state safely**

`p ^ 1` flips zero to one and one to zero. In the source expression `f[v & 1 ^ 1]`, Python operator precedence evaluates the bitwise AND before XOR, so it means `f[(v & 1) ^ 1]`.

Only `f[p]` is assigned. `f[p ^ 1]` is a different list entry and still contains the previous processed-prefix value when read, so no temporary copy of the two-state array is needed.

**A walkthrough**

For `nums = [2, 3, 6, 1, 9, 2]` and penalty five:

- Start with even state 2 and odd state unreachable.
- At 3, switching from even would give `2 - 5 + 3 = 0`, so odd state becomes zero.
- At 6, extending the even state gives `2 + 6 = 8`, better than switching from odd.
- At 1, switching from even gives `8 - 5 + 1 = 4`, improving the odd state.
- At 9, same odd parity adds freely, making the odd state 13.
- Later choices update their corresponding parity.

The score 13 represents visiting values 2, 6, 1, and 9, with one parity-change penalty.

**Why skipped positions need no explicit transition**

When a value of parity `p` is processed, the opposite state is unchanged and therefore skips it. The same-parity state is improved by taking it due to positivity. Thus both possibilities relevant to future paths remain represented.

Earlier paths of the same ending parity do not need separate storage. Future penalties depend only on ending parity, so among such paths, the one with greatest current score is always at least as good for every future continuation.

**Why the recurrence is correct**

Any valid subsequence ending at current `v` has a previous last visited value of parity `p` or `p ^ 1`. The former pays no penalty; the latter pays exactly `x`. By the state definition, `f` contains the best score available for each predecessor parity. Taking the better transition and adding `v` yields the best path ending here.

Induction from the mandatory index-zero initialization proves the two state values after every processed index. A globally optimal path ends in one of the two parities, so `max(f)` is the answer.

**The source has constant DP state but creates a linear slice**

The manifest reports `O(1)` auxiliary space, which describes the two-state recurrence. The exact loop is `for v in nums[1:]`. In Python, `nums[1:]` creates a new list containing `n - 1` references before iteration. Therefore the exact implementation uses `O(n)` auxiliary space even though the algorithm can be written with constant extra space by iterating indices or an iterator.

This implementation-level detail must be separated from the abstract DP state.

## Complexity detail

Let `n` be `len(nums)`. Creating the slice `nums[1:]` takes `O(n)` time, and the loop processes each later value once with constant work. Total time is `O(n)`.

The two DP entries use `O(1)` state. However, the list slice uses `O(n)` additional storage in the exact Python source. Its actual auxiliary space is therefore `O(n)`, contradicting the manifest's `O(1)` implementation claim. Replacing the slice with `itertools.islice(nums, 1, None)` or index iteration would realize the constant-space recurrence.

## Alternatives and edge cases

- **Full DP table:** Store both parity states for every index. It is correct but uses `O(n)` space without benefit when only the final maximum is needed.
- **Constant-space index loop:** Iterate `for index in range(1, n)` and read `nums[index]`. This removes the exact source's linear slice while preserving the recurrence.
- **Greedy take every positive value:** It ignores parity-switch penalties; skipping a positive value can be worthwhile when it forces an expensive switch.
- **Track only one best score:** Future transition cost depends on ending parity, so one globally best score is insufficient.
- **All values have the starting parity:** No penalty is ever paid, and positivity makes visiting every position optimal.
- **Very large penalty:** The solution may stay in one parity and skip values of the other parity.
- **Penalty smaller than a value:** Switching may improve the destination state even after paying `x`.
- **Unreachable opposite state early:** Negative infinity prevents a path from starting anywhere except index zero.
- **Positive-value guarantee:** It justifies always appending a same-parity current value rather than retaining a skip state.
- **Repeated parity switches:** Every transition from the opposite state subtracts `x` exactly once.
- **Bitwise parity:** `v & 1` works for all positive integers in the constraints.
- **Input preservation:** The slice copies references but neither the slice nor the algorithm mutates `nums`.
