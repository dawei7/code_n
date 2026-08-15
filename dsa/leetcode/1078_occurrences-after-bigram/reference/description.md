### 1. Description

Given two strings `first` and `second`, consider occurrences in some text of the form `"first second third"`, where `second` comes immediately after `first`, and `third` comes immediately after `second`.

Return *an array of all the words* `third` *for each occurrence of* `"first second third"`.

### 2. Function Contract

**Inputs**

- `text`: Input parameter (`str`).
- `first`: Input parameter (`str`).
- `second`: Input parameter (`str`).

**Return value**

- Returns `List[str]`.

### 3. Examples

#### Example 1

- **Input:** $text = "alice is a good girl she is a good student", first = "a", second = "good"$
- **Output:** `["girl","student"]`

#### Example 2

- **Input:** $text = "we will we will rock you", first = "we", second = "will"$
- **Output:** `["we","rock"]`

### 4. Constraints

- $1 \le \text{text.length} \le 1000$

- `text` consists of lowercase English letters and spaces.

- All the words in `text` are separated by **a single space**.

- $1 \le \text{first.length}, \text{second.length} \le 10$

- `first` and `second` consist of lowercase English letters.

- `text` will not have any leading or trailing spaces.
