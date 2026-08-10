## General

**Each day's decision should protect the most urgent apples**

At most one apple can be eaten per day. When several batches are still edible, choosing an apple from the batch that rots earliest is always safe: postponing that urgent batch risks losing it, while a later-expiring batch remains available for at least as long.

The source implements this earliest-expiration-first rule with a min-heap `q`. Each heap entry is a pair `(t, v)`:

- `t` is the last day on which the batch is still edible.
- `v` is the number of apples remaining in that batch.

Python compares tuple entries first by `t`, so `q[0]` always has the smallest expiration day.

**Translate the rotting day into an inclusive deadline**

A batch grown on day `i` with lifetime `days[i]` becomes rotten on day `i + days[i]`. It can be eaten on days `i` through `i + days[i] - 1`. The source therefore inserts

`(i + days[i] - 1, apples[i])`.

Storing the last edible day makes the expiration test direct: an entry is unusable on current day `i` exactly when `t < i`.

The source inserts only when `apples[i]` is nonzero. Under the contract, a zero-apple day also has zero lifetime, so skipping it avoids a meaningless empty batch.

**Continue after the tree stops growing**

`i` is the current day and `ans` is the number eaten. The outer condition

`while i < n or q`

keeps processing while either a scheduled growth day remains or at least one stored batch remains. This is essential because apples grown near day `n - 1` may remain edible after the first $n$ days.

When `i < n`, today's new batch is inserted before eating. A newly grown apple is therefore eligible on its growth day.

If the heap is empty during an early day with no apples, the loop still increments `i` because future input days may grow apples. Once `i >= n`, an empty heap ends the process.

**Remove every batch that has already rotted**

After today's insertion, the loop repeatedly removes the heap front while `q[0][0] < i`. Because the heap is ordered by expiration, once the earliest entry is not expired, no later entry can be expired either.

Expired batches contribute nothing to `ans`. Their remaining counts may be positive, but those apples are no longer legal choices.

Insertion before cleanup is safe: valid input gives a positive lifetime for a nonzero batch, so its last edible day is at least the current day and it will not be removed immediately.

**Eat one apple from the earliest deadline**

If a valid batch remains, the source pops the minimum pair `t, v`, decrements `v`, and increments `ans`. Popping before modifying is convenient because heap entries are immutable tuples; the updated count can be reinserted as a new tuple.

If apples remain and `t > i`, the batch is pushed back for a future day. Both conditions matter:

- If `v == 0`, the batch is exhausted.
- If `t == i`, leftover apples rot before tomorrow, so reinserting them would only cause an expiration pop on the next iteration.

The popped batch is known to satisfy `t >= i` after cleanup, so these are the only cases.

**Why earliest expiration is optimal**

Consider any day on which the greedy algorithm eats from a batch $A$ with the earliest deadline. Suppose an optimal schedule instead eats from another available batch $B$ with a deadline no earlier than $A$'s.

If that schedule never eats an $A$ apple later, replacing today's $B$ apple with $A$ preserves the number eaten. If it does eat an $A$ apple on a later day, swap the choices: eat $A$ today and $B$ on that later day. Batch $B$ is still edible then because its deadline is at least $A$'s deadline, and the original schedule successfully ate $A$ then. The swap preserves feasibility and total apples.

Thus some optimal schedule agrees with the greedy choice today. Repeating the exchange day by day proves that the heap strategy reaches a maximum total.

**A small deadline trace**

Suppose today's heap contains three apples expiring today and two apples expiring three days later. The source eats from today's batch. Any apples from that batch left after today are intentionally not reinserted because they cannot be saved. The later batch remains available for subsequent days.

Choosing the later batch first could waste all urgent leftovers without creating any compensating opportunity, which is precisely what the greedy order prevents.

## Complexity detail

Let $n$ be the number of growth days and $E$ the number of apples actually eaten. Each nonempty daily batch is inserted once initially and removed at most once when it expires or becomes exhausted. A partially consumed batch is popped and reinserted for each apple eaten from it, so there are $O(n+E)$ heap operations.

The heap holds at most one entry per nonempty growth-day batch, hence at most $n$ entries. Each operation costs $O(\log n)$, giving $O((n+E)\log n)$ time, matching the manifest. There are exactly $n$ possible growth-day iterations; after those, every iteration that continues with a valid heap eats an apple, apart from cleanup that permanently removes a batch, so the day-by-day loop is also covered by $O(n+E)$ plus the $O(n)$ batch removals.

The heap uses $O(n)$ space in the worst case. All other variables are scalar, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Scan all batches daily:** Select the earliest expiration by a linear search. It is correct but can take $O(n)$ per day.
- **Sort all individual apples:** Expanding every apple into its own deadline may require space proportional to the total apple count, far larger than the number of batches.
- **Latest-expiration first:** It can consume flexible apples while urgent ones rot and is not optimal.
- **Ordered deadline counts:** A balanced ordered map can support the same greedy choice, but a min-heap is simpler because batches only enter and leave.
- **No apples on a day:** Nothing is inserted; the clock still advances so future growth days are reached.
- **Batch edible for one day:** Its deadline equals its growth day. At most one is eaten, and leftovers are not reinserted.
- **Several batches share a deadline:** Their tuple counts may order ties arbitrarily, but all are equally urgent and the total optimum is unchanged.
- **Expired batches at the front:** The cleanup uses a loop because several batches can expire before the same current day.
- **Eating after day `n - 1`:** The outer `or q` condition keeps the simulation alive.
- **Heap becomes empty before `n`:** The loop continues through input days because later batches may grow.
- **Many apples in one batch:** The batch count is decremented one per day and reinserted only while a future edible day exists.
- **Input mutation:** Neither `apples` nor `days` is reordered or modified.
- **Inclusive deadline:** The test is `t < i`, not `t <= i`, because an apple is still edible on its stored last day.
