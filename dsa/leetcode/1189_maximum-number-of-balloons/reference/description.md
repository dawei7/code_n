### 1. Description

Given a string `text`, you want to use the characters of `text` to form as many instances of the word **"balloon"** as possible.

You can use each character in `text` **at most once**. Return the maximum number of instances that can be formed.

### 2. Function Contract

**Inputs**

- `text`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

**

![](images/1536_ex1_upd.JPG)

**

- **Input:** $text = "nlaebolko"$
- **Output:** `1`

#### Example 2

**

![](images/1536_ex2_upd.JPG)

**

- **Input:** $text = "loonbalxballpoon"$
- **Output:** `2`

#### Example 3

- **Input:** $text = "leetcode"$
- **Output:** `0`

### 4. Constraints

- $1 \le \text{text.length} \le 10^{4}$

- `text` consists of lower case English letters only.

### 5. Note

This question is the same as <a href="https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/" target="_blank"> 2287: Rearrange Characters to Make Target String.</a>
