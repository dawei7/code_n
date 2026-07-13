# Design Excel Sum Formula

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 631 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Graph Theory, Design, Topological Sort, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/design-excel-sum-formula/) |

## Problem Description
### Goal
Design a spreadsheet with rows `1` through `height` and columns `A` through `width`, initially filled with zeroes. Support `set(row, column, value)` for replacing a cell with a literal integer, `get(row, column)` for reading its current value, and `sum(row, column, references)` for assigning a sum formula and returning its value.

A formula may reference individual cells and inclusive rectangular ranges, and repeated or overlapping references contribute with their full multiplicity. Formulas remain active: changing a referenced cell must update every dependent formula value. Assigning a literal or a new formula replaces the target cell's previous contents and dependency behavior.

### Function Contract
**Inputs**

- `operations`: a sequence beginning with `Excel`, followed by `set`, `get`, or `sum` calls
- `arguments`: the matching constructor dimensions, cell coordinates and values, or formula reference lists
- `Excel(height, width)`: create rows `1` through `height` and columns `A` through `width`, initially filled with zeroes
- `set(row, column, value)`: replace the target cell, including any previous formula, with a literal value
- `get(row, column)`: read the target cell's current value
- `sum(row, column, references)`: replace the target with a formula, then return its current value; each reference is a cell such as `A1` or an inclusive range such as `A1:C3`

**Return value**

- The operation trace returns null for construction and `set`, and returns the requested integer for `get` and `sum`
- Repeated or overlapping references contribute with their full multiplicity

### Examples
**Example 1**

- Input: construct a `3` by `A:C` sheet; set `A1 = 2`; set `C3` to `SUM(A1, A1:B2)`; then set `B2 = 2` and get `C3`
- Output: `null, null, 4, null, 6`

**Example 2**

- Input: construct a `2` by `A:B` sheet; get `A1`; set `A1 = 5`; get `A1`
- Output: `null, 0, null, 5`

**Example 3**

- Input: set `A1 = 2`, define `B1 = SUM(A1)`, define `C1 = SUM(A1:B1)`, then change `A1` to `3` and get `C1`
- Output: the final value is `6`

### Required Complexity

- **Time:** $O(N + F)$
- **Space:** $O(N + F)$

<details>
<summary>Approach</summary>

#### General

**Store direct formula multiplicities**

Represent each cell by its row and column indices. A formula is a frequency map from referenced cells to the number of times each one occurs after expanding ranges. This preserves duplicates and overlaps without materializing the same coordinate repeatedly.

**Reverse every dependency edge**

For each source cell, also store a frequency map of formula cells that directly depend on it. When a formula is replaced, remove its old reverse edges before installing its new ones. Literal assignments therefore sever the old formula completely, while downstream formulas that reference the target remain connected.

**Propagate only the numeric difference**

When a target changes from `old` to `new`, propagate `new - old` through its reverse edges. A dependent that mentions the target `m` times changes by `m * (new - old)`; recursively forwarding that difference updates every downstream formula. The contract excludes circular references, so propagation always terminates.

**Why each stored value stays current**

Initially every stored value is zero and correct. Installing a formula computes its value from already-current source cells, and installing a literal writes its exact value. Every later source change is sent along every direct dependency edge with the edge's multiplicity, which is precisely that source's contribution to the dependent sum. Inductively, all reachable formulas receive the full change, so `get` can return the stored value immediately.

#### Complexity detail

Let `N` be the number of cells reached by one update and `F` the traversed formula-reference multiplicity. `get` takes $O(1)$ time. Parsing a formula and propagating a change take $O(N + F)$ worst-case time; `set` has the same worst case because it may affect every downstream formula. Cell values, formulas, and reverse edges occupy $O(N + F)$ space over the sheet.

#### Alternatives and edge cases

- **Recursive evaluation on every read:** store formulas but resolve their dependencies only in `get`; it is simpler and correct, but repeated reads of a long dependency chain can take quadratic total time.
- **Full topological recomputation:** rebuild every formula value after each assignment; it handles the dependency graph directly but spends $O(N + F)$ even when most cells are unrelated.
- **Flatten formulas to transitive source coefficients:** makes reads immediate, but changing a formula can require rewriting many downstream coefficient maps and may consume much more space.
- Blank cells have value zero until assigned a literal or formula.
- A range includes both corner cells and every row and column between them.
- Duplicate references and overlapping ranges must be counted repeatedly rather than deduplicated.
- `set` and `sum` overwrite the target's previous literal or formula and remove obsolete dependencies.
- The input guarantees that formulas do not create circular references.

</details>
