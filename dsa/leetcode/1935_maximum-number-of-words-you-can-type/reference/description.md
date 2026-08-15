### 1. Description

There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string `text` of words separated by a single space (no leading or trailing spaces) and a string `brokenLetters` of all **distinct** letter keys that are broken, return *the **number of words** in* `text` *you can fully type using this keyboard*.

### 2. Function Contract

**Inputs**

- `text`: Input parameter (`str`).
- `brokenLetters`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $text = "hello world", brokenLetters = "ad"$
- **Output:** `1`
- **Explanation:** We cannot type "world" because the 'd' key is broken.

#### Example 2

- **Input:** $text = "leet code", brokenLetters = "lt"$
- **Output:** `1`
- **Explanation:** We cannot type "leet" because the 'l' and 't' keys are broken.

#### Example 3

- **Input:** $text = "leet code", brokenLetters = "e"$
- **Output:** `0`
- **Explanation:** We cannot type either word because the 'e' key is broken.

### 4. Constraints

- $1 \le \text{text.length} \le 10^{4}$

- $0 \le \text{brokenLetters.length} \le 26$

- `text` consists of words separated by a single space without any leading or trailing spaces.

- Each word only consists of lowercase English letters.

- `brokenLetters` consists of **distinct** lowercase English letters.
