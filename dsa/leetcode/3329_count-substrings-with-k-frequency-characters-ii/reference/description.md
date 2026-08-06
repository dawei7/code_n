## Description

Given a lowercase English string `s` and a positive integer `k`, consider every nonempty contiguous substring of `s`. A substring qualifies when at least one character occurs at least `k` times inside that substring. The character that reaches the threshold may differ between substrings, and no particular character is designated beforehand.

Return the total number of qualifying substrings. Substrings are distinguished by their start and end indices, so equal text at different positions contributes more than once. Once a substring qualifies, extending it to the right cannot make it invalid because existing character frequencies never decrease.
