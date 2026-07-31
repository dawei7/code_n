## General

**Keep the fixed reporting interval explicit.** Start by retaining dates from `2024-02-01` through `2024-02-28`. The half-open upper bound `2024-02-29` is intentional: although 2024 has a leap day, the problem defines its February calculation as exactly 28 days and four weeks.

**Measure every possible burst endpoint.** Partition the filtered posts by `user_id` and order each partition by `post_date`. For each row, a temporal window from six days before that date through the current date covers seven consecutive calendar days. Counting rows in that frame includes every post on both boundary dates and handles multiple posts on the same date as peers.

It is sufficient to end windows on dates that contain a post. If a seven-day interval has a fixed set of posts but ends on an empty date, shifting its right endpoint left until it reaches the latest included post cannot lose any included post; the corresponding row-anchored interval therefore has at least the same count.

**Compare each user's two aggregates.** A second window count obtains the user's total February posts, so dividing by $4$ gives the required weekly average. Group the annotated rows by user, retain the maximum temporal count, and keep the user exactly when that maximum is at least twice the average. Sorting by `user_id` finishes the output contract.

The date filter admits exactly the rows that belong to the four-week calculation. The temporal frame evaluates a count at every endpoint needed to realize a maximum, and the final maximum is consequently the greatest possible seven-day count for that user. The `HAVING` comparison is precisely the definition of bursty behavior, so the returned users and reported aggregates are correct.

## Complexity detail

Let $n$ be the number of posts from February 1 through February 28. A database may sort the filtered rows by user and date before evaluating the windows, which takes $O(n \log n)$ time in the general case. The window scans and final aggregation take $O(n)$ additional time. Filtered rows, sort state, and window state require $O(n)$ working space.

## Alternatives and edge cases

- **Correlated range count per post:** Counting matching posts with a separate subquery or self-join for every anchor is direct but can compare every pair in one user's partition and take $O(n^2)$ time.
- **Aggregate into fixed calendar weeks:** Four non-overlapping weekly buckets miss seven-day bursts that cross a bucket boundary.
- **Use a seven-row frame:** `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` counts rows rather than calendar days and mishandles dates containing multiple posts.
- **Include February 29:** That conflicts with the problem's explicit February 1 through 28 interval and four-week denominator.
- A post exactly six days before the anchor belongs to the inclusive seven-day window; a post seven days before does not.
- Multiple posts on one date are all counted in the same temporal frame.
- The threshold is inclusive, so equality qualifies.
- Users with no posts in the measured interval have neither an average nor a burst and do not appear.
