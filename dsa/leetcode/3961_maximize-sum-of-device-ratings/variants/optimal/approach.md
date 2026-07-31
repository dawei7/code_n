## General

When each device contains one unit, moving a unit empties its source and gives the destination a rating no greater than either original capacity. Every move strictly decreases the positive original sum, so the `n = 1` case returns the sum of all singleton capacities.

Now suppose $n \ge 2$. For each device, only its smallest and second-smallest capacities matter. If the device acts as a source, removing anything except its minimum cannot improve its rating; removing the minimum raises its rating to the second minimum (or leaves it unchanged when they are equal).

Concentrate every removed minimum in one destination device. Its final rating is the smallest capacity seen anywhere, because it receives all those minima. Every other device can remove its own minimum and contribute its second minimum. Sending all removed units to one place is optimal because it confines their possible rating damage to a single device.

If device $i$ is chosen as the destination, the resulting sum is

$$
\text{global minimum}
+ \sum_j \text{secondMinimum}_j
- \text{secondMinimum}_i.
$$

Choose the device with the smallest second minimum as the destination, minimizing the subtracted contribution. This plan is feasible: leave that destination unused as a source and send every other device's minimum to it. Each source is used once, and adding units to the destination never raises its rating above the global minimum. Since each non-destination source reaches the greatest rating obtainable after one removal, no other transfer pattern can produce a larger total.

Both minima for a row can be found in one scan, including duplicates.

## Complexity detail

Every one of the $U$ capacities is inspected once, so the running time is $O(U)$. Only the global minimum, the smallest second minimum, their sum, and two row-local minima are stored, giving $O(1)$ auxiliary space beyond the input.

## Alternatives and edge cases

- **Sort every device:** Sorting exposes the two minima but costs $O(U\log n)$ time and may use additional sorting space.
- **Try transfer destinations:** Simulating each possible destination repeats the same second-minimum sum and costs unnecessary extra work.
- **One unit per device:** Any transfer empties a source and decreases the positive rating sum, so keep the original arrangement.
- **One device:** No different destination exists; the formula for $n \ge 2$ reduces to that device's original minimum.
- **Duplicate minima:** When a row's two smallest capacities are equal, removing one copy does not raise its rating, but the same formula remains valid.
- **Wide total:** Up to $10^5$ devices can contribute ratings of $10^5$, requiring a wide integer type.
