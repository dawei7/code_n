# Implement Router

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3508 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Design, Queue, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/implement-router/) |

## Problem Description

### Goal

Design a `Router` that stores network packets. Each packet is identified by three integers: its `source` machine, its `destination` machine, and the `timestamp` at which it arrived. The constructor receives `memoryLimit`, the maximum number of packets that may be stored simultaneously.

`addPacket` attempts to store one packet. It must reject a packet when the same `(source, destination, timestamp)` triple is already present. Otherwise it stores the packet and returns `true`; if this successful insertion would exceed the memory limit, it first removes the oldest stored packet. Calls to `addPacket` arrive in non-decreasing timestamp order.

`forwardPacket` removes and returns the oldest stored packet in FIFO order as `[source, destination, timestamp]`, or returns an empty list when the router has no packet. `getCount` reports how many packets currently stored for one destination have timestamps inside an inclusive interval. Implement all operations for a sequence of at most $10^5$ method calls.

### Function Contract

**Inputs**

- `Router(memoryLimit)`: Creates an empty router that can retain at most `memoryLimit` packets.
- `addPacket(source, destination, timestamp)`: Attempts to insert the specified packet.
- `forwardPacket()`: Removes and returns the next FIFO packet, if one exists.
- `getCount(destination, startTime, endTime)`: Counts currently stored packets for `destination` whose timestamps lie in `[startTime, endTime]`.

The constraints are $2 \le \texttt{memoryLimit} \le 10^5$, $1 \le \texttt{source},\texttt{destination} \le 2\cdot 10^5$, $1 \le \texttt{timestamp} \le 10^9$, and $1 \le \texttt{startTime} \le \texttt{endTime} \le 10^9$. At most $10^5$ calls are made across the three public methods.

**Return value**

`addPacket` returns whether insertion succeeded. `forwardPacket` returns the removed packet or `[]`. `getCount` returns the requested active-packet count. The constructor has no return value.

### Examples

**Example 1**

- Input: `operations = ["Router","addPacket","addPacket","addPacket","addPacket","addPacket","forwardPacket","addPacket","getCount"]`, `arguments = [[3],[1,4,90],[2,5,90],[1,4,90],[3,5,95],[4,5,105],[],[5,2,110],[5,100,110]]`
- Output: `[null,true,true,false,true,true,[2,5,90],true,1]`
- Explanation: The repeated `(1,4,90)` packet is rejected. Adding `(4,5,105)` at capacity evicts `(1,4,90)`, and forwarding then removes `(2,5,90)`.

**Example 2**

- Input: `operations = ["Router","addPacket","forwardPacket","forwardPacket"]`, `arguments = [[2],[7,4,90],[],[]]`
- Output: `[null,true,[7,4,90],[]]`
- Explanation: The first forwarding call removes the only packet; the next call finds the router empty.
