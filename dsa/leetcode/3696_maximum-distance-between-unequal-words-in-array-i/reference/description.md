## Description

Given an array of strings `words`, choose two distinct indices $i$ and $j$ whose stored words are not equal. For an ordered pair with $i<j$, its distance includes both endpoints and is defined as

$$
j-i+1.
$$

Among every pair satisfying `words[i] != words[j]`, find the greatest possible distance. If the array contains no valid pair because all of its words are equal, return zero.
