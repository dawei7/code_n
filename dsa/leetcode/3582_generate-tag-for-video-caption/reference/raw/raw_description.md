## Description

You are given a string `<font face="monospace">caption</font>` representing the caption for a video.

The following actions must be performed **in order** to generate a **valid tag** for the video:

	- **Combine all words** in the string into a single *camelCase string* prefixed with `'#'`. A *camelCase string* is one where the first letter of all words *except* the first one is capitalized. All characters after the first character in **each** word must be lowercase.

	- **Remove** all characters that are not an English letter, **except** the first `'#'`.

	- **Truncate** the result to a maximum of 100 characters.

Return the **tag** after performing the actions on `caption`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">caption = "Leetcode daily streak achieved"</span>

**Output:** <span class="example-io">"#leetcodeDailyStreakAchieved"</span>

**Explanation:**

The first letter for all words except `"leetcode"` should be capitalized.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">caption = "can I Go There"</span>

**Output:** <span class="example-io">"#canIGoThere"</span>

**Explanation:**

The first letter for all words except `"can"` should be capitalized.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">caption = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"</span>

**Output:** <span class="example-io">"#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"</span>

**Explanation:**

Since the first word has length 101, we need to truncate the last two letters from the word.

</div>

**Constraints:**

	- `1 <= caption.length <= 150`

	- `caption` consists only of English letters and `' '`.
