## Description

A signal must travel through a directed weighted graph whose `n` nodes are numbered from `0` through `n - 1`. Every entry `edges[i] = [u_i, v_i, t_i]` describes a one-way connection from `u_i` to `v_i` that takes `t_i` seconds. The signal begins at `source` at time zero with the supplied amount of `power`.

Forwarding the signal from node `u` along any one of its outgoing edges requires at least `cost[u]` remaining power. That amount is consumed when the signal leaves `u`; merely arriving at a node consumes nothing. Traversing the chosen edge then adds its travel time. Consequently, a path is legal only when the signal can pay the departure cost at every node it leaves, while the cost at its final node need not be paid.

Find the minimum time in which the signal can reach `target`. If several legal paths attain that same minimum time, choose the greatest remaining power among them. Return those two values as `[minimum time, maximum remaining power]`, or return `[-1, -1]` when no legal directed path can reach the target.
