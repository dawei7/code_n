## Description

A set of real numbers can be expressed as the union of disjoint half-open intervals. An interval $[a,b)$ contains exactly the real numbers $x$ for which $a \le x < b$; its left endpoint belongs to the interval, while its right endpoint does not.

The sorted list `intervals` represents such a set. Each entry `intervals[i] = [a_i,b_i]` denotes the half-open interval $[a_i,b_i)$. Another interval, `toBeRemoved`, specifies the real numbers to subtract from that set.

Return every real number that belongs to the union represented by `intervals` but does not belong to `toBeRemoved`. Express the remainder as a sorted list of disjoint half-open intervals of the same form.
