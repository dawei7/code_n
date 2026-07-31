## Description

A transformation sequence from `beginWord` to `endWord`, using dictionary `wordList`, has the form `beginWord -> s1 -> s2 -> ... -> sk` and must satisfy every rule below:

- Each adjacent pair differs in exactly one letter.
- Every word `si`, for $1 \le i \le k$, belongs to `wordList`; `beginWord` itself does not have to be in the dictionary.
- The final word `sk` equals `endWord`.

Given `beginWord`, `endWord`, and `wordList`, return the number of words in the shortest valid transformation sequence. Return `0` if no sequence reaches `endWord`.
