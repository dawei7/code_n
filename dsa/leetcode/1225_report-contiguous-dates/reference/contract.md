## Function Contract

**Input tables**

`Failed(fail_date)` and `Succeeded(success_date)` contain unique dates for the corresponding task outcomes. Let $d$ be the combined number of rows whose dates fall from `2019-01-01` through `2019-12-31`, inclusive.

**Return value**

- Return exactly the columns `period_state`, `start_date`, and `end_date`.
- Produce one row for every maximal continuous interval of recorded days having the same state.
- Use only the lowercase labels `failed` and `succeeded`.
- For a one-day interval, return the same date as both endpoints.
- Ignore dates outside 2019 when forming the reported intervals.
- Order the rows by `start_date` in ascending order.
