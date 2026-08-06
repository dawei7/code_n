## Description

A sentence can be represented as an ordered array of words. For example, `"I am happy with leetcode"` corresponds to `arr = ["I", "am", "happy", "with", "leetcode"]`.

You are given two such arrays, `sentence1` and `sentence2`, together with `similarPairs`. Each row `similarPairs[i] = [x_i, y_i]` declares the two words `x_i` and `y_i` similar. Return `true` when the two sentences are similar and `false` otherwise.

Two sentences are similar exactly when both conditions hold:

- They contain the same number of words.
- For every valid position `i`, `sentence1[i]` is similar to `sentence2[i]`.

Every word is similar to itself. Similarity is not transitive: even if `a` is similar to `b` and `b` is similar to `c`, `a` and `c` are not necessarily similar.
