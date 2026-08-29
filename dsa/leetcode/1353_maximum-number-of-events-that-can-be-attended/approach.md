## General

Each event may be attended on any one day from its start through its end, and only one event can be attended per day. On a given day, among all currently available events, attending the one that ends earliest is the safest choice: events with later deadlines leave more future opportunities.

The checked-in solution sweeps through calendar days and maintains a min-heap of end days for events that have started but have not yet been attended.

**Group events by their start day**

`g[start]` stores the end day of every event beginning on `start`. During the same pass, `l` becomes the earliest start day and `r` becomes the latest end day. The sweep only needs days from `l` through `r` because no event is available outside that range.

Unlike an approach that sorts the event list by start, this source uses a dictionary of start-day buckets.

**Remove events whose opportunity has expired**

At day `s`, an event with end day below `s` can no longer be attended. Because `pq` is a min-heap, its smallest end day is at the root. The loop pops while `pq[0] < s`. Once the root is at least `s`, every remaining heap entry also ends on or after the current day.

The comparison is strict. An event whose end equals the current day is still attendable because interval endpoints are inclusive.

**Add events that start today**

Every end day in `g[s]` is pushed into the heap. The input guarantee `start <= end` means these newly starting events cannot already be expired on their start day.

After removal and insertion, the heap contains exactly the unattended events whose start is no later than `s` and whose end is no earlier than `s`.

**Attend the earliest-ending available event**

If the heap is nonempty, `heappop(pq)` removes the event with the smallest deadline, and `ans` increases by one. This schedules that event on the current day. Only one pop is used for attendance because only one event may be attended per day.

To see why this greedy choice is safe, compare the earliest-ending event `A` with any other available event `B` chosen by an optimal schedule on the current day. If that schedule already chooses `A`, nothing changes. Otherwise, replace `B` with `A` today. If the schedule never attends `A` later, the number attended stays the same. If it attends `A` on a later day, put `B` on that later day instead. Both events had already started today, and `B` ends no earlier than `A`, so any later day valid for `A` is also within `B`’s interval. The swap preserves feasibility and attendance count.

Therefore, some optimal schedule always agrees with the greedy selection today. Repeating the exchange day by day proves that the final `ans` is maximum.

Days with an empty heap simply pass without attendance. The sweep cannot gain anything by inventing work on such a day because no event is then available.

## Complexity detail

Let $n$ be the number of events and let $D = r-l+1$ be the number of calendar days traversed.

Grouping takes $O(n)$ expected time. Every event end is pushed once and popped once, either when expired or when attended. Total heap work is $O(n\log n)$. The day loop adds $O(D)$ overhead, so the exact total is

$$
O(D+n\log n).
$$

This source does not sort `events`. A bound written only as $O(n\log n)$ suppresses the calendar-span term, which is bounded by the problem’s maximum day but can exceed $n$ for sparse inputs.

The end-day lists collectively store $n$ values, and the heap can store $O(n)$ values. Additionally, `g` is a `defaultdict`, and evaluating `g[s]` for every swept day creates an empty entry for days with no starting event. The exact dictionary footprint can therefore be $O(n+D)$. A normal dictionary access through `g.get(s, [])` would avoid those empty keys and keep working storage at $O(n)$.

## Alternatives and edge cases

- **Sorted starts with a pointer:** Sort events by start day, add all whose start has arrived, and jump over empty calendar gaps. This gives $O(n\log n)$ time without an explicit $D$ term.
- **Disjoint-set day assignment:** Sort by end day and use a union-find structure to locate the earliest unused day in each interval. It is useful for very large sparse day coordinates.
- **Choose latest-ending event first:** This can waste an early deadline and reduce the total; earliest end is the exchange-safe rule.
- **End equals current day:** The event remains valid because expiration uses `end < day`.
- **Several events with the same deadline:** Attending any one of them today is equivalent for the greedy proof.
- **Duplicate intervals:** They are distinct events and may be attended on different days if their range permits.
- **One-day event:** It must be used on its only day or becomes expired on the next iteration.
- **Empty heap:** No event can be attended that day, so the algorithm correctly leaves `ans` unchanged.
- **Nonempty input:** The constraints guarantee at least one event, so `l` is replaced from infinity before `range` is constructed.
- **Sparse large span:** The exact source still visits every day and creates empty `defaultdict` buckets; a pointer-based sweep avoids that cost.
