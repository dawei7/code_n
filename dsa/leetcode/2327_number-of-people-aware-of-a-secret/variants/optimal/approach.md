## General

Let `learned[day]` be the number of people who discover the secret on that
exact day. The initial condition is `learned[1] = 1`. A cohort born on day
`start` contributes to new discoveries from day `start + delay` through day
`start + forget - 1`.

**Maintain the sharing population as a sliding window**

Before computing a day, add the cohort whose delay has just expired:
`learned[day - delay]`. Remove the cohort that forgets on this day:
`learned[day - forget]`. The resulting running total is precisely the number
of people allowed to share today, and every one of them teaches one new
person, so it is also `learned[day]`.

Each update preserves the window of discovery days
$[\texttt{day}-\texttt{forget}+1,\ \texttt{day}-\texttt{delay}]$. Those and
only those cohorts know the secret and are old enough to share. Therefore the
new cohort count is correct by induction from day 1.

After day `n`, cohorts discovered on or before `n - forget` have forgotten.
Summing the remaining entries from `n - forget + 1` through `n` counts exactly
the people who still know the secret. Apply the modulus during every update
and to the final sum.

## Complexity detail

The algorithm performs constant work for each of the $n$ days and one final
sum over at most $n$ cohorts, so it uses $O(n)$ time. The daily cohort array
contains $n+1$ entries and uses $O(n)$ space.

## Alternatives and edge cases

- **Prefix-sum dynamic programming:** Prefix sums can obtain each sharing
  window in constant time and have the same $O(n)$ bounds, but the rolling
  sharing total makes the two boundary events more explicit.
- **Direct cohort simulation:** Summing every eligible earlier cohort for each
  day is correct but takes $O(n^2)$ time.
- **Forgetting day:** A cohort must be removed before today's discoveries are
  computed because nobody shares on the day they forget.
- **One-day sharing window:** When `forget = delay + 1`, each cohort contributes
  on exactly one day; adding and removing the scheduled cohorts in the proper
  order handles this case.
- **Large counts:** Intermediate population counts grow quickly, so every
  stored daily count and the sharing total are reduced modulo $10^9+7$.
