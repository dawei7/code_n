# Guided Example: Promise Time Limit

## 1. The instance and the two candidate outcomes

A time-limited wrapper is a *race with a deadline*, and every part of its behaviour follows from one question: which of two pending outcomes settles first. The instance below is the statement's first example, in which the deadline is the faster candidate.

$$
\text{duration of the source} = 100\ \text{ms}, \qquad \text{limit}\ t = 50\ \text{ms}, \qquad \text{source arguments} = [5], \qquad \text{source result} = 25 .
$$

The required outcome is that the wrapper rejects at $50$ milliseconds with the message `Time Limit Exceeded`.

Two facts about that outcome deserve attention before the machinery is laid out. First, the wrapper rejects at $50$ milliseconds, exactly the deadline, and not at $100$ milliseconds when the source would have produced $25$. Second, the source function is not stopped by that rejection: a promise cannot be cancelled once it has been created, so the source continues toward its own settlement at $100$ milliseconds, and whatever it produces is simply no longer connected to anything the caller can observe.

## 2. The two candidates and what each contributes

The wrapper constructs two pending outcomes and forwards the caller's arguments to one of them.

| Candidate | Created by | Settles at | Settles with | Wins in this instance |
|---|---|---|---|---|
| the source outcome | invoking the wrapped function with the forwarded arguments | $100$ ms | the value $25$, since $5 \times 5 = 25$ | no |
| the deadline outcome | starting a timer for $t$ milliseconds that fails with the time-limit message | $50$ ms | the text `Time Limit Exceeded` | yes |

The wrapper's entire decision procedure is to adopt whichever candidate settles first and to ignore the other. Because only the first settlement is adopted, the wrapper settles exactly once, even though both candidates eventually settle; a promise that has already settled ignores every later settlement attempt.

Argument forwarding is part of the contract and not a detail: the statement requires that the wrapped function receive the arguments supplied to the time-limited function, and the constraint $0 \le \text{inputs.length} \le 10$ admits anything from no arguments at all to ten of them. The authored check that passes the ten values $0$ through $9$ to a summing source expects $45$, so the wrapper must forward the argument list as a whole rather than a fixed number of positions.

## 3. Timeline of the traced instance

Each row is an event on the wrapper's timeline; the outcome column shows which candidate, if any, has settled.

| Time | Event | Source candidate | Deadline candidate | Wrapper |
|---|---|---|---|---|
| 0 | wrapper called with the argument $5$; the deadline timer starts; the source is invoked and begins its own $100$ ms sleep | pending, wakes at 100 | pending, fires at 50 | pending |
| 50 | the timer fires and fails with the time-limit message | pending, still asleep | settled: rejected | rejects with `Time Limit Exceeded` |
| 50, immediately after | the losing candidate can no longer influence anything; the deadline timer has already fired | pending | settled | settled |
| 100 | the source's sleep ends and it returns $25$ | settled with $25$, discarded | settled | settled, unchanged |

The discarded settlement at $100$ milliseconds is the semantic heart of the problem. The wrapper answered the caller at $50$ milliseconds, and a second answer is impossible; the value $25$ computed at $100$ milliseconds is correct but irrelevant. A design that instead waited for the source and then compared a stopwatch reading against $t$ would deliver the same rejection, but only at $100$ milliseconds, which contradicts the expected rejection time and defeats the purpose of a limit.

## 4. Which candidate wins, at and near the boundary

The interesting cases are the ones where the two settlement times are close. Writing $T$ for the instant the source settles, the observed behaviour is determined by how the two candidates are ordered.

| Situation | First to settle | Mechanism that decides it | Observed outcome |
|---|---|---|---|
| $T < t$, as in $100$ ms against a limit of $150$ | the source | the source's own wake-up is scheduled for the earlier instant | resolves with the source's value at $T$ |
| $T > t$, as in this instance | the deadline | the timer expires before the source wakes | rejects with the time-limit message at $t$ |
| $T = t$, as in a $25$ ms source against a limit of $25$ | the deadline | two scheduled wake-ups share one instant, and the deadline timer was started *before* the source was invoked, so it precedes the source's own wake-up | rejects with the time-limit message at the shared instant |
| $t = 0$ while the source is already settled, as in a source that returns immediately | the source | an already-settled promise delivers its outcome through the microtask queue, and the entire microtask queue drains before any scheduled timer callback runs | resolves with the source's value, with no wait at all |
| the source rejects before $t$ | the source | the earlier rejection is simply the first settlement | rejects with the source's own error, not with the time-limit message |
| the source rejects after $t$ | the deadline | the wrapper has already settled | rejects with the time-limit message; the later source error is discarded |

The third row establishes that the equality case is not a tie in practice: the deadline is constructed before the source is ever invoked, which places its wake-up earlier in the order of same-instant wake-ups. The fourth row shows that a zero limit does not automatically mean an immediate rejection, because a source that is already settled needs no timer at all to deliver its outcome. Both rows are pinned by authored checks — a $25$ ms source with a $25$ ms limit rejects with the time-limit message, while an immediately resolving source with a limit of $0$ resolves with its value.

