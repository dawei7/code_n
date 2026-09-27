# Guided Example: Determine if Two Events Have Conflict

## 1. The instance and what "conflict" means

Each event is a pair of timestamps on the same day, written in 24-hour
`HH:MM` form, and it covers every minute from its start through its end. An
event is therefore a **closed interval** of the day's timeline:

$$
I_1 = [s_1, e_1], \qquad I_2 = [s_2, e_2],
$$

where $s_1 \le e_1$ and $s_2 \le e_2$ are guaranteed by the problem. A conflict
exists exactly when the two intervals share at least one instant, that is, when
$I_1 \cap I_2 \neq \emptyset$. This lesson works through the first official
example, chosen because it sits precisely on the inclusive-endpoint boundary:

- **Input:** $event1 = [\texttt{"01:15"}, \texttt{"02:00"}]$ and
  $event2 = [\texttt{"02:00"}, \texttt{"03:00"}]$
- **Required output:** `true`

The first event ends at `"02:00"` and the second begins at `"02:00"`. Whether
the method answers `true` or `false` here depends entirely on one modelling
decision: whether an interval includes its endpoints. The problem defines a
conflict as a non-empty intersection, and a single shared moment is non-empty,
so the two events do conflict at `02:00`.

---

## 2. Turning `HH:MM` strings into an ordered quantity

No parsing is required if the comparison uses the right ordering. Every
timestamp has exactly five characters, hour digits are zero-padded to two
positions, minute digits are zero-padded to two positions, and the colon always
occupies index 2.

Because the widths are fixed, lexicographic (character-by-character) comparison
of two timestamps agrees with chronological comparison. When two such strings
first differ, that differing position is the most significant decimal place in
which the two times differ, and the larger digit there belongs to the later
time. The colon sits at the same index in both strings, so it can never be the
position that decides the comparison.

| Left timestamp | Right timestamp | Lexicographic outcome | Chronological meaning |
|---|---|---|---|
| `"01:15"` | `"02:00"` | left is smaller | hour 1 precedes hour 2 |
| `"09:45"` | `"10:00"` | left is smaller | hour 9 precedes hour 10, even though the digit `9` exceeds `1` at the first position |
| `"14:05"` | `"14:50"` | left is smaller | identical hour, minute 05 precedes 50 |
| `"02:00"` | `"02:00"` | equal | the same instant to the minute |
| `"23:59"` | `"00:00"` | left is larger | the last minute of the day is the largest timestamp |

The second row is the reason the zero-padding guarantee matters. Written as
`"9:45"`, the string would compare *after* `"10:00"` because the character `9`
outranks `1`, and a naive string test would silently reverse the chronology.

---

## 3. Describing disjointness instead of intersection

It is easier to enumerate the ways two closed intervals *fail* to intersect than
to enumerate the ways they do. Two intervals on a line are disjoint in exactly
two configurations.

| Disjoint configuration | Ordering condition | What it looks like |
|---|---|---|
| Event 1 lies entirely before event 2 | $e_1 < s_2$ | `... 1 ...` then `... 2 ...` |
| Event 2 lies entirely before event 1 | $e_2 < s_1$ | `... 2 ...` then `... 1 ...` |

Both conditions use strict inequalities. If $e_1 = s_2$, the shared endpoint
belongs to both closed intervals, so the two events intersect and must not be
classified as disjoint. The same reasoning applies when $e_2 = s_1$.

Negating the disjunction gives the decision rule used by the method: a conflict
exists exactly when neither strict condition holds. Equivalently, and perhaps
more transparently, the intervals intersect exactly when the later start is no
later than the earlier end:

$$
\max(s_1, s_2) \le \min(e_1, e_2).
$$

Both forms are logically identical, and each is worth checking against the
representative instance.

---

## 4. Worked check on the touching-endpoint instance

