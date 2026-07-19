## General
**Count participants for every catalog activity.** Left join `Activities` to `Friends` on the activity name and group by the activity identity. Counting `f.id`, rather than all joined rows, gives zero to an activity with no matching friend and the exact number of friends otherwise.

**Compute the popularity bounds once.** From the grouped counts, derive the minimum and maximum participant totals. Keep only rows whose count is strictly greater than the minimum and strictly less than the maximum. Strict inequalities exclude every tie at either extreme, as required.

The grouped relation contains one row for every listed activity. Its bounds are therefore the global popularity extremes, and the final predicate returns exactly the activities at neither extreme.

## Complexity detail
In the general sort/group model, joining and grouping $N$ input rows takes $O(N \log N)$ time. Hash aggregation can make the expected time linear. The grouped counts and lookup state contain at most $A$ activities, giving $O(A)$ auxiliary space.

## Alternatives and edge cases
- **Correlated count per activity:** Counting matching friends independently for every activity is correct but may take $O(AF)$ time without an index.
- **Window functions:** Applying `MIN` and `MAX` windows to grouped counts is equivalent, though the staged aggregate is often easier to read.
- **All counts equal:** The minimum equals the maximum, so no activity qualifies.
- **Ties at one extreme:** Every activity sharing the minimum or maximum must be excluded.
- **Zero participants:** A catalog activity with no friends has count zero and can define the minimum.
- **Only two popularity levels:** Every activity belongs to an extreme, leaving an empty result.
