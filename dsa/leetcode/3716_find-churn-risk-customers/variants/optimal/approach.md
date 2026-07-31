## General

Use one windowed pass over each user's event history. `ROW_NUMBER` in descending event order identifies the current row, while windowed `MIN`, `MAX`, and a conditional maximum attach the first date, last date, greatest monthly amount, and downgrade flag to every event.

Keep only the row with recency one. That row supplies the current plan, current amount, and active/cancel status; the attached window values still summarize the complete history. Apply all four predicates together: latest type is not `cancel`, downgrade flag is present, twice the current amount is strictly less than the historical maximum, and the first-to-last date difference is at least 60.

Multiplying the current amount by two avoids rounding a percentage before the strict comparison. The date difference produces the requested duration. Finally, order by that duration descending and `user_id` ascending, matching the output contract.

## Complexity detail

Let $R$ be the number of event rows and $U$ the number of users. Partition ordering for the window functions costs $O(R\log R)$ in the general case, and sorting the qualifying users costs $O(U\log U)$. Window state and the materialized result can use $O(R+U)$ space.

## Alternatives and edge cases

- **Correlated subqueries per user:** Repeatedly finding the latest event, maximum amount, downgrade count, and date bounds can rescan the table and approach $O(R^2)$ work.
- **Group only by user:** Aggregation finds historical summaries but does not by itself preserve the current row's plan and event type; it needs a ranked-row join or equivalent.
- **Exactly 50% revenue:** The source says less than 50%, so equality must be excluded.
- **Exactly 60 days:** The duration requirement is at least 60, so equality qualifies.
- **Latest cancellation:** Historical downgrades and long tenure cannot compensate for an inactive current state.
- **No downgrade:** A low current amount reached without a `downgrade` event does not qualify.
- **First-to-last duration:** Measure the complete recorded history, not the time since the last plan change.
- **Output order:** Longer duration comes first; only equal durations use ascending `user_id`.
