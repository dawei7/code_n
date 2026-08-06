## Function Contract

**Inputs**

- `year`: the calendar year whose month length is requested.
- `month`: the numeric month, with `1` denoting January and `12` denoting December.

April, June, September, and November have 30 days. Every other non-February month has 31 days. February has 29 days when `year` is divisible by 400, or when it is divisible by 4 but not by 100; otherwise February has 28 days.

**Return value**

- The integer number of days in the specified month and year.
