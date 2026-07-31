## Function Contract

**Inputs**

- `operations`: A list beginning with `"EventManager"`, followed by method names from `"updatePriority"` and `"pollHighest"`.
- `arguments`: A parallel list containing the constructor or method arguments for each operation.

The constructor receives one list of distinct `[eventId, priority]` pairs. An update receives `[eventId, newPriority]`; its ID is guaranteed to name an active event. A poll receives no arguments, removes at most one event, and ranks active events by greater priority first and then smaller ID first.

Let $E$ be the number of initial events and let $Q$ be the number of subsequent method calls.

**Return value**

Return one result for every operation: `null` for construction and priority updates, the removed `eventId` for a nonempty `pollHighest`, and `-1` for a poll on an empty manager.
