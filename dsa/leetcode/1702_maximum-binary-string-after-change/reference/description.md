### 1. Description

You are given a binary string `binary` consisting of only `0`'s or `1`'s. You can apply each of the following operations any number of times:

- Operation 1: If the number contains the substring `"00"`, you can replace it with `"10"`.

		- For example, `"<u>00</u>010" -> "<u>10</u>010`"

- Operation 2: If the number contains the substring `"10"`, you can replace it with `"01"`.

		- For example, `"000<u>10</u>" -> "000<u>01</u>"`

*Return the **maximum binary string** you can obtain after any number of operations. Binary string `x` is greater than binary string `y` if `x`'s decimal representation is greater than `y`'s decimal representation.*

### 2. Function Contract

**Inputs**

- `binary`: Input parameter (`str`).

**Return value**

- Returns `str`.

### 3. Examples

#### Example 1

- **Input:** $binary = "000110"$
- **Output:** `"111011"`
- **Explanation:** A valid transformation sequence can be:
"0001<u>10</u>" -> "0001<u>01</u>"
"<u>00</u>0101" -> "<u>10</u>0101"
"1<u>00</u>101" -> "1<u>10</u>101"
"110<u>10</u>1" -> "110<u>01</u>1"
"11<u>00</u>11" -> "11<u>10</u>11"

#### Example 2

- **Input:** $binary = "01"$
- **Output:** `"01"`
- **Explanation:** "01" cannot be transformed any further.

### 4. Constraints

- $1 \le \text{binary.length} \le 10^{5}$

- `binary` consist of `'0'` and `'1'`.
