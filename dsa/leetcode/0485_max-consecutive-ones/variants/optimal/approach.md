## General

“Consecutive” is the key word. The task does not ask for the total number of ones; it asks for the length of the longest uninterrupted run. A zero separates two runs, so ones on opposite sides of a zero must never be added together. The solution tracks the length of the run ending at the current position and separately remembers the largest run seen anywhere.

The two variables have distinct meanings:

- `cnt` is the number of consecutive ones at the end of the already-processed prefix.
- `ans` is the maximum run length anywhere in that processed prefix.

Both start at zero because no values have been examined. These meanings form a loop invariant: they are true before the loop, and each branch restores them after the next element is read.

**When the next value is one.** If `x` is `1`, the run that ended at the previous position continues through the current position. Its new length is therefore `cnt + 1`, so the code performs `cnt += 1`. This could create a new global maximum, and `ans = max(ans, cnt)` records it immediately.

For example, while reading `[1, 1, 0, 1, 1, 1]`, the first two elements make `cnt` progress from zero to one and then two, while `ans` follows it to two. The zero ends that run. The final three ones make `cnt` progress through one, two, and three; `ans` remains two until the last value raises it to three.

**When the next value is zero.** A run of ones cannot extend through a zero. The longest suffix of the processed prefix that consists entirely of ones is therefore empty, so its length becomes zero with `cnt = 0`. `ans` is deliberately not reset: a completed run may still be the best run in the entire array.

The constraints guarantee that every value is either zero or one. Python treats zero as false and one as true, so `if x` is exactly the binary test required by the contract. If arbitrary integers were allowed, this condition would treat every nonzero value as a one, but that broader behavior is irrelevant under the stated input domain.

**Why update the maximum inside the one branch.** Some implementations update the maximum only when a zero closes a run, then need an additional final comparison because a run may reach the array's end. This solution instead updates `ans` every time `cnt` grows. A trailing run is therefore captured at the moment each one is processed, and `return ans` needs no special final correction.

The invariant gives a compact correctness proof. Assume `cnt` and `ans` have their stated meanings after some prefix. If the next value is one, appending it extends the suffix run by exactly one; taking the maximum of the old `ans` and this new suffix accounts for every run in the longer prefix. If the next value is zero, the suffix run becomes length zero, and no new all-one run is created, so the previous `ans` remains correct. By induction, after the final value, `ans` is the longest consecutive-one run in the entire array.

This method is also information-efficient. To decide what a future one does, the algorithm needs only the current suffix length, not the positions or contents of all earlier runs. Once a zero has ended a run and its maximum contribution is reflected in `ans`, the exact run can be forgotten. That is why no auxiliary array, stack, or list of run lengths is needed.

Consider several boundaries. With `[0, 0, 0]`, every iteration leaves `cnt = 0` and the answer correctly remains zero. With `[1, 1, 1]`, there is no reset; both counters reach three. With alternating values such as `[1, 0, 1, 0]`, each one creates a run of length one and each zero resets it, so the maximum remains one. A single-element array returns one for `[1]` and zero for `[0]` without separate cases.

The algorithm must examine every input position in the worst case. If even one unexamined position could be a one extending a long suffix, the result might change. Thus the direct one-pass scan is not only simple but asymptotically optimal: reading the array itself requires linear time.

## Complexity detail

Let $n$ be the number of elements in `nums`. The loop reads each element exactly once and performs constant-time comparisons, assignments, addition, and `max` work. The running time is $O(n)$. This matches the lower bound for an arbitrary input array because any skipped element could affect the maximum run.

Only `ans`, `cnt`, and the loop variable are stored, regardless of input length. Auxiliary space is $O(1)$. The input is read without modification, and the integer result uses constant output space.

## Alternatives and edge cases

- **Split a converted string on zero:** Converting all values to text, splitting, and taking the longest segment can be concise, but it allocates several linear-size objects and obscures the simple streaming invariant.
- **Store every run length:** Appending completed counts to a list and taking their maximum later works, but retains $O(n)$ unnecessary data. Only the best previous run and current run matter.
- **Two nested loops:** One loop could locate a one and another could consume its entire run. With careful index movement this can still be linear, but the single loop is easier to verify and has fewer boundary conditions.
- **Update only at zeros:** This requires a final `max(ans, cnt)` so that an all-one suffix is not missed. Updating when a one arrives removes that special ending case.
- **All zeros:** The answer is zero because no one-run ever begins; initializing both counters to zero handles it naturally.
- **All ones:** No separator appears, so `cnt` reaches the full array length and `ans` follows it.
- **Alternating values:** Every run has length one, and resets prevent separate ones from being combined.
- **Single element:** The general loop returns `1` for `[1]` and `0` for `[0]` without branching on the array length.
- **Binary-input guarantee:** `if x` is correct only because values are guaranteed to be zero or one. For a more general array, the explicit condition `x == 1` would be required.
