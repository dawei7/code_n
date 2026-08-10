## General

**Store only the information future operations need**

The system receives three kinds of calls. A check-in starts a trip, a check-out finishes one, and an average query asks about all completed trips for a directed station pair.

Two dictionaries separate these responsibilities:

- `ts` maps a customer ID to that customer's most recent check-in time and start station.
- `d` maps a pair `(startStation, endStation)` to the total duration and number of completed trips on that route.

The design never stores every individual finished duration. An average needs only the sum and the count, because

$$
\text{average}=\frac{\text{total duration}}{\text{number of trips}}.
$$

This compression keeps queries constant time even after many journeys.

**Check-in**

`self.ts[id] = (t, stationName)` records the two facts that a later check-out does not provide: the start time and start station. Customer ID is the lookup key because interleaved calls for many customers may occur before any particular one checks out.

The contract guarantees one active location per customer, so a valid `checkIn` does not overwrite an unfinished trip. If the same customer takes another trip later, the new check-in overwrites the old completed-trip data stored under that ID.

The tuple order is time first and station second. `checkOut` unpacks it as `t0, station` in the same order.

**Check-out**

For a customer checking out at time `t` from `stationName`, the stored tuple identifies the route start. The trip duration is `t - t0`, which is positive by the consistency guarantee.

The directed route key is `(station, stationName)`. Direction matters: Leyton to Waterloo and Waterloo to Leyton are different dictionary entries and can have different averages.

`self.d.get(key, (0, 0))` returns the previous total and trip count or zeroes for a route seen for the first time. The update

`(x[0] + t - t0, x[1] + 1)`

adds the new duration and increments the number of completed journeys exactly once.

For two trips lasting 12 and 10 minutes, the route entry evolves from absent to `(12,1)` and then `(22,2)`. No averaging or floating-point rounding occurs during updates.

**Average query**

`getAverageTime` retrieves the tuple for the exact directed key and returns `x[0] / x[1]`. Python's slash performs floating-point division, so a total of 22 over two trips returns 11.0, while 20 over three returns approximately 6.66667.

The contract guarantees at least one completed journey for every queried route, so the dictionary key exists and the count is nonzero. No defensive default or division-by-zero branch is necessary.

**Why totals are better than repeatedly stored averages**

One could update an average after each trip, but repeated floating-point operations accumulate rounding error and still require the old count. Storing an exact integer total and integer count postpones division until the query. It also makes the invariant easy to verify.

Storing a list of every trip duration would also work, but each average query would need either a fresh sum proportional to the route's history or a redundant maintained total. The tuple is the minimum sufficient aggregate.

**The state invariant**

After any valid call sequence:

- For every customer ID in `ts`, its tuple is that customer's latest recorded check-in.
- For every route key in `d`, the first tuple component is the sum of all completed direct trip durations for that route, and the second is their count.

Check-in establishes or replaces the first fact for one ID. Check-out reads that correct start record and adds exactly the derived trip to the correct directed aggregate, preserving the second fact. Average query changes no state and divides the two exact aggregate values. By induction over calls, every returned average is correct.

**The exact implementation retains completed check-ins**

The exact `checkOut` reads `self.ts[id]` but does not delete it. Correctness is unaffected under consistent calls because a future check-in for that ID overwrites the tuple before another check-out. However, memory can retain one entry for every distinct customer ID ever seen, rather than only customers currently traveling.

Using `self.ts.pop(id)` would reduce long-running memory to active trips while preserving behavior. This is an implementation-level distinction worth knowing when translating the interview solution to a real service.

## Complexity detail

Under expected constant-time dictionary operations, each individual `checkIn`, `checkOut`, and `getAverageTime` call is $O(1)$. Across $q$ calls, total time is $O(q)$, matching the manifest.

Let $A$ be the number of customer IDs retained in `ts` and $R$ the number of directed routes that have completed trips. Space is $O(A+R)$. Because the exact code does not delete on checkout, $A$ means distinct IDs ever checked in, not strictly the number concurrently active. The manifest notation remains correct when `A` is interpreted this way.

Station strings and tuple keys have bounded length under the constraints, so hashing them is treated as constant time.

## Alternatives and edge cases

- **Remove check-ins on checkout:** Use `pop` to keep only active journeys. This improves long-running memory without changing expected operation time.
- **Store all trip durations:** It preserves raw data but uses space per journey and makes naive average queries slower.
- **Store a running average:** It saves neither the need for a count nor much space and introduces compounded floating-point error.
- **Nested route dictionaries:** Map start station to a dictionary of end stations. It is equivalent but more verbose than a tuple key.
- **Reverse direction:** `(A,B)` and `(B,A)` are distinct keys, as required.
- **First trip on a route:** The default `(0,0)` makes its total and count initialize correctly.
- **Interleaved passengers:** Customer-ID lookup pairs each checkout with its own check-in regardless of other calls.
- **Repeated customer trips:** A later valid check-in overwrites the retained old tuple before its next checkout.
- **Query before any trip:** The contract excludes it; otherwise direct dictionary access would raise a key error.
- **Invalid checkout:** The contract guarantees consistency; otherwise missing `id` would raise a key error.
- **Chronological events:** Positive duration follows from `t0 < t` and no timestamp sorting is needed.
- **Real-world persistence:** In-memory dictionaries satisfy the coding contract but would need durable, concurrent storage in a production transit system.
