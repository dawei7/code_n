## Description

You are given an integer array `nums`. For any index `i`, consider two values:
the sum of every element strictly before `i`, and the product of every element
strictly after `i`. The element at `i` belongs to neither side.

An index is balanced when those two values are equal. The empty-side rules are
part of this definition: a missing left side contributes a sum of $0$, while a
missing right side contributes a product of $1$.

Return the smallest balanced index. If equality never holds at an array index,
return `-1` instead. Products may grow far beyond ordinary fixed-width integer
ranges even though each individual array value satisfies the stated bounds.
