### 1. Description

You own a **Goal Parser** that can interpret a string `command`. The `command` consists of an alphabet of `"G"`, `"()"` and/or `"(al)"` in some order. The Goal Parser will interpret `"G"` as the string `"G"`, `"()"` as the string `"o"`, and `"(al)"` as the string `"al"`. The interpreted strings are then concatenated in the original order.

Given the string `command`, return *the **Goal Parser**'s interpretation of *`command`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $command = "G()(al)"$
- **Output:** `"Goal"`
- **Explanation:** The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
#### Example 2

- **Input:** $command = "G()()()()(al)"$
- **Output:** `"Gooooal"`
#### Example 3

- **Input:** $command = "(al)G(al)()()G"$
- **Output:** `"alGalooG"`

### 4. Constraints

- $1 \le \text{command.length} \le 100$

- `command` consists of `"G"`, `"()"`, and/or `"(al)"` in some order.