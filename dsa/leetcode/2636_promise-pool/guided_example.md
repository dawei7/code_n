# Guided Example: Promise Pool

## 1. The instance we will schedule

Concurrency limiting is a scheduling problem, not an evaluation problem: the individual promises already know how to finish, and the only question the pool answers is *when each function is allowed to start*. The statement fixes two requirements — at most $n$ promises may be pending at any instant, and the functions must be executed in array order — and this instance is the statement's own second-limit case, where the pool must both fill up and refill.

$$
m = 3 \text{ functions with durations } 300,\ 400,\ 200 \text{ milliseconds}, \qquad n = 2 .
$$

The required outcome is that the three functions start at $0$, $0$ and $300$ milliseconds, finish at $300$, $400$ and $500$ milliseconds, that the peak number of pending promises is $2$, and that the returned promise resolves at $500$ milliseconds.

The interesting part of that outcome is the third function. It may not start at time $0$, because two promises are already pending and the limit forbids a third. It also does not wait for both of its predecessors: it begins the moment the *first* free slot appears, at $300$ milliseconds, even though the second function is still running until $400$. The pool's job is to keep exactly that tension — never exceed the limit, never leave a slot idle while unstarted work remains.

## 2. Two pieces of state and one rule

The pool needs a shared queue position and a set of running slots. Three quantities describe the whole system at any instant.

| State quantity | Meaning | Role in the contract |
|---|---|---|
| claim cursor | the index of the next function that has not yet been started | advances by one per start; captures the required array order |
| pending count | how many claimed functions have not yet resolved | must never exceed $n$ |
| completed count | how many of the $m$ functions have resolved | when it reaches $m$, the pool may resolve |

The management rule that makes the limit hold is a single indivisible step: a free slot takes the current claim cursor *and* advances it before doing anything asynchronous. Because taking and advancing happen together, no two slots can ever obtain the same index, and no index can be skipped. Once a slot owns an index, it may await that function's promise for as long as the promise needs; the slot is occupied for that whole interval, which is precisely what a "pending promise" means.

The lifecycle every slot follows is therefore a small loop with one exit.

```mermaid
accTitle: Lifecycle of one pool slot
accDescr: A slot repeatedly claims the next index while unstarted functions remain, awaits that function's promise, and exits once the cursor has passed the end of the array.
flowchart TD
    S["slot starts"] --> C{"cursor is before the end?"}
    C -->|"yes: claim the index and advance the cursor"| A["await that function's promise"]
    A --> C
    C -->|"no: nothing left to claim"| E["slot exits"]
```

## 3. Timeline of the traced instance

The pool opens $\min(n, m) = 2$ slots at time $0$. Each event below is either a start or a resolution, and the pending column shows that the limit of two is respected at every instant.

| Time | Event | Index claimed | Pending after the event | Completed after the event | Cursor after the event |
|---|---|---|---|---|---|
| 0 | slot 1 opens and claims work | 0, a 300 ms function | 1 | 0 | 1 |
| 0 | slot 2 opens and claims work | 1, a 400 ms function | 2 | 0 | 2 |
| 300 | the 300 ms function resolves; slot 1 is free and claims more work | 2, a 200 ms function | 2 | 1 | 3 |
| 400 | the 400 ms function resolves; slot 2 is free but the cursor is past the end | none | 1 | 2 | 3 |
| 500 | the 200 ms function resolves; slot 1 is free and the cursor is past the end | none | 0 | 3 | 3 |

At time $300$ the pending count is momentarily $1$ — the instant the first promise resolves and before its slot claims the next index — and then returns to $2$. That refill is what distinguishes a real pool from a batch. Two batching designs go wrong here in opposite directions: starting all three functions at time $0$ would peak at $3$ pending promises and violate the limit, while starting each function only after every earlier one resolved would be the $n = 1$ behaviour, finishing at $900$ milliseconds instead of $500$.

Because the cursor never moves backwards and each claim consumes exactly one index, the whole run performs exactly $m = 3$ starts, and the pool resolves when the third of them resolves. The partition of work among the slots for this instance is:

| Slot | Indices it ran, in order | Its load | Its finish times |
|---|---|---|---|
| 1 | 0 then 2 | $300 + 200 = 500$ ms | 300, then 500 |
| 2 | 1 | $400$ ms | 400 |

The completion time is the largest of the slot loads, $\max(500, 400) = 500$ milliseconds — not the sum of all durations, and not the largest single duration.

## 4. Invariants and correctness of the pool

Let a *claim* be the indivisible step that reads the cursor, records the index for one slot, and advances the cursor by one.

**Claim invariant.** After any finite prefix of the run, the indices already claimed are exactly $0, 1, \dots, c - 1$, where $c$ is the current cursor value, each claimed exactly once; and every function that has started was started by a claim.

*Preservation.* A claim returns the current cursor value $c$ and leaves the cursor at $c + 1$ without yielding control in between, so the set of claimed indices grows from $\{0, \dots, c-1\}$ to $\{0, \dots, c\}$ with no duplicate and no gap. Because starting a function is possible only by owning its index, no function can start twice, and no index below the cursor can be started later, since a later claim returns a strictly larger value.

**Order invariant.** Claimed indices increase strictly over time, so the sequence of start events is ordered by index. The statement's requirement that the pool execute $\text{functions}[i]$ then $\text{functions}[i+1]$ then $\text{functions}[i+2]$ is therefore satisfied as a *start order*, which is the only ordering a concurrently running pool can honour.

