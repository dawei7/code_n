## Function Contract

`solve(time: str) -> str`

**Inputs**

- `time`: a valid zero-padded 24-hour time string in `"HH:MM"` format.

**Return value**

Return the first valid `"HH:MM"` display reached by moving forward in time whose four digits all come from the input display. Digits may be reused any number of times.
