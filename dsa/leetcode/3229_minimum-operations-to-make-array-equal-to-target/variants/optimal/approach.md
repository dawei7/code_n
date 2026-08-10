## General

**Convert the problem into required signed changes.** Define

$$
d_i=\texttt{target}[i]-\texttt{nums}[i].
$$

If $d_i>0$, position $i$ needs that many unit increments. If $d_i<0$, it needs $\lvert d_i\rvert$ unit decrements. If zero, it already matches.

One operation applies the same sign and one unit to a contiguous interval. Picture each $\lvert d_i\rvert$ as a stack of unit layers above the index, colored positive or negative by sign. An operation creates one horizontal layer across a contiguous run of positions needing that sign.

The minimum number of operations is the number of layer intervals that must start.

**Pay for every layer at the first position.** At index zero, no operation can have started earlier. All $\lvert d_0\rvert$ required layers must begin there. The source initializes

`f = abs(target[0] - nums[0])`.

**Reuse same-direction layers across adjacent positions.** Let previous required difference be $y=d_{i-1}$ and current be $x=d_i$.

If `x * y > 0`, both are nonzero and have the same sign. Up to

$$
\min(\lvert x\rvert,\lvert y\rvert)
$$

layers can continue across the boundary between positions. If the current magnitude is no larger, no new operation must start; surplus previous layers simply end at $i-1$. If current magnitude is larger, exactly

$$
\lvert x\rvert-\lvert y\rvert
$$

new layers begin at $i$.

The source computes this difference and adds it only when positive.

**A zero or sign change breaks every active layer.** If `x * y <= 0`, the values have opposite signs or at least one is zero. An increment operation cannot continue into a position needing decrements, and vice versa. No nonzero layer can pass through a zero requirement without incorrectly changing it. Therefore all $\lvert x\rvert$ current layers must start anew, which the else branch adds.

When $x=0$, this adds zero and merely ends earlier layers. When the next nonzero difference appears, its full magnitude starts after the gap.

**Why counting starts is a lower bound.** At the first position of a same-sign run, every required unit must come from an operation starting there or earlier; earlier is impossible across a sign/zero break. Whenever magnitude rises by $q$ within a run, $q$ additional simultaneous unit operations are necessary because only the previous magnitude's layers could already be active. Every valid transformation must pay at least all counted starts.

**Why the lower bound is constructible.** For each maximal run of positive differences, create horizontal increment intervals layer by layer. Start new layers exactly where the required height rises, continue each while subsequent positions still need that layer, and end it just before height falls below the layer. This constructs the positive profile with exactly the counted starts. Do the same independently for negative runs using decrement operations. Runs are separated by zero or opposite sign, so their intervals do not conflict.

The construction reaches every `d_i` and uses exactly `f` operations. Hence the lower bound is the true minimum.

**Trace the first example.** Differences between target and nums are `[1,1,1,2]`. Index zero starts one positive layer. The next two equal magnitudes reuse it. The final magnitude rises from one to two, so one new layer starts there. Total operations are two: one increment across the whole array and one increment at the final position.

For `nums=[1,3,2]` and `target=[2,1,4]`, differences are `[1,-2,2]`. Every boundary changes sign, so no layer continues. Costs are $1+2+2=5$.

**The source computes differences on demand.** It does not allocate a separate `d` array. At each index it recomputes current and previous differences from the two input arrays, preserving $O(1)$ auxiliary space.

## Complexity detail

Let $n$ be array length. Initialization is constant, and the loop visits indices one through $n-1$ once with constant arithmetic. Time is $O(n)$.

Only scalar variables `f,x,y,d` and the loop index are stored, so auxiliary space is $O(1)$. Both input arrays are read only.

Differences can have magnitude near $10^8$, and the total can be much larger than 32-bit range across $10^5$ positions. Python integers remain exact.

## Alternatives and edge cases

- **Build the difference array explicitly:** It can make the layer picture easier to inspect but uses $O(n)$ additional space.
- **Simulate one operation at a time:** Magnitudes up to $10^8$ make literal unit updates infeasible.
- **Segment-tree greedy updates:** Range data structures are unnecessary because the closed layer-start count follows from adjacent differences.
- **All differences zero:** Initial and added costs are zero, so no operation is needed.
- **Constant positive run:** Start its magnitude once and extend all layers across the run.
- **Increasing same-sign magnitude:** Only the increase starts new operations.
- **Decreasing same-sign magnitude:** Extra layers end; ending costs no operation.
- **Positive-to-negative transition:** Every negative layer starts fresh; increment and decrement operations cannot be shared.
- **Zero gap:** It ends all active layers and separates later work.
- **Single element:** The answer is simply its absolute required change.
- **Negative differences:** Absolute magnitudes count decrement layers exactly like positive increment layers.
- **Positive input values:** Intermediate operations may change them, but only the final signed difference profile matters.
- **Input preservation:** No operation is physically simulated on `nums`.
