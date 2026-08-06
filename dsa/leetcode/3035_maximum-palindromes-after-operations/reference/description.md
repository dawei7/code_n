## Description

You are given a **0-indexed** string array `words` having length `n` and containing **0-indexed** strings.

You are allowed to perform the following operation **any** number of times (**including** **zero**):

<ul>
	<li>Choose integers `i`, `j`, `x`, and `y` such that `0 <= i, j < n`, `0 <= x < words[i].length`, `0 <= y < words[j].length`, and **swap** the characters `words[i][x]` and `words[j][y]`.</li>
</ul>

Return *an integer denoting the **maximum** number of <span data-keyword="palindrome-string">palindromes</span> *`words`* can contain, after performing some operations.*

**Note:** `i` and `j` may be equal during an operation.
