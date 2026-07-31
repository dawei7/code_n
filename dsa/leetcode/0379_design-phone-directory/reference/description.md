## Description

Design a phone directory with `maxNumbers` initially empty slots. It must allocate an available number, report whether a specified slot is available, and release a slot for reuse.

Implement the `PhoneDirectory` class:

- `PhoneDirectory(maxNumbers)` initializes the directory with that many available slots.
- `get()` reserves and returns any unassigned number, or returns `-1` when none remains.
- `check(number)` returns whether `number` is currently available.
- `release(number)` makes the specified slot available again.
