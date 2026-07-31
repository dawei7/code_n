## Description

You are given a nested list of integers named `nestedList`. Each element is either an integer or another list whose elements can recursively be integers or lists.

An integer's depth is the number of lists that contain it. For instance, in `[1,[2,2],[[3],2],1]`, the displayed integer values also happen to equal their depths. Let `maxDepth` denote the greatest depth occupied by any integer.

Assign an integer at depth $d$ the inverse-depth weight

$$
\texttt{maxDepth}-d+1.
$$

Return the sum of every integer multiplied by its weight.
