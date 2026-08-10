## General

**A strategy must minimize its worst outcome.** Dropping an egg from one floor creates two possible worlds. If it breaks, only one egg remains and the critical floor is below the tested floor. If it survives, both eggs remain and the critical floor is at or above that floor. Because the task asks for certainty, a proposed first drop must budget enough moves for whichever branch is harder. This is why the recurrence uses a maximum inside a minimum.

**Define a one-dimensional state.** `f[i]` is the minimum number of moves needed in the worst case to determine the threshold when there are `i` consecutive candidate floors to resolve and both eggs are still available. Absolute floor labels do not matter: any block of `i` consecutive unknown floors has the same decision structure after shifting its labels. The base `f[0] = 0` says no drops are needed when there are no unknown floors.

The list is initialized as `[0] + [inf] * n`. Infinity marks states whose best first drop has not yet been considered. The outer loop fills `f[1]` through `f[n]` in increasing order, so every smaller state referenced by a transition is already complete.

**Consider every possible first drop.** For a state of `i` floors, `j` ranges from one through `i` and represents dropping the first egg at the `j`-th floor of the current unresolved block. The current drop costs one move regardless of its result.

If the egg breaks, the threshold lies among the `j - 1` floors below. Only the second egg remains, so those floors must be checked in increasing order. With one egg, no skipping is safe: breaking it before all lower possibilities are separated would make the threshold unknowable. The worst-case number of additional moves in this branch is therefore `j - 1`.

If the egg survives, the `j` tested-and-lower floors no longer need investigation, both eggs remain, and `i - j` higher floors are unresolved. Their optimal worst-case cost is `f[i - j]`. The first-drop choice consequently costs

$$
1+\max\bigl(j-1,\ f[i-j]\bigr).
$$

The code takes the minimum of this quantity over every `j`, selecting the first floor whose harder branch is as small as possible.

**Why balancing the branches matters.** Choosing a very low `j` makes the break branch cheap but leaves many floors if the egg survives. Choosing a very high `j` reduces the survival branch but makes a break expensive because the final egg may need a long linear scan. The best position generally occurs where `j - 1` and `f[i - j]` are close. The DP does not assume exact equality, which might be impossible for integer floors; it tries all positions and keeps the true minimum.

**Trace a small state.** For one floor, the only choice is `j = 1`, giving `1 + max(0, f[0]) = 1`. For two floors, dropping at the first gives `1 + max(0, f[1]) = 2`, while dropping at the second gives `1 + max(1, f[0]) = 2`, so `f[2] = 2`. For three floors, choosing the second floor gives `1 + max(1, f[1]) = 2`, better than starting at either extreme, so `f[3] = 2`. That strategy distinguishes all four possible thresholds `0, 1, 2, 3` in at most two drops.

**Why one egg implies a linear scan.** Suppose the first egg breaks at relative floor `j`. The threshold could be any value from below the first candidate through floor `j - 1`. With the remaining egg, test those lower floors from bottom to top. A survival rules out everything below and allows the scan to continue; the first break identifies the preceding floor as the threshold. In the worst case the egg survives through all `j - 1` floors, requiring exactly that many additional drops. Testing a higher lower-floor first could break the last egg while leaving several thresholds indistinguishable.

**Why the recurrence is globally correct.** Every valid strategy for `i` floors has some first drop `j`. Its two outcome branches require at least `j - 1` and `f[i - j]` additional moves respectively, so its worst case is at least the recurrence candidate. Conversely, choosing `j` and then using the linear one-egg procedure after a break or the optimal stored strategy after survival achieves exactly that candidate. Minimizing over all possible first drops therefore gives neither an underestimate nor an avoidable overestimate. Induction from `f[0]` proves `f[n]` is the minimum guaranteed move count.

## Complexity detail

The outer loop visits $n$ states. State `i` tries `i` first-drop positions, so the total number of transitions is

$$
\sum_{i=1}^{n} i=\frac{n(n+1)}{2}=O(n^2).
$$

Each transition performs constant work, making the exact source $O(n^2)$ time. The list `f` contains $n+1$ values, so auxiliary space is $O(n)$.

These bounds differ from the variant manifest's $O(1)$ time and $O(1)$ space labels. A closed-form triangular-number solution can return the smallest $m$ with $m(m+1)/2\ge n$ and can be implemented with constant extra space, but that is not what the checked-in source executes. The current implementation explicitly allocates a DP list and runs nested loops.

For $n\le1000$, the quadratic transition count is about half a million, which is practical. Every finite DP value is at most $n$, and `inf` is only an initialization sentinel. Python's numeric types safely support both.

## Alternatives and edge cases

- **Triangular-number strategy:** With $m$ allowed moves, choose successive gaps $m, m-1, ..., 1$. This covers $m(m+1)/2$ floors, so the answer is the smallest $m$ reaching $n$. It achieves the manifest's intended constant-form calculation but is a different implementation.
- **Binary search as if eggs were unlimited:** Ordinary binary search can break the first egg while leaving too many unknown lower floors for one remaining egg, so its logarithmic decision tree is not valid under the resource constraint.
- **Two-dimensional eggs-by-floors DP:** A general egg-drop table works but stores a redundant egg dimension when the number of eggs is fixed at two. The one-egg break cost has a direct formula.
- **One floor:** `f[1]` becomes one; one drop distinguishes threshold zero from one.
- **Threshold zero:** The strategy must allow the first tested floor to break. The lower interval can then be empty, represented by `j - 1 = 0`.
- **Threshold `n`:** Eggs survive every test. The recurrence's survival branches still guarantee termination and identification of the top threshold.
- **Identical eggs:** The state needs only the number of unbroken eggs, not an egg identity. After a break, the other egg supplies the linear scan.
- **Manifest versus source:** Complexity documentation for this file must describe the nested-loop DP honestly. Presenting the triangular formula as though it were executed would misrepresent both runtime and memory.
