## Description

Given a string `password`, compute a strength score from the distinct characters that it contains. Character categories have different point values:

- each distinct lowercase English letter contributes $1$ point;
- each distinct uppercase English letter contributes $2$ points;
- each distinct digit contributes $3$ points;
- each distinct special character from `"!@#$"` contributes $5$ points.

A particular character contributes at most once, regardless of how many times it occurs. Lowercase and uppercase forms are different characters, so, for example, `a` and `A` can both contribute.

Return the total strength after scoring every distinct character in the password.
