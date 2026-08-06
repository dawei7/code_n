## Description

A polynomial linked list stores one term per `PolyNode`. Each node contains an integer `coefficient`, a nonnegative integer `power`, and a pointer to the next term. Lists are in standard form: powers decrease strictly from head to tail, and zero-coefficient terms are omitted.

Given the heads `poly1` and `poly2`, add terms with equal powers and preserve every term whose power occurs in only one polynomial. Omit any equal-power term whose summed coefficient is zero. Return the head of the sum in the same strictly descending standard form. An empty list represents the zero polynomial.