Substituting the representative timestamps gives
$s_1 = \texttt{"01:15"}$, $e_1 = \texttt{"02:00"}$,
$s_2 = \texttt{"02:00"}$, $e_2 = \texttt{"03:00"}$.

| Evaluation step | Expression under test | Value of the expression | Meaning |
|---|---|---|---|
| Does event 1 start after event 2 ends? | $s_1 > e_2$ | `"01:15" > "03:00"` is false | event 1 does not lie after event 2 |
| Does event 1 end before event 2 starts? | $e_1 < s_2$ | `"02:00" < "02:00"` is false | the endpoint is shared, so this is *not* strictly before |
| Any disjoint configuration left? | $s_1 > e_2 \ \lor\ e_1 < s_2$ | false | the intervals must intersect |
| Cross-check with the overlap formula | $\max(s_1,s_2) \le \min(e_1,e_2)$ | `"02:00" <= "02:00"` is true | the shared instant is exactly `02:00` |
| Final state | — | conflict | return `true` |

The second row is the whole lesson in one line. Changing `<` to `<=` there — or
changing `>` to `>=` in the first row — would declare this pair disjoint and
return `false`, contradicting the problem's own first example.

---

## 5. How tight the boundary is at minute resolution

Timestamps are exact to the minute and each interval is closed, so the two
outcomes are separated by the smallest possible time step. The table contrasts
the representative instance with the nearest possible non-conflict.

| Pair of events | $e_1$ versus $s_2$ | Disjoint predicate | Outcome |
|---|---|---|---|
| `["01:15","02:00"]` and `["02:00","03:00"]` | equal | false | `true`, they share `02:00` |
| `["08:00","08:59"]` and `["09:00","09:30"]` | `"08:59" < "09:00"` | true | `false`, a one-minute gap separates them |
| `["12:34","12:34"]` and `["12:34","12:34"]` | both point events at the same minute | false | `true`, identical instants intersect |
| `["00:00","23:59"]` and `["23:59","23:59"]` | equal at the last minute of the day | false | `true`, the full day contains the final point |

The first two rows differ only by whether the boundary minute is shared or
skipped. A minute-resolution timeline has no room between them, which is why the
strictness of the disjoint test is the crux of the problem.

---

## 6. Other boundary shapes handled by the same two comparisons

| Scenario | $event1$ | $event2$ | Disjoint test | Result | Reason |
|---|---|---|---|---|---|
| Containment | `["09:00","17:00"]` | `["12:30","13:00"]` | neither condition holds | `true` | the smaller event sits strictly inside the larger |
| Reversed supply order | `["18:00","19:00"]` | `["06:00","07:00"]` | $s_1 > e_2$ is true | `false` | the later event is presented first, so the second condition must also be tested |
| Point event before a range | `["01:15","01:15"]` | `["02:00","03:00"]` | $e_1 < s_2$ is true | `false` | a zero-length event still needs a shared minute |
| Point event inside a range | `["01:15","02:00"]` | `["02:00","02:00"]` | neither condition holds | `true` | the point coincides with the first event's final minute |

Two structural facts explain why the method only ever needs these two tests.
First, because both events stay inside a single day and each satisfies
$s_i \le e_i$, the case of an event wrapping past midnight never arises, so
ordinary ordering of the endpoints is meaningful. Second, the two disjoint
conditions cannot both hold at once: if $e_1 < s_2$ and $e_2 < s_1$ were both
true, chaining them would give
$e_1 < s_2 \le e_2 < s_1 \le e_1$, a contradiction. Disjointness is therefore a
genuine either/or, and testing the disjunction is exactly as strong as testing
each case separately.

---

## 7. Why the reasoning is correct

> **Invariant.** For two closed intervals on one day, the predicate
> $s_1 > e_2 \ \lor\ e_1 < s_2$ is true if and only if $I_1 \cap I_2$ is empty.

