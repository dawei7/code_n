### 1. Description

Given a string `paragraph` and a string array of the banned words `banned`, return *the most frequent word that is not banned*. It is **guaranteed** there is **at least one word** that is not banned, and that the answer is **unique**.

The words in `paragraph` are **case-insensitive** and the answer should be returned in **lowercase**.

### 2. Function Contract

**Inputs**

- `paragraph`: Input parameter (`str`).
- `banned`: Input parameter (`List[str]`).

**Return value**

- Returns `str`.

### 3. Note

that words can not contain punctuation symbols.

### 4. Examples

#### Example 1

- **Input:** $paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]$
- **Output:** `"ball"`
- **Explanation:** "hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.

#### Example 2

- **Input:** $paragraph = "a.", banned = []$
- **Output:** `"a"`

### 5. Constraints

- $1 \le \text{paragraph.length} \le 1000$

- paragraph consists of English letters, space `' '`, or one of the symbols: `"!?',;."`.

- $0 \le \text{banned.length} \le 100$

- $1 \le \text{banned}[i].length \le 10$

- $\text{banned}[i]$ consists of only lowercase English letters.
