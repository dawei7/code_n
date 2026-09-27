# Guided Example: Debounce

## 1. The instance and the dispatch rule

A *debounced* wrapper around a function `fn` does not run the call it receives. Instead, each call at time $c$ arms one pending execution for the later instant $c + t$, and that pending execution is discarded if the wrapper is called again before it becomes due. The wrapper must also pass through whatever arguments the call carried.

This lesson works one instance all the way to its output: delay `t = 150`, with three calls in the given order.

| Call order | Arrival time | Argument list |
|---|---|---|
| 1 | 50 | `[1, 2]` |
| 2 | 300 | `[3, 4]` |
| 3 | 300 | `[5, 6]` |

| Execution | Time | Argument list |
|---|---|---|
| first | 200 | `[1, 2]` |
| second | 450 | `[5, 6]` |

The instance is deliberately the smallest one that forces all three decisions the rule can make: a call that arms an execution into an empty window, a call that arms after an earlier window already closed, and a call that lands at the *same* instant as its predecessor and must overwrite it. The second and third calls share the timestamp `300`, which separates time order from arrival order and is where most implementations go wrong.

The statement bounds the instance exactly: $0 \le t \le 1000$, $1 \le \text{calls.length} \le 10$, $0 \le \text{calls}[i].t \le 1000$, and $0 \le \text{calls}[i].\text{inputs.length} \le 10$. So a burst is at most ten calls, and an execution time never exceeds $1000 + 1000$.

## 2. What the wrapper must remember between two calls

Write the arrivals in order as $c_1 \le c_2 \le \dots \le c_n$ and the argument list of call $k$ as $a_k$. The wrapper needs only three facts, never the history of the burst:

| State | Meaning at the current instant | Initial value |
|---|---|---|
| `armedDeadline` | the time at which the single pending execution is due | no execution is armed |
| `armedArgs` | the argument list the pending execution will be invoked with | nothing retained |
| `log` | executions already committed, in time order | empty |

**Invariant.** After call $k$ has been processed, at most one execution is armed; if one is armed, its deadline is $c_k + t$ and its arguments are $a_k$. Every earlier call of the same burst has been eliminated, and every execution already in the log is permanent.

The invariant is what makes the lesson short: because each call either finds nothing armed or destroys what it finds, the amount of live scheduling state never grows with the length of a burst. A burst of ten calls still leaves exactly one pending execution.

```text
50   call 1 [1,2]   arms an execution for 200
                    200  execution [1,2] committed
300  call 2 [3,4]   arms an execution for 450
300  call 3 [5,6]   cancels that one, arms its own for 450
                    450  execution [5,6] committed
```

## 3. Step-by-step trace of the instance

| Call processed | Pending execution before | Action taken | Pending execution after | Executions logged |
|---|---|---|---|---|
| call 1, arrival 50, `[1, 2]` | none | nothing to cancel; arm one execution for `50 + 150 = 200` | deadline 200, arguments `[1, 2]` | none |
| quiet interval from 50 to 300 | deadline 200, arguments `[1, 2]` | no call arrives before 200, so the armed execution becomes due and commits | none | `(200, [1, 2])` |
| call 2, arrival 300, `[3, 4]` | none | the earlier window has closed; arm one execution for `300 + 150 = 450` | deadline 450, arguments `[3, 4]` | `(200, [1, 2])` |
| call 3, arrival 300, `[5, 6]` | deadline 450, arguments `[3, 4]` | `300 < 450`, so the pending execution is inside the window: discard it and arm one for `300 + 150 = 450` | deadline 450, arguments `[5, 6]` | `(200, [1, 2])` |
| end of input | deadline 450, arguments `[5, 6]` | the window stays quiet, so the armed execution becomes due and commits | none | `(200, [1, 2])`, `(450, [5, 6])` |

The final log is exactly the required output: the first execution at 200 carrying `[1, 2]`, the second at 450 carrying `[5, 6]`. Note what is absent: nothing runs at 50 or at 300, and no execution ever carries `[3, 4]`.

The trace exposes a closed-form survival rule. Call $k$ is the one that survives its burst, and therefore reaches the log, if and only if it is the last call or the next arrival is not inside its window:

$$
k \text{ survives} \iff k = n \;\lor\; c_{k+1} \ge c_k + t .
$$

| Call $k$ | $c_k$ | $c_k + t$ | Next arrival $c_{k+1}$ | Is $c_{k+1} < c_k + t$? | Survives into the log? |
|---|---|---|---|---|---|
| 1 | 50 | 200 | 300 | no | yes, at 200 |
| 2 | 300 | 450 | 300 | yes | no |
| 3 | 300 | 450 | none, it is the last call | not applicable | yes, at 450 |

## 4. Why the reasoning is correct

**Deadlines never move backwards.** Call $k$ arms $c_k + t$ and nothing else. Because arrivals are processed in non-decreasing order, every replacement deadline satisfies $c_{k-1} + t \le c_k + t$. A later call can therefore postpone an execution or keep its time equal, but can never pull it earlier, which is why the committed log is emitted in non-decreasing time order — the first entry stays at 200 while the burst that follows is scheduled at 450.

