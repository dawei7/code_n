## Description

You are given a string `s` containing one or more words separated by single spaces. Every word consists only of lowercase English letters.

Construct the conceptual expanded string `t` word by word. Within each word, repeat its first character once, its second character twice, and in general its character at one-based position $p$ exactly $p$ times. Keep the single spaces between words as single spaces in `t`.

For example, when `s = "hello world"`, the expansion is `t = "heelllllllooooo woorrrllllddddd"`.

You are also given `k`, which is guaranteed to be a valid zero-based index of `t`.

Return the character stored at index `k` in the expanded string.
