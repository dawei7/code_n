## General
**View the combinations as leaves of a decision tree**

At depth `i`, choose one letter mapped from `digits[i]`. Append it to the current path, recursively fill the next position, then remove it before exploring the next letter. A path reaching depth `n` contains one choice for every digit and is copied into the result.

The branching factor is three for digits `2`, `3`, `4`, `5`, `6`, and `8`, and four for `7` and `9`. The empty input is handled separately because the contract requests no combinations rather than a list containing one empty string.

**Backtrack with one reusable path**

On entry to depth `i`, the path contains exactly one valid mapped letter for each of the first `i` digits and no other characters. Every branch appends one valid choice for digit `i`; after the recursive call, removing that choice restores the same path before the sibling branch begins.

Copy the path into a string only when it reaches length `n`. Storing the mutable path object itself would be incorrect because later backtracking would modify every saved reference.

**Trace a representative input**

For `23`, first choose `a` from digit 2 and combine it with `d`, `e`, and `f` from digit 3. Backtrack to choose `b` and then `c`, producing three groups of three combinations and all nine possible strings.

**One root-to-leaf path per combination**

At depth `i`, every branch appends exactly one letter permitted by digit `digits[i]`. A leaf at depth `n` therefore contains one legal choice for every input position and is a valid result.

Conversely, any valid output uniquely determines which letter edge to take at each depth. The depth-first traversal enumerates every permitted edge at every position, so it follows that unique path and reaches the output once. Distinct paths differ at some digit position and cannot produce the same string, giving both completeness and uniqueness.

## Complexity detail
Each digit has at most four letters, so there are at most $4^{n}$ leaves. Materializing each length-`n` result costs $O(n)$, giving output-tight $O(n \cdot 4^n)$ time. More precisely, if the digits have branching factors `b₁..bₙ`, there are exactly `∏bᵢ` outputs. The recursion and mutable path use $O(n)$ auxiliary space; the required output itself uses $O(n \cdot 4^n)$ in the worst case.

## Alternatives and edge cases
- **Iterative Cartesian product:** repeatedly expands every current prefix with the next digit's letters. It has the same output-tight complexity but stores partial combinations at every step.
- **Generate all alphabet strings then filter:** explores many invalid branches and is exponentially larger than the required search space.
- **Lazy generator:** can reduce retained output memory for streaming consumers, but the required return type asks for a complete list.
- Input order must be preserved: letters chosen for a later digit may not be moved ahead of an earlier digit's letter.
- The mapping contains only digits `2` through `9`; handling `0` or `1` is outside the stated contract.
