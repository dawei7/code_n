## Description

Two integer arrays, `value` and `decay`, describe a collection of selectable indices. Index `i` begins with gain `value[i]`. It may be selected repeatedly, but each previous selection reduces its next gain by `decay[i]`. Consequently, its first, second, and later gains form a decreasing arithmetic sequence.

More precisely, selecting index `i` for the $t$th time, with $t$ numbered from one, gains `value[i] - decay[i] * (t - 1)`. Across all indices, make at most `m` selections. Because the limit is an upper bound rather than an exact requirement, no non-positive gain ever needs to be accepted.

Maximize the total unmodded gain from the selected terms. Return that maximum modulo $10^9 + 7$.
