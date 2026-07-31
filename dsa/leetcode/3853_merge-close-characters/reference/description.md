## Description

You are given a string `s` of lowercase English letters and an integer `k`. All indices and distances below refer to the current form of the string, which may become shorter as merges occur.

Two equal characters are close when the distance between their current indices is at most `k`. A merge keeps the left character and removes the right character. Perform exactly one merge at a time, update the string and its indices, and continue until no close equal pair remains.

Return the string left after every possible merge has been performed.

**Note.** When more than one merge is currently possible, choose the pair with the smallest left index. If that left index can pair with several right indices, choose the smallest such right index.
