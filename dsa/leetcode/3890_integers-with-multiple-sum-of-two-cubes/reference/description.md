## Description

Given an integer `n`, call an integer $x$ **good** when it has at least two distinct representations as a sum of two positive cubes. Every representation is written as a pair $(a,b)$ satisfying

$$
1 \le a \le b
\quad\text{and}\quad
x=a^3+b^3.
$$

The ordering condition makes each pair canonical, so swapping the same two bases does not create a second representation. Two pairs are distinct only when their canonical base values differ.

Return every good integer $x \le n$ in ascending order.
