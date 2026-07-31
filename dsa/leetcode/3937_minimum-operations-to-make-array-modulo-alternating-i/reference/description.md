## Description

An integer array `nums` is changed through unit operations. Each operation selects one element and either increases or decreases its value by exactly one.

For a given modulus `k`, the array is **modulo alternating** when two distinct residues $x$ and $y$ can be chosen from $0$ through $k-1$ such that every element at an even index has residue $x$ modulo $k$, while every element at an odd index has residue $y$ modulo $k$. Indices are zero-based, and the two parity classes must use different residues even when one class contains no element.

Return the smallest total number of unit operations that can make the array modulo alternating.
