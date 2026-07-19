## General
**Process cars in road order, not input order**

Sort paired positions and speeds by position from closest to farthest from `target`. For a car at position $p$ with speed $v$, its unobstructed arrival time is

$$
t = \frac{\texttt{target}-p}{v}.
$$

The closest car begins the first fleet. While moving backward through the sorted cars, compare each arrival time with the arrival time of the nearest fleet ahead.

If the rear car's time is less than or equal to the fleet's time, it catches that fleet before or exactly at the destination and contributes no new fleet. If its time is greater, it cannot catch the fleet ahead, so it begins another fleet and becomes the new comparison time for still farther cars.

**Compare arrival times exactly**

Store the fleet time as a distance numerator and speed denominator. To test whether a car's time is greater, compare `distance * fleet_speed` with `fleet_distance * car_speed`. All quantities are positive, so cross multiplication preserves the inequality and avoids floating-point rounding near equal arrival times.

After processing the closest prefix, the stored fleet time is the slowest effective arrival boundary visible to the next rear car. The no-passing rule means that car can affect only that nearest fleet first. Thus each strict increase in arrival time identifies exactly one fleet, while every non-increase merges into the fleet ahead.

## Complexity detail
Sorting the $n$ cars takes $O(n\log n)$ time, and the subsequent scan is $O(n)$. The sorted list of position-speed pairs uses $O(n)$ space.

## Alternatives and edge cases
- **Monotonic stack of arrival times:** Push times in position order and merge non-increasing rear times; it expresses the same rule in $O(n\log n)$ time after sorting.
- **Floating-point times:** Usually convenient, but exact cross multiplication handles simultaneous arrivals without precision concerns.
- **Quadratic comparison sorting:** Selection or bubble sort preserves correctness but raises the total time to $O(n^2)$.
- **Single car:** It forms one fleet by itself.
- **Catch at the destination:** Equal arrival times count as one fleet, so only a strictly greater rear time starts another.
- **Faster rear car:** A smaller unobstructed arrival time means it must slow to the fleet ahead.
- **Slower rear car:** A larger arrival time means it never catches that fleet and remains separate.
- **Cascading merges:** Once a car joins a fleet, the fleet ahead's arrival time remains the comparison boundary for farther cars.
- **Unsorted input:** Position and speed must remain paired during sorting.
- **Unique positions:** No two cars begin side by side, as guaranteed by the contract.
