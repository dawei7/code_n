## General
**Keep the active call stack**

The most recently started unfinished call owns the CPU. Store active function identifiers in a stack so its top always identifies the function that should receive elapsed exclusive time.

**Track the first unassigned timestamp**

Let `previous` be the first time unit not yet credited. At a `start` event at time `t`, the old stack top owns the half-open interval `[previous, t)`, contributing `t - previous`; then push the new call and set `previous = t`.

**Handle inclusive end events separately**

At an `end` event at time `t`, the active call owns `[previous, t]`, which has `t - previous + 1` integer units. Credit and pop it, then set `previous = t + 1` so the resumed caller cannot also claim the ending time unit.

**Why every time unit is credited exactly once**

Before each log, all time units below `previous` have been assigned to whichever call was on top when they elapsed. Start processing assigns only the interval before the new call becomes active. End processing assigns through the ending call's inclusive final unit and advances beyond it. These disjoint intervals cover the execution timeline, while the stack always names their correct owner, so the accumulated totals are exact.

## Complexity detail
Each of the `L` logs is parsed once, and each call identifier is pushed and popped once, giving $O(L)$ time. The result uses $O(n)$ space and the active stack uses $O(D)$ space for maximum nesting depth `D`.

## Alternatives and edge cases
- **Simulate every timestamp:** increment the active function one unit at a time; it is correct but can depend on the numeric timestamp span rather than the number of logs.
- **Pair starts and ends before accounting:** explicit call-tree construction can recover the same totals, but requires extra nodes and a later traversal.
- **Subtract child durations from parent durations:** works with a call tree but is more stateful than assigning elapsed intervals directly.
- An end timestamp is inclusive, so a call starting and ending at the same timestamp contributes one unit.
- Recursive calls push the same identifier more than once and all contributions accumulate at that identifier.
- Sequential calls may resume or start at exactly the time unit after an inclusive end.
- Functions with no calls retain zero exclusive time.
- Nested calls may have identical boundary timestamps; log order and the stack determine which call is active.
