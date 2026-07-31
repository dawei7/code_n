## General

Keep two pieces of closure state: whether a throttle window is active and either no pending call or the latest pending receiver-and-arguments tuple. On an invocation outside a window, call `fn` immediately, mark the window active, and schedule its release after `t` milliseconds. During a window, replace the pending tuple without starting another timer.

When the timer fires, clear the window if nothing is pending. Otherwise, remove the saved tuple, invoke `fn` with its receiver and arguments, and schedule the next release after another complete interval. Removing the tuple before invoking matters because a reentrant call must become new pending work rather than being erased afterward.

At most one timer and one pending tuple exist. The first call in each idle period executes immediately; every active period retains exactly the latest blocked call; and a trailing execution begins the next period. These state transitions are precisely the throttle contract.

## Complexity detail

Each returned-function invocation and timer callback performs $O(1)$ work, and the closure retains one timer state plus one pending tuple, using $O(1)$ auxiliary space under the fixed argument bound. The app-local timeline simulator processes the bounded call schedule separately.

The source permits at most ten calls, so a bounded-domain certificate replaces unreliable scaling tiers. Its regression runs the real closure with deterministic fake timers across the authored boundary schedules.

## Alternatives and edge cases

- **Drop every blocked call:** A leading-only throttle is simpler but violates the required latest trailing execution.
- **Queue every blocked call:** Preserving all calls violates latest-only coalescing and can use unbounded space outside the judge limit.
- Empty argument arrays still represent a pending invocation and cannot share a falsy sentinel with “no pending call.”
- A trailing execution starts a new full interval; it does not merely finish the previous one.
- Preserve the invocation receiver when forwarding to `fn`, not only the positional arguments.