**Concurrency invariant.** The number of pending promises is exactly the number of claims issued minus the number of resolutions observed. There are at most $\min(n, m)$ slots, each of which awaits at most one function at a time before returning to its loop, so claims minus resolutions is at most $\min(n, m) \le n$ at every instant. The limit is never exceeded.

**Termination and progress.** Each claim consumes one of the finitely many indices, so at most $m$ claims can ever occur, and each slot executes one await per claim. The statement guarantees that no function rejects, so no await abandons a slot: after the $m$-th resolution every slot finds the cursor at $m$, exits its loop, and the join over the slots completes. The returned promise therefore resolves only after all $m$ functions have resolved, and it does resolve, because every claimed function eventually settles. For $m = 0$ the pool opens no slots at all and the join over an empty set completes immediately, which is why the empty authored check expects completion at time $0$ with a peak of $0$ pending promises.

**Work conservation.** Whenever a slot becomes free and the cursor is still before the end, that slot claims immediately, so the pool never leaves a slot idle while unstarted work remains. This is a liveness property rather than a safety one: it is what makes the completion time as small as the ordering constraint allows, and it is why the third function starts at $300$ rather than at $400$.

## 5. How the limit changes the schedule

The three official instances differ only in $n$, and the comparison isolates what the pool limit buys.

| Limit $n$ | Start times | Finish times | Completion time | Peak pending |
|---|---|---|---|---|
| 1 | 0, 300, 700 | 300, 700, 900 | 900 ms, the total duration | 1 |
| 2 | 0, 0, 300 | 300, 400, 500 | 500 ms | 2 |
| 5 | 0, 0, 0 | 300, 400, 200 | 400 ms, the longest duration | 3 |

Two regimes are visible. When the limit reaches or exceeds the number of functions, every function starts at time $0$, the peak pending count is the number of functions, and the completion time collapses to the longest single duration. When the limit is smaller, the completion time is the largest slot load, and it lies between the average load $\lceil \sum_i d_i / n \rceil$ and Graham's list-scheduling bound

$$
M \;\le\; \frac{1}{n}\sum_{i} d_i \;+\; \left(1 - \frac{1}{n}\right) \max_i d_i ,
$$

where $d_i$ denotes duration $i$. For the traced instance the average load is $\lceil 900 / 2 \rceil = 450$ and the bound is $450 + 200 = 650$, both consistent with the observed $500$.

## 6. Traps this instance exposes

| Trap | The tempting but wrong move | What this instance reveals |
|---|---|---|
| Batch instead of pool | start the first $n$ functions and wait for all of them before starting more | the third function would start at $400$ and the pool would finish at $600$, not $500$ |
| Ignore the limit | start every function at once | peak pending would be $3$ for a limit of $2$; the limit is a hard constraint, not a target |
| Serialise everything | await each function inside one loop before the next | that is the $n = 1$ schedule, finishing at $900$ in this instance |
| Split the claim | read the cursor, then await something, then advance it | two slots could read the same value and run the same function twice, or skip an index |
| Slots versus limit | open $n$ slots without bounding by the number of functions | harmless here but wasteful; with $m = 0$ and $n \ge 1$ the clamp is what keeps the pool's join empty and immediately complete |
| Stop early | resolve the returned promise when the first slot's loop ends | a slot exiting says nothing about the other slots' pending promises; the join must cover every slot |
| Assume durations | schedule by shortest or longest duration first | functions must start in array order, so durations may not influence who claims an index; the fastest-slot check with durations `10,2,2,2,2` and $n = 2$ shows the reusable slot claiming indices $2,3,4$ in order rather than reordering the work |
| Assume rejection | treat a failing function as ordinary work | the contract guarantees no function rejects; if one did, that slot would leave its loop early, and the pool's joined promise would not resolve normally |

Rows four and six are the ones that actually decide correctness. The claim must be indivisible with respect to the awaits around it, and completion must be signalled by the last slot to finish rather than by the first.

## 7. Complexity: linear bookkeeping over a bounded pool

Let $m = \text{functions.length}$ with $0 \le m \le 10$ and $1 \le n \le 10$ as the statement guarantees, so the pool opens $w = \min(n, m)$ slots.

**Scheduling work.** Exactly $m$ claims occur, each performing a constant amount of state change, and exactly $m$ awaits are issued, one per claimed function. The join covers $w$ slots. The pool's own administrative cost is therefore

$$
O(m)
$$

operations, independent of how long the functions take; the wall-clock completion time is instead governed by the workload, $M = \max$ over slots of that slot's load, bounded below by $\max(\max_i d_i,\ \lceil \sum_i d_i / n \rceil)$ and above by the list-scheduling bound of section 5.

**Auxiliary space.** The pool holds the cursor, the pending and completed counts, and the collection of $w$ slot tasks, so its own state is $O(w) = O(\min(n, m))$, which is at most $n$. No copy of the function array is made, and no per-index bookkeeping array is needed, because the cursor alone certifies which indices have been claimed.

**Why no ordering structure is required.** A priority queue of ready work would be redundant: the array order makes the claim order a simple increasing counter, and the only competition is over *who* claims next, which is decided by which slot frees first. That is why the same loop serves every value of $n$, from strictly serial execution up to fully parallel execution, without any change to the shared state beyond the size of the pool.
