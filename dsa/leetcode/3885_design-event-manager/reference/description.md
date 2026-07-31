## Description

An initial collection of events is provided. Every event has a unique `eventId` and an associated `priority`.

Implement the stateful `EventManager` class with these operations:

- `EventManager(events)` initializes all listed events, where each pair is `[eventId, priority]`.
- `updatePriority(eventId, newPriority)` replaces the priority of the specified active event.
- `pollHighest()` removes and returns the active event with greatest priority. If several active events share that priority, it removes the one with the smallest `eventId`. It returns `-1` when no active event remains.

An event is active exactly until it is removed by `pollHighest()`; priority updates do not remove it.
