## General

**Each limit creates a capacity.** Consider all elements whose limit is exactly $L$. Once the active count reaches $L$, every member of this group becomes permanently inactive. Before that event, each activated member of the group remains active, so the process cannot activate more than $L$ members of the group. It may activate all of them when the group contains fewer than $L$ elements. Therefore the group contributes at most $\min(L,\text{group size})$ values.

**The capacities can be achieved together.** Process chosen elements in increasing limit order. Elements from a smaller-limit group disappear as soon as their threshold is reached. If that group has fewer elements than its limit, later activations eventually reach the missing threshold and expire it, while the later elements survive because their limits are larger. Repeating this transition permits the selected quota from every group; no capacity needs to be traded against another limit group.

All values are positive, so within a limit group the best quota consists of its largest values. Sort pairs by limit ascending and value descending. Consecutive equal-limit pairs then form one group, and the first `limit` values are precisely the ones to add.

## Complexity detail

Sorting the $n$ `(limit, value)` pairs takes $O(n\log n)$ time. The following scan is $O(n)$. The sorted pair list uses $O(n)$ auxiliary space.

The benchmark sets size $N=n$, puts every element in one group of capacity $N/2$, and uses tiers 32, 128, and 512 for a 16x span. Sorting once remains $O(N\log N)$. A correct repeated-selection method rescans the remaining group to choose each of $N/2$ maxima, taking $O(N^2)$ time.

## Alternatives and edge cases

- **Heap per limit:** Keeping each group's best values in a bounded heap also takes $O(n\log n)$ time and $O(n)$ space, and is useful for streaming input.
- **Repeated maximum selection:** It avoids a global sort but rescans a group for every chosen value, producing quadratic work for a large group.
- **Limit one:** Only the single largest value among all elements with limit 1 can be activated.
- **Small group:** When a group contains fewer than its limit, every one of its positive values contributes.
- **Equal values:** Their relative order is irrelevant; only how many are selected matters.
- **Large total:** The result may exceed 32-bit integer range, so fixed-width implementations need a 64-bit accumulator.
