## Description

Given an array of strings `strs`, choose independently whether each string keeps its original orientation or is
reversed. Concatenate the selected orientations in the array's existing order and connect the end back to the
beginning to form a loop.

Producing an answer has two phases:

1. Build any such loop while preserving the given order of the string blocks.
2. Choose one breakpoint anywhere in that loop, including inside a block, and read a full traversal beginning at the
   character immediately after the break.

Return the lexicographically largest regular string obtainable over every orientation choice and every possible
breakpoint. Each input character occurs exactly once in the result, and the string blocks may not be permuted.
