## General

**Simulate simultaneous days with a snapshot**

Each day’s decisions must use values from the previous day. Mutating `arr` from left to right and immediately consulting those new values would produce an incorrect asynchronous process.

The exact solution creates `t = arr[:]` at the start of every day. `t` is the immutable snapshot used for all comparisons that day, while changes are written into `arr`.

For every interior index:

- if `t[i]` is strictly greater than both neighbors, decrement `arr[i]`;
- if `t[i]` is strictly smaller than both neighbors, increment `arr[i]`.

The first and last indices are excluded by `range(1, len(t) - 1)`, so endpoints never change.

**Why there are two independent `if` statements**

An element cannot be simultaneously strictly greater and strictly smaller than the same two neighbors. Therefore, at most one update applies. Using two `if` statements rather than `if/elif` produces the same result under the contract.

Equality with either neighbor makes both strict conditions false, so plateaus are left unchanged.

**Detect the stable day**

`f` means that at least one element changed during the most recently simulated day. It is initialized true so the loop executes once. At the start of a day it becomes false; every increment or decrement sets it true.

If a complete scan makes no change, `f` stays false and the while loop ends. The returned `arr` then contains no strict interior peak or valley, exactly the stable condition.

**Following the first example**

For `[6,2,3,4]`, the snapshot’s value 2 is below both 6 and 3, so it increments to 3. The value 3 at the next position is compared with snapshot neighbors 2 and 4; it is neither below both nor above both, so it stays 3. The day produces `[6,3,3,4]`.

On the next day, both interior values equal one neighbor, so neither is a strict extremum. No flag is set and the method returns.

**Why the snapshot changes decisions in the second example**

For `[1,6,3,4,3,5]`, positions one through four are evaluated against the original day simultaneously. The peak 6 falls to 5, the valley 3 rises to 4, the peak 4 falls to 3, and the valley 3 rises to 4. The new day is `[1,5,4,3,4,5]`.

If the loop compared against already-mutated `arr`, an update at one position could alter the next position’s decision during the same day, contradicting the specification.

**Why the process must terminate**

Consider total variation:

\[
P=\sum_{i=0}^{n-2}\lvert arr[i+1]-arr[i]\rvert.
\]

It is a nonnegative integer. On a rising edge, the left endpoint can only stay or move upward if it is a valley, and the right endpoint can only stay or move downward if it is a peak. These movements cannot increase the positive difference. On a falling edge, the symmetric movements cannot increase its absolute difference. Equal adjacent values do not move away from one another because neither can be strictly above or below the equal neighbor.

If any interior element changes, it is a strict peak or valley. Its two adjacent differences each move toward zero by at least one, so total variation strictly decreases. Other edges do not increase. Therefore, every changing day lowers the nonnegative integer \(P\), and only finitely many changing days are possible.

This is stronger than merely relying on the statement’s promise of stabilization: it explains why no oscillating cycle can occur.

**Why the final state is the specified result**

Each loop iteration exactly implements one simultaneous day. The method stops at the first day whose output equals its input, indicated by no updates. At that moment, applying the rules again would also make no changes, so the array is stable.

Because the daily transformation is deterministic, repeatedly applying it from the given start produces one fixed sequence; the returned stable state is the required endpoint of that sequence.

**Input mutation**

The method changes the supplied list in place and returns that same list object. The snapshots are separate shallow copies of integer references. Callers retaining `arr` will observe its stabilized contents.

## Complexity detail

Let \(n=\lvert\texttt{arr}\rvert\) and let \(D\) be the number of days that perform at least one change. There is one final no-change scan as well. Each day copies and scans \(O(n)\) entries, so exact time is \(O(n(D+1))\), usually written \(O(nD+n)\).

If \(C\) is the total number of individual increments and decrements, then every changing day performs at least one operation, so \(D\leq C\). This gives the loose bound \(O(nC+n)\), not the manifest’s event-driven \(O(n+C)\) for this full-rescan source.

Each snapshot `t` uses \(O(n)\) auxiliary space. All other state is constant, so total auxiliary space is \(O(n)\).

## Alternatives and edge cases

- **Compute a separate next array:** Build each new day from the old array and then replace it. This makes simultaneity explicit and has the same \(O(n)\) space per day.
- **Event-driven active indices:** Recheck only positions near a change. With careful scheduling by days, this can approach an \(O(n+C)\)-style bound, but preserving simultaneous semantics is more complex.
- **Already stable input:** The loop still performs one copy and scan, makes no changes, and returns.
- **Strict comparisons:** Equality with either neighbor prevents an update; using non-strict comparisons would alter plateaus incorrectly.
- **Endpoints:** The loop never visits indices zero or \(n-1\), so they remain exactly unchanged.
- **Adjacent extrema:** Snapshot comparisons let both update based on the old day, as required.
- **Two independent conditions:** They cannot both hold for one element, so no element changes twice in a day.
- **Termination:** Integer total variation decreases on every changing day, ruling out cycles.
- **In-place result:** The caller’s original list is mutated; copy it first if preservation is required.
- **Minimum allowed length:** With three elements, only the center can change, and the same simulation and termination proof apply.