## 5. Invariant and correctness of the race

Let $S$ be the source candidate, $D$ the deadline candidate, $T$ the instant $S$ settles if it is allowed to, and $t$ the limit.

**Single-settlement invariant.** The wrapper's returned promise settles at most once, and its state is a function of the first settlement among $S$ and $D$ only. Once either candidate settles, the wrapper's outcome is fixed and no later event — including the other candidate's eventual settlement — can alter it.

*Proof.* The wrapper's promise is settled by the first of the two candidates to settle, and both JavaScript promises and the race construct in the contract's model ignore any settlement attempt after the first. So the wrapper's outcome equals the outcome of $\arg\min$ over the two settlement instants.

**Soundness.** If the wrapper resolves, it resolves with exactly the source's value, because the deadline candidate never resolves — it can only fail — so a resolution can only have come from the source, and no transformation is applied to the value on the way through. If the wrapper rejects, the reason is either the source's own error, which is passed through unchanged, or the defined time-limit message produced by the deadline. Hence no third kind of outcome is possible.

**Completeness and the boundary rule.** With the winner determined by the order of settlement instants, the wrapper's behaviour matches the contract in every regime of section 4: it resolves when the source settles first and rejects otherwise, and the equality case is resolved by the construction order described there rather than left ambiguous. Consequently the observed settlement time is $\min(T, t)$ for the wrapper's own decision, with the deadline winning when the two instants coincide.

**No leak of the losing candidate.** Each call's deadline is scoped to that call, and once the wrapper has settled, the losing timer is cleared so that it cannot fire later. Without that cleanup, a source that resolves at $100$ milliseconds against a limit of $1000$ milliseconds would leave a pending timer behind that fires long after the caller has its answer; if that late failure were never observed it would surface as an unhandled error rather than a harmless no-op.

## 6. Traps this instance exposes

| Trap | The tempting but wrong move | What this instance reveals |
|---|---|---|
| Measure, then decide | await the source, then compare elapsed time against the limit | the rejection would arrive at $100$ ms rather than $50$ ms, contradicting the expected time |
| Reject too early | decide from the arguments or the source's identity instead of racing | the same wrapper is reused across calls with different limits, so the outcome must be per-call |
| Assume cancellation | believe the rejection stops the source's work | the source keeps running to its own settlement; only the caller's view ends at the deadline |
| Forget cleanup | leave the losing timer scheduled | a stale timer fires after the call is long settled and can become an unhandled failure |
| Drop the source error | replace every rejection with the time-limit message | a source that fails before the deadline must reject with its own error, as the immediate-throw and $40$ ms cases show |
| Resurrect a late error | let the delayed source error replace the deadline message | once settled, the wrapper keeps the time-limit message even though the source fails later at $200$ ms |
| Assume a zero limit always rejects | treat $t = 0$ as "reject immediately" | an already-settled source wins through the microtask queue, so a limit of $0$ can still resolve |
| Lossy forwarding | pass a fixed number of arguments | the contract forwards the caller's whole argument list, from zero up to ten values |
| Per-call reuse of the timer | start the deadline once, outside the returned function | the deadline belongs to one call; a shared timer would expire during a later call and reject it spuriously |

The first and the seventh rows are the two that most often produce plausible-looking but wrong behaviour: the first because it satisfies the *decision* without satisfying the *deadline*, and the seventh because it assumes that a limit of zero always outruns the source, which is false when the source has nothing to wait for.

## 7. Complexity: constant bookkeeping around the caller's arguments

Let $k = \text{inputs.length}$ with $0 \le k \le 10$ as the statement guarantees.

**Work.** Each call does a constant amount of work: it starts one timer, constructs two pending outcomes, and forwards $k$ arguments to the source. Forwarding touches each argument once, so the wrapper's own cost is

$$
O(k)
$$

which is $O(1)$ under the stated constraint, plus the cost of the wrapped function itself, which the wrapper observes but does not execute. The caller's observed latency is the earlier of the two settlement instants, $\min(T, t)$ under the boundary rule of section 4, so the limit bounds how long the caller waits even if the source would never settle.

**Auxiliary space.** The wrapper holds one timer handle, one pending source outcome, and the forwarded argument list, so its own state is $O(k) = O(1)$ plus a single reference to the source's eventual value — the value is passed through, never copied or buffered. The wrapper adds no queue, no table and no per-call history, which is what allows it to be applied as a decorator to any promise-returning function without changing that function's storage behaviour.

**Why the limit cannot be improved on.** A wrapper that must reject whenever the source has not settled by $t$ cannot avoid waiting until $t$ to know that fact, so $t$ is a lower bound on the rejection path, and the source's own settlement time is a lower bound on the resolution path. Racing the two candidates attains both bounds simultaneously, which is the strongest guarantee available without the ability to cancel the source.
