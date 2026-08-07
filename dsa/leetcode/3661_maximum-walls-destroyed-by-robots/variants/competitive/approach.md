## General
Given <div data-docx-has-block-data="false" data-lark-html-role="root" data-page-id="Rax8d6clvoFeVtx7bzXcvkVynwf">, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O((R + W) log(R + W))$ — Operation count bound.
- **Space Complexity**: $O(R + W)$ — Auxiliary memory allocation bound.
