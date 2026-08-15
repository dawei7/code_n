### 1. Description

Given an array of strings `words`, return *the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below*.

### 2. Function Contract

**Inputs**

- `words`: Input parameter (`List[str]`).

**Return value**

- Returns `List[str]`.

### 3. Note

that the strings are **case-insensitive**, both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the **American keyboard**:

- the first row consists of the characters `"qwertyuiop"`,

- the second row consists of the characters `"asdfghjkl"`, and

- the third row consists of the characters `"zxcvbnm"`.

![](images/keyboard.png)

### 4. Examples

#### Example 1

- **Input:** words = ["Hello","Alaska","Dad","Peace"]

- **Output:** ["Alaska","Dad"]

- **Explanation:** Both `"a"` and `"A"` are in the 2nd row of the American keyboard due to case insensitivity.

#### Example 2

- **Input:** words = ["omk"]

- **Output:** []

#### Example 3

- **Input:** words = ["adsdf","sfd"]

- **Output:** ["adsdf","sfd"]

### 5. Constraints

- $1 \le \text{words.length} \le 20$

- $1 \le \text{words}[i].length \le 100$

- $\text{words}[i]$ consists of English letters (both lowercase and uppercase).
