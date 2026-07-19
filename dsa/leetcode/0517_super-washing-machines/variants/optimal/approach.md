## General
**Reject totals that cannot be shared equally**

If the total number of dresses is not divisible by the machine count, no sequence of transfers can make all loads equal. Otherwise let `target = total / n` and express each machine's excess as `load - target`.

**Measure forced flow across every boundary**

Maintain the prefix balance after each machine. A positive balance means that many dresses must eventually cross from the processed prefix to its right; a negative balance means its magnitude must cross leftward. Only the two machines adjacent to that boundary can transfer a dress across it, so `abs(prefix_balance)` is a lower bound on the move count.

**Measure forced outgoing work at each machine**

A machine with positive excess must send that many dresses away. Because one machine can send only one dress per simultaneous move, its excess is another lower bound. A deficit machine may receive from both sides in the same round, so its negative excess does not impose the analogous outgoing bound.

**Take the largest congestion value**

Scan once and maximize both `abs(prefix_balance)` and each positive excess. The prefix values prescribe the net flow on every edge of the line. These transfers can be pipelined: in each round, machines send along still-unsatisfied flow directions, subject to one outgoing dress per machine. On a path, the edge-flow load and each node's required outgoing load are exactly the possible bottlenecks, so their maximum number of rounds is also achievable.

## Complexity detail
One pass computes the total and a second pass updates prefix balance and the answer, for $O(n)$ time. Apart from scalar counters, no storage grows with the input, so space is $O(1)$.

## Alternatives and edge cases
- **Recompute every prefix sum independently:** uses the same formula but takes $O(n^2)$ time.
- **Explicit round-by-round simulation:** can be difficult to schedule optimally and may perform work proportional to the answer as well as the input size.
- **Prefix-balance array:** clarifies the flows but uses $O(n)$ space that the streaming scan avoids.
- **Indivisible total:** must return `-1` before defining an integer target.
- **Already balanced:** every excess and prefix balance is zero, so the answer is zero.
- **One overloaded machine:** its positive excess may dominate all boundary loads.
- **Long-distance deficit:** a prefix boundary may dominate even when no single surplus is as large.
