## Description

You are given a string `word`, and an integer `numFriends`.

Alice is organizing a game for her `numFriends` friends. There are multiple rounds in the game, where in each round:

	- `word` is split into `numFriends` **non-empty** strings, such that no previous round has had the **exact** same split.

	- All the split words are put into a box.

Find the **lexicographically largest** string from the box after all the rounds are finished.

A string `a` is **lexicographically smaller** than a string `b` if in the first position where `a` and `b` differ, string `a` has a letter that appears earlier in the alphabet than the corresponding letter in `b`.

If the first `min(a.length, b.length)` characters do not differ, then the shorter string is the lexicographically smaller one.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">word = "dbca", numFriends = 2</span>

**Output:** <span class="example-io">"dbc"</span>

**Explanation:**

All possible splits are:

	- `"d"` and `"bca"`.

	- `"db"` and `"ca"`.

	- `"dbc"` and `"a"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">word = "gggg", numFriends = 4</span>

**Output:** <span class="example-io">"g"</span>

**Explanation:**

The only possible split is: `"g"`, `"g"`, `"g"`, and `"g"`.

</div>

**Constraints:**

	- `1 <= word.length <= 2 * 10^5`

	- `word` consists only of lowercase English letters.

	- `1 <= numFriends <= word.length`
