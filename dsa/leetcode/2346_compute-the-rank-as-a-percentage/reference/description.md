## Description

The `Students` table records each student's department and exam mark. Rank students independently within their departments by descending mark, so the highest mark has rank 1. Students with the same mark share the same standard competition rank; later ranks retain the resulting gaps.

For a student in a department of size $d$, convert rank $r$ to the percentage

$$
\frac{(r-1)\cdot 100}{d-1}.
$$

Round the percentage to two decimal places and return it with the student and department identifiers. A department containing one student has percentage 0. Result rows may appear in any order.
