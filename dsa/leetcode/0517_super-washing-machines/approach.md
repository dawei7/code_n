## General

The final number of dresses in every machine is forced by conservation: moves only transfer dresses, so the total never changes. If there are `n` machines and total `D`, each must finish with `D / n` dresses.

`divmod(sum(machines), n)` returns the quotient `k` and remainder `mod` together. If `mod != 0`, the total cannot be divided evenly among integer machine counts, so no sequence of moves can succeed and the method returns `-1`.

When division is exact, `k` is the target dresses per machine.

**Normalize each machine into surplus or deficit.** During the scan, local `x` is replaced by `x - k`:

- positive `x` means this machine must send out `x` dresses;
- negative `x` means it must receive `-x` dresses;
- zero means it already has the target count.

The normalized values sum to zero because `k` is the average.

**Prefix imbalance describes mandatory boundary traffic.** `s` accumulates normalized values from the first machine through the current one. If `s > 0`, that prefix collectively owns `s` extra dresses, and those dresses must cross the boundary to the right. If `s < 0`, the prefix lacks `-s` dresses, which must cross that boundary from right to left.

Either way, at least `abs(s)` dress transfers must cross that one boundary. Only one net dress can use a particular adjacency in one simultaneous move, so `abs(s)` is a lower bound on the number of moves.

For `[1, 0, 5]`, the target is two and normalized values are `[-1, -2, 3]`. Prefix balances are negative one, negative three, and zero. The middle boundary must carry three dresses leftward over time, proving at least three moves are needed.

**A machine's own surplus is a second lower bound.** In one move, a chosen machine passes one dress to one adjacent machine. It cannot send two dresses simultaneously, even if it has neighbors on both sides. Therefore a machine with local surplus `x > 0` needs at least `x` moves to discharge that surplus.

This constraint is not always captured by one prefix boundary because the machine may need to send some dresses left and some right. For `[0, 3, 0]`, the target is one and normalized values are `[-1, 2, -1]`. Prefix imbalance magnitude never exceeds one, but the middle machine must send two dresses in two different moves. The local surplus bound correctly raises the answer to two.

Negative local `x` does not form the same bound: a deficient machine can receive one dress from its left neighbor and one from its right neighbor simultaneously because those are two different sending machines. That is why the code considers `x`, not `abs(x)`, as the local term.

**Combine all unavoidable bottlenecks.** At every index, the source updates

`ans = max(ans, abs(s), x)`.

Across the full scan, this becomes the maximum boundary flow magnitude and maximum single-machine surplus. Any valid schedule needs at least that many moves.

The deeper greedy fact is that this lower bound is achievable on a line. Prefix balances uniquely determine the net number of dresses that must cross each boundary. Transfers can be pipelined simultaneously across different boundaries. A machine's positive surplus accounts for the only conflict where its required outgoing transfers to one or both sides cannot occur more than one per move. Once both the maximum edge flow and maximum local outgoing load are respected, the necessary unit transfers can be scheduled within their maximum. Therefore the combined lower bound is also the minimum.

One way to visualize this is as flow. Each normalized positive machine supplies units and each negative machine demands units. Prefix `s` is the net flow across the boundary after that machine. Different machines can send concurrently, allowing flows along a chain to advance in parallel, while each source machine's one-send-per-round capacity is enforced by its surplus term.

For the last prefix, `s` returns to zero because total surplus equals total deficit. This is a useful consistency check but does not erase larger imbalances encountered earlier; `ans` retains their maximum.

The algorithm does not mutate `machines`. Reassigning loop variable `x` changes only the local scalar, unlike an implementation that writes normalized values back into the array.

Correctness combines feasibility and optimality. Divisibility is necessary and sufficient for an integer target. For feasible inputs, boundary imbalance and local surplus establish the lower bound recorded by `ans`. The line-flow scheduling argument shows no additional bottleneck exists, so that lower bound can be attained and is the minimum number of simultaneous moves.

## Complexity detail

Computing the sum scans $n$ values, and the main loop scans them once more. Each iteration performs constant arithmetic, so total time is $O(n)$.

Only `n`, `k`, `mod`, `ans`, `s`, and the local `x` are stored. Auxiliary space is $O(1)$, and the input list is not copied or modified.

## Alternatives and edge cases

- **Simulate individual moves:** Choosing transfers round by round creates a huge state space and obscures the closed-form bottlenecks. The prefix method derives the answer without constructing a schedule.
- **Use only maximum prefix imbalance:** This fails for `[0, 3, 0]`, where one machine must send twice but every boundary needs net flow only one.
- **Use only maximum local surplus:** This misses cases such as `[1, 0, 5]`, where several dresses must cross the same boundary over three moves.
- **Non-divisible total:** Return `-1` immediately because dresses cannot be split fractionally.
- **Already balanced:** Every normalized value and prefix is zero, so the answer remains zero.
- **One machine:** Its total is automatically divisible by one and it already equals the average, producing zero moves.
- **Deficit between two suppliers:** It may receive from both sides in one move, explaining why negative local imbalance is not converted with `abs`.
- **Large counts:** Python integers avoid overflow in totals and prefix balances; fixed-width languages should use a sufficiently wide type.
- **Final prefix:** It must be zero for feasible normalization, but the maximum earlier absolute prefix determines cross-boundary work.
