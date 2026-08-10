## General

Planting uses the one shared resource: on each day, work can be done for only one seed. Growth is different. Once a seed is completely planted, it grows on its own while planting work continues on other seeds. The schedule should therefore start long independent waits early.

**Treat planting as consecutive blocks**

The rules permit interrupting one seed’s planting and returning to it later, but interruption is not needed for an optimal result. What ultimately matters is the order in which seeds finish planting and begin growing.

For any schedule, take the first seed that finishes planting. Move all of its planting days together at the beginning without increasing its completion time; the displaced work for other unfinished seeds can occupy the released days. Repeating this idea yields a schedule with the same completion order in which each seed’s planting is one consecutive block. Thus the problem can be viewed as choosing an order for whole planting jobs.

**Order seeds by decreasing growth time**

The exact solution combines corresponding values with `zip(plantTime, growTime)` and sorts the pairs by `key=lambda x: -x[1]`. Negating the second component makes Python’s ascending sort place larger growth times first.

The reason is captured by an exchange argument. Consider two adjacent seeds $A$ and $B$ beginning after $t$ planting days, with planting times $p_A,p_B$ and growth times $g_A,g_B$. Suppose $g_A < g_B$ but $A$ is planted first.

In order $A,B$, their bloom days are $t+p_A+g_A$ and $t+p_A+p_B+g_B$.

Now swap them into order $B,A$. Their bloom days become $t+p_B+g_B$ and $t+p_B+p_A+g_A$.

The second old bloom time, $t+p_A+p_B+g_B$, is at least both new bloom times: it exceeds the first new time by $p_A>0$, and it exceeds the second by $g_B-g_A>0$. Therefore swapping the longer-growing seed forward cannot increase the later bloom day of this pair. Seeds before the pair are unchanged, and seeds after it begin planting at the same time because $p_A+p_B$ is unchanged.

Any ordering that contains a shorter-growth seed immediately before a longer-growth seed can be improved or preserved by swapping them. Repeating such swaps produces non-increasing growth time without worsening the final answer. Hence the sorted order is optimal. Seeds with equal growth times may appear in either order because the exchange leaves the maximum unchanged.

**Track planting completion and bloom days**

The variable `t` is cumulative planting time. Initially no planting days have been used, so `t = 0`. For each sorted pair `pt, gt`, the statement `t += pt` marks the day on which that seed finishes planting and starts its autonomous growth.

Its bloom day is then `t + gt`. The code updates `ans = max(ans, t + gt)` because all flowers are blooming only when the last individual flower has bloomed.

For `plantTime = [1,4,3]` and `growTime = [2,3,1]`, sorting by growth gives pairs `(4,3)`, `(1,2)`, and `(3,1)`. Their cumulative planting completion times are $4,5,8$, so their bloom days are $7,7,9$. The maximum is $9$.

The order differs from the example’s listed schedule but reaches the same optimum. The task asks for the earliest day, not a unique planting plan.

**Why idle days never help**

Before all seeds finish planting, leaving the planting resource idle delays the completion of the current or a later seed and cannot make any growth finish sooner. An optimal block schedule can therefore plant continuously from day zero until all planting work is complete.

**Why the returned maximum is globally minimal**

The loop computes the exact final-bloom day for the decreasing-growth order. The exchange argument proves that any other order can be transformed into this order without increasing its latest bloom. Thus no alternative schedule can have a strictly smaller maximum bloom day than the value the loop produces.

## Complexity detail

Let $n$ be the number of seeds. Creating the zipped pairs and sorting them costs $O(n\log n)$ time. The following loop visits each pair once in $O(n)$ time. Sorting dominates, so total time is $O(n\log n)$.

In Python, `sorted(zip(...))` materializes a new list of $n$ pairs. TimSort also uses auxiliary storage whose worst case is linear. The exact implementation therefore uses $O(n)$ auxiliary space. The scalar variables `ans`, `t`, `pt`, and `gt` require only constant additional space beyond the sorted list.

The integer sums may reach the total planting time plus one growth time, but Python integers handle the legal values without overflow.

## Alternatives and edge cases

- **Sort by planting time:** Shortest-planting-first can delay a seed with a very long growth period and is not generally optimal. Growth time, not planting duration, determines urgency.
- **Sort by total `plantTime + growTime`:** This does not have the exchange property. Only the waiting tail continues independently after planting, so decreasing `growTime` is the justified key.
- **Preempt planting:** Interleaving planting days is allowed but unnecessary. There is always an equally good completion-order schedule with consecutive planting blocks.
- **Simulate every day:** The answer depends on cumulative planting completion times, so day-by-day state adds work without new information.
- **One seed:** The seed finishes planting after `plantTime[0]` days and blooms after its growth time, so the answer is their sum.
- **Equal growth times:** Their relative planting order does not change the maximum contributed by the pair. Python’s stable sort may preserve input order, but correctness does not depend on it.
- **Equal planting times:** Longer growth still goes first; equal planting durations do not change the ordering argument.
- **Very long growth with short planting:** It belongs early because its large autonomous wait can overlap with most later planting.
- **Very long planting with short growth:** It may appear late. Although its planting block delays completion, placing it earlier would delay longer growth tails.
- **Bloom-day convention:** If planting ends at cumulative time `t` and growth requires `gt` full days, the bloom day is `t + gt`, matching the examples.
- **No idle time:** Waiting before or between planting blocks cannot improve any completion or bloom day.
- **Input preservation:** `sorted` creates new pairs and does not reorder either input array.
