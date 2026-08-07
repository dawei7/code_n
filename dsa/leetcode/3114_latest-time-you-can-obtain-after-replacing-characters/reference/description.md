### 1. Description

You are given a string `s` representing a 12-hour format time where some of the digits (possibly none) are replaced with a `"?"`.

12-hour times are formatted as `"HH:MM"`, where `HH` is between `00` and `11`, and `MM` is between `00` and `59`. The earliest 12-hour time is `00:00`, and the latest is `11:59`.

You have to replace **all** the `"?"` characters in `s` with digits such that the time we obtain by the resulting string is a **valid** 12-hour format time and is the **latest** possible.

Return *the resulting string*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "1?:?4"

**Output:** "11:54"

**Explanation:** The latest 12-hour format time we can achieve by replacing `"?"` characters is `"11:54"`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "0?:5?"

**Output:** "09:59"

**Explanation:** The latest 12-hour format time we can achieve by replacing `"?"` characters is `"09:59"`.

</div>

### 4. Constraints

- $\text{s.length} = 5$

- $s[2]$ is equal to the character `":"`.

- All characters except $s[2]$ are digits or `"?"` characters.

- The input is generated such that there is **at least** one time between `"00:00"` and `"11:59"` that you can obtain after replacing the `"?"` characters.