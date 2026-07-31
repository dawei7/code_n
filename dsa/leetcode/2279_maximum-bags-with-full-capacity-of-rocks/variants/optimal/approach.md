## General

**Turn every bag into one completion cost**

Bag $i$ needs exactly `capacity[i] - rocks[i]` additional rocks to become full.
Once these deficits are computed, the original distribution problem becomes:
buy as many items as possible with a fixed budget, where every completed bag
has the same value of one and its deficit is its cost.

**Complete the cheapest deficits first**

Sort all deficits in ascending order and traverse them from smallest to
largest. If the next deficit fits in the remaining budget, spend that amount
and count the bag. Otherwise, stop.

To see why this order is optimal, consider any choice of $k$ bags. Its total
deficit cannot be smaller than the sum of the $k$ smallest deficits overall.
Therefore, whenever some $k$ bags can be filled, the greedy prefix of length
$k$ can also be filled. Conversely, if the next sorted deficit does not fit
after paying for the current prefix, no selection of one more bag can be
cheaper. The counted prefix is consequently the largest feasible number of
full bags.

Deficits of zero require no budget and are counted naturally, including bags
that were already full before any distribution.

## Complexity detail

Let $n$ be the number of bags. Building the deficit array takes $O(n)$ time,
sorting it takes $O(n \log n)$ time, and the final scan takes $O(n)$ time.
The deficit array and sorting storage use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Repeated minimum selection:** Finding and removing the cheapest remaining deficit on every iteration is correct, but an array-based implementation takes $O(n^2)$ time.
- **Min-heap:** Heapifying all deficits and repeatedly removing the minimum is also correct in $O(n \log n)$ time, but sorting gives a simpler sequential scan.
- **Original index or capacity order:** Neither a bag's position nor its total capacity determines how cheaply it can be completed; only its remaining deficit matters.
- **Already-full bags:** A zero deficit is affordable without consuming any additional rocks and must be included.
- **Unused surplus:** The operation permits using at most the available rocks, so excess rocks need not be placed after every bag is full.
- **Exact budget:** A deficit equal to the remaining number of rocks is affordable and leaves a zero balance.
- **Unaffordable next deficit:** Once the next value in sorted order exceeds the remaining budget, every later deficit is at least as large, so the scan can stop.
- **Equal deficits:** Their relative order is irrelevant because they have identical completion costs.
