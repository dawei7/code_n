## General

**Find the intersection endpoints first**

Alice's inclusive date interval and Bob's inclusive date interval overlap from the later arrival through the earlier departure.

The exact source computes:

```python
a = max(arriveAlice, arriveBob)
b = min(leaveAlice, leaveBob)
```

Because every date uses fixed-width zero-padded format `"MM-DD"` within the same year, lexicographic string order is chronological order. The month occupies the first two characters, and when months tie, the day occupies the last two.

This property would fail for formats such as `"M-D"` without leading zeros or for dates spanning different years, but both are excluded.

**Convert one date to its day-of-year ordinal**

The month-length tuple lists the twelve non-leap-year month sizes. For date string `a`:

```python
sum(days[: int(a[:2]) - 1]) + int(a[3:])
```

adds all days in months strictly before `a`'s month, then adds its one-based day within the current month. January 1 becomes ordinal one.

The same conversion produces `y` for overlap end `b`.

For August 16, the prefix sums January through July, then adds sixteen. Comparing or subtracting ordinals now works across month boundaries without separate date cases.

**Count an inclusive interval**

If overlap start ordinal is `x` and end ordinal is `y`, the number of included days is:

$$
y-x+1.
$$

The plus one counts both endpoints. When both travelers share exactly one date, `x = y` and the formula returns one.

If the intervals do not overlap, the later arrival lies after the earlier departure, so `y - x + 1` is zero or negative. The final:

```python
max(y - x + 1, 0)
```

returns zero instead of a negative day count.

**Trace the August example**

The later arrival is August 16, and the earlier departure is August 18. Their ordinal difference is two, and inclusive length is `2 + 1 = 3`. These dates are the sixteenth, seventeenth, and eighteenth.

For Alice ending October 31 and Bob arriving November 1, intersection start is November 1 while intersection end is October 31. The ordinal formula is nonpositive and clamps to zero.

**Why string max and min are safe**

Compare two valid fixed-format dates. If their months differ, the first differing character occurs within the zero-padded two-digit month, so lexicographic order matches numeric month order. If months match, the first differing character is within the zero-padded day, so it matches numeric day order.

Thus, selecting max arrivals and min departures as strings produces the same endpoints as converting all four dates first. The source saves two ordinal conversions by exploiting the representation.

**Why the ordinal conversion is correct**

Every day before month $m$ belongs to exactly one of months one through $m-1$, and the prefix sum counts all of them. Adding day $d$ counts days one through $d$ in the current month. The result is the unique one-based position of that date in the year.

Ordinal conversion preserves chronological order and differences. Therefore, the inclusive numeric intersection length equals the number of shared calendar dates.

**Why converting only two dates loses nothing**

Let `ord(date)` be the day-of-year conversion. Because both string comparison and `ord` preserve chronological order, they commute with endpoint selection:

$$
\operatorname{ord}(\max(A,B))=\max(\operatorname{ord}(A),\operatorname{ord}(B)),
$$

and the analogous identity holds for `min`. The source first chooses the later arrival and earlier departure as strings, then converts them. A four-conversion approach would choose the same two numeric endpoints. No duration information from the discarded earlier arrival or later departure can affect the interval intersection.

**No leap-year adjustment**

February is fixed at 28 days by the statement. The tuple exactly represents the specified year. Introducing leap-year logic would be unnecessary and could contradict the contract.

## Complexity detail

The date strings have fixed length five, and the month tuple has fixed length twelve. String max/min, slicing, integer parsing, and summing at most eleven month values all take constant bounded work.

Time complexity is $O(1)$ and auxiliary space is $O(1)$. The tuple itself contains twelve fixed integers.

If generalized to an arbitrary calendar with $M$ months and no prefix preprocessing, each ordinal conversion would cost $O(M)$; here $M=12$ is a fixed constant.

## Alternatives and edge cases

- **Convert all four dates first:** Then compute max ordinal arrivals and min ordinal departures. It is equally correct but performs two extra conversions.
- **Precomputed month-prefix array:** Store cumulative days before each month and convert with one lookup. Useful for many queries but unnecessary for one call.
- **Simulate every calendar day:** It works over one year but is more complex than interval arithmetic.
- **Same one shared day:** Inclusive plus one returns one.
- **Adjacent non-overlapping visits:** Later arrival one day after earlier leave produces zero after clamping.
- **Identical intervals:** The full inclusive interval length is returned.
- **Cross-month overlap:** Ordinals handle it without special branches.
- **February:** It has 28 days because the year is explicitly non-leap.
- **Fixed-width requirement:** Lexicographic date comparison depends on leading zeros.
- **Same-year requirement:** Without a year field, cross-year chronology could not be inferred.
