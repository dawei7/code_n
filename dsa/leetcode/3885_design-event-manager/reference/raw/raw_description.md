## Description

You are given an initial list of events, where each event has a unique `eventId` and a `priority`.

Implement the `EventManager` class:

	- `EventManager(int[][] events)` Initializes the manager with the given events, where `events[i] = [eventId_i, priority_​​​​​​​i]`.

	- `void updatePriority(int eventId, int newPriority)` Updates the priority of the **active** event with id `eventId` to `newPriority`.

	- `int pollHighest()` Removes and returns the `eventId` of the **active** event with the **highest** priority. If multiple active events have the same priority, return the **smallest** `eventId` among them. If there are no active events, return -1.

An event is called **active** if it has not been removed by `pollHighest()`.

**Example 1:**

<div class="example-block">
**Input:**

<span class="example-io">["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"]

[[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []]</span>

**Output:**

<span class="example-io">[null, 2, null, 5, 9] </span>

**Explanation**

EventManager eventManager = new EventManager([[5,7], [2,7], [9,4]]); // Initializes the manager with three events

eventManager.pollHighest(); // both events 5 and 2 have priority 7, so return the smaller id 2

eventManager.updatePriority(9, 7); // event 9 now has priority 7

eventManager.pollHighest(); // remaining highest priority events are 5 and 9, return 5

eventManager.pollHighest(); // return 9</div>

**Example 2:**

<div class="example-block">
**Input:**

<span class="example-io">["EventManager", "pollHighest", "pollHighest", "pollHighest"]

[[[[4, 1], [7, 2]]], [], [], []]</span>

**Output:**

<span class="example-io">[null, 7, 4, -1] </span>

**Explanation**

EventManager eventManager = new EventManager([[4,1], [7,2]]); // Initializes the manager with two events

eventManager.pollHighest(); // return 7

eventManager.pollHighest(); // return 4

eventManager.pollHighest(); // no events remain, return -1</div>

**Constraints:**

	- `1 <= events.length <= 10^5`

	- `events[i] = [eventId, priority]`

	- `1 <= eventId <= 10^9`

	- `1 <= priority <= 10^9`

	- All the values of `eventId` in `events` are **unique**.

	- `1 <= newPriority <= 10^9`

	- For every call to `updatePriority`, `eventId` refers to an **active** event.

	- At most `10^5` calls in **total** will be made to `updatePriority` and `pollHighest`.
