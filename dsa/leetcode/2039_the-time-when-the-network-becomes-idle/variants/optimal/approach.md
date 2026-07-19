## General
**Find every shortest round-trip time**

Because every channel takes one second, breadth-first search from server `0`
gives the shortest edge distance $d_i$ to each server $i$. Its first request
and reply require

$$
R_i = 2d_i
$$

seconds for the round trip.

**Locate the final resend before the first reply**

Server $i$ sends at seconds $0,p_i,2p_i,\ldots$ only while it has not received
the first reply. Since the reply arriving at second $R_i$ is checked before a
possible resend, the last send time is the greatest multiple of $p_i$ strictly
less than $R_i$:

$$
L_i =
\left\lfloor\frac{R_i-1}{p_i}\right\rfloor p_i.
$$

The reply to that last copy arrives at second $L_i+R_i$. This formula also
covers the no-resend case: when $p_i \ge R_i$, it gives $L_i=0$.

**Wait one second beyond the final arrival**

No later copy can exist for a server because $L_i$ is its last send, and every
copy uses the same shortest round-trip duration. Therefore the latest message
activity anywhere in the network occurs at the maximum of $L_i+R_i$ over all
data servers. The network is first idle at the following second, so return that
maximum plus one.

## Complexity detail
Building the adjacency lists and performing BFS takes $O(N+E)$ time. Computing
the final arrival for each server takes another $O(N)$ time. The graph,
distance array, and BFS queue occupy $O(N+E)$ space.

## Alternatives and edge cases
- **Shortest-path search from every server:** Repeating BFS is correct but can
  take $O(N(N+E))$ time; one BFS from the common master suffices.
- **Second-by-second message simulation:** Explicitly generating every resend
  can be enormous when patience is small and obscures the closed-form final
  send time.
- A patience value equal to the round-trip time causes no resend at that time,
  because the first reply is processed first.
- With patience `1`, the last resend occurs exactly one second before the first
  reply.
- Multiple shortest paths do not affect timing because only their common
  length matters.
- The master has patience `0` but never sends an originating request, so it is
  excluded from the resend calculation.
- The requested answer is one second after the latest arrival, not the arrival
  second itself.
