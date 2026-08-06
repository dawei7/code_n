## Description

You are given an array `words` containing lowercase English words. A word is
eligible when every nonempty prefix obtained by taking its first $1, 2, \ldots,
\lvert w \rvert$ characters also occurs as an element of `words`. Thus the word
itself must be present, as must the one-character word that begins its prefix
chain and every intermediate length.

Return the longest eligible word. When several eligible words have the same
maximum length, choose the lexicographically smallest one. If no input word has
all of its required prefixes, return the empty string.
