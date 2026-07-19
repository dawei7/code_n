## General
Left join every user to rides on the user identifier. Group by the user's identifier and name, sum ride distances, and replace the null aggregate for an unmatched user with zero.

The left join contributes every matching ride to exactly its user while preserving one null-extended row for a user without rides. Summation therefore gives each true total, and `COALESCE` gives exactly zero only for the no-ride case. Grouping by the identifier keeps different users separate even if names happen to match.

Finally order by the computed total descending and `name` ascending to apply both required ranking keys.

## Complexity detail
With indexed or hash joining, reading $U$ users and $R$ rides and aggregating by user takes $O(U + R)$ time and $O(U)$ grouping space. Sorting the $U$ output rows adds $O(U\log U)$ time.

## Alternatives and edge cases
- **Correlated sum per user:** A scalar subquery is concise but can rescan all $R$ rides for each user, costing $O(UR)$ without an effective index.
- **Inner join:** It incorrectly removes users who have no rides.
- **Null aggregate:** Convert it to integer zero with `COALESCE`.
- **Several rides:** Sum every distance for the user rather than selecting one row.
- **Equal totals:** Apply name ascending as the secondary ordering key.
- **Equal names:** Group by user ID as well as name so separate user records are not merged.
