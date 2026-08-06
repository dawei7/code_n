## Description

A string `compressed` describes character frequencies as consecutive groups. Each group contains one lowercase English letter followed by its positive decimal frequency. The same letter may occur in several different groups, and a frequency may contain multiple digits. For example, `"a3b1a1c2"` represents three `a` characters, one `b`, one more `a`, and two `c` characters.

Create a better compression in which every letter with a nonzero total frequency appears exactly once. Its count must be the sum of that letter's counts across all input groups, and the output groups must be ordered alphabetically by letter. Reordering the groups is explicitly allowed.
