### 1. Description

You are given a string `s` of even length. Split this string into two halves of equal lengths, and let `a` be the first half and `b` be the second half.

Two strings are **alike** if they have the same number of vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`, `'A'`, `'E'`, `'I'`, `'O'`, `'U'`). Notice that `s` contains uppercase and lowercase letters.

Return `true`* if *`a`* and *`b`* are **alike***. Otherwise, return `false`.

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).

**Return value**

- Returns `bool`.

### 3. Examples

#### Example 1

- **Input:** `s = "book"`
- **Output:** `true`
- **Explanation:** a = "b<u>o</u>" and b = "<u>o</u>k". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

#### Example 2

- **Input:** `s = "textbook"`
- **Output:** `false`
- **Explanation:** a = "t<u>e</u>xt" and b = "b<u>oo</u>k". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

### 4. Constraints

- $2 \le \text{s.length} \le 1000$

- `s.length` is even.

- `s` consists of **uppercase and lowercase** letters.