*Soundness.* If $s_1 > e_2$, then every instant of $I_1$ is at least $s_1$ and
therefore strictly greater than $e_2$, which is the largest instant of $I_2$;
no instant is common. The case $e_1 < s_2$ is symmetric. So a `false` answer,
which is the negation of the predicate, always corresponds to a genuine shared
instant.

*Completeness.* Suppose the intervals are disjoint. Then $e_2 < s_1$ or
$e_1 < s_2$, because if both $e_2 \ge s_1$ and $e_1 \ge s_2$ then
$\max(s_1,s_2) \le \min(e_1,e_2)$ and that common bound is an instant belonging
to both intervals. Hence the predicate is true whenever the intervals are
disjoint, and a `true` answer is never reported for a disjoint pair.

Combining the two directions with the fixed-width lexicographic order of
Section 2 gives an exact decision procedure: the timestamps compare
chronologically, and the interval predicate is a faithful translation of
"non-empty intersection".

---

## 8. Alternatives and their trade-offs

| Method | Idea | Time | Auxiliary space | Trade-off |
|---|---|---|---|---|
| Two strict comparisons of timestamp strings | negate the two disjoint configurations | $O(1)$ | $O(1)$ | the method used here; relies on fixed-width zero padding |
| Later-start versus earlier-end | test $\max(s_1,s_2) \le \min(e_1,e_2)$ | $O(1)$ | $O(1)$ | equally correct; makes the shared instant explicit |
| Numerical minutes | convert each timestamp to $60h + m$ and compare integers | $O(1)$ | $O(1)$ | robust for unpadded or variable formats, unnecessary under this contract |
| Bitmap of the day | mark every minute each event covers, then test the intersection of the marks | $O(1440)$ | $O(1440)$ bits | correct but wasteful; it hides that overlap depends only on endpoints |

The bitmap variant is the instructive failure of judgement: it produces the same
answers while turning a four-timestamp decision into a scan over an entire day,
and it invites the classic mistake of treating the end minute as exclusive, in
which case the representative instance would be reported as a non-conflict.

---

## 9. Complexity derivation

**Time.** Each timestamp is a string of exactly $m = 5$ characters, and the
comparison of two such strings examines at most $m$ characters before deciding.
The method performs two such comparisons and combines their results with
constant-time Boolean work. Under the problem's fixed-width contract $m$ is a
constant, so the running time is

$$
O(m) = O(1),
$$

and it does not grow with the number of events, the length of the day, or the
magnitude of the times. Substituting minutes for strings would not change
asymptotics; it would only replace a five-character scan with a constant-time
integer comparison.

**Auxiliary space.** The method stores no parsed copies, no collection and no
recursion. It reads the four timestamp positions in place and evaluates one
short-circuiting disjunction, so peak auxiliary space is

$$
O(1).
$$

---

## 10. Traps this instance exposes

- **Exclusive endpoints:** treating an event as covering $[s, e)$ makes
  `"02:00"` non-shared and returns `false` for the representative instance.
- **Reversing a strict inequality:** writing the disjoint test with `>=` or
  `<=` converts a touching endpoint into a false non-conflict.
- **Testing only one ordering:** an instance supplied as
  `["18:00","19:00"]` against `["06:00","07:00"]` is disjoint through
  $s_1 > e_2$ alone, while the representative instance is decided by the other
  term; both terms must be present.
- **Assuming one interval always precedes the other in the input:** the pairs
  are unordered, and the second event may be the earlier one.
- **Comparing unpadded times as strings:** `"9:00"` would sort after `"10:00"`,
  so the fixed `HH:MM` width is what makes string order chronological.
- **Ignoring the minute granularity:** a one-minute gap is the tightest possible
  non-conflict, and it is easy to shrink it to zero by an off-by-one in the
  endpoint test.
- **Assuming midnight wrap-around:** every event lies within one day and no
  interval crosses midnight, so `"23:59"` is simply the largest timestamp.
- **Zero-length events:** a point event such as `["12:34","12:34"]` is still a
  legal closed interval and can conflict.