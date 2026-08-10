## General

**Group people by the day they first learn the secret**

People who discover the secret on the same day behave identically. They begin sharing on the same future day, stop sharing on the same day, and forget together. The array `cnt` stores these cohort sizes:

> `cnt[i]` is the number of people who first learn the secret on day `i`.

The initial person forms the day-one cohort, so `cnt[1] = 1`.

Processing cohorts rather than individuals is essential because the population can grow rapidly. One update can schedule the behavior of an entire group with arithmetic on its count.

**A cohort teaches one new person per member on every eligible day**

A person who learns on day `i` begins sharing on day `i + delay`. They forget on day `i + forget` and cannot share that day, so their sharing days are the half-open interval

`[i + delay, i + forget)`.

For a cohort of `cnt[i]` people, every eligible day gains exactly `cnt[i]` new learners. The code starts `nxt = i + delay` and, while `nxt < i + forget`, performs

`cnt[nxt] += cnt[i]`.

Each future day's cohort accumulates contributions from every earlier cohort that is actively sharing on that day. When the outer loop eventually reaches that day, `cnt[nxt]` is the complete number of new discoverers for it, and their own future sharing is scheduled in the same way.

The strict upper comparison is important. Day `i + forget` is excluded because the cohort forgets before it can share on that day.

**Use a difference array to record who is still aware**

Every person in the day-`i` cohort knows the secret from day `i` through day `i + forget - 1`. The array `d` records this active interval with two events:

- `d[i] += cnt[i]` starts the cohort's contribution;
- `d[i + forget] -= cnt[i]` ends it on the forgetting day.

In an ordinary difference-array reconstruction, the number aware on day `q` is the prefix sum

`d[0] + d[1] + \cdots + d[q]`.

The method needs only day `n`, so it does not reconstruct every intermediate prefix. At the end, `sum(d[:n + 1])` is exactly that day-`n` prefix and hence the number of people who still know the secret at the end of day `n`.

Events after day `n` are stored but are outside the final slice. A cohort whose forgetting day is later than `n` contributes its positive start event without its later negative removal, correctly counting it as still aware.

**Why the arrays extend beyond day n**

The source sets `m = 2 * n + 10`. During processing of day at most `n`, the largest scheduled forgetting index is `i + forget <= 2n` because `forget <= n`. The extra capacity safely holds every future event and every sharing-day cohort written by the loops, even if that date is beyond the requested final day.

Those beyond-`n` cohort counts are never processed by the outer loop, because their later behavior cannot affect day `n`. Allocating enough space prevents boundary checks from complicating the exact scheduling logic.

**A day-by-day trace of the two schedules**

With `delay = 2` and `forget = 4`, the day-one cohort has size one. It adds awareness on day one and removes it on day five. It contributes one new learner to `cnt[3]` and one to `cnt[4]`, the only days in `[3,5)`.

When day three is processed, its newly formed cohort schedules its own awareness through day six and future learners starting on day five. Multiple cohorts can add to the same `cnt` entry; that sum represents all people who discover the secret on that date.

This matches the story without naming individuals. Every cohort is processed once, and its count is distributed to exactly its legal sharing days.

**Why every person is counted correctly**

Use induction on days. `cnt[1]` is correct by the initial condition. Assume cohort counts through day `i` are correct. Every earlier cohort that is allowed to share on day `q` adds its full size to `cnt[q]` when it is processed; cohorts outside their sharing interval add nothing. Each active person teaches exactly one new person that day, so the accumulated `cnt[q]` is exactly the number who learn on day `q`. This proves the future cohort counts.

For awareness, each person contributes plus one starting on their learning day and minus one on their forgetting day. The prefix through `n` includes that person exactly when `learning_day <= n < learning_day + forget`, which is precisely when they still know the secret at the end of day `n`.

Reducing the final exact total modulo `10^9 + 7` gives the required remainder.

**The exact implementation does not maintain a rolling sharer count**

The manifest summary describes scheduled cohort updates that can support an `O(n)` sliding count of active sharers. The provided source instead loops across every sharing day for every nonempty cohort. It is mathematically correct, but its literal time bound is different and should be documented as such.

It also postpones the modulus until the final answer. Python arbitrary-precision integers preserve correctness, but intermediate counts can become very large.

## Complexity detail

For each day `i`, the inner loop spans `forget - delay` future dates when `cnt[i]` is nonzero. In the worst case most processed days have nonzero cohorts, so the literal running time is `O(n(forget - delay))`, which is `O(n^2)` under the constraints. This differs from the manifest's `O(n)` claim, which corresponds to maintaining a rolling count of active sharers with difference-style additions and removals rather than distributing each cohort day by day.

The two arrays have length `2n + 10`, giving `O(n)` auxiliary space. The final slice `d[:n + 1]` creates another temporary list of length `O(n)` before `sum`, so peak space remains `O(n)`.

Because no intermediate update is reduced modulo `10^9 + 7`, Python integer bit lengths grow with the population. The stated operation count assumes arithmetic as unit-cost; exact bit complexity is higher. Applying the modulus during every `cnt` and `d` update would keep values bounded and preserve the final remainder.

## Alternatives and edge cases

- **Rolling active-sharer count:** Let each learning cohort enter the sharing population after `delay` days and leave after `forget` days. Updating two scheduled boundaries per day gives `O(n)` time and `O(n)` space.
- **Deque of waiting and sharing cohorts:** Move cohorts between queues on their delay and forgetting dates while maintaining total sharers. This also achieves `O(n)` time and mirrors the lifecycle explicitly.
- **Individual-person simulation:** The population can grow exponentially, so creating an object or event per person is infeasible. Cohort counts are necessary.
- **Include the forgetting day in sharing:** Using `nxt <= i + forget` would let people share on the exact day they forget, contradicting the contract. The loop correctly uses a strict bound.
- **Begin sharing too early:** The first eligible day is exactly `i + delay`, not `i + delay - 1`.
- **Count only active sharers in the final answer:** People waiting for their delay still know the secret and must be included. The awareness difference array counts both waiting and sharing cohorts until they forget.
- **Day one:** The initial positive event records the original person. No earlier day exists.
- **`delay = 1`:** A cohort starts sharing the next day, and the future-day loop begins at `i + 1`.
- **`forget = delay + 1`:** Each cohort has exactly one sharing day because the half-open interval contains one integer.
- **Forgetting after day n:** Its negative event lies outside the summed prefix, so the cohort remains counted at day `n`.
- **Forgetting on day n:** The negative event is included in `sum(d[:n + 1])`, correctly excluding that cohort at the end of day `n`.
- **Zero cohort day:** The `if cnt[i]` guard skips awareness and scheduling work because there are no people to represent.
- **Events beyond n:** They are harmless for the requested answer but motivate the `2n + 10` allocation in the exact source.
- **Delayed modulus:** It is mathematically valid in Python but resource-heavy. Fixed-width implementations must reduce during updates to avoid overflow.
- **Final slice allocation:** `d[:n + 1]` is a linear temporary; an explicit running sum or `islice` could avoid it without changing the result.
