## General

**Sort all events into chronological order**

Passengers board in order of arrival, and buses depart in order of time. The input arrays are not sorted, so the method first sorts both in ascending order.

The pointer `j` is the index of the earliest passenger who has not boarded yet. For each bus departure `t`, `c` starts at `capacity` and the inner loop boards passengers while three conditions hold: a seat remains, a passenger remains, and that passenger arrived no later than `t`.

Advancing `j` after every boarding means passengers taken by earlier buses are never reconsidered. When the bus loop ends, the simulation exactly matches the schedule without the new traveler.

**Only the final bus determines the latest possible arrival**

Any arrival that catches an earlier bus cannot be later than a feasible arrival for the last bus unless the later buses' seats are completely claimed by earlier-arriving passengers. The chronological simulation tells us the boundary at the final departure.

After the final bus:

- if `c > 0`, it has a spare seat after all eligible existing passengers board, so arriving at the final departure time itself is initially feasible;
- if `c == 0`, it is full, and the latest new traveler could enter its queue no later than the arrival time of the last passenger who obtained a seat.

The code first decrements `j` because during simulation it points one position after the last boarded passenger. Then it sets `ans` to `buses[-1]` for a nonfull final bus, or `passengers[j]` for a full one.

In the full case, matching the last boarded passenger's time is forbidden, so the later collision-removal loop immediately retreats below it.

**Retreat through occupied arrival times**

The candidate cannot equal any existing passenger arrival, even if that passenger boarded an earlier bus. Because `passengers` is sorted, the relevant occupied times at or below the candidate appear immediately backward from `j`.

The loop condition `~j` is a compact Python test for `j != -1` in this controlled range. When `j >= 0`, `~j` is a nonzero negative integer and is truthy. When `j == -1`, `~j == 0` and the loop stops.

If `passengers[j] == ans`, the candidate is occupied. The method subtracts one from `ans` and moves `j` to the previous passenger. If that earlier passenger occupies the new candidate, it repeats. The final value is the greatest unoccupied integer time at or below the boarding boundary.

For a full last bus whose last boarded passenger arrives at 17, the initial candidate 17 collides and becomes 16. If another passenger arrived at 16, it becomes 15, continuing until a gap is found.

**Why the final candidate can board**

If the final bus had a spare seat, arriving at its departure time or any earlier unoccupied candidate cannot displace eligibility; the traveler joins before departure and occupies the spare seat.

If it was full, the traveler ends strictly before the last boarded passenger's arrival after collision retreat. They therefore appear earlier in the queue and take a seat, displacing that boundary passenger or another later one.

Retreating across existing arrivals never makes the traveler worse relative to queue order. It only moves them earlier, while maintaining a legal distinct arrival time.

**Why no later legal time works**

With a spare seat, no time after the last bus departure can catch any bus, so `buses[-1]` is the absolute upper bound.

With a full final bus, arriving after the last boarded passenger would place the traveler behind at least `capacity` eligible passengers, leaving no seat. Arriving at the same time is prohibited. Thus the last boarded arrival is the upper boundary, and every occupied integer at or below it must also be skipped.

The backward loop stops at the first gap, so every later time up to the boundary is either too late or occupied. The returned feasible value is therefore the latest possible one.

## Complexity detail

Let `b` be the number of buses and `p` the number of passengers. Sorting costs `O(b \log b + p \log p)`. The boarding pointer advances at most `p` times across all buses, and the collision retreat also moves backward at most `p` times, so simulation is linear after sorting.

Python sorts both lists in place and may use `O(b + p)` temporary merge storage in the worst case. Other state is constant-size. The input arrays are observably reordered.

All times fit in Python integers. The answer may retreat below the smallest passenger time, but passenger and bus times start at two, leaving legal earlier integer times available.

## Alternatives and edge cases

- **Binary search an arrival time:** Simulate boarding for each candidate and test feasibility. This repeats substantial work and is unnecessary once the final boarding boundary is known.
- **Use a set for collision checks:** Start from the boundary and decrement while the candidate is in a passenger set. This is correct with expected constant lookup but uses additional `O(p)` storage; the sorted backward pointer reuses ordering.
- **Simulate the new traveler explicitly at many times:** Only the boundary passenger and occupied-time gaps matter. Full schedule resimulation for every candidate is wasteful.
- **Final bus has spare capacity:** Its departure time is best unless an existing passenger has exactly that arrival, in which case retreat finds the next gap.
- **Final bus is full:** Start from its last boarded passenger's time, then retreat at least once because that time is occupied.
- **No passenger boards any bus:** After `j -= 1`, `j = -1` and the last bus has spare capacity. The collision loop safely skips, returning the last departure.
- **Consecutive occupied times:** The backward loop retreats through the entire consecutive block.
- **Passengers arriving after the last bus:** They never board and lie beyond pointer `j`. They cannot collide with a candidate at or before the last departure unless equal ordering made them eligible, so ignoring them is correct.
- **Capacity one:** Each bus boards at most the earliest waiting passenger; the same pointer simulation applies.
- **Many early passengers:** Earlier buses remove them from the queue, which is why simulating every bus before inspecting the last one is necessary.
- **Unique passenger times:** The source guarantee means one backward step handles one occupied time; duplicates would require different queue and collision handling.
- **Bitwise complement condition:** `~j` is correct only because `j` stops at `-1` and never needs values below it. An explicit `j >= 0` would be clearer.
- **Input mutation:** Both `buses` and `passengers` are sorted in place.
