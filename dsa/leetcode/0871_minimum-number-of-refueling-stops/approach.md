## General

The car must pass stations in increasing position order, but it does not have to decide immediately whether it stopped at every reachable station. The central greedy idea is to postpone that decision. Whenever the car passes a station, remember its fuel amount. If the car later discovers that it cannot reach the next position, retroactively choose the largest fuel supply among all stations it has already passed.

This “retroactive” wording is an accounting technique, not time travel. If the algorithm later selects a previously passed station, interpret the journey as having stopped there when the car originally reached it. Delaying the decision is safe because carrying extra fuel earlier has no penalty: the tank has unlimited capacity, fuel never expires, and fuel consumption is always exactly one liter per mile.

**Track the physical fuel between consecutive positions.** The variable `pre` is the previous station position, initially the start at position zero. For a station at `pos`, the distance just traveled is `pos - pre`, so the solution subtracts that amount from `startFuel`. Although the variable retains the original parameter name, after the first update it represents current tank balance, not merely initial fuel.

If the balance is nonnegative, the car can reach `pos` without selecting another stop. A balance of exactly zero is valid: the statement explicitly allows arriving at a station or the target with no fuel remaining.

If the balance becomes negative, the initially planned journey was short by some fuel. The heap contains fuel amounts from stations that the car had already reached. The solution repeatedly selects the largest one until the balance becomes nonnegative. Each selection adds one stop to `ans`.

**How Python provides a max-heap.** Python's `heapq` removes the smallest stored number. The solution inserts `-fuel`, so the most negative entry represents the largest actual fuel amount. Calling `heappop(pq)` returns that negative value, and `startFuel -= heappop(pq)` subtracts a negative number, thereby adding the selected station's fuel to the balance.

The current station is pushed only after the algorithm proves it can reach that station. This order prevents an impossible circular argument: fuel located at position `pos` cannot help the car travel to `pos` itself. Once the station is reachable, its negated fuel is added to the heap and becomes available for a later shortage.

**Why choosing the largest passed supply minimizes stops.** Suppose a shortage requires the algorithm to select one of several reachable stations. Every selection costs exactly one stop, regardless of how much fuel the station contains. Choosing the station with the largest fuel gives at least as much remaining range as choosing any smaller station for the same cost of one stop. Therefore it can never require more future stops.

An exchange argument makes this precise. Take any feasible plan using the minimum number of stops up to the current position. If that plan selected a smaller passed station while leaving a larger passed station unused, exchange the two. The number of stops stays the same, and the car has no less fuel at every subsequent point. The modified plan is still feasible. Repeating this exchange shows that, for any fixed number of retroactive stops, selecting the largest available supplies maximizes reachable distance. Consequently, when the greedy algorithm needs $q$ heap removals to erase a deficit, no plan using fewer than $q$ passed stations could have supplied more fuel and reached the same point.

**The target sentinel.** The input contains only stations strictly before `target`. The solution appends `[target, 0]` and then processes it like one final station. This avoids a separate block for the last drive. When the sentinel is reached, the same shortage logic selects past stations as needed. Its zero fuel is pushed only after arrival, where it has no effect.

Appending the sentinel mutates the local `stations` list supplied to the method. That does not change the algorithm's result, but callers that reuse the list would observe the extra pair. A nonmutating version could iterate over `stations + [[target, 0]]` instead.

**Failure detection.** If the balance is negative and the heap is empty, every station already reached has already been selected, or no station was reachable at all. No future station can help because the car cannot reach it. Returning `-1` is therefore necessary. Conversely, if the loop reaches the target sentinel with a nonnegative balance, the selected historical stops describe a valid journey.

For `target = 100`, `startFuel = 10`, and stations `[[10,60],[20,30],[30,30],[60,40]]`, the car reaches position 10 with zero and remembers 60. Attempting position 20 makes the balance negative, so it retroactively takes 60 and has enough to continue. Later, attempting the target creates another shortage. At that moment the heap contains fuels from all reachable unselected stations, and choosing 40 is sufficient. Exactly two heap removals mean exactly two actual stops.

## Complexity detail

Let $n$ be the number of original stations. Each station, plus the target sentinel, is processed once. Every fuel amount is pushed once and popped at most once. A heap operation costs $O(\log n)$.

- **Time complexity:** $O(n\log n)$.
- **Space complexity:** $O(n)$ for the heap, which may retain fuel from all passed but unselected stations.

The appended sentinel adds one list entry and does not change either bound. The algorithm assumes the stations are already ordered by strictly increasing position, as guaranteed by the input contract; it does not pay for sorting.

## Alternatives and edge cases

- **Dynamic programming by stop count:** Let `dp[t]` be the farthest position reachable with exactly `t` stops. Updating it backward for each station gives $O(n^2)$ time and $O(n)$ space. It is correct but slower than the heap method.
- **Refuel immediately at every station:** This certainly may reach far, but it can make many unnecessary stops and does not minimize their count.
- **Choose the nearest or smallest station during a shortage:** Every stop has equal cost, so selecting less fuel can only reduce reach and may force additional stops.
- **Initial fuel already reaches target:** The target sentinel is reached without a shortage, the heap is never popped, and the answer is zero.
- **Cannot reach the first station:** Fuel becomes negative while the heap is empty, so the method immediately returns `-1`.
- **Arrive with exactly zero fuel:** The shortage loop uses `startFuel < 0`. Zero is accepted at both stations and the destination, matching the contract.
- **No stations:** Only the target sentinel is processed. The result is zero if initial fuel is sufficient and `-1` otherwise.
- **Several stations at useful positions:** They enter the heap only after being reached. A later deficit may select several of them, always in descending fuel order.
- **Unused passed stations:** Remaining heap entries simply represent stations the optimal plan skipped. There is no requirement to consume their fuel.
- **Zero-fuel target sentinel:** It is not a real refueling opportunity and never increases range; it exists only to reuse the normal travel-and-shortage logic.
- **Unbounded tank:** The proof relies on being able to add all selected fuel without a capacity limit. A bounded-tank version would require decisions at the time of arrival and is a different problem.
- **Mutation of `stations`:** The exact solution appends a sentinel. Copying or chaining the sentinel during iteration would preserve the caller's list if that behavior matters outside the judge.
