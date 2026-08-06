## Description

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s_1 -> s_2 -> ... -> s_k` such that:

<ul>
	<li>Every adjacent pair of words differs by a single letter.</li>
	<li>Every `s_i` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.</li>
	<li>`s_k == endWord`</li>
</ul>

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return *all the **shortest transformation sequences** from* `beginWord` *to* `endWord`*, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words *`[beginWord, s_1, s_2, ..., s_k]`.
