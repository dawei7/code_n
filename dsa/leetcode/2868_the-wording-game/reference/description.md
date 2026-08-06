## Description

Alice and Bob own lexicographically sorted word lists `a` and `b`. Alice begins by playing the lexicographically smallest word in `a`. After that forced opening, the players alternate turns and select words from their own lists.

A new word must be lexicographically greater than the word played immediately before it. Its first letter must also be either the same as the previous word's first letter or the next letter of the alphabet. A player who has no legal word on their turn loses.

All words across the two lists are distinct. Assuming both players choose optimally, determine whether Alice can force a win.
