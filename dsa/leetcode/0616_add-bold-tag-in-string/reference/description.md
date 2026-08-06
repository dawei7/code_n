## Description

You are given a source string `s` and an array of dictionary strings `words`. Every substring of `s` that is equal to a value in `words` must be displayed in bold by placing `<b>` before it and `</b>` after it.

The tagged regions represent the union of all matching occurrences. When two occurrences overlap, one tag pair must cover their combined span. The same rule applies when their spans are consecutive: because no untagged character separates them, they belong to one bold region rather than two adjacent regions.

Return `s` after adding the tags. The result therefore surrounds each maximal covered region with exactly one pair of bold tags while preserving every original character and its order.
