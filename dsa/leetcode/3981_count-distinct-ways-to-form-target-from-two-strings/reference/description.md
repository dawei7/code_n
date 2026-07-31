## Description

You receive three lowercase strings: `word1`, `word2`, and `target`. Form `target` from left to right by selecting one matching character for each target position from either source word. Within `word1`, the selected indices must be strictly increasing; the indices selected from `word2` must also be strictly increasing. These two order constraints are independent, so the construction may switch between the source words repeatedly.

A valid construction must select at least one character from each word. Two constructions are distinct when any target position uses a different source word or a different index within that word. Return the number of valid constructions modulo $10^9+7$.
