# Building H2O

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1117 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Python |
| Official Link | [LeetCode](https://leetcode.com/problems/building-h2o/) |

## Problem Description

### Goal

Hydrogen and oxygen threads arrive asynchronously at a shared `H2O` object. A hydrogen thread calls `hydrogen(releaseHydrogen)`, whose callback emits `"H"`; an oxygen thread calls `oxygen(releaseOxygen)`, whose callback emits `"O"`.

Release threads in complete water-molecule groups. Every consecutive group of three emitted markers must contain exactly two `"H"` values and one `"O"`, in any internal order. All three callbacks belonging to one molecule must finish before callbacks from the next molecule begin. An oxygen arriving alone waits for two hydrogens, and a hydrogen arriving alone waits for another hydrogen and one oxygen.

### Function Contract

**Inputs**

- `releaseHydrogen` and `releaseOxygen`: zero-argument callbacks executed by atom threads sharing one `H2O` instance.
- The arrival string has length $3m$, contains exactly $2m$ hydrogen threads and $m$ oxygen threads, and $1 \le m \le 20$.

**Return value**

- Methods return `None`; each consecutive three callback markers must be a permutation of `"HHO"`, with no molecule groups overlapping.

### Examples

**Example 1**

- Input: `water = "HOH"`
- Valid outputs: `"HHO"`, `"HOH"`, or `"OHH"`

**Example 2**

- Input: `water = "OOHHHH"`
- One valid output: `"HHOHHO"`

Other outputs are valid when both consecutive three-character blocks contain two hydrogens and one oxygen.
