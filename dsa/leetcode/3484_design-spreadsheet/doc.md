# Design Spreadsheet

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3484 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Design, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-spreadsheet/) |

## Problem Description

### Goal

A spreadsheet has 26 columns labeled from `A` through `Z` and a requested number of rows. A cell is named by its column letter followed by its 1-indexed row, such as `A1` or `B10`. Every cell initially contains zero and can hold an integer from 0 through $10^5$.

Implement a `Spreadsheet` that can assign a value to a named cell, reset a named cell to zero, and evaluate a formula. Every formula has exactly the form `=X+Y`. Each operand is independently either a valid cell reference or a non-negative integer no greater than $10^5$.

Formula evaluation is immediate: read the two operands' current values and return their sum. A cell that has never been assigned, or that has been reset, contributes zero. Formulas are not stored in cells and create no dependency graph.

### Function Contract

**Inputs**

- `rows`: The number of spreadsheet rows used to construct the object.
- `cell`: A valid reference consisting of one uppercase letter from `A` through `Z` followed by a row number from 1 through `rows`.
- `value`: The integer assigned by `setCell`.
- `formula`: A string `=X+Y` whose operands are valid cell references or non-negative integer literals.

The constraints are $1\le\texttt{rows}\le10^3$ and $0\le\texttt{value}\le10^5$. At most $10^4$ calls are made in total to `setCell`, `resetCell`, and `getValue`.

The package adapter receives parallel `operations` and `arguments` lists. It constructs one spreadsheet, applies the operations in order, and records one result per operation.

**Return value**

`setCell` and `resetCell` return no value. `getValue` returns the sum of the formula's two current operand values. The adapter returns `null` for construction and mutating calls and the integer result for each query.

### Examples

**Example 1**

- Input: `operations = ["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]`, `arguments = [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]`
- Output: `[null, 12, null, 16, null, 25, null, 15]`

The first query adds two literals. Later queries use the current values of `A1` and `B2`; after `A1` is reset, it contributes zero.

**Example 2**

- Input: `operations = ["Spreadsheet", "getValue", "setCell", "getValue"]`, `arguments = [[1000], ["=Z1000+A1"], ["Z1000", 100000], ["=Z1000+100000"]]`
- Output: `[null, 0, null, 200000]`

Unset cells read as zero, and the maximum cell value may be added to the maximum literal.
