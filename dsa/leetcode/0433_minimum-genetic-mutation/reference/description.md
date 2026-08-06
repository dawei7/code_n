## Description

A gene is an eight-character string whose characters are chosen from `A`, `C`, `G`, and `T`. One mutation changes
exactly one character, leaving the other seven positions unchanged. For example, changing `"AACCGGTT"` to
`"AACCGGTA"` is one mutation.

The gene bank lists the strings that are valid after a mutation. Starting from `startGene`, find the minimum number
of single-character mutations needed to reach `endGene`, with each newly reached gene present in `bank`. Return `-1`
when no such sequence exists.

The starting gene is assumed to be valid and therefore does not have to appear in the bank.
