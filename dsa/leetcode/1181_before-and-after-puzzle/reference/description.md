## Description

Given a list `phrases`, generate every Before and After puzzle that the list permits. Each phrase contains only lowercase English letters and spaces, has neither a leading nor trailing space, and uses exactly one space between adjacent words.

Choose two phrase positions `i` and `j` with `i != j`. They can be merged in that order when the final word of `phrases[i]` equals the first word of `phrases[j]`. The shared boundary word appears only once: keep the entire first phrase, then append everything in the second phrase after its first word.

Pair direction matters, so both `(i, j)` and `(j, i)` must be considered when each direction qualifies. Input phrases with equal text remain separate positions and may therefore be paired if their indices differ.

After considering every ordered pair of distinct indices, remove duplicate puzzle strings and return the remaining strings in lexicographic order.
