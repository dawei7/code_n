## General

**Fix the difficult factor: the minimum efficiency**

Team performance is

$$
\left(\sum \text{speed}\right)\times\left(\min \text{efficiency}\right).
$$

Choosing a fast engineer can increase the sum while a low-efficiency engineer can decrease the multiplier. The key is to enumerate which engineer supplies the minimum efficiency. Once that multiplier is fixed at $e$, every other eligible teammate must have efficiency at least $e$, and maximizing performance reduces to maximizing the selected speed sum.

The code pairs each engineer as `(speed, efficiency)` and sorts the pairs by decreasing efficiency:

`sorted(zip(speed, efficiency), key=lambda x: -x[1])`.

When the loop reaches current engineer `(s, e)`, every previously processed engineer has efficiency at least $e$. Therefore the current engineer plus any selected previous engineers form a team whose minimum efficiency is $e$ or higher. Including the current engineer gives a concrete candidate whose minimum is $e$.

**Why a min-heap stores speeds**

For a fixed minimum efficiency, all eligible teammate efficiencies have already passed the threshold, so only their speeds matter. With capacity at most $k$, the best companions are the largest speeds.

The min-heap `h` lets the solution maintain those speeds dynamically. `tot` is the sum of the speeds currently represented in the heap. Before processing a new engineer, the heap contains at most $k-1$ speeds retained from earlier, at-least-as-efficient engineers. Adding current `s` produces a candidate team of at most $k$ members.

The code performs these operations in this exact order:

1. Add `s` to `tot`.
2. Evaluate `tot * e`.
3. Push `s` into the heap.
4. If the heap size is now exactly $k$, pop its smallest speed and subtract it from `tot`.

Although the push appears after the candidate calculation, `tot` already includes current `s`, so the calculated team corresponds to previous heap members plus the current engineer. After evaluation, pushing makes the heap represent that team. If it reaches size $k$, removing the smallest leaves the best $k-1$ speeds available as companions for the next, less-efficient candidate.

**Why pruning to $k-1$ previous speeds is safe**

Suppose the next current engineer will define the minimum efficiency. That engineer must occupy one of the at most $k$ slots, leaving at most $k-1$ previous teammates. Among all processed engineers, keeping the largest $k-1$ speeds gives the greatest possible companion speed sum for every future threshold. Any discarded speed is no larger than every retained speed and can never be a better replacement while efficiencies only become less restrictive as the scan proceeds.

The minimum heap root identifies exactly the speed to discard when there are $k$ stored speeds. Heap size remains at most $k-1$ between iterations.

**Why teams with fewer than `k` members are still considered**

Early in the scan there may be fewer than $k-1$ previous eligible engineers, so the candidate uses all available speeds and has fewer than $k$ members. This covers smaller teams.

Because all speeds are positive, once a minimum efficiency threshold is fixed, adding another eligible engineer while capacity remains always increases the speed sum without lowering that fixed threshold. Therefore there is no reason to omit an eligible positive speed merely to make a smaller team, except that earlier iterations already cover teams with a higher minimum efficiency.

**Tied efficiencies**

Engineers with equal efficiency may appear in either order. A candidate computed early in the tied block covers teams available so far; later candidates see more engineers with that same threshold while the heap retains the fastest companions. By the end of the block, every potentially useful high speed at that efficiency has had a chance to enter the retained set. Since the multiplier is identical across the block, arbitrary tie order does not lose the optimum.

**Why the greedy enumeration is correct**

Consider an optimal team and choose one member whose efficiency equals the team's minimum $e$. When the sorted scan processes the relevant efficiency level, every other team member is already processed or belongs to the same tied level. The heap mechanism retains the largest speeds available under that threshold, so the candidate speed sum considered at some point in that level is at least the optimal team's sum for the allowed number of slots. Multiplying by the same $e$ yields performance at least as large.

Conversely, every candidate calculated by the algorithm is a real team of no more than $k$ distinct processed engineers, and its members all have efficiency at least current $e$ while current engineer has efficiency $e$. Thus `tot * e` is its genuine performance. The maximum over valid candidates is exactly the global optimum.

**Why modulo is applied only at the end**

`ans` stores true performance values so ordinary numeric comparison identifies the largest. Taking remainders before comparing would destroy order: a larger true value can have a smaller remainder. Only after the maximum is known does `ans % (10**9 + 7)` produce the required returned representation.

## Complexity detail

Let $n$ be the number of engineers. Creating and sorting the pair list takes $O(n\log n)$ time. Each engineer causes one heap push and, once capacity is reached, one heap pop. Heap size is at most $k$, so these operations total $O(n\log k)$. Since $k\le n$, overall time is $O(n\log n)$.

The sorted list `t` stores $n$ pairs and Python sorting may use linear temporary storage. The heap stores at most $k$ speeds. Total extra space is $O(n+k)=O(n)$, matching the manifest.

## Alternatives and edge cases

- **Enumerate all teams:** This considers exponentially many subsets and is infeasible for $n$ up to 100,000.
- **Sort by speed alone:** It can select fast engineers with a disastrously low minimum efficiency and does not control the multiplier.
- **Re-sort eligible speeds for every threshold:** It expresses the fixed-efficiency idea but repeats work, potentially costing $O(n^2\log n)$.
- **Balanced multiset of speeds:** It can maintain the largest $k-1$ values, but a min-heap provides exactly the needed remove-smallest operation more simply.
- **`k = 1`:** After each one-engineer candidate is evaluated, its speed is popped. The answer becomes the best individual `speed * efficiency`.
- **`k = n`:** The heap can retain up to $n-1$ previous speeds, so every useful prefix-size team is considered.
- **Positive speeds:** Adding an eligible member cannot reduce a fixed-threshold performance, justifying use of as many slots as available.
- **Equal efficiencies:** Sorting tie order is irrelevant because the multiplier is the same and heap retention favors larger speeds.
- **Current engineer has the smallest speed:** It is still included for its candidate, then may be immediately popped so it does not weaken future teams.
- **Pop timing:** The candidate must be evaluated before reducing a size-$k$ heap to $k-1$ companions; otherwise a valid full team could be skipped.
- **Large performance:** Python integers do not overflow, and the modulus is safely delayed until after maximization.
- **Parameter `n`:** Pairing the two arrays determines the actual iteration; `n` belongs to the required signature and agrees with their lengths.
- **Required heap names:** `heappush` and `heappop` must be available, normally from `heapq`.
