## General

**Convert clock text into one numeric timeline.** Helper `f` parses the two hour characters and two minute characters, returning `hours * 60 + minutes`. A time of day becomes an integer from zero through 1439. Minute arithmetic is easier and less error-prone than separately adjusting hours and minute fields.

**Unwrap an overnight session.** Let `a` be login minutes and `b` logout minutes. If `a > b`, logout occurs on the following day, so `b += 1440`. This places both endpoints on one increasing timeline: login remains within day zero, and logout moves into day one. If `a < b`, the session stays within the same day and no change is needed. Equal inputs are excluded by the contract.

For example, `21:30` becomes 1290 and `03:00` becomes 180. Since login is later as a time of day, logout becomes `180 + 1440 = 1620`, representing 03:00 next day.

**Round the login upward to a legal round start.** Tournament rounds begin at minute multiples of 15. Logging in during a round does not make that round full, so the first playable full round starts at the first multiple of 15 at or after `a`. Its boundary index is the ceiling

$$
\left\lceil\frac{a}{15}\right\rceil,
$$

implemented with integer arithmetic as `(a + 14) // 15`. If login is already exactly on a boundary, adding 14 still leaves floor division at that same boundary index.

**Round logout downward to a completed boundary.** A round is full only if its ending boundary is no later than logout. `b // 15` is the index of the last 15-minute boundary at or before logout. Think of this as an exclusive boundary: rounds can start at indices from the rounded login index up to one less than this logout boundary.

The number of such rounds is `b_boundary - a_boundary`. The source overwrites `a` and `b` with these two boundary indices and returns `max(0, b - a)`. The maximum prevents a negative count when the session is too short to contain even one complete aligned interval.

**Derive the counting formula from intervals.** Round `q` occupies minutes `[15q, 15(q+1)]`. It is fully played when `15q >= login` and `15(q+1) <= logout`. The first inequality gives `q >= ceil(login/15)`. The second gives `q <= floor(logout/15) - 1`. The number of integer `q` values is therefore `floor(logout/15) - ceil(login/15)` when positive, exactly the code's subtraction.

**Trace `09:31` to `10:14`.** Login is minute 571; rounding upward gives boundary index 39, which is 09:45. Logout is minute 614; rounding downward gives index 40, which is 10:00. Difference is one, representing round 09:45–10:00. The partly observed rounds on either side are excluded.

**Trace the overnight example.** `21:30` is exactly boundary index 86. Next-day `03:00` becomes minute 1620, boundary index 108. Difference 22 counts ten rounds before midnight and twelve afterward. Midnight needs no special split because the unwrapped timeline treats it as minute 1440.

**Why constant arithmetic is sufficient.** Round starts repeat with a fixed period and the session spans at most one midnight under the problem's interpretation. Once endpoints are aligned inward to complete-round boundaries, every 15-minute interval between them qualifies. No loop over rounds or minutes is needed.

The aligned interval is deliberately contained inside the actual session: rounding login upward never chooses a time before arrival, and rounding logout downward never chooses a time after departure. Conversely, every full scheduled round inside the session lies between those same aligned boundaries. The subtraction therefore counts all qualifying rounds, not merely a convenient subset.

## Complexity detail

Input strings have fixed five-character format. Parsing two substrings, performing arithmetic, and comparing endpoints all take constant time. Time complexity is $O(1)$.

Only a fixed number of integers and short parsed substrings are used, so auxiliary space is $O(1)$. This matches the manifest. The returned value is at most 96 because a day has 96 quarter-hour rounds and the times are unequal within a single same-day-or-overnight span.

## Alternatives and edge cases

- **Simulate quarter-hour starts:** Checking all at most 96 daily rounds is bounded and correct, but arithmetic directly counts them without iteration.
- **Adjust minute fields manually:** Separate hour/minute carry logic invites boundary errors. Total minutes makes ceiling, floor, and midnight addition uniform.
- **Login exactly on a boundary:** Ceiling retains that boundary, so the immediately starting round can count.
- **Logout exactly on a boundary:** Floor retains it as a completed ending boundary, so the round ending then counts.
- **Session shorter than one full aligned round:** Rounded login may meet or exceed rounded logout; `max(0, ...)` returns zero.
- **Crossing midnight:** Adding 1440 only when logout time-of-day is earlier creates a continuous next-day endpoint.
- **Times not equal:** The contract removes ambiguity between a zero-length session and a full 24-hour session.
- **Partial first and last rounds:** Upward login rounding and downward logout rounding exclude them independently.
- **Integer ceiling:** `(a + 14) // 15` is valid because minutes are nonnegative. Using ordinary floor division for login would incorrectly count a round already in progress.
- **Longest possible session:** An overnight interval can approach but not exceed 24 hours because equal clock times are disallowed; the boundary difference remains within one day's 96 scheduled rounds.
