## Description

Given a `time` represented in the format `"HH:MM"`, form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, `"01:34"`, `"12:09"` are all valid. `"1:34"`, `"12:9"` are all invalid.
### Function Contract

`solve(time: str) -> str`

**Inputs**

- `time`: a valid zero-padded 24-hour time string in `"HH:MM"` format.

**Return value**

Return the first valid `"HH:MM"` display reached by moving forward in time whose four digits all come from the input display. Digits may be reused any number of times.

### Examples
#### Example 1

- **Input:** $time = "19:34"$
- **Output:** `"19:39"`
- **Explanation:** The next closest time choosing from digits **1**, **9**, **3**, **4**, is **19:39**, which occurs 5 minutes later.
It is not **19:33**, because this occurs 23 hours and 59 minutes later.
#### Example 2

- **Input:** $time = "23:59"$
- **Output:** `"22:22"`
- **Explanation:** The next closest time choosing from digits **2**, **3**, **5**, **9**, is **22:22**.
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
### Constraints

- $\text{time.length} = 5$

- `time` is a valid time in the form `"HH:MM"`.

- $0 \le HH < 24$

- $0 \le MM < 60$