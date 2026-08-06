## Description

You are given an array of strings `chunks`. Concatenate all strings in `chunks` in order to form a string `s`.

You are also given an array of strings `queries`.

A **joiner hyphen** is a hyphen character `'-'` in `s` whose previous and next characters both exist and are lowercase English letters.

A **word** is a **maximal** <span data-keyword="substring-nonempty">substring</span> of `s` consisting only of lowercase English letters and **joiner hyphens**.

All other characters, including spaces and hyphens that are not **joiner hyphens**, are treated as separators.

Return an integer array `ans`, where `ans[i]` is the number of times `queries[i]` appears as a word in `s`.
