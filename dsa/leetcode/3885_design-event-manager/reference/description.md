### 1. Description

You are given an initial list of events, where each event has a unique `eventId` and a `priority`.

Implement the `EventManager` class:

- `EventManager(int[][] events)` Initializes the manager with the given events, where $\text{events}[i] = [\text{eventId}_{i}, priority_​​​​​​​i]$.

- `void updatePriority(int eventId, int newPriority)` Updates the priority of the **active** event with id `eventId` to `newPriority`.

- `int pollHighest()` Removes and returns the `eventId` of the **active** event with the **highest** priority. If multiple active events have the same priority, return the **smallest** `eventId` among them. If there are no active events, return -1.

An event is called **active** if it has not been removed by `pollHighest()`.

### 2. Function Contract

**Inputs**

- `operations`: A list beginning with `"EventManager"`, followed by method names from `"updatePriority"` and `"pollHighest"`.
- `arguments`: A parallel list containing the constructor or method arguments for each operation.

The constructor receives one list of distinct `[eventId, priority]` pairs. An update receives `[eventId, newPriority]`; its ID is guaranteed to name an active event. A poll receives no arguments, removes at most one event, and ranks active events by greater priority first and then smaller ID first.

Let $E$ be the number of initial events and let $Q$ be the number of subsequent method calls.

**Return value**

Return one result for every operation: `null` for construction and priority updates, the removed `eventId` for a nonempty `pollHighest`, and `-1` for a poll on an empty manager.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:**

["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"]

[[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []]

**Output:**

[null, 2, null, 5, 9]

**Explanation**

EventManager eventManager = new EventManager([[5,7], [2,7], [9,4]]); // Initializes the manager with three events

eventManager.pollHighest(); // both events 5 and 2 have priority 7, so return the smaller id 2

eventManager.updatePriority(9, 7); // event 9 now has priority 7

eventManager.pollHighest(); // remaining highest priority events are 5 and 9, return 5

eventManager.pollHighest(); // return 9</div>
#### Example 2

<div class="example-block">
**Input:**

["EventManager", "pollHighest", "pollHighest", "pollHighest"]

[[[[4, 1], [7, 2]]], [], [], []]

**Output:**

[null, 7, 4, -1]

**Explanation**

EventManager eventManager = new EventManager([[4,1], [7,2]]); // Initializes the manager with two events

eventManager.pollHighest(); // return 7

eventManager.pollHighest(); // return 4

eventManager.pollHighest(); // no events remain, return -1</div>

### 4. Constraints

- $1 \le \text{events.length} \le 10^{5}$

- $\text{events}[i] = [eventId, priority]$

- $1 \le eventId \le 10^{9}$

- $1 \le priority \le 10^{9}$

- All the values of `eventId` in `events` are **unique**.

- $1 \le newPriority \le 10^{9}$

- For every call to `updatePriority`, `eventId` refers to an **active** event.

- At most $10^{5}$ calls in **total** will be made to `updatePriority` and `pollHighest`.