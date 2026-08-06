## Description

You are given a list `synonyms` of equivalent string pairs. Each entry `[s_i, t_i]` declares that its two strings are synonymous. Words connected through a chain of equivalent pairs belong to the same synonym group and may be used interchangeably when forming a sentence.

You are also given a sentence `text`. Generate every sentence obtainable by choosing an equivalent form for each replaceable word while preserving the word positions and spacing. Words with no listed equivalent remain unchanged. Return all possible synonymous sentences sorted lexicographically.
