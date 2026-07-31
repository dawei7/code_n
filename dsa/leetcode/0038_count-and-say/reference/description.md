## Description

The count-and-say sequence consists of digit strings defined recursively:

- `countAndSay(1) = "1"`.
- For $n > 1$, `countAndSay(n)` is the run-length encoding of `countAndSay(n - 1)`.

Run-length encoding scans a string by maximal consecutive groups of the same character. Each group is replaced by its length followed by that character. For example, the groups in `"3322251"` are `"33"`, `"222"`, `"5"`, and `"1"`. They encode as `"23"`, `"32"`, `"15"`, and `"11"`, producing `"23321511"`.

Given a positive integer `n`, return the $n$th string in this sequence.
