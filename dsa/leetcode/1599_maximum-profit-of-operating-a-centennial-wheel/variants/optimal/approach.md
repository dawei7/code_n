## General
Let $n$ be the number of scheduled arrival groups.

**Simulate every potentially useful service rotation.** Track how many customers are waiting. Before rotation $i+1$, add `customers[i]` when that arrival exists, board `min(4, waiting)`, and subtract those riders from the queue. Continue after the arrival array ends while anyone still waits; those additional paid rotations may increase the attainable profit.

**Maintain cumulative profit and its earliest maximum.** Each rotation changes profit by `boarded * boardingCost - runningCost`. Start the best profit at zero and the answer at `-1`. Update the recorded rotation only when cumulative profit becomes strictly greater than the previous best. This both excludes non-positive histories and preserves the earliest rotation when the same positive maximum occurs more than once.

After each iteration, the waiting count equals all arrived customers not yet boarded, and `profit` equals revenue from everyone boarded so far minus the cost of exactly the rotations performed. Therefore it is the profit obtained by stopping service at that point. Every useful stopping point occurs either during scheduled arrivals or while draining the final queue, and the loop examines all of them. Taking the earliest strictly greatest positive value yields the required answer.

## Complexity detail
The simulation performs $n$ scheduled rotations plus at most $\lceil W/4 \rceil$ extra rotations for the final waiting count $W$. Since each arrival is at most 50, $W \le 50n$, so the total is $O(n)$. The waiting count, cumulative profit, best profit, and rotation counters use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Recompute every service prefix:** Simulating from the beginning for every possible stopping rotation is correct but repeats work and can take $O(n^2)$ time.
- **Stop when scheduled arrivals end:** This can miss the optimum because profitable rotations may remain while the final queue is drained.
- **Update on equal profit:** This incorrectly returns a later rotation; the contract asks for the minimum rotation count attaining the maximum.
- A rotation with no boarded customers still incurs `runningCost` while service continues through the arrival schedule.
- If every cumulative profit is zero or negative, return `-1`, not the rotation producing zero.
- Large early arrivals can require many rotations after the final arrival index.
