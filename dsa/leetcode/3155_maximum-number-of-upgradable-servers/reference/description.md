## Description

A company operates $n$ data centers and wants to upgrade as many of their existing servers as possible. For center $i$, `count[i]` is its number of servers, `upgrade[i]` is the cost to upgrade one server, `sell[i]` is the money received by selling one server, and `money[i]` is the cash initially available there.

Each server at a center can be used in at most one way: it may be upgraded, sold to finance other upgrades at that same center, or left unchanged. Funds cannot be transferred between data centers. Return the maximum number of servers that can be upgraded independently at every center.
