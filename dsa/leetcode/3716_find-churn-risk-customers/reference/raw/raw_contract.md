## Function Contract

**Inputs**

- `subscription_events`: The table of chronological subscription-state changes described above.

The current plan and amount come from the latest event for each user. Historical maximum and downgrade presence use the user's complete event history. The 50% comparison is strict: an amount equal to half the historical maximum does not qualify.

**Return value**

Return an ordered table with columns:

- `user_id`
- `current_plan`
- `current_monthly_amount`
- `max_historical_amount`
- `days_as_subscriber`

`days_as_subscriber` is the calendar-day difference between the user's last and first event dates.
