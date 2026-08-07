## Description

Given an array of strings `words`, return *the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below*.

**Note** that the strings are **case-insensitive**, both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the **American keyboard**:

	- the first row consists of the characters `"qwertyuiop"`,

	- the second row consists of the characters `"asdfghjkl"`, and

	- the third row consists of the characters `"zxcvbnm"`.

![](images/keyboard.png)

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">words = ["Hello","Alaska","Dad","Peace"]</span>

**Output:** <span class="example-io">["Alaska","Dad"]</span>

**Explanation:**

Both `"a"` and `"A"` are in the 2nd row of the American keyboard due to case insensitivity.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">words = ["omk"]</span>

**Output:** <span class="example-io">[]</span>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">words = ["adsdf","sfd"]</span>

**Output:** <span class="example-io">["adsdf","sfd"]</span>

</div>

**Constraints:**

	- `1 <= words.length <= 20`

	- `1 <= words[i].length <= 100`

	- `words[i]` consists of English letters (both lowercase and uppercase).
