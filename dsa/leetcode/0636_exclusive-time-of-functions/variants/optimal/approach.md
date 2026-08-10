## General

**Model the runtime call stack directly.** On a single-threaded CPU, only the most recently started unfinished call executes. `stk` stores those active function IDs in call order, so `stk[-1]` is exactly the function running at the current moment. Recursive calls work naturally because the same ID may appear in several stack positions.

`ans[id]` accumulates exclusive time across every invocation of that function. The remaining variable, `pre`, is the beginning of the next time segment that has not yet been credited to any function.

**Why event boundary semantics matter.** A start log at timestamp `t` means the new call begins at the beginning of time unit `t`. An end log at `t` means the current call continues through the end of unit `t`. Consequently:

- a segment ending just before a start at `t` has length `t - pre`;
- a segment ending with an inclusive end at `t` has length `t - pre + 1`.

The source's two branches differ by exactly that `+ 1`.

**Handle a start event.** Parsing `"id:start:time"` gives function `i` and timestamp `cur`. If the stack is nonempty, its top function has been executing continuously from `pre` through `cur - 1`. The method credits

`cur - pre`

to that function before it becomes paused by the new call.

It then pushes the new function ID and sets `pre = cur`. The new top starts executing at the beginning of `cur`, and no time unit has been lost or counted twice.

If the stack was empty, no function was executing before this top-level start, so there is nothing to credit. The same push and `pre` assignment begin the first segment.

**Handle an end event.** The top call is the one ending because logs follow call-stack behavior. It has executed from `pre` through `cur` inclusive, so its segment length is

`cur - pre + 1`.

The method pops that function and adds the segment to its accumulated answer. Execution can resume in the caller only at the beginning of the next unit, so it sets

`pre = cur + 1`.

If another log starts at that next timestamp, the caller receives zero intervening units, which is correct. If the caller continues longer, the next event will credit the interval beginning at this updated `pre`.

**Trace the first sample.**

- `0:start:0` pushes 0 and sets `pre = 0`.
- `1:start:2` credits function 0 with `2 - 0 = 2` units, covering times 0 and 1. It pushes 1 and sets `pre = 2`.
- `1:end:5` credits function 1 with `5 - 2 + 1 = 4` units, covering 2 through 5. It pops 1 and sets `pre = 6`.
- `0:end:6` credits resumed function 0 with `6 - 6 + 1 = 1` unit.

Totals are 3 for function 0 and 4 for function 1.

**Why recursion needs no special case.** If function 0 starts another invocation of function 0, the outer 0 is first credited and paused, then another 0 is pushed. When the inner call ends, its time is added to the same `ans[0]` bucket and the outer call resumes. Exclusive time is requested per function ID across all calls, so combining both invocations is exactly right.

**The timeline-partition invariant.** Before each log is processed, every CPU unit earlier than `pre` has been credited exactly once, and if the stack is nonempty, its top function owns the uncredited segment beginning at `pre`. A start credits the segment before `cur` and transfers ownership at `cur`. An end credits through `cur` and advances the next boundary to `cur+1`. Induction over the logs proves every executed unit is assigned once to the function actually on top of the stack, which is the definition of exclusive time.

`op[0] == "s"` distinguishes `"start"` from `"end"` without comparing the entire string. The log format guarantees those are the only operations.

## Complexity detail

Let $L$ be the number of log entries and $D$ the maximum active call depth. Each log is split, parsed, and processed once. Each start pushes one ID, and its matching end pops it once. Total time is $O(L)$.

`ans` uses $O(n)$ space. The stack holds at most $D$ active calls, using $O(D)$ space. All other state is constant, so total auxiliary space is $O(n+D)$, matching the manifest. Parsing creates short temporary strings whose sizes are bounded by the log representation.

Timestamp magnitude does not affect the number of operations. Python integers safely hold differences up to the provided $10^9$ range and accumulated totals.

## Alternatives and edge cases

- **Store start times in stack frames:** Push each function with its effective start and subtract child durations on return. It works but needs more per-frame bookkeeping than the global segment boundary.
- **Event-by-event segment accounting:** The exact approach is preferable because each interval is credited immediately to the current stack top.
- **Start and end at the same timestamp:** The call executes for one unit; `cur - pre + 1` correctly returns 1.
- **Nested calls:** The parent is credited before the child starts and again only after the child ends, so child time is excluded.
- **Recursive calls:** Duplicate IDs on the stack are valid and their separate intervals accumulate into one answer entry.
- **Adjacent events:** Setting `pre = cur + 1` after an end prevents the inclusive end unit from being counted again.
- **Top-level gaps:** Valid program logs describe execution periods; when the stack is empty, no function receives time before the next start.
- **Well-formed nesting:** The algorithm trusts that every end corresponds to the current stack top, as guaranteed by call-stack logs.
- **Inclusive end timestamp:** Omitting `+ 1` is the most common off-by-one error and undercounts every completed call.
- **Large timestamps:** Only differences matter; the algorithm does not iterate through individual time units.
- **Functions never called:** Their initialized answer entries remain zero.