**Cancellation is local and cannot destroy committed work.** An execution leaves the pending state at the instant it becomes due; after that it is a fact in the log and is no longer reachable by any cancellation. So a call at 300 cannot retract the execution that ran at 200. Information is only ever superseded, never lost, and the log behaves as a growing prefix.

**The last call of a burst is the only survivor.** Suppose two consecutive calls satisfy $c_{k+1} < c_k + t$. The execution armed by call $k$ carries $a_k$ and is still pending when call $k+1$ arrives, so it is discarded and replaced by one carrying $a_{k+1}$. By induction over the calls of a maximal burst, every execution carrying the arguments of a non-final call is discarded before it can commit, and the execution carrying the newest arguments is the one that commits. That is why `[3, 4]` never appears in the output even though call 2 was processed normally.

**Completeness.** Every maximal burst contributes exactly one execution: its armed execution is untouched from the arrival of the last call until $c + t$, so no cancellation intervenes and it commits at exactly $t$ after that last arrival. No call is executed at its arrival time — the required times 200 and 450 are $50 + 150$ and $300 + 150$, not 50 and 300 — and no call is executed twice, since each call arms at most one execution and each armed execution is discarded at most once.

## 5. Boundary behaviour of the same rule

| Situation | Concrete instance | Observed outcome | Why the one rule already covers it |
|---|---|---|---|
| Zero delay | $t = 0$, a single call at time 0 with no arguments | one execution at 0 with an empty argument list | the deadline equals the arrival time, so the window has zero width and nothing can arrive strictly inside it |
| Equal timestamps | $t = 150$, calls at 300 with `[3, 4]` then at 300 with `[5, 6]` | only one execution, at 450, carrying `[5, 6]` | equality still counts as arriving inside the window; arrival order decides the arguments while the deadline stays 450 |
| Smallest gap that does not cancel | $t = 30$, calls at 0 with `[7]` then at 31 with `[8]` | executions at 30 with `[7]` and at 61 with `[8]` | the call at 31 is past the armed deadline of 30, so the earlier execution had already committed and the new call opens a fresh burst |
| Delay at the upper bound | $t = 1000$, one call at 1000 with `[4, 5, 6]` | one execution at 2000 | an execution time of `arrival + delay` may legitimately exceed the arrival bound of 1000; no clamping is involved |
| Empty argument list | a call whose `inputs.length` is 0 | an execution invoked with an empty argument list | argument forwarding is generic over the list, including the length-zero case |
| Long burst | $t = 25$, ten calls all at time 100 | one execution at 125 carrying the tenth call's arguments | nine cancellations and one survivor; the live state stayed constant throughout |

## 6. Alternatives this instance eliminates

| Alternative | What it would produce here | Why it is eliminated |
|---|---|---|
| Leading-edge throttle | an execution at 50 with `[1, 2]`, then suppression of the rest of the burst | the contract delays every execution by $t$; running at the arrival instant is not the requested behaviour |
| Queue every call without cancelling | executions at 200, 450 and 450 | two executions at the same instant with different arguments contradicts being cancelled when the function is called again within the window |
| Replace the pending call only when the arguments differ | keeps the execution that carries `[3, 4]` and drops `[5, 6]` | the criterion is purely temporal; argument identity is irrelevant, and equal arguments from a later burst must still refresh the deadline |
| Timestamp bookkeeping with no timer to cancel | the same log, produced lazily when a later call or the end of the input proves the window closed | correct but strictly more state and a flush step at the end; it also cannot commit an execution while the caller is idle, which is the whole point of the delay |
| A library-style debounce with leading and trailing options | options would change whether the first call of a burst also runs | the contract exposes only `fn` and `t`, so the trailing-only behaviour with argument replacement is the entire specification |

## 7. Time and auxiliary space complexity

Let $n = \text{calls.length}$. Processing one call costs a constant amount of work regardless of how many calls preceded it: consult the pending state, discard at most one armed execution, arm at most one replacement, and retain the newest argument list. The total scheduling cost is therefore $O(n)$, that is $O(1)$ per call, and the number of committed executions is at most $n$.

For space, let $m = \max_i \text{calls}[i].\text{inputs.length}$ be the length of the widest argument list. The live state is one deadline plus one retained argument list, so it occupies $O(m)$ space, and the constraints cap $m \le 10$, making the live state $O(1)$. Crucially it does not grow with the burst length: each call cancels its predecessor, so the runtime holds at most one pending execution no matter how many calls arrive, whereas queueing every call would need $O(n)$ pending entries. The returned log holds at most $n$ executions, which is output rather than auxiliary space, so auxiliary space is $O(m) = O(1)$. The wall-clock gap between the last call of a burst and its execution is exactly $t$, and every committed time is bounded by $1000 + 1000$ given $0 \le t \le 1000$ and $0 \le \text{calls}[i].t \le 1000$.
