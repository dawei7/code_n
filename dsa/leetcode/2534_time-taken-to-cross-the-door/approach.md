## General

**Maintain one FIFO queue per direction**

`q[0]` stores arrived people waiting to enter, and `q[1]` stores arrived people waiting to exit.

People are considered in increasing original index `i`. Because `arrival` is nondecreasing, appending them to their direction queue preserves arrival order and index order. Popping from the left therefore selects the smallest-index waiting person within that direction.

**Interpret `st` as the preferred direction**

`st=0` means entering has priority when both queues are non-empty. `st=1` means exiting has priority.

Before time zero, the door was not used in the previous second, so exiting should win an initial tie. The source initializes `st=1`.

After someone crosses, `st` remains or becomes that person's direction. If both directions compete in the next consecutive second, the previous direction wins as required.

If a second passes with nobody using the door, `st` resets to one, representing the rule that exiting wins after an idle previous second.

**Add everyone who has arrived by current time**

At the start of second `t`, the inner loop enqueues all still-unprocessed people with `arrival[i]<=t`.

Using `<=` rather than equality is robust when time advances through earlier idle iterations: anyone who arrived before or at current time must now be waiting.

The input order and monotonically increasing `i` ensure each person is enqueued exactly once.

**When both queues have people**

If `q[0]` and `q[1]` are non-empty, pop from `q[st]`. This follows the previous-use priority:

- after entering, `st=0` and an entrant goes;
- after exiting or idleness, `st=1` and an exiting person goes.

The selected person's answer is set to current second `t`.

`st` needs no assignment in this branch because the chosen direction equals its existing value.

**When only one direction waits**

If exactly one queue is non-empty, that direction must use the otherwise idle door regardless of previous priority.

The code sets

`st=0 if q[0] else 1`

then pops that queue. Updating `st` records the direction actually used for next second's tie.

**When nobody waits**

No one crosses during second `t`, so the previous-second state for the next iteration must be “unused.” The code represents that with `st=1` because exit has priority after idleness.

It then increments time by one. Unlike the manifest summary's claim, the exact implementation does not jump directly to the next arrival.

This is still linear under the given constraint `arrival[i]<=n`: there can be only $O(n)$ seconds before the last arrival, plus one crossing second per person.

**One person crosses per loop second**

After queue handling, `t+=1` advances to the next second. At most one queue pop occurred, respecting door capacity.

The outer loop continues while some person has not yet been enqueued or either waiting queue is non-empty. It ends only after all `n` people have crossed.

**Trace the first tie**

At `t=0`, person 0 enters. The only non-empty queue sets `st=0`.

At `t=1`, person 1 waits to exit and person 2 waits to enter. Both queues are non-empty, and `st=0` from the immediately previous entering use, so person 2 crosses.

This directly produces the priority described in the example.


At the start of each decision:

- every arrived, uncrossed person is in exactly one direction queue;
- queue order is increasing person index;
- `st` equals the prior second's used direction, or one if that second was idle.

The enqueue step, three queue cases, and time increment preserve this invariant. The selected queue exactly follows the stated priority rules, and its leftmost person satisfies the smallest-index tie rule.

Thus each recorded `ans[p]=t` is the mandated crossing time, and termination returns all answers.

## Complexity detail

Each person is appended once and popped once, for $O(n)$ queue operations. The loop can also execute idle seconds, but arrival times are bounded by `n`, so there are $O(n)$ such time steps. Total time is $O(n)$.

The two queues and answer array store $O(n)$ indices and results. Auxiliary space including the required output is $O(n)$.

The exact source increments through idle time; it does not perform the event jumps described by the manifest.

## Alternatives and edge cases

- **Jump over idle gaps:** Set `t` to the next arrival when both queues are empty; this removes dependence on the arrival-time bound.
- **Simultaneous arrivals:** Enqueue all before choosing, then apply direction and index priorities.
- **Initial tie:** Exit wins because the door was previously unused.
- **Consecutive same-direction use:** That direction retains priority.
- **Idle previous second:** Reset preference to exit.
- **Only one queue:** Its direction crosses regardless of prior preference.
- **Same direction tie:** FIFO order yields the smallest person index.
- **Arrival while others wait:** The new person joins the appropriate queue's tail.
- **One person per second:** Only one pop occurs per outer iteration.
- **Manifest mismatch:** This code advances idle seconds individually rather than jumping.
