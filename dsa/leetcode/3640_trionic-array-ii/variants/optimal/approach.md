## General

A trionic subarray has an increasing run, then a decreasing run, then an increasing run. All three phases need at least one edge.

The exact source groups the array into maximal monotone runs. For each valid increase-decrease-increase shape, it includes the mandatory center and chooses the best-sum optional extension on the left and right.

This differs from the manifest summary, which describes phase dynamic programming.

**Find a maximal first increasing run**

At the start of an outer iteration, `l=i`. The source advances i while:

`nums[i-1]<nums[i]`.

If only one element was consumed (`i==l+1`), there is no increasing edge, so this position cannot begin a trionic subarray and the loop continues.

Otherwise `p=i-1` is the peak ending the first increasing phase.

**The minimum required left part**

A valid first phase ending at p must contain at least indices `p-1,p`. The source starts the candidate sum with:

`nums[p-1]+nums[p]`.

Earlier elements from the same increasing run are optional. They can extend the subarray leftward, but negative values may reduce the total, so the source chooses their best suffix later.

**Consume the decreasing run**

Starting after p, every strict decrease is mandatory for the maximal center run. The source adds each visited value to `s`.

When this loop stops, `q=i-1` is the valley.

The candidate is rejected if:

- `i==p+1`: no decreasing edge occurred;
- `i==n`: the array ended, leaving no third phase;
- `nums[i-1]==nums[i]`: equality prevents a strict final increase.

If it stops because `nums[i-1]<nums[i]`, the third increasing phase can begin.

**Minimum required right part**

The valley `nums[q]` is already included by the decreasing loop. The source adds `nums[q+1]` and advances i once, guaranteeing one strict increasing edge for the third phase.

At this point the minimal valid trionic center spans:

`p-1 ... p ... q ... q+1`,

with the entire decreasing run included.

**Choose the best right extension**

The third maximal increasing run may continue beyond `q+1`. Any valid right endpoint must take a contiguous prefix of these extra values.

The source accumulates `t` as it scans extra increasing values and records:

`mx=max(mx,t)`,

starting both at zero.

Adding zero means stop at `q+1`. A positive maximum prefix chooses the right endpoint yielding the largest additional sum. Negative prefixes are skipped, but later values can make a longer prefix positive because contiguity requires including everything before them.

**Choose the best left extension**

Likewise, optional values before `p-1` must form a contiguous suffix of the first increasing run.

The source scans backward from `p-2` to l, accumulating t. Each backward prefix corresponds to extending the subarray left by one more value. The maximum accumulated sum, or zero, is added.

This independently chooses the best left endpoint because left and right extensions do not affect monotonic validity or one another.

**Why the decreasing center cannot be shortened**

Within one maximal increase-decrease-increase shape, could a better trionic subarray choose a smaller internal decreasing interval?

The turning peak must be where increase changes to decrease; moving p into the decreasing run would make the first phase end with a decrease, while moving it left before the maximal increasing run ends would make the middle begin with an increase.

The same argument fixes q at the change from decrease to increase. Thus the full decreasing run between p and q is mandatory for this shape.

Only the outer ends within the first and third increasing runs are flexible.

**Why maximum suffix/prefix sums are sufficient**

Once p and q are fixed, every valid left endpoint lies somewhere in the maximal first increasing run at or before `p-1`. Its additional contribution is exactly one suffix of optional left values.

Every valid right endpoint similarly contributes one prefix of optional right values. The total candidate is:

`mandatory center + chosen left suffix + chosen right prefix`.

Since the choices are independent, maximizing each separately maximizes the whole shape.

**Advancing to the next shape**

After evaluating a valid shape, the scan may have moved through its third increasing run. The source sets `i=q`.

That valley is the first element of the just-seen third increasing run, which may serve as the beginning of the next trionic candidate's first increasing phase. Reconsidering from q prevents missing overlapping candidate shapes.

Although an increasing run can be scanned once as a right phase and once as the next left phase, each edge is revisited only a constant number of times. Total work remains linear.

**Negative values**

`ans` begins at negative infinity because every valid trionic subarray may have a negative sum. Initializing answer to zero would incorrectly prefer an empty subarray, which is not allowed.

Optional extension maxima begin at zero because omitting an optional extension is allowed. Mandatory phase elements remain included even when negative.

**Following the second example**

For `[1,4,2,7]`, p=1, q=2, and there are no optional extensions.

The mandatory sum includes `1+4`, then decreasing value 2, then first final-increase value 7, totaling 14.

**Following the negative example conceptually**

The maximal runs identify the same p and q as the valid subarray. Optional values outside its chosen endpoints have negative cumulative contribution, so the zero-based extension maxima omit them. The mandatory center still sums to -4, which can correctly beat other negative candidates.

**Why the best candidate cannot be missed**

Every trionic subarray belongs to a maximal monotone shape with forced turning points p and q. The outer scan reaches that shape. Its mandatory sum is included exactly once, and its endpoints correspond to a suffix/prefix choice examined by the two cumulative scans.

The source selects the best endpoint choices for each shape and takes the maximum over all shapes. Every constructed candidate is valid, and every valid candidate is bounded by one computed shape optimum, proving that the returned maximum is globally optimal.

**Exact-source dependencies**

The shown file uses `inf` and `List` without imports or definitions. A standalone module must provide them, for example `from math import inf` and `from typing import List`. Otherwise it raises `NameError` before completing.

## Complexity detail

The grouped loops advance across monotone runs. A run may be scanned once as a third phase and once again as the next candidate's first phase, while backward left-extension scans cover disjoint/constant-overlap run portions.

Each array position participates in only constant many operations, giving `O(n)` time.

Only indices, running sums, and maxima are stored. Auxiliary space is `O(1)`.

These are the same asymptotic bounds as the manifest, but the mechanism is grouped-run optimization rather than phase-state DP.

## Alternatives and edge cases

- **Three-phase dynamic programming:** Track best sum ending in increasing, decreasing, and completed-increasing phases, matching the manifest summary.
- **Prefix sums plus run boundaries:** They can evaluate endpoint sums but require additional arrays.
- **Enumerate l,p,q,r:** It is prohibitively expensive.
- **All values negative:** Answer must still be a valid negative sum; `ans=-inf` is essential.
- **Optional negative left values:** Maximum suffix may choose zero and omit them.
- **Optional negative right values:** Maximum prefix may stop at the mandatory first increasing edge.
- **Equality at a boundary:** Strict monotonicity fails, and the source rejects/restarts.
- **No first increase:** The candidate start is skipped.
- **No decrease after peak:** No middle phase exists.
- **Decrease reaches array end:** No final increasing phase exists.
- **Minimal four-element pattern:** It contains one edge per phase and no optional extension.
- **Overlapping shapes:** Resetting i to q allows the previous third run to become the next first run.
- **Guaranteed existence:** The contract ensures ans is eventually updated from negative infinity.
- **Manifest mismatch:** The exact source does not maintain per-endpoint phase DP states.
- **Input preservation:** The method reads `nums` without mutation.
- **Missing names:** Standalone execution must import `List` and define `inf`.
