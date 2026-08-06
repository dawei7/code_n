## Description

Design a data structure that can efficiently manage data packets in a network router. Each data packet consists of the following attributes:

<ul>
	<li>`source`: A unique identifier for the machine that generated the packet.</li>
	<li>`destination`: A unique identifier for the target machine.</li>
	<li>`timestamp`: The time at which the packet arrived at the router.</li>
</ul>

Implement the `Router` class:

`Router(int memoryLimit)`: Initializes the Router object with a fixed memory limit.

<ul>
	<li>`memoryLimit` is the **maximum** number of packets the router can store at any given time.</li>
	<li>If adding a new packet would exceed this limit, the **oldest** packet must be removed to free up space.</li>
</ul>

`bool addPacket(int source, int destination, int timestamp)`: Adds a packet with the given attributes to the router.

<ul>
	<li>A packet is considered a duplicate if another packet with the same `source`, `destination`, and `timestamp` already exists in the router.</li>
	<li>Return `true` if the packet is successfully added (i.e., it is not a duplicate); otherwise return `false`.</li>
</ul>

`int[] forwardPacket()`: Forwards the next packet in FIFO (First In First Out) order.

<ul>
	<li>Remove the packet from storage.</li>
	<li>Return the packet as an array `[source, destination, timestamp]`.</li>
	<li>If there are no packets to forward, return an empty array.</li>
</ul>

`int getCount(int destination, int startTime, int endTime)`:

<ul>
	<li>Returns the number of packets currently stored in the router (i.e., not yet forwarded) that have the specified destination and have timestamps in the inclusive range `[startTime, endTime]`.</li>
</ul>

**Note** that queries for `addPacket` will be made in non-decreasing order of `timestamp`.
