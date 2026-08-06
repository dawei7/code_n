## Description

You are given an array of keywords `words` and a lowercase string `s`. Every appearance of every `words[i]` as a contiguous substring of `s` must be made bold by placing its covered letters between `<b>` and `</b>` tags.

Return `s` after inserting a valid combination of bold tags. Use the least possible number of tags: positions covered by overlapping or directly adjacent keyword appearances belong to one maximal bold region and therefore share one tag pair. Characters outside all keyword appearances remain unchanged.
