## Description

Given a lowercase English string `text` and an array `words` of distinct lowercase English strings, find every occurrence in `text` of every supplied word. Represent an occurrence by its inclusive zero-based boundaries `[i, j]`, meaning that the contiguous substring from index `i` through index `j` equals one of the strings in `words`.

Return all such index pairs in ascending lexicographic order: pairs with a smaller start index come first, and pairs sharing a start index are ordered by their end index. Include overlapping occurrences, matches nested inside longer matches, and separate occurrences of the same word at different positions.
