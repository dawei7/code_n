## Description

Students arrive in the order given by `ranks`, where `ranks[i]` is the rank of the $i$th arriving student. A smaller integer represents a better rank. The first arriving student is selected initially and does not count as a replacement.

For every later arrival, replace the selected student only when the new student's rank is strictly better than the current selected rank. Equal or larger rank values leave the selection unchanged. Return the total number of replacements made after processing the complete arrival sequence.
