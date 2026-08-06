## Description

You are given a string `s` consisting of lowercase English letters, and an integer `k`. Your task is to *convert* the string into an integer by a special process, and then *transform* it by summing its digits repeatedly `k` times. More specifically, perform the following steps:

<ol>
	<li>**Convert** `s` into an integer by replacing each letter with its position in the alphabet (i.e. replace `'a'` with `1`, `'b'` with `2`, ..., `'z'` with `26`).</li>
	<li>**T****ransform** the integer by replacing it with the **sum of its digits**.</li>
	<li>Repeat the **transform** operation (step 2) `k`** times** in total.</li>
</ol>

For example, if `s = "zbax"` and `k = 2`, then the resulting integer would be `8` by the following operations:

<ol>
	<li>**Convert**: `"zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124`</li>
	<li>**Transform #1**: `262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17`</li>
	<li>**Transform #2**: `17 ➝ 1 + 7 ➝ 8`</li>
</ol>

Return the **resulting** **integer** after performing the **operations** described above.
