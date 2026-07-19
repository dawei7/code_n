## General
**Sort starts and endings as separate event streams**

Sort all start times and all end times separately. At the next start, reuse a room if the earliest ending is no later than that start; otherwise allocate another room.

The end pointer counts meetings already finished before the current start. Therefore `started - finished` is the number of occupied rooms, and its maximum is the required capacity.

**Peak simultaneous occupancy is the room count**

Before processing a start, every ending no later than that time can release its room. If the earliest remaining ending is later, all currently allocated rooms are still occupied and the new meeting needs another one. The sweep therefore maintains the exact number of active meetings after each event. Its maximum is necessary because those meetings overlap, and sufficient because a released room is always reused whenever possible.

## Complexity detail
The two sorts cost $O(n \log n)$; the pointers each move at most `n` times. The two event arrays use $O(n)$ space.

## Alternatives and edge cases
- **Check overlap at every time or against every interval:** can take $O(n^2)$ or depend on the coordinate range.
- Meetings that end exactly when another starts can share a room; an empty schedule needs zero rooms.
