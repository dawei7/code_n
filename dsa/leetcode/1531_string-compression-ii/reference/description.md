## Description

<a href="http://en.wikipedia.org/wiki/Run-length_encoding">Run-length encoding</a> is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string `"aabccc"` we replace <font face="monospace">`"aa"`</font> by <font face="monospace">`"a2"`</font> and replace <font face="monospace">`"ccc"`</font> by <font face="monospace">`"c3"`</font>. Thus the compressed string becomes <font face="monospace">`"a2bc3"`.</font>

Notice that in this problem, we are not adding `'1'` after single characters.

Given a string `s` and an integer `k`. You need to delete **at most** `k` characters from `s` such that the run-length encoded version of `s` has minimum length.

Find the *minimum length of the run-length encoded version of *`s`* after deleting at most *`k`* characters*.
