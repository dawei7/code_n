## Description

You are given an initial list of events, where each event has a unique `eventId` and a `priority`.

Implement the `EventManager` class:

<ul>
	<li>`EventManager(int[][] events)` Initializes the manager with the given events, where `events[i] = [eventId_i, priority_​​​​​​​i]`.</li>
	<li>`void updatePriority(int eventId, int newPriority)` Updates the priority of the **active** event with id `eventId` to `newPriority`.</li>
	<li>`int pollHighest()` Removes and returns the `eventId` of the **active** event with the **highest** priority. If multiple active events have the same priority, return the **smallest** `eventId` among them. If there are no active events, return -1.</li>
</ul>

An event is called **active** if it has not been removed by `pollHighest()`.
